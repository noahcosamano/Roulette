import random

decide_lives_r_1 = int(0)
player_lifes = int(2)

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
    return decide_lives_r_1, shells, blanks, lives

def start_turn(target,shells,blanks,lives):
    global decide_lives_r_1
    global player_lifes

    if target.lower() == "s":
        if decide_lives_r_1 == 1:
            player_lifes -= 1
            print("IT WAS A LIVE ROUND! Lifes remaining:",player_lifes)
            shells -= 1
            lives -= 1
            return False
        else:
            decide_lives_r_1 -= 1
            print("PHEW! IT WAS A BLANK.")
            shells -= 1
            blanks -= 1
            return True,shells,lives
    elif target.lower() == "d":
        if decide_lives_r_1 == 1:
            print("IT WAS A LIVE ROUND! DEALER DOWN!")
            shells -= 1
            lives -= 1
            return False
        else:
            decide_lives_r_1 -= 1
            print("IT WAS A BLANK! DEALERS TURN!")
            shells -=1
            blanks -= 1
            return False

def dealer_start_turn(shells,blanks,lives):
    global decide_lives_r_1
    print(shells)
    print(blanks)
    print(lives)

def main():
    shells,blanks,lives = 3,2,1
    rack_round_one(shells,blanks,lives)
    while True:
        target = input("To aim at yourself press 's', to aim at dealer press 'd': ")
        print()
        if not start_turn(target,shells,blanks,lives):
            break
    dealer_start_turn(shells,blanks,lives)

main()


