#!/usr/bin/env python3
"""Fill passage `from` links, resolve flagged turns, restamp V4 HTML."""
from __future__ import annotations

import html as H
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML_PATH = ROOT / "document" / "The_Nine_Bodies_of_Authority_v4.html"
DATA_PATH = ROOT / "data" / "nine-bodies.json"
TR_PATH = ROOT / "source" / "transcript.json"
DISP_PATH = ROOT / "source" / "FLAGGED_DISPOSITION.md"

STOP = set(
    """the a an and or of to in on for as is are was were be been being that this those
    these it its with by from at not no into than then so if but which who whom whose
    their they them we you your our his her hers he she i me my mine all any each other
    such only own same too very can may will would should could must also about over
    after before between through during without within what when where how why does do
    did has have had there here one two three four five six seven eight nine ten""".split()
)

# CONVERSION.md thirteen + two transcription-doubt (spec notes fifteen)
FLAG_IDS = [
    "t0010", "t0013", "t0014", "t0045", "t0056",
    "t0072", "t0073", "t0075", "t0082", "t0083", "t0092", "t0093", "t0105",
    "t0028", "t0032",
]

DISPOSITIONS = {
    "t0010": {
        "disposition": "kept-overlap-marked",
        "note": "Claude acknowledgement remains inside Percy speech; flag retained; no invented split without timed audio.",
    },
    "t0013": {
        "disposition": "kept-overlap-marked",
        "note": "Short Percy question may share a beat with Claude; flag retained.",
    },
    "t0014": {
        "disposition": "kept-overlap-marked",
        "note": "Checking that quickly may be glued to the previous beat; flag retained.",
    },
    "t0028": {
        "disposition": "kept-doubt-marked",
        "note": "transcription-doubt retained; verbatim text kept; UI shows [?].",
    },
    "t0032": {
        "disposition": "kept-doubt-marked",
        "note": "transcription-doubt retained; verbatim text kept; UI shows [?].",
    },
    "t0045": {
        "disposition": "kept-overlap-marked",
        "note": "Claude clause sits inside Percy turn; flag retained.",
    },
    "t0056": {
        "disposition": "kept-overlap-marked",
        "note": "Mm-hm and Checking it in that frame sit inside Percy speech; flag retained.",
    },
    "t0072": {
        "disposition": "noise-trimmed",
        "note": "Leading pasted framework prose removed; spoken resume kept from I believe so; attachment-noise cleared.",
        "trim": "t0072",
    },
    "t0073": {
        "disposition": "kept-mixed-paste",
        "note": "Claude ack, document paste, and later water-case prompt are glued; flag retained; no invented turn ids.",
    },
    "t0075": {
        "disposition": "kept-mixed-paste",
        "note": "Confirmation speech and long pasted water/religious-account prose are glued; flag retained.",
    },
    "t0082": {
        "disposition": "noise-only-held",
        "note": "Turn is only paste/UI filenames. Kept verbatim; attachment-noise retained; id stable.",
    },
    "t0083": {
        "disposition": "noise-trimmed",
        "note": "UI chrome prefix output thisClaude removed; spoken remainder kept; attachment-noise cleared.",
        "trim": "t0083",
    },
    "t0092": {
        "disposition": "kept-mixed-paste",
        "note": "Tool chrome and spoken correction are interleaved; flag retained; no invented split.",
    },
    "t0093": {
        "disposition": "noise-trimmed",
        "note": "Used 3 tools and memory-chrome phrases removed where separable; speech kept; attachment-noise cleared.",
        "trim": "t0093",
    },
    "t0105": {
        "disposition": "resolved-as-content",
        "note": "Account-boundary note and generated title are Claude's own status speech, not paste noise; flag cleared; via stays inferred.",
    },
}


def toks(s: str) -> list[str]:
    return [
        w
        for w in re.findall(r"[a-z0-9']+", s.lower())
        if w not in STOP and len(w) > 2
    ]


def clean_html_text(t: str) -> str:
    t = re.sub(r"<[^>]+>", "", t)
    t = H.unescape(t)
    return re.sub(r"\s+", " ", t).strip()


