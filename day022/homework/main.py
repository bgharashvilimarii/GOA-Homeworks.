# დაბეჭდე ყველა კენტი რიცხვი 1–20-ის ფარგლებში.
# for i in range(1,21):
#     if i % 2 != 0:
#         print(i)

# მომხმარებელი ჩაწერს რიცხვებს. სანამ არ ჩაწერს 0-ს, დაბეჭდე 
# ე.წ. „მოხსენება“, რომელიც ამბობს რიცხვი პოზიტიურია თუ ნეგატიური.

# num = int(input("write any number: "))
# while num > 0:
#     print(num, "is positive number")
#     num = int(input("Try again: "))
# if num == 0:
#     print(num, "is zero")
# else:
#     print(num,"is negative number")
#     num = int(input("Try again: "))

# 1–30-ის რიცხვებისთვის დაბეჭდე:

# „Fizz“, თუ რიცხვი 3-ის ჯერადია,

# „Buzz“, თუ 5-ის ჯერადია,

# „FizzBuzz“, თუ ორივეს ჯერადია,

# თვითონ რიცხვი, თუ არც ერთი არ არის.

# for i in range (1,30 + 1):
#     if i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     elif i % 3 == 0 and i % 5 == 0:
#         print("fizzbuzz")
#     else:
#         print(i)

# შექმენი რიცხვების ჯამი, რომელიც შეგროვდება, სანამ ჯამი არ გახდება ≥ 50.
# მომხმარებელმა თითოეული რიცხვი შეიყვანოს.
# დაბეჭდე ჯამი ყოველი შეტანის შემდეგ.
sum_numbers = 0
while sum_numbers < 50:
    number = int(input("შეიყვანეთ რიცხვი: "))
    sum_numbers += number  # ვამატებთ რიცხვს ჯამს
    print("ჯამი ამ ეტაპზე:", sum_numbers)

print("ჯამი ≥ 50 გახდა, პროგრამა დასრულებულია.")
    