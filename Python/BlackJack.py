import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def maquina_juega(suma_inicial_maquina,suma_inicial,mano_inicial,mano_inicial_maquina):
    testeo(suma_inicial_maquina,suma_inicial,mano_inicial,mano_inicial_maquina)
    #mientras la suma de las cartas de la maquina es menor a la mia, entonces genera una nueva para el
    while suma_inicial_maquina < suma_inicial:
        carta_nueva_maquina = random.choice(cards)
        suma_inicial_maquina+= carta_nueva_maquina
        if carta_nueva_maquina == 11 and suma_inicial_maquina>21:
          suma_inicial_maquina-=carta_nueva_maquina
          carta_nueva_maquina = 1
          suma_inicial_maquina+=carta_nueva_maquina
        mano_inicial_maquina.append(carta_nueva_maquina)
        print(f"Computer cards: {mano_inicial_maquina}")
        testeo(suma_inicial_maquina,suma_inicial,mano_inicial,mano_inicial_maquina)

def testeo(suma_inicial_maquina,suma_inicial,mano_inicial,mano_inicial_maquina):
  # Testea si yo gano
  if suma_inicial_maquina > 21:
    print("\nYou win\n"f"Your cards: {mano_inicial}, final score: {suma_inicial}\nComputer cards: {mano_inicial_maquina}, final score: {suma_inicial_maquina}\n")
  #Testea si la computadora gana
  if (suma_inicial_maquina > suma_inicial) and (suma_inicial_maquina <= 21) or suma_inicial > 21:
    print("\nComputer wins\n"f"Computer cards: {mano_inicial_maquina}, final score: {suma_inicial_maquina}\nYour cards: {mano_inicial}, final score: {suma_inicial}\n")
  #Testea si hay empate
  if suma_inicial_maquina == suma_inicial :
    print("\nDraw\n"f"Your cards: {mano_inicial}, final score: {suma_inicial}\nComputer cards: {mano_inicial_maquina}, final score: {suma_inicial_maquina}\n")
    

def jugar_o_dejar(suma_inicial_maquina,suma_inicial,mano_inicial,mano_inicial_maquina):
  choice = input("\nType 'y' to get another card, type 'n' to pass: ")
  if choice == "n":
    maquina_juega(suma_inicial_maquina,suma_inicial,mano_inicial,mano_inicial_maquina)

  while choice == "y" and suma_inicial<=21:
    #Tomo una carta nueva para mi
      carta_nueva = random.choice(cards)
      suma_inicial+= carta_nueva
      if carta_nueva == 11 and suma_inicial>21:
        suma_inicial-=carta_nueva
        carta_nueva = 1
        suma_inicial+=carta_nueva
      mano_inicial.append(carta_nueva)
      print(f"Your cards: {mano_inicial}, current score: {suma_inicial}")
      if suma_inicial>21:
       testeo(suma_inicial_maquina,suma_inicial,mano_inicial,mano_inicial_maquina)
      elif suma_inicial <= 21:
        choice = input("\nType 'y' to get another card, type 'n' to pass: ")
        if choice == "n":
          maquina_juega(suma_inicial_maquina,suma_inicial,mano_inicial,mano_inicial_maquina)

#---------------------MAIN-------------------------#   
decision = "y"
while decision == "y":
  decision = input("Do you want to play a game of Blackjack? Type'y' or 'n': ")
  if decision == "y":
  #Ronda inicial
  #Mano mia inicial
    mano_inicial = [1,1]
    mano_inicial[0] = random.choice(cards)
    mano_inicial[1] = random.choice(cards)
    suma_inicial = mano_inicial[0]+mano_inicial[1]
    print("\n"f"Your cards: {mano_inicial}, current score: {suma_inicial}")
    
    #Mano de la maquina inicial
    mano_inicial_maquina = [1,1]
    mano_inicial_maquina[0] = random.choice(cards)
    mano_inicial_maquina[1] = random.choice(cards)
    suma_inicial_maquina = mano_inicial_maquina[0]+mano_inicial_maquina[1]
    print(f"Computer's first card: {mano_inicial_maquina[0]} ")
    
    #Funcion del juego a partir del maso inicial
    jugar_o_dejar(suma_inicial_maquina,suma_inicial,mano_inicial,mano_inicial_maquina)

  else:
      print("Goodbye\n")

