from hashlib import sha256
import os

Secure_data_extraction = open(r"Secure_data_storage.txt", "a")
Secure_data_extraction.close()
Secure_data_extraction = open(r"Secure_data_storage.txt", "r")
Extracted_Data = Secure_data_extraction.readline()
Secure_data_extraction.close()
Extracted_Data = Extracted_Data.split(",")
Listed_Users = Extracted_Data[0::2]
Listed_Passwords = Extracted_Data[1::2]

Option = input("Log in or Sign in? ")
if Option == "Log in":
  Username = input(str("Enter your username: "))
  Password = input(str("Enter your password: "))
  h = sha256()
  h.update(f'{Password}'.encode('utf-8'))
  Encoded_Password = h.hexdigest()
  for i in range(len(Listed_Passwords)):
    if Username == Listed_Users[i] and Encoded_Password == Listed_Passwords[i]:
      Current_User = open(f"User_{i+1}.txt", "a+")
      Current_User.close()
      Current_User = open(f"User_{i+1}.txt", "r")
      Current_User_Data = Current_User.read()
      Current_User_Data = Current_User_Data.split(",")
      Current_User.close()
      if Username == "USSB":
        Setting_change_affirmation = input("Open USSB setting changer? [y/n] ")
        if Setting_change_affirmation == "y":
          USSB_TM = open(r"User_1.txt", "w+")
          USSB_TM_Data = USSB_TM.read()
          USSB_TM_Data = USSB_TM_Data.split(",")
          USSB_TM.close()
          Setting_change = input("USSB setting change: ")
          Secure_data_insertion = open(r"User_1.txt", "w")
          Secure_data_insertion.write("User Special Status Bot, Bot Activation Or Settings Change,"+Setting_change+",")
        elif Setting_change_affirmation == "n":
          USSB_TM = open(r"User_1.txt", "w+")
          USSB_TM_Data = USSB_TM.read()
          USSB_TM_Data = USSB_TM_Data.split(",")
          USSB_TM.close()
         
          if Current_User_Data[2] == "Affirmed User Deletion":
            print("User Deletion Affirmed")
            Selective_Deletion = input("Selective Deletion? [y/n] ")
            if Selective_Deletion == "y":
                print("Selective Deletion Selected")
                User_found = False
                User_ID = 0
                User_Deletion = input("Which user is to be deleted? ")
                if User_Deletion == "USSB":
                  print("USSB cannot be deleted")
                elif User_Deletion != "USSB":
                  for i in range(len(Listed_Passwords)):
                    if User_Deletion == Listed_Users[i]:
                      os.remove(f"User_{i+1}.txt")
                      User_found = True
                      User_ID = i+1
                    elif User_found == True and User_ID < i+1:
                      os.rename(f"User_{i+1}.txt", f"User_{i}.txt")
                  Secure_data_removal = open(r"Secure_data_storage.txt", "w")
                  Secure_data_removal.write("")
                  Secure_data_removal.close()
                  for i in range(len(Listed_Passwords)):
                    if User_Deletion != Listed_Users[i]:
                      Secure_data_removal = open(r"Secure_data_storage.txt", "a")
                      Secure_data_removal.write(Listed_Users[i])
                      Secure_data_removal.write(",")
                      Secure_data_removal.write(Listed_Passwords[i])
                      Secure_data_removal.write(",")
                      Secure_data_removal.close()
                else:
                  print("An error has occured")
            elif Selective_Deletion == "n":
              print("Delete all Selected")
              User_wipe = open(r"Secure_data_storage.txt", "w")
              User_wipe.write(Username+","+Encoded_Password+",")
              User_wipe.close()
              for i in range(len(Listed_Passwords)):
                if Username != Listed_Users[i]:
                  if f"User_{i+1}" in os.listdir():
                    os.remove(f"User_{i+1}.txt")
                   
          elif Current_User_Data[2] == "Affirmed User Info Clear":
            print("User Info Clear Affirmed")
            Selective_Clear = input("Selective Clear? [y/n] ")
            if Selective_Clear == "y":
              print("Selective Clear Selected")
              User_Clear = input("Which user is to be cleared? ")
              if User_Clear == "USSB":
                print("USSB cannot be cleared")
              elif User_Clear != "USSB":
                for i in range(len(Listed_Users)):
                  if User_Clear == Listed_Users[i]:
                    os.remove(f"User_{i+1}.txt")
            elif Selective_Clear == "n":
              print("Clear all Selected")
              for i in range(len(Listed_Passwords)):
                if Username != Listed_Users[i]:
                  os.remove(f"User_{i+1}.txt")
      else:
        print("Welcome back, " + Username)
    elif Username == Listed_Users[i] and Password != Listed_Passwords[i]:
      print("Incorrect username or password")
 
elif Option == "Sign in":
  Username = input("Create a username ")
  Password = input("Create a password ")
  if Username in Listed_Users:
    print("This username is already taken, but remember that your display name can be changed later in settings. (display name does not equal username)")
  else:
    h = sha256()
    h.update(f'{Password}'.encode('utf-8'))
    Encoded_Password = h.hexdigest()
    Secure_data_insertion = open(r"Secure_data_storage.txt", "a")
    Secure_data_insertion.write(Username)
    Secure_data_insertion.write(",")
    Secure_data_insertion.write(Encoded_Password)
    Secure_data_insertion.write(",")
    Secure_data_insertion.close()
    print("You have signed in!")
else:
  print("Invalid command.")