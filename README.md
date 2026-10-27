# Itatiba Mall · remap do site

Protótipo do novo site do Itatiba Mall, com direção de arte própria, para celular, tablet e desktop.

**Conceito:** *um ponto de encontro onde Itatiba acontece*. A direção de arte, a auditoria do site anterior, a paleta validada com a identidade oficial e a lista de fotos a produzir estão em [docs/direcao-de-arte.md](docs/direcao-de-arte.md).

## Como abrir

Online: https://itatibamall.vercel.app/ (o `vercel.json` faz a raiz do domínio servir `prototipo/`).

No computador, sirva a pasta `prototipo/` por um servidor local, porque as imagens são arquivos separados:

```bash
python -m http.server 5173 --directory prototipo
```

Depois abra http://localhost:5173.

## O que tem no protótipo

- Home editorial: hero com foto real, manifesto, “o que fazer”, cardápio com as placas de cada operação, cinema, diretório por nome, tipo ou placa, novidades do blog e visita
- Diretório com busca (inclusive por placa, como D06), filtros por tipo, subtipo e bloco, e lista ou grade
- Fichas das operações, agenda, roteiros e “quem faz o mall”
- Área do lojista: perfil e contatos, horários (semana e exceção do dia), promoções e eventos com aprovação
- Como chegar (mapa do Google só sob demanda), 404, política de privacidade (LGPD) e aviso de cookies
- Capa de link (Open Graph) e favicon

Só entra conteúdo real: lojas, placas, endereço, fotos e logos vêm do site oficial, e as novidades vêm do blog do mall, com datas e links. Eventos de exemplo aparecem sinalizados. Filmes, horários e contatos não são inventados: a programação fica no site da Multiplex, e horários e contatos chegam pela Área do lojista.

## Estrutura

```
docs/direcao-de-arte.md   auditoria, conceito, identidade e fotos a produzir
prototipo/
  index.html              site gerado
  img/                    fotos (WebP 800/1600 px) e logos otimizados
  capa-link.jpg           capa de link (Open Graph, 1200x630)
  fonte/
    index.src.html        código-fonte (HTML, CSS e JS)
    build.py              otimiza as imagens e gera ../index.html e ../img/
    capa.py               gera a capa de link com o Edge/Chrome em modo headless
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
