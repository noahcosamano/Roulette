import random

RESCUSITATIONS = 3

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

def play():
    play_again = input("Type 'Y' to play again, type 'N' to exit")
    lower_play_again = play_again.lower()
    if lower_play_again == "y":
        return True
    return False

def r_one_rack(shells):
    print(shells,"shells are loaded...")
    bad_shell = random.randint(1,shells)
    return bad_shell
    
def choose_target():
    target = input("Press 's' to aim at yourself, press 'd' to aim at dealer: ")
    lower_target = target.lower()
    return lower_target

def main():
    rules()
    # choose_target()
    # r_one_rack(3)

if __name__ == "__main__":
    main()
