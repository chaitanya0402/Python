
'''b=[4,5,6]
print(b)
print(len(b))
print(max(b))
print(min(b))
y=(2.3,"str",5)
print(y)
print(y[1])
y.add(5)
print(y)
y.clear()'''

x={'a':1,'b':2}                    #Dictionary
print(x.get('a'))
x.update({'c':3})
print(x)

n=[1,2,3,1,2]         #set
n_set=set(n)
print(n_set)

occurance=dict(m=1,n=2,o=3)                       #dictionary
print(occurance)
occurance['d']=5                              # to add new value
print(occurance)

def create_t():
    return 'T','2000','India'                      #tupple
t=create_t()
name,year,place=t
print(t)