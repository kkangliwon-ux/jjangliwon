// usage: node render.js   (put photos in ./photos/01.jpg … 09.jpg, then re-run)
const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
(async()=>{const dir=__dirname;const D=JSON.parse(fs.readFileSync(dir+'/slides.json'));
const have=D.map(d=>fs.existsSync(path.join(dir,'photos',d.photo)));
fs.writeFileSync(dir+'/_build.html',fs.readFileSync(dir+'/template.html','utf8').replace('__DATA__',JSON.stringify(D)).replace('__HAVE__',JSON.stringify(have)));
const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350}});
await p.goto('file://'+dir+'/_build.html',{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);
fs.mkdirSync(dir+'/out',{recursive:true});
for(let i=1;i<=D.length;i++){await p.locator('#s'+i).screenshot({path:`${dir}/out/slide_${String(i).padStart(2,'0')}.png`});}
await b.close();console.log('photos found:',have.filter(Boolean).length,'/',D.length);})();
