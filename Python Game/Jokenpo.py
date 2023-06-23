import random

#declarando funções e variaveis
def get_choices(): 
  player_choice = input("Enter a choice (rock, paper or scissors): ")
  options = ["paper", "rock", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices
  
def check_win(player, computer):
  print(f"You chose {player}, computer chose {computer}")
  if player == computer:
    return "It's a Tie!"
  #para substituir o And, podemos utilizar Refactoring, quando a comparação do elif é igual
  elif player == "rock":
    if computer == "scissors":
      return "Rocks smashes scissors! You win!"
    else:
      return "Papers covers rock! You lose..."
  elif player == "paper":
    if computer == "rock":
      return "Paper covers rock! You win!"
    else:
      return "Scissors cuts paper! you lose..."
  elif player == "scissors":
    if computer == "rock":
      return "Rocks smashes scissors! you lose..."
    else:
      return "Scissors cuts paper! you win!"
    
choices = get_choices()

#Uma variavel que chama a função 'check_win' passando a dictionary choices com as keys player e computer, que retorna uma string
result = check_win(choices["player"], choices["computer"])
print(result)

#exemplo de f-string
  #age = 25 
  #print(f"Jim is {age} years old")

#chamando a função
  #choices = get_choices()

  #print(choices)

  #food = ["pizza", "ramcambole", "ovo"]
  #dinner = random.choice(food)

#exemplo de declaração de Dictionaries 

disc = {
  "name": #key
  "bean", #value
  "color": "blue"
}
