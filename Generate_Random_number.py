import random
def gen_Random(x,y):
    return random.uniform(x,y)

a = float(input("Enter lower bound : "))
b = float(input("Enter upper bound : "))
myRandom = gen_Random(a,b)
print(f"The random number between {a} and {b} is : {myRandom}")