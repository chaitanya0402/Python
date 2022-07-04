
'''fileptr=open("D:\File1.txt")
    fileptr.read()
if fileptr:
    print("Successfully")
else:
    print("Failed or some error")
    fileptr.close()'''

with open("D:\File1.txt") as m:
    print(m.read())
    p=m.write("Hiii")
    print(p)