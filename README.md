# Itatiba Mall · remap do site

Protótipo navegável da nova versão do site do Itatiba Mall, pensado primeiro para o celular e com versão para desktop.

## Como abrir

Online: https://itatibamall.vercel.app/ (o `vercel.json` faz a raiz do domínio servir `prototipo/index.html`).

No computador: abra `prototipo/index.html` no navegador (dois cliques). O arquivo funciona sozinho: fotos e logos já estão embutidos.

No desktop, o botão **“Ver versão celular”** mostra o site dentro de um aparelho, com notas que explicam cada decisão do remap.

## O que tem no protótipo

- Home com o que acontece **hoje no mall**, categorias, programas prontos, agenda da semana, lojas em destaque, cinema e “Gente do mall”
- **Diretório de lojas** com busca, filtros, status “aberto agora” e ação direta (WhatsApp, programação do cinema)
- Fichas de loja, eventos, roteiros e perfis
- **Área do lojista**: horários (semana e exceção do dia), promoções e eventos com aprovação do mall
- Como chegar, página 404, política de privacidade (LGPD) e aviso de cookies
- Capa de link para compartilhamento e favicon

Horários, eventos e filmes são **ilustrativos**. Lojas, códigos de localização, endereço, fotos e logos vêm do site atual do mall.

## Estrutura

```
prototipo/
  index.html          protótipo gerado (é o arquivo para abrir)
  capa-link.jpg       capa de link (Open Graph, 1200x630)
  fonte/
    index.src.html    código-fonte do protótipo (HTML, CSS e JS)
    build.py          comprime as fotos e gera ../index.html
    capa.py           gera a capa de link com o Edge/Chrome em modo headless
    fotos/            fotos e logos originais, do site oficial do mall
```

## Como editar

Edite `prototipo/fonte/index.src.html` e gere de novo o arquivo final (precisa de Python com Pillow):

```bash
cd prototipo/fonte
python build.py
```

Para gerar de novo a capa de link:

```bash
cd prototipo/fonte
python capa.py
```
