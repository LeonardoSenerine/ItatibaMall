"""Servidor local do protótipo: serve prototipo/ e responde /api/cinema com a mesma função da Vercel (api/cinema.js).
Uso (na raiz do projeto):  python prototipo/fonte/servidor.py   ->  http://localhost:5173
Precisa de Node 18+ para a rota /api/cinema."""
import http.server, subprocess, os

AQUI = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.normpath(os.path.join(AQUI, '..'))
API = os.path.normpath(os.path.join(AQUI, '..', '..', 'api', 'cinema.js'))
# chama o handler da Vercel com uma resposta mínima e imprime o corpo
NODE = ("const h=require(process.argv[1]);let st=200;"
        "h({},{setHeader(){},status(c){st=c;return this},send(b){process.stdout.write(b)},json(o){process.stdout.write(JSON.stringify(o))}})"
        ".then(()=>{process.exitCode=st===200?0:1})")

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k): super().__init__(*a, directory=SITE, **k)
    def do_GET(self):
        if self.path.startswith('/api/cinema'):
            p = subprocess.run(['node', '-e', NODE, API], capture_output=True, timeout=30)
            corpo = p.stdout or b'{"erro":"falha ao ler a programacao"}'
            self.send_response(200 if p.returncode == 0 else 502)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Content-Length', str(len(corpo)))
            self.end_headers(); self.wfile.write(corpo)
            return
        super().do_GET()

if __name__ == '__main__':
    print('http://localhost:5173')
    http.server.ThreadingHTTPServer(('127.0.0.1', 5173), Handler).serve_forever()
