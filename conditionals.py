def plus(a, b):
    if type(b) is int or type(b) is float:
        return a + b
    else:
         return None

def age_check(age):
    print(f"you are {age}")
    if age < 18:
        print("you can't drink")
    elif age == 18:
        print("you are new to this !")
    elif age > 20 and age < 25:
        print("you are still kind of young")
    else:
        print("enjoy your drink")

age_check(18)

