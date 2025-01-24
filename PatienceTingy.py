level = 1
difficulty_number = 1
difficulty = "easy"
n = 0
mult = 1
specialmult = 1
level_req_for_specialmult = 10
difficulty = input("what difficulty do you want to play on? (easy, medium, hard)")
if difficulty == "easy":
  difficulty_number = 1
elif difficulty == "medium":
  difficulty_number = 2
elif difficulty == "hard":
  difficulty_number = 3
while True:
  while n < (level*specialmult)**difficulty_number:
    n+=1*mult
    print(n)
  n = 0
  if level_req_for_specialmult == level:
    specialmult *= 10
    level_req_for_specialmult += 10
  continue1 = input("Do you want to continue? (y/n)")
  if continue1 == "y":
    level_choise = input(f"Do you want to go up a level? (y/n) (yes = {level}+1 no = {mult}*2)")
    if level_choise == "y":
      level += 1
    elif level_choise == "n":
      mult = mult*2
  elif continue1 == "n":
    print(f"you ended at level {level}")
    quit()