import random #randomizes computer choices
import colorterminal #add color to some text




class HumanPlayer:
    def __init__(self, name):
        self.name = name
        self.score = 0  

    def choose(self):
        choice = input(f"{self.name}, enter your choice of rock, paper or scissors: ")
        while choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose again.")
            choice = input(f"{self.name}, enter your choice of rock, paper, or scissors: ")
        return choice #user will put in choice and if they give anything other than RPS, they will get an error
    
class ComputerPlayer(HumanPlayer):

    mylist = ['rock', 'paper', 'scissors']

    def choose(self):
        return random.choice(self.mylist)    
    
    #will inherit everything from parent class, and random.choice will allow it get a random choice

class Game:
    
    def start_game(self):
        print(colorterminal.ColorText.BLUE + ' Welcome to Rock, Paper, Scissors!')
        player_name = input("Enter your name: ")
        self.human_player = HumanPlayer(player_name)
        self.computer_player = ComputerPlayer("Computer")
        self.display_menu()
        

    #this startgame function creates player objects & initializes game object. this will serve
    #as the starting point anytime the game is executed

        while True:
            self.play_round()
            self.display_scoreboard()
            play_again = input("Do you want to play another round? (yes/no): ")
            if play_again != 'yes':
                print(f"Final Results:{self.human_player.name} scores {self.human_player.score} & {self.computer_player.name} scores {self.computer_player.score}")
                self.display_winner()
                break

    def display_menu(self):
        rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

        paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

        scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
        print("\nMenu:")
        print("1. Play Rock, Paper, Scissors")
        print("2. Rules:")
        print("  - Rock beats Scissors.")
        print("  - Scissors beats Paper.")
        print("  - Paper beats Rock.")
        print("  - If both players choose the same item, it's a tie.\n")
        print("Images:")
        print("Rock:\n" + rock)
        print("Paper:\n" + paper)
        print("Scissors:\n" + scissors)

    def play_round(self):
        print("New round!\n")
        human_choice = self.human_player.choose()
        computer_choice = self.computer_player.choose()
        print(f"{self.human_player.name} chooses {human_choice}.")
        print(f"{self.computer_player.name} chooses {computer_choice}.")

        #the choose method allows human players to input their choice & the computer to randomize its choices
        #this is possible because of the methods defined above

        if human_choice == computer_choice:
            print(f"Both players selected {human_choice}. It's a tie!")

            #this would indicate a tie


        elif human_choice == "paper":
            if computer_choice == "rock":
                print("You win - paper covers rock!!! :)")
                self.human_player.score += 1
            else:
                print("You lose - scissors cuts paper. :()")
                self.computer_player.score += 1

        elif human_choice == "scissors":
            if computer_choice == "paper":
                print("You win - scissors cuts paper!!! :) ")
                self.human_player.score += 1

            else:
                print("You lose - rock smashes scissors. :() ")
                self.computer_player.score += 1

        
        elif human_choice == "rock":
            if computer_choice == "scissors":
                print("You win - rock smashes scissors!!! :)")
                self.human_player.score += 1

            else:
                print("You lose - paper covers rock. :() ")
                self.computer_player.score += 1


        #covers all possible scenarios & keeps a score

    def display_scoreboard(self):
        print("\nScoreboard:")
        print(f"{self.human_player.name}: {self.human_player.score}")
        print(f"{self.computer_player.name}: {self.computer_player.score}\n")
    
    def display_winner(self):
        if self.human_player.score > self.computer_player.score:
            print(f"{self.human_player.name} wins the game with {self.human_player.score} points!!! :)")
        elif self.human_player.score < self.computer_player.score:
            print(f"{self.computer_player.name} wins the game with {self.computer_player.score} points! Sorry, {self.human_player.name}, better luck next time!")
        else:
            print("The game is a tie!")
                #score determines winner on screen
    
    


    
    
    
   

        

