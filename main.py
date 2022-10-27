import random
  
  
score = 0
english = ["computer", "lake", "food", "pencil", "storage"]
right_answer = ["rorohiko", "roto", "kai","pene", "rokiroki" ]
option_1 = ["tangata" , "waka" , "poti" , "waiata", "tāne"]
option_2 = ["rangatira" , "karakia" , "kaumatua" , "moana", "Aotearoa"]
  
  
def generate_question(english, right_answer, option_1, option_2):
  global score
  print("What is the correct word for", english , "in maori")
  
  random_sequence = random.randint(0,2)
    
  if (random_sequence == 0):
   print("A", option_1)
   print("B", option_2)
   print("C", right_answer)
   answer = input().lower()
   if answer == "c":
     score += 1
   else:
     print('Incorrect.')
  elif(random_sequence == 1):
    print("A", right_answer)
    print("B", option_1)
    print("C", option_2)
    answer = input().lower()
    if answer == "a":
      score += 1
    else:
      print("Incorrect")
  elif(random_sequence == 2):
    print("A", right_answer)
    print("B", option_2)
    print("C", option_1)
    answer = input().lower()
    if answer == "a":
      score += 1
    else:
      print("Incorrect")
      
  elif(random_sequence == 3):
    print("A", right_answer)
    print("B", option_2)
    print("C", option_1)
    answer = input().lower()
    if answer == "a":
      score += 1
    else:
      print("Incorrect")
   
  elif(random_sequence == 4):
    print("A", right_answer)
    print("B", option_2)
    print("C", option_1)
    answer = input().lower()
    if answer == "a":
      score += 1
    else:
      print("Incorrect")

      
for i in range (0, 5):
 generate_question(english[i],right_answer[i],option_1[i],option_2[i])


print(score)