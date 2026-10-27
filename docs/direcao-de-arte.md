# Itatiba Mall · auditoria e direção de arte

## 1. Auditoria do site publicado (itatibamall.vercel.app)

**Stack e arquitetura.** Site estático de uma página (`prototipo/index.html`), gerado a partir de `prototipo/fonte/index.src.html` por `build.py`. JavaScript puro, sem framework: roteador por `#hash`, View Transitions, IntersectionObserver e `localStorage`. Publicado na Vercel pelo `vercel.json`. A arquitetura é adequada e foi preservada.

**Funcionalidades a preservar.** Diretório com busca, filtros e lista/grade. Fichas de loja. Agenda e página de evento (com arquivo .ics). Roteiros. Perfil "Gente do mall". Área do lojista (horários, promoções e eventos com aprovação). Como chegar com Google Maps/Waze. Menu em gaveta. Busca no topo. Política de privacidade e aviso de cookies. Página 404. Capa de link e favicon. Versão celular/desktop.

**O que deixava o site genérico**
- A mesma composição em quase todas as seções: título, linha laranja e uma fileira de cards iguais (eventos, roteiros, gente, lojas).
- Tipografia só em sans-serif: títulos e textos com o mesmo peso de voz, sem contraste editorial.
- Hero dominado por um evento (Domingo Pet), não pelo lugar.
- Nenhum elemento gráfico próprio além da faixa de 4 cores.

**Conteúdo inventado que precisava sair**
- Filmes e horários do cinema ("A Última Estação", sessões das 21h40): não existem.
- Horários de funcionamento das lojas e o status "Aberto agora" calculado a partir deles: não há horários confirmados.
- A agenda "Hoje no mall", montada a partir desses horários e filmes.
- Eventos apresentados como se fossem reais.
- Perfis "Gente do mall" de equipes sem conteúdo.
- Botões de WhatsApp, ligar e Instagram que só exibiam um aviso.

**Imagens**

| Arquivo | Origem | Uso |
|---|---|---|
| Itatiba-Mall-52 (pátio com árvore e murais) | real | hero |
| beco-do-mall (Beco do Mall, murais) | real | manifesto, 404 |
| slider "serviços" (galeria coberta, placas da Bella Forneria e da Wandda's) | real | gastronomia, fichas dessas duas lojas |
| Capa.jpg (entrada com mural) | real | novidades |
| tema_header-contatos (vista aérea) | real | visita |
| tema_header-office (torre de escritórios) | real | saúde e escritórios |
| tema_header-mall (entrada com palmeiras + arcos 3D da marca) | real | convivência |
| tema_header-Servicos (estacionamento + arcos 3D) | real | visita |
| Itatiba-Mall-123 (posto) | real | lojas e serviços, ficha do posto |
| DNBurger (prato do 1600 Burger) | real | destaque de gastronomia, ficha da loja |
| Snapinsta (criança cozinhando no Pacová) | real | ficha do Pacová, novidades |
| IM_POST_CLIMARK (campanha "Pets no Itatiba Mall") | real (peça da marca) | novidades |
| sliders "Pet" e "cinema", AdobeStock, headers "cinema", "alameda" e "notícias" | **banco de imagens** | **removidas** |

## 2. Conceito

**"Um ponto de encontro onde Itatiba acontece."**

O próprio mall já se descreve assim: no blog oficial, o Itatiba Mall é *"o local onde os melhores encontros acontecem"*. O conceito vem daí, não de um slogan inventado. A frase "Itatiba acontece aqui" é direção criativa do hero, não assinatura oficial.

## 3. Identidade validada

**Cores.** O logo usa vermelho `#ce383f`, laranja `#f58b3a`, verde `#40a953` e verde Itatiba `#17664b`. O site atual usa ainda o laranja `#dc4e13` e o verde-noite `#05291c`. A paleta proposta no briefing foi confrontada com isso:

| Proposta do briefing | Decisão | Motivo |
|---|---|---|
| off-white | **Cal** `#f4efe6`, **Papel** `#fbf8f1`, **Areia** `#e6dccb` | neutros quentes que não competem com as fotos |
| carvão | **Carvão** `#1c1f1d` | texto e seções escuras (cinema, rodapé) |
| oliva | **verde Itatiba** `#17664b` no papel do oliva | não existe oliva na identidade; o verde oficial cumpre a função e mantém a marca |
| terracota | **Terracota** `#c4501f`, derivada do laranja `#dc4e13` do site | mesmo matiz da marca, mais terroso; com texto branco tem contraste AA |
| — | vermelho, laranja e verde do logo | só no logo, nos arcos e na faixa de 4 cores |

**Tipografia.** *Fraunces* (serifada editorial, com itálico expressivo) nos títulos. *Jost* (geométrica, da mesma família visual do "Itatiba" do logo) na navegação, nos dados e no texto.

**Grafismos autorais.**
- **Arcos que se encontram:** a copa da árvore do logo é feita de arcos que se cruzam, e os banners oficiais já usam arcos 3D nas cores da marca. Viram o sinal gráfico do conceito "encontro", desenhados como um traço. Aparecem em poucos lugares: hero, cinema, banda do lojista e 404.
- **Placas:** cada operação tem um código real de bloco e número (D06, F01, J42). Eles viram placas de sinalização, no diretório, no cardápio e nas fichas, e permitem filtrar por bloco.
- **Numeração editorial:** as seções da home são numeradas (01 a 06), como capítulos.

## 4. Fotografias a produzir

1. Fachada e acesso principal, de dia e à noite.
2. Pátio com movimento: pessoas almoçando, fim de tarde, iluminação noturna.
3. Uma foto de cada restaurante e bar: ambiente e prato principal. Hoje só existe a do 1600 Burger.
4. Multiplex: fachada, bilheteria e sala. Hoje não há nenhuma foto real.
5. Pacová em funcionamento, com autorização de imagem dos responsáveis.
6. Clínicas e salão: recepção ou ambiente.
7. Estacionamento e sinalização de entrada, sem os arcos sobrepostos, para uso editorial.
8. Pets no pátio, em uma ação real.
9. Detalhes: placas de bloco, murais do Beco, vegetação.

Formato recomendado: horizontal 3:2 e vertical 4:5 de cada cena, com no mínimo 2400 px no lado maior.

## 5. Dados a confirmar com o mall

- Horário de funcionamento do complexo e de cada operação. Os lojistas podem preencher pela Área do lojista.
- Regras e valores do estacionamento.
- Telefone, WhatsApp e Instagram oficiais do mall.
- Acessibilidade: rampas, vagas e banheiros.
- Integração com a programação da Multiplex (feed ou API), para mostrar filmes e sessões no site.
- Razão social, CNPJ e encarregado(a) de dados, para a política de privacidade.
