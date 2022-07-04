#num = int(input("Enter a number: "));
#sum = 0;
#temp = num;
#while temp > 0:
   #digit = temp % 10;
   #sum += digit ** 3;
   #temp //= 10;
#if num == sum:
   #print(num,"is an Armstrong number");
#else:
   #print(num,"is not an Armstrong number");

num1 = int(input("Enter a number: "));
flag = False;
if num1 > 1:
    for i in range(2, num1):
        if (num1 % i) == 0:
           flag = True;
           break;
if flag:
    print(num1, "is not a prime number");
else:
    print(num1, "is a prime number");



    num = int(input("Enter a number: "));
    if (num % 2) == 0:
       print("{0} is Even".format(num));
    else:
       print("{0} is Odd".format(num));
