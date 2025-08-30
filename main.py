'''
1 for snake
-1 for water 
0 for gun
 
'''
import random
computer=random.choice([-1,0,1])
yousstr=(input("Enter your choice"))
Youdict={"s":1,"w":-1,"g":0}
reversedict={1:"Snake",-1:"water",0:"Gun"}

you =Youdict[yousstr]

print(f"you chose{reversedict[you]}\nComputer chose{reversedict[computer]}")

if(computer==you):
    print("Its a Draw,,")


else:
  if(computer==-1 and you==1):
    print("You Winn !")

  elif(computer==-1 and you==0):
    print("You Lose !")    

  elif(computer==1 and you==-1):
    print("You lose !")

  elif(computer==1 and you==0):
    print("You Win !")

  elif(computer==0 and you==-1):
    print(" You Win !")

  elif(computer==0 and you==1):
    print("You Lose !")        

  else:
    print("Something Went Wrong")    