print("Title of program: Encouragement bot :) :D :P")
print()
while True:
  description = input("How do you feel?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append("to talk to your family and friends, they can help you feel better! 😁🍙")
      counter += 1
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("to keep smiling and spread joy through good deeds. 😁🍙")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("to get some rest when needed and not to stress yourself out too much. 😁🍙")
      counter += 1
    if each_word == "onigiri":
      feelings_list.append("onigiri")
      encouragement_list.append("congratulations, you have unlocked the final level of onigiris. Good job, and continue being and feeling like an onigiri! 😁🍙")
      counter += 1
  if each_word == "dead":
      feelings_list.append("dead")
      encouragement_list.append("to seek encouragement from friends and family, they would always cheer you up! Stay positive! 😁🍙. Good job, and continue being and feeling like an onigiri")
      counter += 1

  if counter == 0:
    
      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember that "+ encouragement_list[0] + "! Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ".  " encouragement "

  print()
  print(output)
  print()
