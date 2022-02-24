# terminal
print("Hello, World!")

# data types
a_string = "This is string type"
a_number = 3
a_float = 3.14
a_boolean = True
a_none = None

# lists
days = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat"]

print("What type is this?:", type(days)) # type 구하기
print("Does monday exist?:", "Mon" in days) # Mon 데이터가 있는지 확인
print("What is in the second index?:", days[2]) # List의 요소 조회하기
print("How long is the array?:", len(days)) # List의 길이 구하기

days.append("Sun") # list에 요소 추가
print("Sunday has been added!", days) 

days.reverse() # list를 거꾸로 뒤집기
print("Days list has been reversed!", days)

# tuple - 값을 바꿀 수 없다
days = ("Mon", "Tue", "Wed", "Thur", "Fri", "Sat")
print("What type is this?:", type(days)) # type 구하기

# dictionary 
person = {
    "name": "Alex",
    "age": 20,
    "isMale": True
}
print(person)

person["pets"] = ["dog", "cat"] # 값 추가
print(person)
