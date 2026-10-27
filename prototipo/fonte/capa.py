"""Gera a capa de link (1200x630, Open Graph) e o favicon a partir do logo oficial.

Renderiza fonte/capa-link.html com o Edge/Chrome em modo headless e salva prototipo/capa-link.jpg.
Uso (na pasta prototipo/fonte):  python capa.py
"""
import os, re, subprocess, tempfile
from PIL import Image

AQUI = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(AQUI, 'index.src.html')
HTML = os.path.join(AQUI, 'capa-link.html')
OUT = os.path.join(AQUI, '..', 'capa-link.jpg')
NAVEGADORES = [r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',
               r'C:\Program Files\Microsoft\Edge\Application\msedge.exe',
               r'C:\Program Files\Google\Chrome\Application\chrome.exe']

src = open(SRC, encoding='utf-8').read()
sprite = re.search(r'(<defs>.*?</defs>\s*.*?<symbol id="logo".*?</symbol>)', src, re.S).group(1)

capa = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Jost:wght@400;500;600&display=swap" rel="stylesheet">
<style>
html,body{{margin:0;width:1200px;height:630px;overflow:hidden;background:#05291c}}
.capa{{position:relative;width:1200px;height:630px;font-family:'Jost',sans-serif;color:#fff}}
.capa>img{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}}
.capa::before{{content:"";position:absolute;inset:0;z-index:1;background:linear-gradient(90deg,rgba(5,41,28,.95) 0%,rgba(5,41,28,.8) 40%,rgba(5,41,28,.1) 80%)}}
.faixa{{position:absolute;z-index:2;top:0;left:0;right:0;height:10px;background:linear-gradient(90deg,#ce383f 0 25%,#f58b3a 25% 50%,#40a953 50% 75%,#17664b 75%)}}
.txt{{position:absolute;z-index:2;left:76px;top:92px;width:660px}}
.logo{{display:block;width:290px;height:63px;--lg-txt:#fff;--lg-tronco:#9fd4ad}}
h1{{font-weight:600;font-size:66px;line-height:1.2;margin:52px 0 22px;letter-spacing:-.01em}}
.hl{{background:#dc4e13;padding:0 .14em;-webkit-box-decoration-break:clone;box-decoration-break:clone}}
p{{font-size:25px;line-height:1.4;color:#dfeee4;margin:0}}
.url{{position:absolute;z-index:2;left:76px;bottom:54px;font-size:22px;font-weight:500;color:#ffd9bd}}
</style></head><body>
<svg width="0" height="0" style="position:absolute">{sprite}</svg>
<div class="capa"><img src="fotos/Itatiba-Mall-52.jpg" alt=""><div class="faixa"></div>
  <div class="txt"><svg class="logo"><use href="#logo"/></svg>
    <h1>Gastronomia, serviços e lazer <span class="hl">a céu aberto</span></h1>
    <p>Restaurantes, bares, cinema e serviços em Itatiba-SP</p></div>
  <div class="url">itatibamall.com.br</div></div>
</body></html>'''
open(HTML, 'w', encoding='utf-8').write(capa)

exe = next(n for n in NAVEGADORES if os.path.exists(n))
png = os.path.join(tempfile.mkdtemp(), 'capa.png')
subprocess.run([exe, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--force-device-scale-factor=1',
                '--window-size=1200,630', '--virtual-time-budget=8000', f'--screenshot={png}',
                'file:///' + HTML.replace('\\', '/')], check=True, timeout=120,
               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
Image.open(png).convert('RGB').crop((0, 0, 1200, 630)).save(OUT, 'JPEG', quality=86, optimize=True)
print('capa salva em', os.path.normpath(OUT), os.path.getsize(OUT) // 1024, 'KB')
