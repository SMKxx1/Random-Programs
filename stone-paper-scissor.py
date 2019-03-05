import random

def art():
    print('''
  ____  _                         ____                           ____       _                    
 / ___|| |_ ___  _ __   ___      |  _ \ __ _ _ __   ___ _ __    / ___|  ___(_)___ ___  ___  _ __ 
 \___ \| __/ _ \| '_ \ / _ \_____| |_) / _` | '_ \ / _ \ '__|___\___ \ / __| / __/ __|/ _ \| '__|
  ___) | || (_) | | | |  __/_____|  __/ (_| | |_) |  __/ | |_____|__) | (__| \__ \__ \ (_) | |   
 |____/ \__\___/|_| |_|\___|     |_|   \__,_| .__/ \___|_|      |____/ \___|_|___/___/\___/|_|   
                                            |_|                                                                                                                            
    _______                                                                                                                                                               
---'   ____)                                                               
      (_____)
      (_____)
      (____)
---.__(___)

    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

''')

art()

bot_score = 0
player_score = 0

def game():
    rule = {1:'stone',2:'paper',3:'scissor'}
    def mid_game():
        while True:
            global bot_score
            global player_score
            print("Stone-Paper-Scissor")
            player = input("> ")

            if player.isdigit():
                if eval(player) in rule:
                    player = rule[eval(player)]
                else:
                    print("I don't know what that is...")
                    print()
                    mid_game()
            else:
                pass

            if player == 'stone' or player == '1':
                pass
            elif player == 'paper' or player == '2':
                pass
            elif player == 'scissor' or player == '3':
                pass
            else:
                print("I don't know what that is...")
                print()
                mid_game()
            bot = random.randint(1,3)
            bot = rule[bot]

            if (bot == 'scissor') and player == 'stone':
                print("Bot chose scissor")
                player_score += 1
                print("Player:",player_score,"Bot:",bot_score)
                print()

            elif bot == 'scissor' and player == 'paper':
                print("Bot chose scissor")
                bot_score += 1
                print("Player:", player_score, "Bot:", bot_score)
                print()
            elif bot == 'paper' and player == 'scissor':
                print("Bot chose paper")
                player_score += 1
                print("Player:", player_score, "Bot:", bot_score)
                print()
            elif bot == 'paper' and player == 'stone':
                print("Bot chose paper")
                bot_score += 1
                print("Player:", player_score, "Bot:", bot_score)
                print()
            elif bot == 'stone' and player == 'scissor':
                print("Bot chose stone")
                bot_score += 1
                print("Player:", player_score, "Bot:", bot_score)
                print()
            elif bot == 'stone' and player == 'paper':
                print("Bot chose stone")
                player_score += 1
                print("Player:", player_score, "Bot:", bot_score)
                print()
            else:
                print("Draw")
                print("Player:", player_score, "Bot:", bot_score)
                print()
            if bot_score > 4:
                break
            elif player_score > 4:
                break
            else:
                continue
        if bot_score > player_score:
            print("The bot has won by",bot_score - player_score,"points")
            print("Better Luck Next Time...")
        else:
            print("You have won by",player_score - bot_score,"points")
            print("Congratulations!!!")

    mid_game()

game()