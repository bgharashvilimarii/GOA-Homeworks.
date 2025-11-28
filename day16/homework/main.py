# num = 10
# while num >= -10:
#     print(num)
#     num -= 1

# 
# მომხმარებელს შემოატანინეთ
# პაროლი იქამდე სანამ ის 
# არ გაუტოლდება "goa123"-ს, ამასთან ერთად მას უნდა ჰქონდეს მხოლოდ
# 3 მცდელობა სწორი პაროლის შესაყვანად. ყოველი 
# არასწორი მცდელობისას დაუბეჭეთ "Password is incorrect! Try again",
# ასევე დაუბეჭდეთ ის თუ რამდენი მცდელობა
# (მხოლოდ რიცხვი არა, ტექსტი გასაგებად).
# თუ მომხმარებელს ამოეწურა მცდელობების რაოდენობა ან სწორად შეიყვანა პაროლი უბრალოდ გათიშეთ while ციკლი

correct_password = "goa123"
input_password = input("Please Enter Your Password: ")
tries = 0
max_tries = 2


while input_password != correct_password and tries < max_tries:
    attampt = attampt + 1
    print("Password is incorrect! Try again")
    print("you only have 3 attampt")
    input_password = input("Please Enter Your Password: ")
