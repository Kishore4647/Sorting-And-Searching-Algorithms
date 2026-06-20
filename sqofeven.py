#wpt print the sqaure of even numbers in a string
s=eval(input())
c=0
for i in s:
    if   int(i)%2==0:
        c=int(i)**2
        print(c)
