l=[12,43,897,-1,20,56,43,8]
target=int(input())
def linear(l,target):
    for i in range(len(l)):
        if l[i]==target:
            return i
    else:
        return -1

print(linear(l,target))
