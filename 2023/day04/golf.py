#1234567890123456789012345678901234567890123456789012345678901234567890123456789
def G(x):return S[x]+Z((G(n)for n in R(x+1,x+S[x]+1)))
D,P,E,R,Z,L,C,I=open(0).readlines(),print,enumerate,range,sum,len,str.split,(set
.intersection);S={x:L(I(*map(lambda l:set(map(int,C(l))),C(C(l,":")[1],"|"))))
for x,l in E(D,1)};P(Z((pow(2,S[n]-1)for n in S.keys()if S[n])),Z([1+(lambda x:
S[x]+Z((G(n)for n in R(x+1,x+S[x]+1))))(w)for w in R(1,L(D)+1)]))
