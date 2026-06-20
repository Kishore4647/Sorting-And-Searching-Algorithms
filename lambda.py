def new(x):
    return (lambda y:x*y)
t=new(5)
print(t(3))