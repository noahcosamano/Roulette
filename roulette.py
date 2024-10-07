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
    global decide_lives_r_1
    print(shells,"shells are racked.",blanks,"shell(s) are blanks,",lives,"shell(s) are lives...")
    decide_lives_r_1 = random.randint(1,shells)
    return decide_lives_r_1

def decide_target(target):
    global decide_lives_r_1
    if target.lower() == "s":
        if decide_lives_r_1 < 2:
            print("IT WAS A LIVE ROUND! LIFE LOST!")
        if decide_lives_r_1 > 1:
            decide_lives_r_1 =- 1
            print("PHEW! IT WAS A BLANK.")
            return True
    elif target.lower() == "d":
        if decide_lives_r_1 < 2:
            print("IT WAS A LIVE ROUND! DEALER DOWN!")
        if decide_lives_r_1 > 1:
            decide_lives_r_1 =- 1
            print("IT WAS A BLANK! DEALERS TURN!")

        

def main():
    rack_round_one(3,2,1)
    decide_target()

main()


