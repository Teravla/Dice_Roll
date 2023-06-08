import random
import time
# -*- coding: utf-8 -*-

class dice:
    
    def __init__(self) -> None:
        self.face_de = 6
        self.de = []
        self.dice_result = []
        self.round = 0
    
    def lancer(self, nb_de:int, mode:str) -> None:
        
        print("\n\n================================================================\n\n{:^75}\n\n================================================================".format("Good Luck!"))
        
        roll = True
        
        while roll:
            self.de = []
            
            print ("\n{} Round\n".format(self.round))
            for i in range(nb_de):
                draw = random.randint(1, 6)
                self.de.append(draw)
                if i == 0: 
                    print("\nYour first draw is {}".format(self.de[i]))
                elif i == 1:
                    print("\nYour second draw is {}".format(self.de[i]))
                elif i == 2:
                    print("\nYour third draw is {}".format(self.de[i]))
                
            print("\n\nThe result is : {}\n" .format(self.de[0]+self.de[1]+self.de[2]))
            self.result = sum(self.de)
            
            self.dice_result.append(self.result)
            self.round += 1
            
            print("Your Draw : ", end="")
            for i in range(len(self.dice_result)):
                print(self.dice_result[i], end="; ")
            
            
            if self.round >= 2:
                if self.dice_result[self.round-1] < self.dice_result[self.round-2]:
                    print("\nYou lose in {} rounds\n". format(len(self.dice_result)))
                    input_lose = input("\nWant to play again? (y/n) : ")
                    while input_lose!= "y" and input_lose!= "n" and input_lose!= "1" and input_lose!= "0":
                        input_lose = input("\nWant to play again? (y/n) : ")
                    if input_lose == "y" or input_lose == "1":
                        dice().lancer(nb_de, mode)
                    elif input_lose == "n" or input_lose == "0":
                        quit()
                
            if mode == "manual":
                input_lancer = input("\nReroll? (y/n) : ")
                while input_lancer!= "y" and input_lancer!= "n":
                    input_lancer = input("\nReroll? (y/n) : ")
                    
                if input_lancer == "y":
                    roll = True
                elif input_lancer == "n":
                    roll = False
                    
            if mode == "automatic":
                print("\nNew roll in 2 seconds")
                time.sleep(1)
                print("New roll in 1 seconds")
                time.sleep(1)
                
                
        
        
        
            
        
            
    
    
    
class game:
    
    def __init__(self) -> None:
        dice().__init__()
    
    def display(self, nb_de:int, mode:str="automatic") -> None:
        print("\n\n{:^75}\n\n".format("--- Dice to Roll ---"))
        print("Welcome to this game, you have " + str(nb_de) + " dice")
        
        print("\n\n")
        
        print("1 - Play")
        print("2 - Settings")
        print("3 - Rules")
        print("4 - Quit")
        
        input_menu = int(input("\nMake your choice: "))
        while input_menu!= 1 and input_menu!= 2 and input_menu!= 3 and input_menu!= 4:
            input_menu = int(input("Make your choice: "))
            
        if input_menu == 1:
            if mode == "manual":
                dice().lancer(nb_de, "manual")
            elif mode == "automatic":
                dice().lancer(nb_de, "automatic")
        if input_menu == 2:
            print("1 - Language")
            print("2 - Difficulty")
            print("3 - Mode")
            print("4 - Play")
            
            input_settings= int(input("\nMake your choice: "))
            while input_settings!= 1 and input_settings!= 2 and input_settings!= 3:
                input_settings = int(input("Make your choice: "))
        
            if input_settings == 1:
                pass
        
            elif input_settings == 2:
                print("1 - Easy")
                print("2 - Medium")
                print("3 - Hard")
                
                input_difficulty= int(input("\nMake your choice: "))
                while input_difficulty!= 1 and input_difficulty!= 2 and input_difficulty!= 3:
                    input_difficulty = int(input("Make your choice: "))
                
                if input_difficulty == 1:
                    game().display(5)
                elif input_difficulty == 2:
                    game().display(3)
                elif input_difficulty == 3:
                    game().display(2)
            
            elif input_settings == 3:
                print("1 - Manual")
                print("2 - Automatic")
                
                input_mode = int(input("\nMake your choice: "))
                while input_mode!= 1 and input_mode!= 2:
                    input_menu = int(input("Make your choice: "))
                
                if input_mode == 1:
                    game().display(3, "manual")
                elif input_mode == 2:
                    game().display(3, "automatic")
                    
            
            elif input_settings == 4:
                game().display(3)
                
        
        if input_menu == 3:
            print("\nWelcome, Your objective is to score the most points by rolling the dice. You must score higher than the previous score to continue. Otherwise, you lose.\n")  
            
            game().display(3)
        
        if input_menu == 4:
            quit()
            
    

if __name__ == "__main__":
    game().display(3)
    