a=lambda x,y,z:x*y*z          #gives 6000 as output
print(a(10,20,30))
def f1(n):
    return lambda x:x*n
f2= f1(15)
print(f2(2))                 #gives 15*2=30 as output

list1={1,2,3,4}
x=list(filter(lambda y:(y%2==0),list1))
print(x)
