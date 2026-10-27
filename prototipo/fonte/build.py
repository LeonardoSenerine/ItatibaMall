"""Gera prototipo/index.html a partir de fonte/index.src.html e exporta as imagens otimizadas.

- Fotos: só registros reais do Itatiba Mall (ver docs/direcao-de-arte.md), em WebP de 800 e 1600 px (srcset).
- Logos: recortados e exportados em prototipo/img/logos/.
- O HTML recebe só o índice das imagens (dimensões e cor de fundo dos logos).
Uso (na pasta prototipo/fonte):  python build.py
"""
import os, json
from PIL import Image, ImageChops

AQUI = os.path.dirname(os.path.abspath(__file__))
FOTOS_DIR = os.path.join(AQUI, 'fotos')
SRC = os.path.join(AQUI, 'index.src.html')
SAIDA = os.path.normpath(os.path.join(AQUI, '..'))
IMG = os.path.join(SAIDA, 'img')

FOTOS = {  # chave -> arquivo original (todos registros reais do mall)
    'patio':          'Itatiba-Mall-52.jpg',
    'beco':           'beco-do-mall-13-1.jpg',
    'galeria':        '1669057117_90c343_112122_slidderssite2_servios.png',
    'portal':         'Capa.jpg',
    'aerea':          'tema_header-contatos.png',
    'office':         'tema_header-office.png',
    'entrada':        'tema_header-mall.png',
    'estacionamento': 'tema_header-Servicos.png',
    'posto':          'Itatiba-Mall-123-1-1.jpg',
    'burger':         'DNBurger.jpeg',
    'pacova':         'Snapinsta.app_359541302_1475117173263924_5097709105557822844_n_1080-1.jpg',
    'pets':           'IM_POST_CLIMARK_142.png',
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
LARGURAS = (800, 1600)

os.makedirs(os.path.join(IMG, 'logos'), exist_ok=True)   # sobrescreve em vez de apagar a pasta (o OneDrive pode travá-la)
gerados = set()

indice = {}
for k, arq in FOTOS.items():
    im = Image.open(os.path.join(FOTOS_DIR, arq)).convert('RGB')
    ws = [w for w in LARGURAS if w <= im.width]          # nunca amplia a foto original
    if im.width < LARGURAS[-1] and im.width not in ws: ws.append(im.width)
    for w in ws:
        h = round(im.height * w / im.width)
        im.resize((w, h), Image.LANCZOS).save(os.path.join(IMG, f'{k}-{w}.webp'), 'WEBP', quality=72 if w <= 800 else 64, method=6)
        gerados.add(f'{k}-{w}.webp')
    indice[k] = {'w': ws, 'r': round(im.width / im.height, 4)}

fundos = {}
for s, arq in LOGOS.items():
    im = Image.open(os.path.join(FOTOS_DIR, arq)).convert('RGBA')
    flat = Image.alpha_composite(Image.new('RGBA', im.size, (255, 255, 255, 255)), im).convert('RGB')
    fundo = flat.getpixel((2, 2))
    diff = ImageChops.difference(flat, Image.new('RGB', flat.size, fundo)).convert('L').point(lambda p: 255 if p > 28 else 0)
    if diff.getbbox(): flat = flat.crop(diff.getbbox())   # recorta a margem do logo
    flat.thumbnail((400, 190), Image.LANCZOS)
    flat.save(os.path.join(IMG, 'logos', f'{s}.webp'), 'WEBP', quality=86, method=6)
    fundos[s] = '#%02x%02x%02x' % fundo

# remove fotos antigas que não fazem mais parte do site
for f in os.listdir(IMG):
    if f.endswith('.webp') and f not in gerados:
        try: os.remove(os.path.join(IMG, f))
        except OSError: pass

dados = (f'window.IMGS={json.dumps(indice, separators=(",", ":"))};\n'
         f'window.LOGO_BG={json.dumps(fundos, separators=(",", ":"))};')
html = open(SRC, encoding='utf-8').read()
assert '<!--FOTOS-->' in html
html = html.replace('<!--FOTOS-->', f'<script>/* gerado por fonte/build.py */\n{dados}\n</script>', 1)
open(os.path.join(SAIDA, 'index.html'), 'w', encoding='utf-8').write(html)

total = sum(os.path.getsize(os.path.join(r, f)) for r, _, fs in os.walk(IMG) for f in fs)
print(f'{len(indice)} fotos + {len(fundos)} logos ({total // 1024} KB em img/) · index.html com {len(html) // 1024} KB')
