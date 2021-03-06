import math,random

y=0
while(y==0):
    x=random.randrange(1,8) #乱数の分布幅をランダムに決める
    a=random.randrange(1,10**x,2) #奇数をランダムに生成
    b=random.randrange(2,10**x+1,2) #偶数をランダムに生成
    if(math.gcd(a,b)==1):   #aとbが互いに素になるまでaとbを生成し続ける(原始ピタゴラス数になる)
        y+=1

n=a**2+b**2 #分解される形にする

p=[] #ピタゴラス数の組を入れておくリストのリスト。これ自体の要素はリスト
m=1 #mの初期化
i=-1 #リストpのインデックス用のカウンタ変数。c-m*mが平方数の時に働く
while((m*m)<n): #それぞれのmに対してcが平方数であるかを確認する
    c=n #毎回初期化する
    c=abs(c-(m*m))
    m+=1
    if(math.sqrt(c)%1==0): #cが平方数のときに以下の処理をする
        i+=1
        p.append([])
        q=c-(m-1)*(m-1)
        t=2*(m-1)*(math.sqrt(c))
        c=int(c)
        t=int(t)
        q=int(q)
        if(math.gcd(c,t)==1 or math.gcd(c,q)==1 and q>0):
            p[i].append(t)
            p[i].append(q)
        else:
            del p[-1]
            i-=1

print(str(n)+"を原始ピタゴラス数に分解しました")
for r in range(int(len(p))):
    print(p[r])
