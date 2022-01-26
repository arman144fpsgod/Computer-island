import pygame as p,random
def mygame():
    q=p.display
    T=16
    b=q.set_mode([256]*2).fill
    l=[]
    d=a=x=1
    c=p.event.get
    while not(x&528 or x in l):
        l=l[a!=x:]+[x]
        while a&528 or a in l:
            a=random.randrange(512)
        b(0)
        [b(99,(o%T*T,o/32*T,T,T)) for o in l+[a]]
        q.flip()
        p.time.wait(99)
        D=d
        for e in c(2):
            v=e.key-272
            n=((v&2)-1)*[1,32][v<3]
            if-n-D and 0<v<5:
                d=n
        c()
        x+=d
    q.quit()