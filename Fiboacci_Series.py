def genFibo(x):
    first = 0
    second = 1
    print(f"{first} {second}",end=" ")
    for i in range(3,x+1):
        fibo = first+second
        first = second
        second = fibo
        print(fibo,end=" ")

n = int(input("Enter a range : "))
if n<=0:
    print("Please enter a positive integer")
else:
   print(f"Fibonacci series till {n}th => ")
   genFibo(n)