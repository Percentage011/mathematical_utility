N = input("Factoring! ")

import time
start = time.time()

n = int(N)
s=n

p = []
exp = []

k = 0
while(n%2==0):
    k += 1
    n=n/2

if(k>0):
    p.append(2)
    exp.append(k)

l = 0
while(n%3==0):
    l += 1
    n=n/3

if(l>0):
    p.append(3)
    exp.append(l)

i=1
while(n>1):
    ae=0
    be=0
    while(n%(6*i-1)==0):
        n=n/(6*i-1)
        ae=ae+1

    if(ae!=0):
        p.append(6*i-1)
        exp.append(ae)
#ここから以上と相同の処理
    while(n%(6*i+1)==0):
        n=n/(6*i+1)
        be=be+1

    if(be!=0):
        p.append(6*i+1)
        exp.append(be)
#ここまでで1つのiに対する処理が終わり、iを更新する
    i=i+1
    if(s>(6*i-1)*(6*i-1)):
        continue

ans=str(s)+" = "
for c in range(len(p)):
    if(exp[c]!=1):
        ans=ans+str(p[c])+"^"+str(exp[c])+"*"
    else:
        ans=ans+str(p[c])+"*"

if(s==1):
    print(str(s)+" = 1")
else:
    print(ans[:-1])

elapsed = time.time()-start
print("time="+str(elapsed)+"s")
