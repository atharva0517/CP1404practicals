MENU = "(G)et a valid score must be 0-100 \n (P)rint result \n (S)how stars \n (Q)uit"
print(MENU)
def main():
    score = 50
    choice = get_choice()
    while choice != "Q":
        if choice == "G":
            score = get_score()

        elif choice == "P":
            result = get_result(score)
            print(result)

        elif choice == "S":
            show_stars(score)

        print(MENU)
        choice = get_choice()
    print("Farewell")


def show_stars(score):
    print("*" * int(score))

def get_result(score):
    if score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"

def get_score():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score

def get_choice():
    choice = input(">>> ").upper()
    return choice

main()