def extract_comprehensive_paras(html: str) -> list[str]:
    """Paragraphs that form the Comprehensive reading (before descView)."""
    cut = html.split('<section id="descView"', 1)[0]
    # Drop network view block if present early
    cut = re.sub(
        r'<section id="networkView".*', "", cut, count=1, flags=re.S
    )
    paras = []
    for raw in re.findall(r"<p(?:\s[^>]*)?>(.*?)</p>", cut, flags=re.S | re.I):
        text = clean_html_text(raw)
        if len(text) < 50:
            continue
        # skip UI chrome
        if text.startswith("The Nine Bodies of Authority · Version"):
            continue
        paras.append(text)
    return paras


def best_turns(text: str, turn_toks: dict[str, set[str]], k: int = 3, min_inter: int = 5) -> list[str]:
    pt = set(toks(text))
    if len(pt) < 4:
        return []
    scored = []
    for tid, tt in turn_toks.items():
        inter = len(pt & tt)
        if inter < min_inter:
            continue
        score = inter / (len(pt) ** 0.5)
        scored.append((score, inter, tid))
    scored.sort(reverse=True)
    out = []
    for score, inter, tid in scored[:k]:
        if inter < min_inter:
            continue
        out.append(tid)
    return out


def thematic_fallback(text: str) -> list[str]:
    """Conservative theme → known turn ranges from Untitled 15 arc. Only real ids."""
    t = text.lower()
    rules = [
        (r"contaminated water|water supply|water case", ["t0060", "t0061", "t0062"]),
        (r"auditorial", ["t0013", "t0015", "t0016"]),
        (r"surveillance|intelligence|enforcement", ["t0038", "t0039", "t0040"]),
        (r"preservational|sanitation|energy resources", ["t0065", "t0066", "t0067"]),
        (r"hamiltonian|cube|bit flips|one bit", ["t0094", "t0095", "t0096"]),
        (r"collective names|consequential|environmental", ["t0097", "t0098", "t0099"]),
        (r"top row|regime", ["t0122", "t0123", "t0124"]),
        (r"three positions|act.*authoris|account", ["t0033", "t0034", "t0035"]),
        (r"seed domains|parsons|pestle", ["t0001", "t0002", "t0003"]),
        (r"blocked story|journalism", ["t0070", "t0071", "t0074"]),
    ]
    for pat, ids in rules:
        if re.search(pat, t):
            return ids
    return []


def trim_turn(tid: str, text: str, kind: str | None) -> str:
    if not kind:
        return text
    original = text
    if kind == "t0072":
        m = re.search(r"\bI believe so\b", text)
        if m:
            text = text[m.start() :]
    elif kind == "t0083":
        text = re.sub(r"^output thisClaude\s*", "", text, flags=re.I)
    elif kind == "t0093":
        text = re.sub(r"\bUsed \d+ tools\b", "", text, flags=re.I)
        text = re.sub(
            r"\bAdded to memory nine-bodies-of-authority\.md\b",
            "",
            text,
            flags=re.I,
        )
    text = re.sub(r"\s+", " ", text).strip()
    return text if text else original


def apply_flag_resolutions(turns: list[dict]) -> list[dict]:
    by_id = {t["id"]: t for t in turns}
    for tid, meta in DISPOSITIONS.items():
        t = by_id[tid]
        t["disposition"] = meta["disposition"]
        t["disposition_note"] = meta["note"]
        kind = meta.get("trim")
        if kind:
            new = trim_turn(tid, t["text"], kind)
            if new != t["text"]:
                t["text_before_trim"] = t["text"]
                t["text"] = new
        disp = meta["disposition"]
        if disp in {"noise-trimmed", "resolved-as-content"}:
            t["flags"] = []
        elif disp == "noise-only-held":
            t["flags"] = ["attachment-noise"]
        # kept-* and kept-mixed-paste leave flags as-is
    return turns


