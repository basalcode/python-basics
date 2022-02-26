# function
def say_hello():
    print("hello world!")
    print ("bye")

say_hello()

def say_hello_to(who = "nobody"):
    print("Hello,", who)

say_hello_to("Alex")

def plus(a, b):
    return a + b

print("plus(1, 3)", plus(1, 3))

def minus(a, b):
    return a - b

print("minus(3, 2)", minus(5, 2))
print("minus(b = 3, a = 2)", minus(b = 5, a = 2)) # keyworded arguments 

# string formatter
def introduce(name, age):
    print("Hello My name is " + name + ". I'm " + str(age) + " years old.")

def introduceWithFormatter(name, age):
    print(f"Hello My name is {name}. I'm {age} years old.")

introduce("Alex", 20)
introduceWithFormatter(age = 20, name = "Alex")