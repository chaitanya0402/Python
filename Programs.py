#num = 5;
#factorial = 1;
#if num < 0:
   #print("Sorry, factorial does not exist for negative numbers");
#elif num == 0:
   #print("The factorial of 0 is 1");
#else:
   #for i in range(1,num + 1):
       #factorial = factorial*i;
  # print("The factorial of",num,"is",factorial);


nterms = int(input("How many terms? "));
n1, n2 = 0, 1
count = 0
if nterms <= 0:
   print("Please enter a positive integer");
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":");
   print(n1);
else:
   print("Fibonacci sequence:");
   while count < nterms:
       print(n1)
       nth = n1 + n2;
       n1 = n2;
       n2 = nth;
       count += 1;

