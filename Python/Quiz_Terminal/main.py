import random
from art import logo 
from art import vs
from game_data import data

def dato_aleatorio(data):
  global personaje
  personaje= random.choice(data)
  return personaje["follower_count"]
  
def presentacion(personaje,letter):
    print(f"Compare {letter}: " ,personaje["name"]+", a "+ personaje["description"]+" from " + personaje["country"])

def a_or_b(a,b):
  mayor = max(a,b)
  
  if a == mayor:
    return "A"
    
  elif b == mayor:
    return "B"

def check(choice,a,b,score):
  if a_or_b(a,b) == choice:
    print(f"You're right!. Current score: {score+1}")
    
  else:
    print(f"Sorry, that's wrong. Final score: {score}")
    global game_over 
    game_over = True 
  

   

#--------MAIN--------
game_over = False
score = 0
b = dato_aleatorio(data)
while game_over == False:
    print(logo)
    a=b
    presentacion(personaje,"A")
    print(vs, "\n")
    b = dato_aleatorio(data)
    presentacion(personaje,"B")
    

    choice = input("Who has more followers? Type 'A' or 'B':")
    
    a_or_b(a,b)
    check(choice,a,b,score)
  
    score+=1
  
