import json,os,urllib.request as R
P='KKKKUUUUMMOQLLMPKKKOLJIKLMMGKKKKACEECGKKEKMNELNOEKNOELMNCGKLACEEKKKKLMMMJKKKJKKKJKKKJKKKJKKKKKKLECCAECCAECCAECCAGEECIGGGOOKKOQMK'
MT=[0,100,320,330,500,900,0]
KN=(-33,-31,-18,-14,14,18,31,33);BG=(-17,-15,15,17);RG=(-16,-1,1,16);DG=BG+RG
DS=(KN,BG,RG,DG,DG)
S64=[i for i in range(128)if i&136<1]
T=[[0]*128 for _ in range(7)]
for i,c in enumerate(P):
 t,r,f=i//32,i//4%8,i%4;a=(1,2,4,6)[t];v=ord(c)*5-375;q=(7-r)*16;T[a][q+f]=v;T[a][q+7-f]=v
INF=9e6;MATE=9e4;BUD=1e5
B=[0]*128;N=[0,0];US=[];KL=[0]*64;GH=set()
CR={0:2,7:1,4:3,112:8,119:4,116:12}
def post(p,b):
 return json.load(R.urlopen(os.getenv('MAKEFUN_ENV_URL')+p,json.dumps(b).encode()))
def nm(s):return chr(97+(s&7))+str(s//16+1)
def sq(u):return ord(u[1])*16+ord(u[0])-881
def mv(u):return sq(u[:2])|sq(u[2:4])<<7|(('nbrq'.find(u[4])+2)<<14 if u[4:] else 0)
def mu(m):
 r=m>>14&7;return nm(m&127)+nm(m>>7&127)+('nbrq'[r-2] if r>1 else '')
def atk(s,by):
 for t in(s-15*by,s-17*by):
  if not t&136 and B[t]==by:return 1
 for d in KN+DG:
  t=s+d
  if not t&136 and B[t]==(2 if d in KN else 6)*by:return 1
 for d in DG:
  t=s+d
  while not t&136 and not B[t]:t+=d
  if not t&136 and B[t]*by in(5,3+(d in RG)):return 1
 return 0
def gen(cp):
 ms=[];o=S
 for f in S64:
  p=B[f]
  if p*o<=0:continue
  a=abs(p)
  if a==1:
   r=f>>4;pm=5<<14 if r+o in(7,0) else 0
   for d in 16,15,17:
    t=f+d*o
    if t&136:continue
    q=B[t]
    if d==16:
     if q:continue
     if pm or not cp:ms.append(f|t<<7|pm)
     u=f+32*o
     if not cp and o*r in(1,-6) and not B[u]:ms.append(f|u<<7)
    elif q*o<0 or t==E:ms.append(f|t<<7|pm)
   continue
  for d in DS[a-2]:
   t=f+d
   while not t&136:
    q=B[t]
    if q*o<0 or not q and not cp:ms.append(f|t<<7)
    if q or a in(2,6):break
    t+=d
 if cp:return ms
 k=K[(1-o)//2]
 for sd in(1,-1):
  bit=1<<((sd<0)+(o<0)*2)
  if C&bit and not(B[k+sd]or B[k+2*sd])and(sd>0 or not B[k+3*sd])and not any(atk(k+i*sd,-S)for i in(0,1,2)):ms.append(k|(k+2*sd)<<7)
 return ms
def order(ms,p):
 ms.sort(key=lambda m:10*MT[abs(B[m>>7&127])]+500*(m==KL[p]),reverse=True)
def make(m):
 global S,C,E
 f=m&127;t=m>>7&127;r=m>>14&7
 p=B[f];w=S;q=abs(p);ki=(1-w)//2;c=B[t]
 US.append((B[:],C,E,K[:]))
 if q==6 and abs(t-f)==2:
  rf,rt=(f+3,f+1)if t>f else(f-4,f-1);rp=B[rf];B[rt]=rp;B[rf]=0;K[ki]=t
 elif q==6:K[ki]=t
 B[t]=r*w if 1<r<6 else p;B[f]=0
 if q<2 and(t-f)&1 and c==0:B[t-16*w]=0
 C&=~(CR.get(f,0)|CR.get(t,0))
 E=f+16*w if q==1 and abs(t-f)==32 else -1
 S=-S
 if atk(K[ki],S):unmake();return 0
 return 1
def unmake():
 global S,C,E
 b,c,e,k=US.pop()
 B[:]=b;C=c;E=e;K[:]=k;S=-S
def ev():
 s=m=0
 for q in S64:
  p=B[q]
  if p:
   a=abs(p);s+=(MT[a]+T[a][q if p>0 else q^112])*(p//a);m+=1<a<6
 s+=(1-m/14)*(T[2][K[0]]-T[6][K[0]]-T[2][K[1]^112]+T[6][K[1]^112])
 return s*S
def sr(a,b,d,p):
 global S,E
 k=K[(1-S)//2]
 N[0]+=1
 if N[0]>BUD:N[1]=1;return 0
 if(tuple(B),S)in GH:return 0

 ck=0
 if d<=0:
  ck=atk(k,-S)
  if not ck:
   s=ev()
   if s>=b:return b
   if s>a:a=s
 elif d>2 and not atk(k,-S):
  e=E;E=-1;S=-S
  s=-sr(-b,-b+1,d-3,p+1)
  S=-S;E=e
  if N[1]:return 0
  if s>=b:return b
 ms=gen(d<=0 and not ck)
 order(ms,p)
 bs=-INF
 for m in ms:
  if not make(m):continue
  s=-sr(-b,-a,d-1,p+1)
  unmake()
  if N[1]:return 0
  if s>bs:bs=s
  if s>a:a=s
  if a>=b:
   KL[p]=m
   break
 if bs==-INF:return -MATE+p if atk(k,-S) else a if d<=0 else 0
 return a if d<=0 and not ck else bs
def setup(g):
 global S,C,E,K
 B[:]=[0]*128
 for i,v in enumerate(b'42356324'):v-=48;B[i]=v;B[i+112]=-v;B[16+i]=1;B[96+i]=-1
 S=1;C=15;E=-1;K=[4,116]

 GH.clear()
 for u in g['moves']:
  GH.add((tuple(B),S))
  make(mv(u))
 US.clear()
def think(g):
 setup(g)
 mi=[mv(u) for u in g['legal_moves']]
 order(mi,0)
 N[:]=0,0;best=mi[0];d=1
 while d<64:
  a=-INF;bs=-INF;bm=mi[0]
  for m in mi:
   if not make(m):continue
   s=-sr(-INF,-a,d-1,1)
   unmake()
   if N[1]:break
   if s>bs:bs,bm=s,m
   if s>a:a=s
  if N[1]:break
  best=bm;d+=1
 return mu(best)
while(g:=post('/game',{}))['status']!='done':
 while g['status']=='your_move':g=post('/move',{'game':g['game'],'move':think(g)})
