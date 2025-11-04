# type არის ფუნქცია რომელიც ამოწმებს მისთვის გადაცემული მონაცემის ტიპს
print(type("mari"))
print(type(5))
print(type(5.3))
print(type(True))

#data conversion არის პროცესი რომლის საშუალებითაც ერთი Data typeს ვცვლით მეორე Data type-ად
a = int(3.7) #floati shevcvale integerad
b = int("10") #stringi shevcvale integerad
c = int(True) #booleani shevcvale integerad
print(a,b,c)


d = float(5) #integeri shevcvale floatad
e = float("7") #stringi shevcvale floatad
f = float(True) #booleani shevcvale floatad
print(d,e,f)

g = str(10) #integeri shevcvale stringad
h = str(7.3) #floati shevcvale stringad
i = str(True) #booleani shevcvale stringad
print(g,h,i)

j = bool(0) #integeri shevcvale booleanad
K = bool(9.2) #floati shevcvale booleanad
l = bool("0") # stringi shevcvale booleanad

number = int(input("Write first number: "))
Number = int(input("Write Second number: "))
number1 = int(input("Write third number: "))

print(number + Number + number1)

num1 = str(number)
num2 = str(Number)
num3 = str(number1)

print(num1 + num2 + num3)

name = input("write your name: ")
slay = int(input("Wtite any number: "))
print(slay * name)



