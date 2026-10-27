
(function(){
  const NAMES={101:'Consequential',111:'Deterministic','011':'Propositional','010':'Environmental',110:'Reproducible',100:'Contractual','000':'Transmissible','001':'Transformational'};
  const ROUTE=['101','111','011','010','110','100','000','001'];
  const HUE={101:1,111:2,'011':3,'010':4,110:5,100:6,'000':7,'001':8};
  function el(root, html){root.innerHTML=html}
  function mountToggle(root){
    el(root,'<span class="kicker">Way</span><div class="pills" role="group"></div>');
    const row=root.querySelector('.pills');
    ['One','Two','Three'].forEach((name,i)=>{
      const b=document.createElement('button');b.type='button';b.textContent=name;b.setAttribute('aria-pressed',i===0);
      b.onclick=()=>{[...row.children].forEach(x=>x.setAttribute('aria-pressed',x===b))};row.appendChild(b);
    });
  }
  function mountViewTabs(root){
    const modes=['Interactive','Illustrative','Comprehensive','Descriptive','Transcriptive'];
    el(root,'<div class="tabs" role="tablist"></div><p id="panel"></p>');
    const list=root.querySelector('.tabs');const panel=root.querySelector('#panel');
    modes.forEach((name,i)=>{
      const b=document.createElement('button');b.type='button';b.textContent=name;b.setAttribute('role','tab');
      b.setAttribute('aria-selected',i===0);b.tabIndex=i===0?0:-1;
      b.onclick=()=>{[...list.children].forEach((x,n)=>{x.setAttribute('aria-selected',x===b);x.tabIndex=x===b?0:-1});panel.textContent=name};
      list.appendChild(b);
    });
    panel.textContent='Interactive';
  }
  function mountNodeRoute(root){
    el(root,'<span class="kicker">Step 1 of 8</span><div class="pills" id="nodes"></div><p id="code"></p><button type="button" id="next">Next step</button>');
    let step=0;
    const nodes=root.querySelector('#nodes');const label=root.querySelector('.kicker');const code=root.querySelector('#code');
    function draw(){nodes.innerHTML='';ROUTE.forEach((c,i)=>{const b=document.createElement('button');b.type='button';b.textContent=String(i+2);b.style.background=i===step?'var(--focal)':'var(--n'+HUE[c]+')';b.style.color='var(--on-node)';b.setAttribute('aria-pressed',i===step);nodes.appendChild(b)});label.textContent='Step '+(step+1)+' of 8';code.textContent=ROUTE[step]+' · '+NAMES[ROUTE[step]]}
    root.querySelector('#next').onclick=()=>{step=(step+1)%8;draw()};draw();
  }
  function mountInspector(root){
    el(root,'<aside class="card"><span class="kicker">Body 2 · 101</span><h2 style="font:650 20px/1.2 var(--serif);margin:8px 0">Legal</h2><p>The embodied agent argues. The authoritative body decides. The authoritative agent records.</p><button type="button" id="close">Close</button><dl><dt class="kicker">Code</dt><dd>101 · Consequential</dd></dl></aside>');
    root.querySelector('#close').onclick=()=>{root.querySelector('aside').hidden=true};
  }
  function mountCompass(root){
    el(root,'<span class="kicker">Reference · bridge</span><svg viewBox="0 0 240 240" width="100%" role="img" aria-label="Compass with a core and eight nodes"></svg>');
    const svg=root.querySelector('svg');
    let h='<circle cx="120" cy="120" r="28" fill="var(--surface)" stroke="var(--ink)" stroke-width="1.6"/>';
    h+='<text x="120" y="125" text-anchor="middle" font-size="16" font-family="ui-monospace,monospace" fill="var(--ink)">1</text>';
    ROUTE.forEach((c,i)=>{const a=(-90+i*45)*Math.PI/180;const x=120+80*Math.cos(a),y=120+80*Math.sin(a);
      h+='<line x1="120" y1="120" x2="'+x+'" y2="'+y+'" stroke="var(--ink-3)" stroke-dasharray="1.5 5"/>';
      h+='<circle cx="'+x+'" cy="'+y+'" r="14" fill="var(--n'+HUE[c]+')" stroke="var(--ink)" stroke-width="1.6"/>';
      h+='<text x="'+x+'" y="'+(y+4)+'" text-anchor="middle" font-size="10" font-family="ui-monospace,monospace" fill="var(--on-node)">'+(i+2)+'</text>';
    });
    svg.innerHTML=h;
  }
  function mountChip(root){el(root,'<span class="chip"><i style="--c:var(--act)"></i>Act</span> <span class="chip"><i style="--c:var(--decide)"></i>Decide</span> <span class="chip"><i style="--c:var(--record)"></i>Record</span>')}
  function mountTable(root){el(root,'<table><thead><tr><th>Body</th><th>Code</th></tr></thead><tbody><tr><td>Legal</td><td>101</td></tr><tr><td>Enforcement</td><td>111</td></tr></tbody></table>')}
  function mountSpine(root){el(root,'<div class="spine"><b>1</b><div class="card"><span class="kicker">Passes forward</span><p style="margin:6px 0 0">A shared conviction.</p></div></div>')}
  function mountCanCannot(root){el(root,'<div class="yes"><span class="kicker">Does</span><p>Records authorised material.</p></div><div class="no"><span class="kicker">Cannot</span><p><s>Argue a case</s></p></div>')}
  function mountStatus(root){el(root,'<span class="status"><i></i>Scored</span>')}
  function mountFold(root){el(root,'<button type="button" class="pills" id="f" aria-expanded="true" style="border:1px solid var(--control);border-radius:999px;background:transparent;padding:8px 11px;font:700 11.5px var(--sans)">Collapse</button><p id="body">The part is open.</p>');root.querySelector('#f').onclick=e=>{const on=e.target.getAttribute('aria-expanded')==='true';e.target.setAttribute('aria-expanded',!on);e.target.textContent=on?'Expand':'Collapse';root.querySelector('#body').hidden=on}}
  function mountTrail(root){el(root,'<span class="kicker">Trail</span><div class="pills"><button type="button">1</button><button type="button">→ 3</button></div>')}
  function mountRail(root){el(root,'<span class="kicker">Contents</span><div class="pills"><button type="button" aria-pressed="true">Positions</button><button type="button">Loop</button></div>')}
  function mountMatrix(root){el(root,'<table><thead><tr><th>Code</th><th>Name</th></tr></thead><tbody id="rows"></tbody></table>');const body=root.querySelector('#rows');ROUTE.forEach(c=>{const tr=document.createElement('tr');tr.innerHTML='<td>'+c+'</td><td>'+NAMES[c]+'</td>';tr.onclick=()=>{mountCompass.sel=c;tr.style.outline='2px solid var(--focal)'};body.appendChild(tr)})}
  function mountCrossRef(root){el(root,'<button type="button" class="chip"><i style="--c:var(--n1)"></i>101 · Consequential</button>')}
  function mountTranscript(root){el(root,'<article><span class="kicker">PERCY · VOICE</span><p>what are other thingts like religion, family, education.</p></article><article style="color:var(--ink-2);margin-left:24px"><span class="kicker">CLAUDE · TEXT</span><p>You are listing the major domains.</p></article><input class="find" aria-label="Find" placeholder="Find" style="margin-top:8px;border:1px solid var(--control);border-radius:999px;padding:8px 12px">')}
  function mountScript(root){el(root,'<span class="kicker">Descriptive · water</span><p>Residents who share a water supply suspect contamination. The concern forms in bodies 8 and 9 before it ever reaches government.</p>')}
  window.FieldNotation={mountToggle,mountViewTabs,mountNodeRoute,mountInspector,mountCompass,mountChip,mountTable,mountSpine,mountCanCannot,mountStatus,mountFold,mountTrail,mountRail,mountMatrix,mountCrossRef,mountTranscript,mountScript};
})();