def fill_from_arrays(data: dict, paras: list[str], turns: list[dict]) -> dict:
    turn_toks = {t["id"]: set(toks(t["text"])) for t in turns}
    valid = {t["id"] for t in turns}
    comps = data["passages"]["comprehensive"]
    # Align: use first 77 paras; if fewer, leave remainder empty + thematic
    for i, slot in enumerate(comps):
        text = paras[i] if i < len(paras) else ""
        ids = best_turns(text, turn_toks) if text else []
        if not ids and text:
            ids = thematic_fallback(text)
        ids = [x for x in ids if x in valid]
        # de-dupe preserve order
        seen = set()
        out = []
        for x in ids:
            if x not in seen:
                seen.add(x)
                out.append(x)
        slot["from"] = out

    # Descriptive water case — map to water discussion turns
    for slot in data["passages"]["descriptive"]:
        ids = [x for x in ["t0060", "t0061", "t0062", "t0063"] if x in valid]
        slot["from"] = ids

    # Illustrative loops figure — cube / loop turns
    for slot in data["passages"]["illustrative"]:
        ids = [x for x in ["t0094", "t0095", "t0096", "t0116"] if x in valid]
        slot["from"] = ids

    # Transcriptive passages: from is self (identity) — leave empty or self?
    # Spec: from points AT recorded turns FROM other modes. Transcriptive entries stay empty.
    for slot in data["passages"]["transcriptive"]:
        slot["from"] = []

    data["provenance"] = (
        "from arrays filled 26 Oct 2026 from Untitled 15 (127 turns). "
        "Only ids present in source/transcript.json. "
        "Overlap/doubt flags kept where no timed split exists; "
        "attachment-noise trimmed where paste/UI chrome was separable."
    )
    return data


