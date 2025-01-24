import random
from hashlib import sha256
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
Password_number = 1
Hash_code_number = 1

print("welcome to the PyPassword Generator and the Hash Checker.")
option_PyPassword_or_Hash_Checker = input("Would you like to generate a PyPassword or check a Hash? (PyPassword/Hash): ")
if option_PyPassword_or_Hash_Checker == "PyPassword":
  print("You have chosen for the PyPassword Generator!")
  Bulking = input(f"Would you like to create PyPasswords in bulk? (y/n): ")
  if Bulking == "y":
    Bulk_amount = int(input(f"How many PyPasswords would you like to create?: "))
    nr_letters= int(input("How many letters would you like your password?\n"))
    nr_symbols= int(input("How many symbols would you like your password?\n"))
    nr_numbers= int(input("How many numbers would you like your password?\n"))
    print("Your passwords and Hash codes are:")
    for i in range(0, Bulk_amount):
      password_part = []

      for l in range(0, nr_letters):
        password_part += letters[random.randint(0,51)]

      for s in range(0, nr_symbols):
        password_part += symbols[random.randint(0,8)]

      for n in range(0, nr_numbers):
        password_part += numbers[random.randint(0,9)]

      random.shuffle(password_part)
      password = "".join(password_part)
      print("Your", Password_number, "password is: ", password)
      print("Your", Hash_code_number, "Hash code is:", sha256(password.encode()).hexdigest())
      print(" ")
      Password_number += 1
      Hash_code_number += 1
    Password_number = 1
    Hash_code_number = 1
    quit()
  if Bulking == "n":
      nr_letters= int(input("How many letters would you like your password?\n"))
      nr_symbols= int(input("How many symbols would you like your password?\n"))
      nr_numbers= int(input("How many numbers would you like your password?\n"))
      password_part = []

      for l in range(0, nr_letters):
        password_part += letters[random.randint(0,51)]

      for s in range(0, nr_symbols):
        password_part += symbols[random.randint(0,8)]

      for n in range(0, nr_numbers):
        password_part += numbers[random.randint(0,9)]

      random.shuffle(password_part)
      password = "".join(password_part)
      print("your password is: ", password)
      print("your Hash code is:", sha256(password.encode()).hexdigest())
      print(" ")
      quit()



elif option_PyPassword_or_Hash_Checker == "Hash":
  print("You have chosen for the Hash Checker!")
  hash_to_check = input("What is the code you want to check?\n")
  h = sha256()
  h.update(f'{hash_to_check}'.encode('utf-8'))
  hash = h.hexdigest()
  print(hash)


else:
  print("I dont understand, please run the code again and select (PyPassword/Hash) Remember that this code is checking for the correct spelling.")