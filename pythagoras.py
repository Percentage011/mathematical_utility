N=input("ピタゴラス数に分解しよう！>>>　")
n=int(N)
s=n #nを保存しておく

import math

#入力を原始ピタゴラス数に揃えるためにできるだけ4で割り、4で割ったあまりが1であるか判定する
k=0
while(n%2==0):
    n=n/2
    k+=1
    continue

p=[] #ピタゴラス数の組を入れておくリストのリスト。これ自体の要素はリスト
#4で割ったあまりが1の場合の処理。ピタゴラス数に分解できる可能性がある
if(n%4==1 and n!=1):
        m=1 #mの初期化
        i=-1 #リストpのインデックス用のカウンタ変数。c-m*mが平方数の時に働く
        while((m*m)<n): #それぞれのmに対してcが平方数であるかを確認する
            c=n #毎回初期化する
            c=abs(c-(m*m)) #1444
            m+=1
            if(math.sqrt(c)%1==0): #cが平方数のときに以下の処理をする
                i+=1
                p.append([])
                q=abs(c-((m-1)*(m-1)))
                t=(2*(m-1)*(math.sqrt(c)))
                if(k!=0):
                    q=q*(2**k)
                    t=t*(2**k)

                c=int(c)
                t=int(t)
                q=int(q)
                p[i].append(t)
                p[i].append(q)

if(len(p)!=0):
    print("できました！")
    for r in range(int(len(p)/2)):
        print(p[r])
else:
    print("ごめんね……無理だったよ")