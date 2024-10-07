'''import random

RESCUSITATIONS = 3
DEALER_RES = 3
LIVES = 2
DEALER_LIVES = 2

def rules():
    print("Welcome to Python Roulette. The rules are simple.. you live, or you dont.")
    print("On each round, there will be you and a dealer. On each new round, the dealer racks a shotgun.")
    print("The shotgun will always contain live rounds and blanks, which the amounts will be announced to you.")
    print("On your turn, you can choose to aim at yourself, or the dealer and take the shot.")
    print("If you aim at yourself, and the shot is a blank, you go again. You can recycle this until a live round goes off.")
    print("If the shot is a live round, then you lose a life, each round you have two lives, along with the dealer.")
    print("After you have used both lives, then you lose a rescusitation. After you have been rescusitated 3 times, the game is over.")
    print("If you aim at the dealer and the shot is a blank, it's the dealers turn to decide.")
    print("If you aim at the dealer and the shot is a live round, the dealer loses a life until both lives are gone.")
    print("After a player loses both lives, the next round will start. You will begin with two new lives, and lose a rescusitation.")
    input("Press enter to start the game: ")

def play():
    play_again = input("Type 'Y' to play again, type 'N' to exit")
    lower_play_again = play_again.lower()
    if lower_play_again == "y":
        return True
    return False

def r_one_rack(shells):
    print("Beginning round one.")
    print(shells,"shells are loaded...")
    BAD_SHELL = random.randint(1,shells)
    return BAD_SHELL

def take_shot(BAD_SHELL,LOWER_TARGET):
    LIVES = 2
    RESCUSITATIONS = 3
    DEALER_LIVES = 2
    DEALER_RES = 3
    while True:
        if LOWER_TARGET == "s":
            shot = BAD_SHELL - 1
            if BAD_SHELL < 1:
                print("IT WAS A LIVE ROUND!!! Lives remaining: ",LIVES - 1)
                if LIVES < 1:
                    print("YOU LOSE!!! RESCUSITATING...",RESCUSITATIONS -1)
                    if RESCUSITATIONS < 1:
                        print("YOU DIED!!! NO MORE RESCUSITATIONS, YOU LOSE!!!")
            return True
        if LOWER_TARGET == "d":
            shot = BAD_SHELL - 1
            if BAD_SHELL < 1:
                print("GOOD JOB! THATS ONE LIFE GONE! Dealer lives remaining: ",DEALER_LIVES - 1)
                if DEALER_LIVES < 1:
                    print("YOU WIN!!! RESCUSITATING DEALER...",DEALER_RES -1)
                    if DEALER_RES < 1:
                        print("DEALER DEAD!!! NO MORE RESCUSITATIONS, YOU WIN!!!")
    
def choose_target():
    target = input("Press 's' to aim at yourself, press 'd' to aim at dealer: ")
    LOWER_TARGET = target.lower()
    return LOWER_TARGET
    

def main():
    # rules()
    r_one_rack(3)
    choose_target()
    take_shot(BAD_SHELL,LOWER_TARGET)

if __name__ == "__main__":
    main()
'''

import random

decide_lives_r_1 = int(0)

def rules():
    print("Welcome to Python Roulette. The rules are simple.. you live, or you dont.")
    print("On each round, there will be you and a dealer. On each new round, the dealer racks a shotgun.")
    print("The shotgun will always contain live rounds and blanks, which the amounts will be announced to you.")
    print("On your turn, you can choose to aim at yourself, or the dealer and take the shot.")
    print("If you aim at yourself, and the shot is a blank, you go again. You can recycle this until a live round goes off.")
    print("If the shot is a live round, then you lose a life, each round you have two lives, along with the dealer.")
    print("After you have used both lives, then you lose a rescusitation. After you have been rescusitated 3 times, the game is over.")
    print("If you aim at the dealer and the shot is a blank, it's the dealers turn to decide.")
    print("If you aim at the dealer and the shot is a live round, the dealer loses a life until both lives are gone.")
    print("After a player loses both lives, the next round will start. You will begin with two new lives, and lose a rescusitation.")
    input("Press enter to start the game: ")

def rack_round_one(shells,blanks,lives):
    print(shells,"shells are racked.",blanks,"shell(s) are blanks,",lives,"shell(s) are lives...")
    decide_lives_r_1 = random.randint(1,shells)
    return decide_lives_r_1

def decide_target(target):
    while True:
        if target.lower() == "s":
            if decide_lives_r_1 < 2:
                print("IT WAS A LIVE ROUND! LIFE LOST!")
                break
            elif decide_lives_r_1 > 1:
                decide_lives_r_1 =- 1
                print("PHEW! IT WAS A BLANK.")
                return True
        elif target.lower() == "d":
            if decide_lives_r_1 < 2:
                print("IT WAS A LIVE ROUND! DEALER DOWN!")
                break
            elif decide_lives_r_1 > 1:
                decide_lives_r_1 =- 1
                print("IT WAS A BLANK! DEALERS TURN!")
                break

        

def main():
    rack_round_one(3,2,1)
    target = input("To aim at yourself press 's', to aim at dealer press 'd':")
    decide_target(target)

main()


