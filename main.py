import random
 
from bke import EvaluationAgent, MLAgent, is_winner, opponent, RandomAgent, train_and_plot, save, train, load, start
 
 
class MyAgent(MLAgent):
    def evaluate(self, board):
        if is_winner(board, self.symbol):
            reward = 1
        elif is_winner(board, opponent[self.symbol]):
            reward = -1
        else:
            reward = 0
        return reward
    
    
class MyRandomAgent(EvaluationAgent):
  def evaluate(self, board, my_symbol, opponent_symbol):
    return random.randint(1, 500)

def tegendom():
  my_random_agent = MyRandomAgent()
  start(player_o=my_random_agent)

def trainAlleen():
  my_agent = MyAgent()
  
  train(my_agent, 3000)
  save(my_agent, 'MyAgent_3000')

def tegenslim():
  my_agent = load('MyAgent_3000')

  my_agent.learning = False
  start(player_x=my_agent)

def tegenander():
  start()

def plot():
  random.seed(1)
 
  my_agent = MyAgent(alpha=0.8, epsilon=0.2)
    #Hier zijn hyperparameters gebruikt. Hyperparameters zijn aanpasbare parameters waarmee je het modeltrainingsproces kunt beheren. Met neurale netwerken bepaal je bijvoorbeeld het aantal verborgen lagen en het aantal knooppunten in elke laag. Hier bij de grafiek verander je het gedrag van de functie door de parameters van de functie te veranderen. Hierdoor configureer je de machine learning-agent. Alpha is de leerfactor van de agent. Deze bepaalt hoe snel de agent nieuwe kennis adopteert. Hoe hoger dit getal, hoe sneller de agent geneigd zal zijn om oude kennis te vervangen door nieuwe kennis. Epsilon is de verkenningsfactor van de agent. Deze bepaalt hoe vaak de agent nieuwe dingen probeert. Hoe hoger dit getal, hoe vaker de agent een willekeurige actie probeert in plaats van de best bekende zet.
  random_agent = RandomAgent()
 
  train_and_plot(
    agent=my_agent,
    validation_agent=random_agent,
    iterations=50,
    trainings=100,
    validations=1000)


print("1: Tegen een domme tegenstander spelen")
print("2: De tegenstander trainen")
print("3: Tegen een slimme tegenstander spelen")
print("4: Tegen een andere persoon spelen")
print("5: Een validatie grafiek plotten")

i = input()

if i == "1":
  tegendom()

if i == "2":
  trainAlleen()

if i== "3":
  tegenslim()

if i == "4":
  tegenander()

if i == "5":
  plot()