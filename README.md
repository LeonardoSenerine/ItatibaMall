# Itatiba Mall · remap do site

Protótipo do novo site do Itatiba Mall, com direção de arte própria, para celular, tablet e desktop.

**Conceito:** *um ponto de encontro onde Itatiba acontece*. A direção de arte, a auditoria do site anterior, a paleta validada com a identidade oficial e a lista de fotos a produzir estão em [docs/direcao-de-arte.md](docs/direcao-de-arte.md).

## Como abrir

Online: https://itatibamall.vercel.app/ (o `vercel.json` faz a raiz do domínio servir `prototipo/`).

No computador, rode o servidor local na raiz do projeto. Ele serve `prototipo/` e responde `/api/cinema` com a mesma função da Vercel (precisa de Node 18+):

```bash
python prototipo/fonte/servidor.py
```

Depois abra http://localhost:5173. Sem o servidor (arquivo aberto direto), o cinema mostra o link para a programação oficial.

## O que tem no protótipo

- Entrada animada (a árvore do logo se desenha; uma vez por sessão, desligada com movimento reduzido)
- Home editorial: hero com foto real de fundo no estilo dos banners do mall, manifesto, “o que fazer”, cardápio com as placas de cada operação, cinema, diretório por nome, tipo ou placa, novidades do blog e visita
- Diretório com busca (inclusive por placa, como D06), filtros por tipo, subtipo e bloco, e lista ou grade
- Cinema com a programação real da Multiplex: dias, cartazes, classificação, duração e horários que levam à compra do ingresso
- Agenda dia a dia (sessões do cinema, transmissões especiais, pré-vendas e eventos aprovados), fichas das operações, roteiros e “quem faz o mall”
- Área do lojista: perfil e contatos, horários (semana e exceção do dia), promoções e eventos com aprovação
- Como chegar (mapa do Google só sob demanda), 404, política de privacidade (LGPD) e aviso de cookies
- Capa de link (Open Graph) e favicon

Só entra conteúdo real: lojas, placas, endereço, fotos e logos vêm do site oficial, e as novidades vêm do blog do mall, com datas e links. Eventos de exemplo aparecem sinalizados. Filmes, horários e contatos não são inventados: a programação do cinema é lida do site da Multiplex por `api/cinema.js` (cache de 30 min), e horários e contatos das lojas chegam pela Área do lojista.

## Estrutura

```
docs/direcao-de-arte.md   auditoria, conceito, identidade e fotos a produzir
api/cinema.js             função da Vercel: lê a programação pública da Multiplex e devolve JSON
prototipo/
  index.html              site gerado
  img/                    fotos (WebP 800/1600 px) e logos otimizados
  capa-link.jpg           capa de link (Open Graph, 1200x630)
  fonte/
    index.src.html        código-fonte (HTML, CSS e JS)
    build.py              otimiza as imagens e gera ../index.html e ../img/
    capa.py               gera a capa de link com o Edge/Chrome em modo headless
    servidor.py           servidor local com a rota /api/cinema
    fotos/                fotos e logos originais do site oficial
```

## Como editar

Edite `prototipo/fonte/index.src.html` e gere de novo (precisa de Python com Pillow):

```bash
cd prototipo/fonte
python build.py
```

Para gerar de novo a capa de link:

```bash
cd prototipo/fonte
python capa.py
```
