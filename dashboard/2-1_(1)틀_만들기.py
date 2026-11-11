# -*- coding: utf-8 -*-
"""[내부망 주피터 · 최초 1회] 대시보드 틀(화면)을 만든다. 실행하면 현재 폴더에 2-1_대시보드_틀.html 이 생긴다.

기존 대시보드 모양(한도 카드·전월 대비·도넛·한도 대비 청약률·구성·WM 영업점 비중)에 청약월 선택(2026.10/2026.11)과 일차 버튼을 넣은 틀이다.
화면을 바꿨을 때만 다시 실행한다. 숫자는 들어 있지 않다(숫자는 2-1 청약현황 코드가 누적 데이터에서 채운다).
- 이 파일은 2-1_대시보드_누적데이터.json 을 건드리지 않는다. 기존 틀은 2-1_대시보드_틀_백업.html 로 보관한다.
- 들여쓰기가 필요한 줄이 없다(복사 중 줄 앞 공백이 사라져도 실행된다)."""

import os, shutil

OUT = '2-1_대시보드_틀.html'

HTML = r'''<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>__TITLE__</title>
<style id="css">
*{box-sizing:border-box}
html,body{margin:0}
body{background:#eef2f6;color:#1b2a3a;font-family:'Malgun Gothic','Apple SD Gothic Neo','Noto Sans KR',sans-serif;font-size:14px;line-height:1.45}
.wrap{max-width:1320px;margin:0 auto;padding:22px 28px 40px}
.top{display:flex;align-items:flex-start;gap:18px;flex-wrap:wrap;margin-bottom:16px}
.tl{flex:1 1 420px}
h1{font-size:26px;margin:0 0 4px;letter-spacing:-.5px}
.sub{color:#6b7a8a;font-size:13px}
.ctl{display:flex;align-items:center;gap:10px;flex-wrap:wrap}
select{font:inherit;font-size:15px;padding:8px 12px;border:1px solid #d5dbe1;border-radius:8px;background:#fff;color:#1b2a3a}
.dtabs{display:flex;gap:6px;background:#fff;border:1px solid #e2e8ee;border-radius:12px;padding:5px}
.dt{border:0;background:none;font:inherit;font-size:15px;padding:8px 16px;border-radius:8px;cursor:pointer;color:#1b2a3a}
.dt.on{background:#0d3a78;color:#fff;font-weight:700}
.dt.dis{color:#b4bec8;cursor:default}
.acts{display:flex;gap:8px}
.bt{font:inherit;font-size:13px;padding:9px 16px;border-radius:8px;border:1px solid #d5dbe1;background:#fff;color:#6b7a8a;cursor:pointer}
.bt.pri{background:#0d3a78;border-color:#0d3a78;color:#fff;font-weight:700}
.lims{display:grid;grid-template-columns:repeat(6,1fr);gap:10px;margin-bottom:14px}
.lc{background:#f7f9fb;border:1px solid #e2e8ee;border-radius:12px;padding:12px 14px}
.lc.sel{background:#e6ecf2;border-color:#b7c4d1}
.lt{font-size:12.5px;color:#4c5b6b;font-weight:600}
.lv{font-size:26px;font-weight:800;margin:2px 0}
.lv small{font-size:13px;font-weight:600;margin-left:3px}
.ld{font-size:12px;color:#6b7a8a}
.up{color:#c0242b;font-weight:700}
.dn{color:#1f5fbf;font-weight:700}
.cadd{display:inline-block;border:0;background:#e9eef3;border-radius:8px;padding:6px 12px;font:inherit;font-size:12.5px;color:#4c5b6b;cursor:pointer;margin-bottom:14px}
.cbox{background:#fff;border:1px solid #e2e8ee;border-radius:12px;padding:14px 18px;margin-bottom:14px}
.cbox .ln{white-space:pre-wrap;margin:2px 0;font-size:14.5px}
.cbox b.k{color:#0b7a6b}
.cbox .bar{display:flex;gap:6px;margin-top:8px}
.cbox textarea{width:100%;min-height:140px;font:inherit;border:1px solid #d5dbe1;border-radius:8px;padding:8px;white-space:pre-wrap}
.sm{font:inherit;font-size:12px;padding:4px 12px;border:1px solid #d5dbe1;border-radius:6px;background:#fff;cursor:pointer}
.row3{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-bottom:18px}
.card{background:#fff;border:1px solid #e2e8ee;border-radius:16px;padding:20px 22px;box-shadow:0 2px 8px rgba(20,40,70,.05)}
.card h3{margin:0 0 6px;font-size:18px}
.big{font-size:38px;font-weight:800;letter-spacing:-1px}
.big small{font-size:14px;font-weight:600;color:#6b7a8a;margin-left:4px}
.dl{margin:4px 0 14px;font-size:14px}
.bars{display:flex;justify-content:space-around;align-items:flex-end;height:150px;margin:6px 0 4px}
.bc{display:flex;flex-direction:column;align-items:center;justify-content:flex-end;height:100%;width:42%}
.bv{font-weight:800;font-size:15px;margin-bottom:4px;color:#445}
.bv small{font-size:10.5px;font-weight:600;color:#6b7a8a}
.bb{width:100%;border-radius:4px}
.bl{font-size:13px;margin-top:6px;color:#445;text-align:center}
.cnt{margin:8px 0 12px;font-size:14px;font-weight:600;border-bottom:1px solid #eef2f6;padding-bottom:12px}
.ph{font-size:12.5px;color:#4c5b6b;font-weight:600;margin-bottom:6px}
.dv{display:grid;grid-template-columns:42% 1fr;align-items:center;height:30px;font-size:13.5px}
.dz{position:relative;height:100%}
.dz i{position:absolute;top:7px;height:16px;display:block}
.dz em{position:absolute;top:5px;font-style:normal;font-weight:700;font-size:13px}
.dz u{position:absolute;top:2px;bottom:2px;width:1px;background:#8b97a3}
.row2{display:grid;grid-template-columns:minmax(300px,34%) 1fr;background:#fff;border:1px solid #e2e8ee;border-radius:16px;margin-bottom:18px;box-shadow:0 2px 8px rgba(20,40,70,.05)}
.row2>div{padding:22px}
.row2>div:first-child{border-right:1px solid #eef2f6}
.row2 h3{margin:0 0 12px;font-size:18px}
.leg{display:grid;grid-template-columns:14px 1fr auto 56px;gap:4px 8px;align-items:center;font-size:13px;margin-top:12px}
.leg i{width:10px;height:10px;display:block}
.leg .r{text-align:right;color:#6b7a8a}
.sp{grid-column:1/-1;margin:2px 0 6px}
.sp div{display:flex;height:10px;border-radius:2px;overflow:hidden}
.sp p{display:flex;justify-content:space-between;margin:2px 0 0;font-size:11px}
.lh{display:flex;gap:14px;flex-wrap:wrap;font-size:12.5px;color:#4c5b6b;margin-bottom:10px}
.lh i{display:inline-block;width:10px;height:10px;margin-right:4px;vertical-align:middle}
.lr,.lg{display:grid;grid-template-columns:120px 1fr 62px 62px 52px 62px;gap:6px;align-items:center;min-height:46px;font-size:14px}
.lg{min-height:24px;color:#6b7a8a;font-size:12.5px}
.lg b{text-align:right;font-weight:700}
.lg b.o{color:#e8731a}
.lr .ln{font-weight:600}
.lr .n{text-align:right;font-variant-numeric:tabular-nums}
.lr .n2{font-weight:800}
.lr .n3{color:#e8731a;font-weight:700}
.lr.tot{border-top:1px solid #e2e8ee;margin-top:6px}
.trk{position:relative;height:30px;background:#eef2f5;border-radius:3px}
.trk s{position:absolute;top:3px;bottom:3px;display:block;text-decoration:none}
.trk .mk{position:absolute;top:-3px;bottom:-3px;width:2px;background:#10243a}
.trk .mk.ds{background:none;border-left:2px dotted #10243a}
.trk .pc{position:absolute;top:5px;font-weight:800;font-size:14px}
.cmp{background:#fff;border:1px solid #e2e8ee;border-radius:16px;padding:22px;margin-bottom:18px;box-shadow:0 2px 8px rgba(20,40,70,.05)}
.cmp>h3{margin:0 0 14px;font-size:18px}
.cmp .two{display:grid;grid-template-columns:1fr 1fr;gap:20px}
.pn{background:#fafbfc;border:1px solid #eef2f6;border-radius:12px;padding:16px 18px}
.pn h4{margin:0 0 6px;font-size:15px;font-weight:600}
.pl{display:flex;gap:14px;font-size:14px;font-weight:600;margin-bottom:10px}
.pl i{display:inline-block;width:14px;height:14px;border-radius:3px;margin-right:5px;vertical-align:-2px}
.sr{display:grid;grid-template-columns:70px 1fr;align-items:center;margin:14px 0}
.sr>span{font-size:13px;color:#4c5b6b}
.sb{display:flex;height:80px}
.sb div{display:flex;flex-direction:column;align-items:center;justify-content:center;color:#fff;font-weight:800;font-size:18px;min-width:0;overflow:hidden}
.sb small{font-size:12px;font-weight:700;opacity:.95}
.wm{background:#fff;border:1px solid #e2e8ee;border-radius:16px;padding:22px;box-shadow:0 2px 8px rgba(20,40,70,.05)}
.wm>h3{margin:0 0 14px;font-size:18px}
.wm .c3{display:grid;grid-template-columns:repeat(3,1fr);gap:26px}
.wm h4{margin:0 0 6px;text-align:center;font-size:15px;font-weight:600}
.hb{height:10px;border-radius:5px}
.hs{font-size:11px;font-weight:700;margin:2px 0 8px}
.wr{display:grid;grid-template-columns:18px 1fr auto 52px;gap:2px 8px;align-items:end;font-size:13px;margin:6px 0}
.wr span.rk{color:#8b97a3}
.wr span.v{text-align:right;font-variant-numeric:tabular-nums}
.wr span.p{text-align:right;color:#4c5b6b}
.wr .bb2{grid-column:2/5;height:7px;background:#eef2f5;border-radius:4px;overflow:hidden}
.wr .bb2 i{display:block;height:100%;border-radius:4px}
.empty{padding:60px;text-align:center;color:#6b7a8a}
@media(max-width:1000px){.row3,.row2,.cmp .two,.wm .c3{grid-template-columns:1fr}.lims{grid-template-columns:repeat(2,1fr)}.row2>div:first-child{border-right:0}}
@media print{body{background:#fff}.acts,.cadd,.ctl select{display:none}.wrap{padding:0}}
</style>
</head>
<body>
<div id="page" class="wrap">
  <div class="top">
    <div class="tl"><h1 id="ttl"></h1><div class="sub" id="sub"></div></div>
    <div class="ctl"><select id="msel"></select><div class="dtabs" id="days"></div></div>
    <div class="acts"><button class="bt pri" id="bImg">이미지로 저장</button><button class="bt" id="bPdf">PDF 출력</button></div>
  </div>
  <div id="app"></div>
</div>
<script>
var TITLE = '__TITLE__';
var DATA = /*__DATA__*/null;
(function(){
var NM = ['3년물(이표)','3년물(복리)','5년물','10년물','20년물'];
var DON = ['#0b7a6b','#129683','#1ba891','#6dccb8','#a9dfd2'];
var OR='#e8731a', OR2='#f6c59f', NV='#0d3a78', NV2='#86a3bd', GR='#13a38c', GY='#d5dbe1';
function $(id){ return document.getElementById(id); }
var months = [];
var sel = {ym:null, n:1, edit:false};

function esc(s){ return String(s).replace(/[&<>"]/g,function(c){ return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]; }); }
function sum(a){ var s=0,i; if(!a) return 0; for(i=0;i<a.length;i++) s+=(a[i]||0); return s; }
function fmt(v,d){ return Number(v).toLocaleString('ko-KR',{minimumFractionDigits:d,maximumFractionDigits:d}); }
function f1(v){ return fmt(v/10,1); }
function fe(v){ return fmt(v,1); }
function fi(v){ return fmt(v,0); }
function sgn(v){ var x=Math.abs(v/10).toFixed(1); return (v>0?'+':(v<0?'−':''))+x; }
function lrm(vals,target){
  var fl=vals.map(function(v){ return Math.floor(v+1e-9); }),rem=vals.map(function(v,i){ return v-fl[i]; });
  var diff=target-sum(fl),order=vals.map(function(v,i){ return i; }).sort(function(a,b){ return diff>0? rem[b]-rem[a] : rem[a]-rem[b]; }),k;
  for(k=0;k<Math.abs(diff)&&k<order.length;k++) fl[order[k]]+= diff>0?1:-1;
  return fl;
}
function snapsOf(ym){ var o=DATA[ym]||{}; return Object.keys(o).map(Number).sort(function(a,b){return a-b;}).map(function(k){ return o[String(k)]; }); }
function getSnap(ym,n){ var o=DATA[ym]; return o? (o[String(n)]||null):null; }
function latestN(ym){ var a=snapsOf(ym); return a.length? a[a.length-1].n:1; }
function ymDot(ym){ return ym.slice(0,4)+'.'+ym.slice(5,7); }
function dDot(d){ return d? d.slice(0,4)+'.'+parseInt(d.slice(5,7),10)+'.'+parseInt(d.slice(8,10),10):''; }

/* 코멘트 */
function mk(line){
  var t=esc(line);
  t=t.replace(/\*\*(.+?)\*\*/g,'<b class="k">$1</b>');
  t=t.replace(/\^\^(.+?)\^\^/g,'<span class="up">$1</span>');
  t=t.replace(/~~(.+?)~~/g,'<span class="dn">$1</span>');
  return t;
}
function ckey(s){ return 'c21:'+sel.ym+':'+s.n; }
function getComment(s){
  var raw=null;
  try{ raw=localStorage.getItem(ckey(s)); }catch(e){}
  return (raw===null||raw===undefined)? (s.comment||[]).join('\n'):raw;
}
function commentBox(s){
  var raw=getComment(s),h,lines,i;
  if(sel.edit){
    return '<div class="cbox"><textarea id="cmt">'+esc(raw)+'</textarea><div class="bar"><button class="sm" data-a="save">저장</button><button class="sm" data-a="cancel">취소</button><button class="sm" data-a="reset">초안으로 되돌리기</button></div><div style="font-size:11px;color:#6b7a8a;margin-top:6px">**굵게(청록)**, ^^빨강^^, ~~파랑~~ · 줄 앞 공백 두 칸은 들여쓰기</div></div>';
  }
  if(!raw.replace(/\s/g,'')) return '<button class="cadd" data-a="edit">+ 코멘트 추가</button>';
  lines=raw.split('\n'); h='<div class="cbox">';
  for(i=0;i<lines.length;i++) h+='<div class="ln">'+(mk(lines[i])||'&nbsp;')+'</div>';
  return h+'<div class="bar"><button class="sm" data-a="edit">편집</button></div></div>';
}

/* 한도 카드 */
function limDelta(cur,prev){
  if(prev===undefined||prev===null) return '전월 대비 -';
  var d=cur-prev; if(!d) return '전월 대비 -';
  return '전월 대비 <span class="'+(d>0?'up':'dn')+'">'+(d>0?'+':'−')+fi(Math.abs(d))+'억원</span>';
}
function limCards(s){
  var L=s.limits; if(!L) return '';
  var P=s.prev&&s.prev.limits? s.prev.limits:null,h='<div class="lims">',i;
  h+='<div class="lc sel"><div class="lt">총 발행한도</div><div class="lv">'+fi(sum(L))+'<small>억원</small></div><div class="ld">'+limDelta(sum(L),P?sum(P):null)+'</div></div>';
  for(i=0;i<5;i++) h+='<div class="lc"><div class="lt">'+NM[i]+' 발행한도</div><div class="lv">'+fi(L[i])+'<small>억원</small></div><div class="ld">'+limDelta(L[i],P?P[i]:null)+'</div></div>';
  return h+'</div>';
}

/* 요약 카드 3개 */
function divRows(rows){
  var mx=0,i,h='',r,w;
  for(i=0;i<rows.length;i++) if(rows[i]&&Math.abs(rows[i].d)>mx) mx=Math.abs(rows[i].d);
  for(i=0;i<rows.length;i++){
    r=rows[i];
    if(!r){ h+='<div class="dv"><span></span><div class="dz"></div></div>'; continue; }
    w=mx? Math.abs(r.d)/mx:0;
    h+='<div class="dv"><span>'+r.name+'</span><div class="dz"><u style="left:22%"></u>';
    if(r.d>0) h+='<i style="left:22%;width:'+(w*56)+'%;background:#c0242b"></i><em style="left:'+(22+w*56+2)+'%">'+sgn(r.d)+'</em>';
    else if(r.d<0) h+='<i style="left:'+(22-w*20)+'%;width:'+(w*20)+'%;background:#1f5fbf"></i><em style="left:24%">'+sgn(r.d)+'</em>';
    else h+='<em style="left:24%">0.0</em>';
    h+='</div></div>';
  }
  return h;
}
function sumCard(o,s){
  var p=s.prev,mx=Math.max(o.cur,o.prev||0),hc=mx? o.cur/mx*104:0,hp=mx? (o.prev||0)/mx*104:0,h='<div class="card"><h3>'+o.title+'</h3>';
  h+='<div class="big">'+f1(o.cur)+'<small>억원</small></div>';
  if(p){ var d=o.cur-o.prev; h+='<div class="dl"><span class="'+(d>=0?'up':'dn')+'">'+(d>=0?'↗ ':'↘ ')+sgn(d)+'억원</span> 전월 '+s.n+'일차 대비</div>'; }
  else h+='<div class="dl" style="color:#6b7a8a">전월 비교 자료 없음</div>';
  h+='<div class="bars">';
  if(p) h+='<div class="bc"><div class="bv">'+f1(o.prev)+' <small>억원</small></div><div class="bb" style="height:'+hp+'px;background:#d8dde2;border:1px dashed #b7c0c9"></div><div class="bl">'+p.month+'월 '+s.n+'일차</div></div>';
  h+='<div class="bc"><div class="bv">'+f1(o.cur)+' <small>억원</small></div><div class="bb" style="height:'+hc+'px;background:'+o.color+'"></div><div class="bl">'+parseInt(sel.ym.slice(5,7),10)+'월 '+s.n+'일차</div></div></div>';
  h+='<div class="cnt">'+o.info+'</div>';
  h+='<div class="ph">종목별 전월 대비'+(p?' ('+p.month+'월 '+s.n+'일차 대비, 억원)':'')+'</div>'+divRows(o.rows)+'</div>';
  return h;
}
function summary(s){
  var p=s.prev,J=sum(s.j),T=sum(s.t),TT=J+T,PJ=p?sum(p.j):0,PT=p?sum(p.t):0,i,all=[],jr=[],tr=[],cn=(s.jn||0)+(s.tn||0);
  for(i=0;i<5;i++){
    var c=s.j[i]+(i>=3? s.t[i-3]:0),q=p? p.j[i]+(i>=3? p.t[i-3]:0):0;
    all.push({name:NM[i],d:c-q});
    jr.push({name:NM[i],d:s.j[i]-(p? p.j[i]:0)});
  }
  tr=[null,null,null,{name:NM[3],d:s.t[0]-(p? p.t[0]:0)},{name:NM[4],d:s.t[1]-(p? p.t[1]:0)}];
  return '<div class="row3">'+
    sumCard({title:'당사 전체',cur:TT,prev:p?PJ+PT:null,color:GR,rows:all,info:'청약 '+fi(cn)+'건 · 건당 평균 '+fi(cn? TT*1000/cn:0)+'만원'},s)+
    sumCard({title:'전용계좌',cur:J,prev:p?PJ:null,color:OR,rows:jr,info:fi(s.jn||0)+'건 · 당사 전체의 '+fmt(TT? J/TT*100:0,1)+'%'},s)+
    sumCard({title:'(당사) 퇴직연금계좌',cur:T,prev:p?PT:null,color:NV,rows:tr,info:fi(s.tn||0)+'건 · 당사 전체의 '+fmt(TT? T/TT*100:0,1)+'%'},s)+'</div>';
}

/* 종목별 비중(도넛) + 한도 대비 */
function donut(s){
  var tot=[],TT=0,i,sh,h,a0=-Math.PI/2,R=92,r=56,cx=100,cy=100,leg='';
  for(i=0;i<5;i++){ tot.push(s.j[i]+(i>=3? s.t[i-3]:0)); TT+=tot[i]; }
  sh=lrm(tot.map(function(v){ return TT? v/TT*1000:0; }),TT?1000:0);
  h='<svg viewBox="0 0 200 200" style="width:100%;max-width:270px;display:block;margin:0 auto">';
  for(i=0;i<5;i++){
    var ang=TT? tot[i]/TT*Math.PI*2:0,a1=a0+ang,x0=cx+R*Math.cos(a0),y0=cy+R*Math.sin(a0),x1=cx+R*Math.cos(a1),y1=cy+R*Math.sin(a1),x2=cx+r*Math.cos(a1),y2=cy+r*Math.sin(a1),x3=cx+r*Math.cos(a0),y3=cy+r*Math.sin(a0),lg=ang>Math.PI?1:0;
    if(ang>0.0001) h+='<path d="M'+x0+' '+y0+' A'+R+' '+R+' 0 '+lg+' 1 '+x1+' '+y1+' L'+x2+' '+y2+' A'+r+' '+r+' 0 '+lg+' 0 '+x3+' '+y3+' Z" fill="'+DON[i]+'" stroke="#fff" stroke-width="1.5"/>';
    if(sh[i]>=70){ var am=(a0+a1)/2,tx=cx+(R+r)/2*Math.cos(am),ty=cy+(R+r)/2*Math.sin(am);
      h+='<text x="'+tx+'" y="'+(ty-2)+'" text-anchor="middle" style="font:800 11px sans-serif;fill:#fff;stroke:#0a3a4a;stroke-width:2.5px;paint-order:stroke">'+NM[i].replace('(이표)','').replace('(복리)','')+'</text><text x="'+tx+'" y="'+(ty+11)+'" text-anchor="middle" style="font:800 11px sans-serif;fill:#fff;stroke:#0a3a4a;stroke-width:2.5px;paint-order:stroke">'+(sh[i]/10).toFixed(1)+'%</text>'; }
    a0=a1;
  }
  h+='</svg><div class="leg">';
  for(i=0;i<5;i++){
    h+='<i style="background:'+DON[i]+'"></i><span>'+NM[i]+'</span><span class="r">'+f1(tot[i])+'억원</span><span class="r">'+(sh[i]/10).toFixed(1)+'%</span>';
    if(i>=3&&tot[i]>0){
      var jp=lrm([s.j[i]/tot[i]*1000,s.t[i-3]/tot[i]*1000],1000);
      h+='<div class="sp"><div><span style="width:'+(jp[0]/10)+'%;background:'+OR+'"></span><span style="width:'+(jp[1]/10)+'%;background:'+NV+'"></span></div><p><span style="color:'+OR+'">전용계좌 '+(jp[0]/10).toFixed(1)+'%</span><span style="color:'+NV+'">(당사) 퇴직연금계좌 '+(jp[1]/10).toFixed(1)+'%</span></p></div>';
    }
  }
  return h+'</div>';
}
function limRow(label,lim,j,t,showPct,dashed){
  var U=100/1.55,fj=lim? j/lim:0,ft=lim? t/lim:0,tot=fj+ft,x=0,segs='',parts=[[fj,OR],[ft,NV]],k,f,inn,out=0,end;
  for(k=0;k<2;k++){
    f=parts[k][0]; if(f<=0) continue;
    inn=Math.max(0,Math.min(f,1-x)); out+=f-inn;
    if(inn>0) segs+='<s style="left:'+(x*U)+'%;width:'+(inn*U)+'%;background:'+parts[k][1]+'"></s>';
    x+=inn;
  }
  if(out>0) segs+='<s style="left:'+(U)+'%;width:'+(Math.min(out,0.55)*U)+'%;background:#c8101e"></s>';
  end=Math.min(tot,1.55)*U; var ins=end>80;
  return '<div class="lr"><div class="ln">'+label+'</div><div class="trk"><div class="mk'+(dashed?' ds':'')+'" style="left:'+U+'%"></div>'+segs+(showPct? '<span class="pc" style="left:'+(ins? end-13:end+1.5)+'%'+(ins? ';color:#fff':'')+'">'+fmt(tot*100,1)+'%</span>':'')+'</div><div class="n">'+fi(lim)+'</div><div class="n n2">'+fe(j+t)+'</div><div class="n n3">'+fe(j)+'</div><div class="n">'+(t>0? fe(t):'-')+'</div></div>';
}
function status(s){
  var L=s.limits,h='',i;
  if(!L) return '<div style="color:#6b7a8a">발행한도 자료가 없습니다.</div>';
  h+='<div class="lh"><span><i style="background:'+OR+'"></i>전용계좌</span><span><i style="background:'+NV+'"></i>(당사) 퇴직연금계좌</span><span><i style="background:#c8101e"></i>한도 초과분</span><span>| 발행한도</span><span>% 한도 대비 청약률</span></div>';
  h+='<div class="lg"><span></span><span></span><b>한도</b><b>합산</b><b class="o">전용</b><b>퇴직</b></div>';
  for(i=0;i<5;i++) h+=limRow(NM[i],L[i],s.j[i]/10,i>=3? s.t[i-3]/10:0,i<3,i>=3);
  h+='<div class="lr tot">'+limRow('당사 합산',sum(L),sum(s.j)/10,sum(s.t)/10,false,false).slice(16);
  return h;
}

/* 당사 누적 청약 구성 */
function groups(s){
  var g={},cur=null,c=s.comp||[],i;
  for(i=0;i<c.length;i++){
    if(c[i].lv===0){ cur=c[i].name; g[cur]={tot:c[i],ch:[]}; }
    else if(c[i].lv===1&&cur) g[cur].ch.push(c[i]);
  }
  return g;
}
function stack(ch,cols,mode){
  var h='<div class="sb">',i,r,p,txt;
  for(i=0;i<ch.length;i++){
    r=ch[i]; p=(mode==='a'? r.as_:r.ns)/10; txt=mode==='a'? f1(r.a)+'억원':fi(r.n)+'건';
    h+='<div style="width:'+p+'%;background:'+cols[i%2]+'">'+p.toFixed(1)+'%<small>'+txt+'</small></div>';
  }
  return h+'</div>';
}
function compPanels(s){
  var g=groups(s),h='',defs=[['전용계좌','전용계좌',[OR,OR2]],['퇴직연금계좌','(당사) 퇴직연금계좌',[NV,NV2]]],k,d,x,i;
  for(k=0;k<2;k++){
    d=defs[k]; x=g[d[0]];
    if(!x||!x.ch.length){ h+='<div class="pn"><h4>'+d[1]+'</h4><div style="color:#6b7a8a">자료 없음</div></div>'; continue; }
    h+='<div class="pn"><h4>'+d[1]+'</h4><div class="pl">';
    for(i=0;i<x.ch.length;i++) h+='<span><i style="background:'+d[2][i%2]+'"></i>'+esc(x.ch[i].name)+'</span>';
    h+='</div><div class="sr"><span>금액 기준</span>'+stack(x.ch,d[2],'a')+'</div><div class="sr"><span>건수 기준</span>'+stack(x.ch,d[2],'n')+'</div></div>';
  }
  return '<div class="two">'+h+'</div>';
}

/* WM 영업점별 비중 */
function wmCol(title,color,t){
  var list=t&&t.by_a? t.by_a:[],tot=sum(list.map(function(r){ return r.a; })),mx=0,i,h,nm;
  for(i=0;i<list.length;i++) if(list[i].a>mx) mx=list[i].a;
  h='<div><h4>'+title+'</h4><div class="hb" style="background:'+color+'"></div><div class="hs" style="color:'+color+'">상위 '+list.length+'곳 100.0%</div>';
  for(i=0;i<list.length;i++){
    nm=esc(list[i].name); if(!/WM$|Direct$/.test(nm)) nm+='WM';
    h+='<div class="wr"><span class="rk">'+(i+1)+'</span><span>'+nm+'</span><span class="v">'+fe(list[i].a)+'억원 · '+fi(list[i].n)+'건</span><span class="p">'+fmt(tot? list[i].a/tot*100:0,1)+'%</span><div class="bb2"><i style="width:'+(mx? list[i].a/mx*100:0)+'%;background:'+color+'"></i></div></div>';
  }
  if(!list.length) h+='<div style="color:#6b7a8a">자료 없음</div>';
  return h+'</div>';
}
function wmPanel(s){
  var t=s.top5; if(!t) return '';
  return '<div class="wm"><h3>WM 영업점별 당월 누적 청약금액 비중</h3><div class="c3">'+wmCol('당사 전체',GR,t.all)+wmCol('전용계좌',OR,t.j)+wmCol('(당사) 퇴직연금계좌',NV,t.t)+'</div></div>';
}

/* 화면 */
function renderTop(s){
  var h='',i,d=s?s.dates:null,m=parseInt(sel.ym.slice(5,7),10);
  $('ttl').textContent=m+'월 '+TITLE;
  $('sub').textContent=s? '청약기간 '+dDot(d&&d[0])+' ~ '+dDot(d&&d[d.length-1])+' · '+dDot(s.date)+', '+s.n+'일차 마감 기준 · 청약금액 기준':'';
  h='';
  for(i=0;i<months.length;i++) h+='<option value="'+months[i]+'"'+(months[i]===sel.ym?' selected':'')+'>'+ymDot(months[i])+'</option>';
  $('msel').innerHTML=h;
  var last=snapsOf(sel.ym),tot=last.length? (last[last.length-1].N_total||last[last.length-1].n):1;
  h='';
  for(i=1;i<=tot;i++) h+='<button class="dt'+(i===sel.n?' on':'')+(getSnap(sel.ym,i)?'':' dis')+'" data-d="'+i+'">'+i+'일차</button>';
  $('days').innerHTML=h;
}
function render(){
  var s=getSnap(sel.ym,sel.n);
  renderTop(s);
  if(!s){ $('app').innerHTML='<div class="empty">'+ymDot(sel.ym)+' '+sel.n+'일차 자료가 아직 없습니다.</div>'; return; }
  $('app').innerHTML=limCards(s)+commentBox(s)+summary(s)+
    '<div class="row2"><div><h3>종목별 청약금액 비중</h3>'+donut(s)+'</div><div><h3>종목별 누적 청약 현황</h3>'+status(s)+'</div></div>'+
    '<div class="cmp"><h3>당사 누적 청약 구성</h3>'+compPanels(s)+'</div>'+wmPanel(s);
}

/* 이벤트 */
$('msel').addEventListener('change',function(){ sel.ym=this.value; sel.n=latestN(sel.ym); sel.edit=false; render(); });
document.addEventListener('click',function(e){
  var t=e.target,a,d,s=getSnap(sel.ym,sel.n);
  while(t&&t!==document){ if(t.getAttribute&&(t.getAttribute('data-a')||t.getAttribute('data-d'))) break; t=t.parentNode; }
  if(!t||t===document) return;
  d=t.getAttribute('data-d'); a=t.getAttribute('data-a');
  if(d){ if(!getSnap(sel.ym,Number(d))) return; sel.n=Number(d); sel.edit=false; }
  else if(a==='edit') sel.edit=true;
  else if(a==='cancel') sel.edit=false;
  else if(a==='save'&&s){ try{ localStorage.setItem(ckey(s),$('cmt').value); }catch(err){ alert('이 브라우저에서는 저장할 수 없습니다.'); } sel.edit=false; }
  else if(a==='reset'&&s){ try{ localStorage.removeItem(ckey(s)); }catch(err){} sel.edit=false; }
  render();
});
$('bPdf').addEventListener('click',function(){ window.print(); });
$('bImg').addEventListener('click',function(){
  try{
    var el=$('page'),w=el.scrollWidth,h=el.scrollHeight,c=el.cloneNode(true),x,svg,img,k,rm=c.querySelectorAll('.acts');
    for(k=0;k<rm.length;k++) rm[k].parentNode.removeChild(rm[k]);
    x=new XMLSerializer().serializeToString(c);
    svg='<svg xmlns="http://www.w3.org/2000/svg" width="'+w+'" height="'+h+'"><foreignObject width="100%" height="100%"><div xmlns="http://www.w3.org/1999/xhtml" style="background:#eef2f6"><style>'+$('css').textContent+'</style>'+x+'</div></foreignObject></svg>';
    img=new Image();
    img.onload=function(){
      var cv=document.createElement('canvas'); cv.width=w*2; cv.height=h*2;
      var g=cv.getContext('2d'); g.scale(2,2); g.fillStyle='#eef2f6'; g.fillRect(0,0,w,h); g.drawImage(img,0,0);
      try{ cv.toBlob(function(b){ var a=document.createElement('a'); a.href=URL.createObjectURL(b); a.download='청약현황_'+sel.ym+'_'+sel.n+'일차.png'; document.body.appendChild(a); a.click(); document.body.removeChild(a); }); }
      catch(err){ alert('이미지 저장이 막혀 있습니다. PDF 출력을 이용하세요.'); }
    };
    img.onerror=function(){ alert('이미지 저장에 실패했습니다. PDF 출력을 이용하세요.'); };
    img.src='data:image/svg+xml;charset=utf-8,'+encodeURIComponent(svg);
  }catch(err){ alert('이미지 저장에 실패했습니다. PDF 출력을 이용하세요.'); }
});

if(!DATA||!Object.keys(DATA).length){
  $('app').innerHTML='<div class="empty">표시할 데이터가 없습니다. 2-1 청약현황 코드를 실행한 뒤 다시 여세요.</div>';
}else{
  months=Object.keys(DATA).sort();
  sel.ym=months[months.length-1];
  sel.n=latestN(sel.ym);
  render();
}
})();
</script>
</body>
</html>
'''

assert '/*__DATA__*/null' in HTML and '__TITLE__' in HTML, '틀 내용이 올바르지 않습니다. 코드 끝까지 복사했는지 확인하세요.'
_old = os.path.exists(OUT)
_bk = shutil.copy(OUT, '2-1_대시보드_틀_백업.html') if _old else None
_f = open(OUT, 'w', encoding='utf-8', newline='\n'); _f.write(HTML); _f.close()
print('기존 틀을 2-1_대시보드_틀_백업.html 로 보관했습니다.' if _old else '(기존 틀 없음)')
print('완료:', os.path.abspath(OUT), '→ 이어서 2-1 청약현황 코드를 실행하세요.')
