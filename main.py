import json,os,urllib.request as R
P='KKKKUUUUMMOQLLMPKKKOLJIKLMMGKKKKACEECGKKEKMNELNOEKNOELMNCGKLACEEKKKKLMMMJKKKJKKKJKKKJKKKJKKKKKKLECCAECCAECCAECCAGEECIGGGOOKKOQMK'
MT=[0,100,320,330,500,900,0]
KN=(-33,-31,-18,-14,14,18,31,33);BG=(-17,-15,15,17);RG=(-16,-1,1,16);DG=BG+RG
DS=(KN,BG,RG,DG,DG)
S64=[i for i in range(128)if i&8<1]
T=[[0]*128 for _ in range(7)]
for i,c in enumerate(P):
 t,r,f=i>>5,i//4%8,i%4;a=t*2 or 1;v=ord(c)*5-375;q=(7-r)*16;T[a][q+f]=T[a][q+7-f]=v
MATE=9e4;BUD=1e5
B=[0]*128;N=[0,0];US=[];KL=[0]*64;TT={}
CR={0:2,7:1,4:3,112:8,119:4,116:12}
def post(p,b):
 return json.load(R.urlopen(os.getenv('MAKEFUN_ENV_URL')+p,json.dumps(b).encode()))
def nm(s):return chr(s%8+97)+str(s//16+1)
def sq(u):return ord(u[1])*16+ord(u[0])-881
def mv(u):return sq(u[:2])|sq(u[2:])<<7|' nbrq'.find(u[4:])<<14
def mu(m):
 return nm(m&127)+nm(m>>7&127)+' nbrq'[m>>14&7].strip()
def atk(s,by):
 for t in(s-15*by,s-17*by):
  if not t&136 and B[t]==by:return 1
 for d in KN+DG:
  t=s+d
  if not t&136 and B[t]==(6,2)[d in KN]*by:return 1
 for d in DG:
  t=s+d
  while not t&136 and not B[t]:t+=d
  if not t&136 and B[t]*by-3 in(2,d in RG):return 1
 return 0
def gen(cp):
 ms=[];o=S
 for f in S64:
  p=B[f]
  if p*o<=0:continue
  a=abs(p)
  if a==1:
   r=f>>4;pm=(r+o in(7,0))<<16
   for d in 16,15,17:
    t=f+d*o
    if t&136:continue
    q=B[t]
    if d==16:
     if q:continue
     if pm or 1-cp:ms.append(f|t<<7|pm)
     if 1-cp and o*r in(1,-6)and not B[f+32*o]:ms.append(f|f+32*o<<7)
    elif q*o<0 or t==E:ms.append(f|t<<7|pm)
   continue
  for d in DS[a-2]:
   t=f+d
   while not t&136:
    q=B[t]
    if q*o<0 or q==cp==0:ms.append(f|t<<7)
    if q or a%4==2:break
    t+=d
 if cp:return ms
 k=K[o<0]
 for sd in(1,-1):
  bit=1<<(sd<0)+(o<0)*2
  if C&bit and not(B[k+sd]or B[k+2*sd])and(sd>0 or not B[k+3*sd])and not any(atk(k+i*sd,-S)for i in(0,1,2)):ms.append(k|(k+2*sd)<<7)
 return ms
def order(ms,p):
 ms.sort(key=lambda m:MT[abs(B[m>>7&127])]+50*(m==KL[p])-MT[abs(B[m&127])]//100,reverse=True)
def make(m):
 global S,C,E
 f=m&127;t=m>>7&127;r=m>>14&7
 p=B[f];q=abs(p);ki=S<0;c=B[t]
 US.append((B[:],C,E,K[:]))
 if q==6 and abs(t-f)==2:
  rf,rt=(f+3,f+1)if t>f else(f-4,f-1);rp=B[rf];B[rt],B[rf]=rp,0;K[ki]=t
 elif q==6:K[ki]=t
 B[t]=(r+1)*S if r else p;B[f]=0
 if q<2 and(t-f)&1 and c==0:B[t-16*S]=0
 C&=~(CR.get(f,0)|CR.get(t,0))
 E=f+16*S if q==1 and abs(t-f)==32 else-1
 S=-S
 if atk(K[ki],S):unmake();return 0
 return 1
def unmake():
 global S,C,E
 b,c,e,k=US.pop()
 B[:]=b;C=c;E=e;K[:]=k;S=-S
def ev():
 s=0
 for q in S64:
  p=B[q]
  if p:
   a=abs(p);v=q^112*(p<0);s+=(MT[a]+T[a][v])*p//a
 return s*S
def sr(a,b,d,p):
 global S,E
 k=K[S<0];oa=a
 N[0]+=1
 if N[0]>BUD:N[1]=1;return 0
 if d>0:
  y=(tuple(B),S);x=TT.get(y)
  if x and x[0]>=d and(x[2]==0 or x[1]>=b if x[2]<2 else x[1]<=a):return x[1]
  if x and x[3]:KL[p]=x[3]

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
 bs=-MATE;bm=0
 for m in ms:
  if not make(m):continue
  s=-sr(-b,-a,d-1,p+1)
  unmake()
  if N[1]:return 0
  if s>bs:bs,bm=s,m
  a=max(a,s)
  if a>=b:KL[p]=m;break
 if bs==-MATE:s=-MATE+p if atk(k,-S) else a if d<=0 else 0
 else:s=a if d<=0 and not ck else bs
 if d>0:TT[y]=(d,s,(s>=b)+2*(s<=oa),bm)
 return s
def setup(g):
 global S,C,E,K
 B[:]=[0]*128
 for i,v in enumerate(b'42356324'):v-=48;B[i]=v;B[i+112]=-v;B[16+i]=1;B[96+i]=-1
 S=1;C=15;E=-1;K=[4,116]
 TT.clear()
 for u in g['moves']:TT[(tuple(B),S)]=(99,0,0);make(mv(u))
 US.clear()
def think(g):
 setup(g)
 mi=[mv(u) for u in g['legal_moves']]
 order(mi,0)
 N[:]=0,0;best=mi[0];d=1
 while 1:
  bs=-MATE;bm=mi[0]
  for m in mi:
   if not make(m):continue
   s=-sr(-MATE,-bs,d-1,1)
   unmake()
   if N[1]:break
   if s>bs:bs,bm=s,m
  if N[1]:break
  best=bm;d+=1
 return mu(best)
while(g:=post('/game',{}))['status']!='done':
 while g['status']=='your_move':g=post('/move',{'game':g['game'],'move':think(g)})
