#შედარებითი ოპერატორებია >, <, <=, >=, ==, !=
print(6 > 5)
print(6 > 4)
print(6 > 3)
print(6 > 2)
print(6 > 1)

print(6 < 4)
print(6 < 7)
print(23 < 87)
print(54 < 99)
print(7 < 77)
 
print(5 == 5)
print(7 == 7)
print(88 == 99)
print(90 == 90)
print(57 == 52)

print(8 >= 9)
print(10 >= 10)
print(88 >= 79)
print(55 >= 55)
print(77 >= 6)
print(89 >= 90)

print(8 <= 9)
print(90 <= 111)
print(77 <= 90)
print(8 <= 65)
print(60 <= 60)

print(5 != 4)
print(0 != 9)
print(27 != 9)
print(77 != 76)
print(9 != 55)

#ლოგიკური ოპერატორები არის  and და or რომლებითაც შესრულებული ოპერაცია პასუხად ყოველთვის გვაძლევს boolean ტიპის მნიშვნელობას

# and
print(True and True) #True
print(False and True) #False
print(True and False) #False
print(False and False) #False

#or
print(True or True) #True
print(False or True) #True0
print(True or False) #True
print(False or False) #False


print(5 > 6 and 3 > 7)
print(7 < 6 and True)
print(True and 90 > 77)

print(7 + 8 > 6 + 5 or True)
print(5 > 4 or 7 > 6)
print(5 + 7 + 9 > 7 or 9 + 9 < 19)

num = int(input("write any number: "))
print(7 < num)

name = input("write your name: ")
print("mari" == name)

age = int(input("write your age: "))
print(18 < age)