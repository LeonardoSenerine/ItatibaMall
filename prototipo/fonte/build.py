"""Gera prototipo/index.html a partir de fonte/index.src.html, embutindo fotos e logos comprimidos.

As imagens em fonte/fotos foram baixadas do site oficial do Itatiba Mall.
Uso (na pasta prototipo/fonte):  python build.py
"""
import io, os, base64
from PIL import Image, ImageChops

AQUI = os.path.dirname(os.path.abspath(__file__))
FOTOS_DIR = os.path.join(AQUI, 'fotos')
SRC = os.path.join(AQUI, 'index.src.html')
OUT = os.path.join(AQUI, '..', 'index.html')

FOTOS = {  # chave -> (arquivo, largura máxima)
    'patio':    ('Itatiba-Mall-52.jpg', 1600),
    'corredor': ('1669057117_90c343_112122_slidderssite2_servios.png', 1400),
    'beco':     ('beco-do-mall-13-1.jpg', 1400),
    'entrada':  ('Capa.jpg', 1400),
    'posto':    ('Itatiba-Mall-123-1-1.jpg', 1400),
    'aerea':    ('tema_header-contatos.png', 1600),
    'office':   ('tema_header-office.png', 1400),
    'burger':   ('DNBurger.jpeg', 1400),
    'kids':     ('Snapinsta.app_359541302_1475117173263924_5097709105557822844_n_1080-1.jpg', 1400),
    'pet':      ('04-14-23_SliderSite_Pet.jpg', 1600),
    'amigos':   ('AdobeStock_583967855-1.jpeg', 1400),
    'cinema':   ('tema_header_cinema.jpg', 1400),
    'mesa':     ('tema_header_alameda_gastronomica.jpg', 1400),
}
LOGOS = {
    '1600-burger': '1600-BURGER.jpg', 'apericena': 'Apericena.jpeg', 'bella-forneria': 'BELLA-FORNERIA.webp',
    'buffalo-bill': 'BUFFALO.webp', 'cervejaria-3-americas': '3-AMERICAS.jpg', 'el-pirata': 'EL-PIRATA.webp',
    'gelato-borelli': 'Borelli.jpeg', 'hop-seekers': 'HOP-SEEKERS.webp', 'mana-poke': 'manapoke.png',
    'macs-restaurante': 'MAX-RESTAURANTE.webp', 'mooca': 'PRACA-DA-MOOCA.jpg', 'mustapha': 'MUSTAPHA.webp',
    'snooker-bar': 'SNOOKER-BAR.webp', 'sobremesa-sobre-rodas': 'SOBREMESAS-SOBRE-RODAS.webp',
    'villa-dos-sabores': 'VILLA-DOS-SABORES.jpg', 'galvao-consolin': 'GALVAO.webp', 'grupo-icd': 'GRUPO-ICD.jpg',
    'wise-investimentos': 'WISE.webp', 'cinema-multiplex': 'MULTIPLEX.webp', 'clinica-mezzalira': 'CLINICA-MEZZALIRA.webp',
    'natalia-garducci': 'NATALIA-GARDUCCI.webp', 'pacova': 'PACOVA.webp', 'tecnoplas': 'Tecnoplas.jpeg',
    'toth-store': 'TOTH-STORE.webp', 'wanddas-fashion-hair': 'WANDDA.webp',
}

def uri(im, q):
    buf = io.BytesIO(); im.save(buf, 'WEBP', quality=q, method=6)
    return 'data:image/webp;base64,' + base64.b64encode(buf.getvalue()).decode()

def foto(arq, w):
    im = Image.open(os.path.join(FOTOS_DIR, arq)).convert('RGB')
    if im.width > w: im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
    return uri(im, 58)

def logo(arq):
    im = Image.open(os.path.join(FOTOS_DIR, arq)).convert('RGBA')
    flat = Image.alpha_composite(Image.new('RGBA', im.size, (255, 255, 255, 255)), im).convert('RGB')
    fundo = flat.getpixel((2, 2))
    diff = ImageChops.difference(flat, Image.new('RGB', flat.size, fundo)).convert('L').point(lambda p: 255 if p > 28 else 0)
    if diff.getbbox(): flat = flat.crop(diff.getbbox())   # recorta a margem do logo
    flat.thumbnail((360, 170), Image.LANCZOS)
    return uri(flat, 82), '#%02x%02x%02x' % fundo

dados, fundos = {}, {}
for k, (arq, w) in FOTOS.items(): dados['f:' + k] = foto(arq, w)
for s, arq in LOGOS.items(): dados['l:' + s], fundos[s] = logo(arq)

js = 'window.FOTOS={' + ','.join(f'"{k}":"{v}"' for k, v in dados.items()) + '};\n'
js += 'window.LOGO_BG={' + ','.join(f'"{k}":"{v}"' for k, v in fundos.items()) + '};'
html = open(SRC, encoding='utf-8').read()
assert '<!--FOTOS-->' in html
html = html.replace('<!--FOTOS-->', f'<script>/* gerado por fonte/build.py */\n{js}\n</script>', 1)
open(OUT, 'w', encoding='utf-8').write(html)
print(f'{len(dados)} imagens · index.html com {len(html) // 1024} KB')