def inject_passages_and_links(html: str, data: dict, turns: list[dict]) -> str:
    """Add data-seg + Source links; embed passages JSON; update turns; stamp Expanded; print CSS."""
    # Replace turnsData with resolved turns
    turns_json = json.dumps(turns, ensure_ascii=False, separators=(",", ":"))
    html = re.sub(
        r'<script type="application/json" id="turnsData">.*?</script>',
        '<script type="application/json" id="turnsData">' + turns_json + "</script>",
        html,
        count=1,
        flags=re.S,
    )

    passages_payload = {
        "comprehensive": data["passages"]["comprehensive"],
        "descriptive": data["passages"]["descriptive"],
        "illustrative": data["passages"]["illustrative"],
        "meta": data["meta"],
    }
    passages_json = json.dumps(passages_payload, ensure_ascii=False, separators=(",", ":"))
    if 'id="passagesData"' in html:
        html = re.sub(
            r'<script type="application/json" id="passagesData">.*?</script>',
            '<script type="application/json" id="passagesData">' + passages_json + "</script>",
            html,
            count=1,
            flags=re.S,
        )
    else:
        html = html.replace(
            '<script type="application/json" id="turnsData">',
            '<script type="application/json" id="passagesData">'
            + passages_json
            + "</script>\n"
            + '<script type="application/json" id="turnsData">',
            1,
        )

    # Band / footer / masthead restamp
    band = (
        'The Nine Bodies of Authority · Version <span data-version>4</span> · '
        "Expanded words · October 2026"
    )
    html = re.sub(
        r'<div class="band">.*?</div>',
        f'<div class="band">{band}</div>',
        html,
        count=1,
        flags=re.S,
    )
    # Masthead: ensure version line under h1
    if 'class="mast"' not in html and "data-masthead" not in html:
        html = html.replace(
            "<h1>The Nine Bodies of Authority</h1>",
            "<h1>The Nine Bodies of Authority</h1>\n"
            '  <p class="mast" data-masthead>Version <span data-version>4</span> · '
            "Words from the Expanded edition (30 pages, 26 October 2026)</p>",
            1,
        )
    html = re.sub(
        r'<p class="foot">.*?</p>',
        '<p class="foot">The Nine Bodies of Authority · Version <span data-version>4</span> · '
        "Expanded words · October 2026 · Solid = settled or travelled · "
        "Dashed = channel or contingent · Dotted = held or unused</p>",
        html,
        count=1,
        flags=re.S,
    )

    # Print / PDF path CSS
    print_css = """
@media print{
  .band,.foot,.mast,[data-masthead]{display:block!important}
  .rail,.modebar,.tool,.travel,.controls,.trail,.links button{display:none!important}
  body{background:#fff;color:#000}
  .band::after{content:" · PDF Version 4"}
  .foot::after{content:""}
  main{data-mode:comprehensive}
}
"""
    if "@media print" not in html:
        html = html.replace("</style>", print_css + "</style>", 1)

    # Mast style
    if ".mast{" not in html:
        html = html.replace(
            "</style>",
            ".mast,[data-masthead]{margin:6px 0 0;font:700 11px/1.4 var(--mono);letter-spacing:.08em;"
            "text-transform:uppercase;color:var(--ink-3)}\n"
            ".prose > p[data-seg]{position:relative}\n"
            ".prose > p[data-seg] > .src{"
            "display:inline-block;margin-left:8px;border:1px solid var(--control);border-radius:999px;"
            "padding:2px 8px;font:700 10px/1.2 var(--mono);letter-spacing:.06em;text-transform:uppercase;"
            "color:var(--ink-3);background:var(--surface);cursor:pointer;vertical-align:middle}\n"
            ".prose > p[data-seg] > .src:hover{border-color:var(--ink);color:var(--ink)}\n"
            ".turn.flagged{border-left:2px solid var(--focal)}\n"
            ".turn .disp{font:700 10px/1.3 var(--mono);letter-spacing:.06em;text-transform:uppercase;"
            "color:var(--ink-3);margin-top:4px}\n"
            "</style>",
            1,
        )

    # Annotate comprehensive paragraphs with data-seg in document order
    cut_at = html.find('<section id="descView"')
    head, tail = html[:cut_at], html[cut_at:]
    comps = data["passages"]["comprehensive"]
    idx = [0]

    def repl_p(m: re.Match) -> str:
        full = m.group(0)
        inner = m.group(1)
        text = clean_html_text(inner)
        if len(text) < 50:
            return full
        if text.startswith("The Nine Bodies of Authority · Version"):
            return full
        if 'data-seg="' in full:
            return full
        i = idx[0]
        if i >= len(comps):
            return full
        seg = comps[i]["id"]
        idx[0] += 1
        # insert data-seg on p and Source button before close
        open_tag = m.group(0)[: m.group(0).find(">") + 1]
        if open_tag.startswith("<p"):
            if " " in open_tag[:-1]:
                open_tag = open_tag[:-1] + f' data-seg="{seg}">'
            else:
                open_tag = f'<p data-seg="{seg}">'
        return (
            open_tag
            + inner
            + f'<button type="button" class="src" data-from-seg="{seg}" '
            f'aria-label="Source turns for {seg}">Source</button></p>'
        )

    head2 = re.sub(
        r"<p(?:\s[^>]*)?>(.*?)</p>",
        repl_p,
        head,
        flags=re.S | re.I,
    )
    html = head2 + tail

    # Update transcript note + FLAG set + render dispositions + Source wiring
    html = html.replace(
        "Flagged turns await a human split.",
        "Flagged turns carry an explicit disposition "
        "(kept-overlap-marked, kept-doubt-marked, noise-trimmed, or noise-only-held).",
    )

    # Replace FLAG set and turn rendering + add jumpFrom / wire Source
    old_v4 = "/* v4 additions */"
    if old_v4 not in html:
        raise SystemExit("v4 additions marker missing")

    new_js = r"""/* v4 additions */
const PASSAGES=JSON.parse($('#passagesData').textContent);
const FROM=Object.fromEntries((PASSAGES.comprehensive||[]).map(p=>[p.id,p.from||[]]));
FROM.water=(PASSAGES.descriptive&&PASSAGES.descriptive[0]&&PASSAGES.descriptive[0].from)||[];
FROM.v09=(PASSAGES.illustrative&&PASSAGES.illustrative[0]&&PASSAGES.illustrative[0].from)||[];
const MODES=['interactive','illustrative','comprehensive','descriptive','transcriptive'];
const TURNS=JSON.parse($('#turnsData').textContent);
function flagLabel(t){
  const f=(t.flags&&t.flags.length)?t.flags.join(' · '):'';
  const d=t.disposition?String(t.disposition):'';
  const doubt=f.includes('transcription-doubt')||d.includes('doubt');
  return {f,d,doubt,flagged:!!(f||d&&d!=='noise-trimmed')};
}
$('#tList').innerHTML=TURNS.map(t=>{
  const L=flagLabel(t);
  const mark=L.doubt?' · [?]':'';
  const fl=L.f?` · ${L.f.toUpperCase()}`:(L.d&&L.d!=='noise-trimmed'?` · ${L.d.toUpperCase()}`:'');
  return `<div class="turn ${t.speaker==='claude'?'cl':''}${L.f?' flagged':''}" id="${t.id}" data-disposition="${L.d||''}"><div class="tk">${t.speaker.toUpperCase()} · ${t.via.toUpperCase()} · TIME ABSENT${fl}${mark}</div><p></p>${L.d?`<div class="disp">${L.d.replace(/-/g,' ')}</div>`:''}</div>`;
}).join('');
TURNS.forEach(t=>{document.querySelector('#'+t.id+' p').textContent=t.text});
function jumpFrom(ids){
  const list=(ids||[]).map(id=>document.getElementById(id)).filter(Boolean);
  setMode('transcriptive',true);
  $('#tSess').open=true;
  if(list[0])requestAnimationFrame(()=>list[0].scrollIntoView({block:'center'}));
  list.forEach(el=>{el.style.outline='2px solid var(--focal)';setTimeout(()=>el.style.outline='',1600)});
}
function doFind(){const q=$('#tFind').value.trim().toLowerCase();let n=0;$$('#tList .turn').forEach((el,i)=>{const m=!q||TURNS[i].text.toLowerCase().includes(q);el.classList.toggle('hide',!m);if(m)n++});$('#tCount').textContent=q?n+' of '+TURNS.length+' turns':'';if(q)$('#tSess').open=true}
$('#tFind').oninput=doFind;
const DP=$$('#water .step').map(st=>({n:+st.querySelector('.dot b').textContent,t:st.querySelector('h4').textContent,rows:$$('.row',st).map(r=>[r.children[0].textContent,r.children[1].textContent])}));
$('#dList').innerHTML=DP.map(p=>`<div class="dpass" data-seg="water"><span class="kicker">Body ${p.n} · Step ${p.n}</span><h3></h3>${p.rows.map(()=>'<p class="drow"><span class="chip e"></span><span></span></p>').join('')}<div class="links"><button data-df="${p.n}:comprehensive">Read ↗</button><button data-df="${p.n}:illustrative">Seen ↗</button><button data-df="${p.n}:interactive">Interactive ↗</button><button type="button" class="src" data-from-seg="water">Source ↗</button></div></div>`).join('');
$$('#dList .dpass').forEach((el,i)=>{el.querySelector('h3').textContent=DP[i].t;$$('.drow',el).forEach((r,j)=>{r.children[0].textContent=DP[i].rows[j][0];r.children[1].textContent=DP[i].rows[j][1]})});
$$('[data-df]').forEach(b=>b.onclick=()=>{const[n,m]=b.dataset.df.split(':');setFocus(+n,true);setMode(m)});
document.addEventListener('click',e=>{const b=e.target.closest('[data-from-seg]');if(!b)return;jumpFrom(FROM[b.dataset.fromSeg]||[])});
/* illustrative figure source */
$$('figure.fig').forEach(fig=>{
  if(fig.querySelector('.src'))return;
  const cap=fig.querySelector('figcaption');
  const btn=document.createElement('button');
  btn.type='button';btn.className='src';btn.dataset.fromSeg='v09';btn.textContent='Source';
  (cap||fig).appendChild(btn);
});
const _sm=setMode;
setMode=function(m,jump=true){main.dataset.mode=m;$$('[role="tab"][data-mode]').forEach(t=>{const on=t.dataset.mode===m;t.setAttribute('aria-selected',on);t.tabIndex=on?0:-1;if(on&&t.parentElement.closest('.modebar:not(.bottom)'))main.setAttribute('aria-labelledby',t.id||'')});
  $('#modeHint').textContent=HINT[m];
  if(m==='interactive'){drawNet();if(jump)main.scrollIntoView({block:'start'})}
  else if(m==='descriptive'||m==='transcriptive'){if(jump)(m==='transcriptive'?$('#transView'):$('#descView')).scrollIntoView({block:'start'})}
  else if(jump){const t=m==='comprehensive'?document.getElementById('body-'+F.focus):$('#figLoop');if(m==='illustrative'&&window.__loopSel)window.__loopSel(F.focus);if(t)requestAnimationFrame(()=>t.scrollIntoView({block:'start'}))}
  try{history.replaceState(null,'','#m='+m+'&r=b'+F.focus)}catch(e){}
  updatePager()};
$$('[role="tab"][data-mode]').forEach(t=>{t.onclick=()=>setMode(t.dataset.mode);t.onkeydown=e=>{const i=MODES.indexOf(t.dataset.mode);let j=i;if(e.key==='ArrowRight')j=(i+1)%5;else if(e.key==='ArrowLeft')j=(i+4)%5;else if(e.key==='Home')j=0;else if(e.key==='End')j=4;else return;e.preventDefault();setMode(MODES[j],false);const tb=t.parentElement.querySelector('[data-mode="'+MODES[j]+'"]');tb&&tb.focus()}});
const _up=updatePager,_pp=$('#pgPrev').onclick,_pn=$('#pgNext').onclick;
function altList(){const m=main.dataset.mode;return m==='descriptive'?$$('#dList .dpass'):null}
updatePager=function(){const a=altList();if(a){$('#pgPrev').disabled=$('#pgNext').disabled=false;$('#pgPrev').textContent='← Previous';$('#pgNext').textContent='Next →';return}if(main.dataset.mode==='transcriptive'){$('#pgPrev').disabled=$('#pgNext').disabled=true;return}_up()};
const step=d=>()=>{const a=altList();if(a){const i=a.findIndex(x=>x.getBoundingClientRect().top>8);const k=Math.max(0,Math.min(a.length-1,(d>0?(i<0?a.length-1:i):(i<0?a.length-1:i-1))));a[k].scrollIntoView({block:'start'})}else(d>0?_pn:_pp)()};
$('#pgPrev').onclick=step(-1);$('#pgNext').onclick=step(1);
/* facets */
const _di=drawInsp;
drawInsp=function(){_di();const b=F.sel,ins=$('#netInsp');const rd=document.querySelector('#body-'+b+' p'),dp=DP.find(p=>p.n===b);
 const bodySeg=rd&&rd.closest('[data-seg]')||rd; const seg=bodySeg&&bodySeg.getAttribute&&bodySeg.getAttribute('data-seg');
 const said=(seg&&FROM[seg])||[];
 const f=(k,sum,ex,m)=>`<div class="facet"><span class="fs">+ ${k} · ${sum}</span>${ex?'<p></p>':''}<button data-fo="${m}">Open ${m} ↗</button></div>`;
 ins.insertAdjacentHTML('beforeend',f('Said',said.length?said.length+' TURNS':'NO LINKED TURNS',said.length,'transcriptive')+f('Explained',dp?'1 PASSAGE':'NONE YET',!!dp,'descriptive')+f('Read','1 PASSAGE',!!rd,'comprehensive')+f('Seen','1 FIGURE',0,'illustrative'));
 const ps=$$('.facet p',ins);let k=0;if(said.length)ps[k++].textContent=(TURNS.find(t=>t.id===said[0])||{}).text||said.join(', ');if(dp)ps[k++].textContent=dp.rows[0][1];if(rd)ps[k++].textContent=rd.textContent;
 $$('[data-fo]',ins).forEach(x=>x.onclick=()=>{setFocus(b,true);if(x.dataset.fo==='transcriptive'&&said.length)jumpFrom(said);else setMode(x.dataset.fo)})};
/* hash + start */
(function(){const h=new URLSearchParams(location.hash.slice(1));const m=h.get('m'),r=h.get('r');if(r&&/^b[1-9]$/.test(r))setFocus(+r.slice(1),true);F.sel=F.focus;setMode(MODES.includes(m)?m:'interactive',false)})();
})();
"""

    # Replace from /* v4 additions */ through end of script
    html = re.sub(
        r"/\* v4 additions \*/.*?\)\(\);\s*</script>",
        new_js + "\n</script>",
        html,
        count=1,
        flags=re.S,
    )
    return html


