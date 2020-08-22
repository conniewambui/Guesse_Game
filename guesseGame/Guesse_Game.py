import random

people= []

for x in range (0,8):
  user =  input("Write names of people you know? ")
  people. append(user)

index = random.randint(0,7)

random_user = people[index]

print( "Pick a random person ", random_user)

print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")


colors = ["red", "green", "pink", "yellow", "purple", "indigo"]

while True:
  color = colors[random.randint(0,len(colors)-1)]
  guesse= input("I am thinking about a color, can you guesse  it? ")
    
  while True:
    
     if(color ==guesse.lower()):
        break
     else:
       guesse= input("Nope! Try again: ")
        
  print("You guessed it!")
       
  play_again = input("Let's play again? Type 'no' to quit:")
      
  if play_again.lower() == 'no' :
    break
       
print("It was fantastic. Thank you for playing. ")