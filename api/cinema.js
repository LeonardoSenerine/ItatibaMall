// Programação real do Multiplex Itatiba Mall.
// Lê a página pública de programação da Multiplex no servidor (evita CORS) e devolve JSON enxuto:
// { fonte, atualizado, filmes: [{ titulo, cartaz, classificacao, duracao, sinopse, sessoes: [{ data, hora, idioma, compra }] }] }
// Cache na borda da Vercel: 30 min, servindo a versão anterior enquanto atualiza.
const FONTE = 'https://multiplexcinemas.com.br/programacao/';

const limpa = s => s.replace(/<[^>]+>/g, ' ')
  .replace(/&#(\d+);/g, (_, n) => String.fromCharCode(+n))
  .replace(/&(amp|quot|#039|apos|nbsp|ndash|mdash|hellip|ldquo|rdquo|lsquo|rsquo);/g, (_, e) =>
    ({amp:'&', quot:'"', '#039':"'", apos:"'", nbsp:' ', ndash:'–', mdash:'—', hellip:'…', ldquo:'“', rdquo:'”', lsquo:'‘', rsquo:'’'}[e]))
  .replace(/\s+/g, ' ').trim();

function primeiraFrase(t, max = 220){
  const m = t.match(/^(.{40,}?[.!?])(\s|$)/);
  const f = m ? m[1] : t;
  return f.length > max ? f.slice(0, max - 1).replace(/\s+\S*$/, '') + '…' : f;
}

function extrair(html){
  const blocos = html.split('<div class="amy-movie-item">').slice(1);
  const filmes = [];
  for (const b of blocos){
    const titulo = (b.match(/amy-movie-field-title[^>]*>\s*<a[^>]*>([\s\S]*?)<\/a>/) || [])[1];
    if (!titulo) continue;
    const cartaz = (b.match(/<img[^>]+src="([^"]+)"/) || [])[1] || null;
    const classificacao = limpa((b.match(/amy-movie-field-mpaa[^>]*>([\s\S]*?)<\/span>/) || [])[1] || '');
    const durTxt = limpa((b.match(/amy-movie-field-duration[^>]*>([\s\S]*?)<\/span>/) || [])[1] || '');
    const h = +(durTxt.match(/(\d+)\s*hora/) || [0, 0])[1], m = +(durTxt.match(/(\d+)\s*minuto/) || [0, 0])[1];
    const sinopse = primeiraFrase(limpa((b.match(/amy-movie-field-desc[^>]*>([\s\S]*?)<\/div>/) || [])[1] || ''));
    const sessoes = [];
    const re = /amy-head[^>]*>\s*<div>[^<]*<\/div>\s*<div>(\d{2})\/(\d{2})\/(\d{4})<\/div>[\s\S]*?amy-intro-times[^>]*>\s*<div>\s*(\d{1,2}:\d{2})\s*([^<]*?)\s*<\/div>\s*<a[^>]+href="([^"]+)"/g;
    let s;
    while ((s = re.exec(b))){
      sessoes.push({data:`${s[3]}-${s[2]}-${s[1]}`, hora:s[4].padStart(5, '0'), idioma:limpa(s[5]), compra:s[6]});
    }
    sessoes.sort((a, z) => (a.data + a.hora).localeCompare(z.data + z.hora));
    filmes.push({titulo:limpa(titulo), cartaz, classificacao, duracao: h * 60 + m || null, sinopse, sessoes});
  }
  return filmes;
}

module.exports = async (req, res) => {
  try {
    const r = await fetch(FONTE, {headers:{'User-Agent':'Mozilla/5.0 (compatible; ItatibaMallSite/1.0)'}, signal:AbortSignal.timeout(9000)});
    if (!r.ok) throw new Error('status ' + r.status);
    const filmes = extrair(await r.text());
    res.setHeader('Content-Type', 'application/json; charset=utf-8');
    res.setHeader('Cache-Control', 'public, s-maxage=1800, stale-while-revalidate=3600');
    res.status(200).send(JSON.stringify({fonte:FONTE, atualizado:new Date().toISOString(), filmes}));
  } catch (e) {
    res.setHeader('Cache-Control', 'no-store');
    res.status(502).json({erro:'Não foi possível ler a programação da Multiplex agora.', fonte:FONTE});
  }
};
module.exports.extrair = extrair;