def write_disposition_md(turns: list[dict]) -> None:
    lines = [
        "# Flagged turn dispositions",
        "",
        "Locked against `source/transcript.json` (127 turns). "
        "Thirteen CONVERSION.md flags plus two transcription-doubt ids.",
        "",
        "| id | disposition | flags now | note |",
        "|---|---|---|---|",
    ]
    by = {t["id"]: t for t in turns}
    for tid in FLAG_IDS:
        t = by[tid]
        flags = ",".join(t.get("flags") or []) or "—"
        lines.append(
            f"| {tid} | {t.get('disposition','')} | {flags} | {t.get('disposition_note','').replace('|','/')} |"
        )
    lines.append("")
    DISP_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    html = HTML_PATH.read_text(encoding="utf-8")
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    tr = json.loads(TR_PATH.read_text(encoding="utf-8"))
    turns = tr["turns"]
    assert len(turns) == 127, len(turns)

    # Prefer turns already mirrored in data if present
    if data.get("turns") and len(data["turns"]) == 127:
        # sync text from source transcript as canonical
        src_by = {t["id"]: t for t in turns}
        for t in data["turns"]:
            if t["id"] in src_by:
                t["text"] = src_by[t["id"]]["text"]
                t["flags"] = list(src_by[t["id"]].get("flags") or [])
                t["speaker"] = src_by[t["id"]]["speaker"]
                t["via"] = src_by[t["id"]]["via"]
        turns = data["turns"]
    else:
        data["turns"] = turns

    turns = apply_flag_resolutions(turns)
    # write back to transcript + data
    tr["turns"] = turns
    # strip text_before_trim from public transcript? keep for audit in data only
    pub_turns = []
    for t in turns:
        pt = {k: v for k, v in t.items() if k != "text_before_trim"}
        pub_turns.append(pt)
    tr["turns"] = pub_turns
    TR_PATH.write_text(json.dumps(tr, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    paras = extract_comprehensive_paras(html)
    data = fill_from_arrays(data, paras, pub_turns)
    data["turns"] = turns  # keep trim audit in data
    data["meta"]["version"] = "4"
    DATA_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    html2 = inject_passages_and_links(html, data, pub_turns)
    HTML_PATH.write_text(html2, encoding="utf-8")
    write_disposition_md(pub_turns)

    # stats
    filled = sum(1 for p in data["passages"]["comprehensive"] if p["from"])
    empty = sum(1 for p in data["passages"]["comprehensive"] if not p["from"])
    all_ids = {t["id"] for t in pub_turns}
    bad = []
    for group in data["passages"].values():
        for p in group:
            for tid in p.get("from") or []:
                if tid not in all_ids:
                    bad.append(tid)
    still_flagged = [t["id"] for t in pub_turns if t.get("flags")]
    print(f"paras_extracted={len(paras)}")
    print(f"comprehensive_filled={filled} empty={empty}")
    print(f"descriptive_from={data['passages']['descriptive'][0]['from']}")
    print(f"illustrative_from={data['passages']['illustrative'][0]['from']}")
    print(f"invalid_ids={bad}")
    print(f"still_flagged={still_flagged}")
    print(f"html={HTML_PATH}")
    print(f"disposition={DISP_PATH}")


if __name__ == "__main__":
    main()
