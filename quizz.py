print("welcome to quizz")
playing=input("Do you want to play a quizz...... ")
if playing!="yes" :
    quit()
else:print("okay! Let's Play")
score=0
answer=input("what is the full form of CPU ?\n")
if answer=="central processing unit" :
 print("correct")
 score+=1
else:print("incorrect!") 
answer=input("which is the full form of RAM ? \n")
if answer=="random access memory" :
   print("correct")
   score+=1
else:print("incorrect!")
answer=input("what is the full form of GB ?\n")
if answer=="gega bytes":
   print("correct")
   score+=1
else :print("incorrect!")
answer=input("what is the unit of capacitance ?\n")
if answer=="farad" :
 print("correct")
 score+=1
else:print("incorrect!")
answer=input("what does LED stand's for ?\n")
if answer=="light emitting diode" :
 print("correct")
 score+=1
else:print("incorrect!")
answer=input("what is the unit of current ?\n")
if answer=="ampere" :
 print("correct")
 score+=1
else:print("incorrect!")
print(f"you answered {score} questions out of 6 ")
print(f"you got {score/6*100} % ")
