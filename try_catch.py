try:
     i=1
     j=10/i
     values={1,'2'}
     sum(values)
except ZeroDivisionError:
     print("ZeroException")
     j=0
except TypeError:
     print("TypeError")
     values=10
else:
    print("else")
finally:
    print("Finally")
print(j)
print("End")
