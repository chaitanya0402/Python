try:
    fileptr=open("D:\File1.txt")
except:
    print("Pass")
else:
    print("Fail")
finally:
    fileptr.close()

