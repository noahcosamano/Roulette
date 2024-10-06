import random

def choose_target():
    target = input("Press 's' to aim at yourself, press 'd' to aim at dealer: ")
    lower_target = target.lower()
    return lower_target

def main():
    choose_target()

if __name__ == "__main__":
    main()
