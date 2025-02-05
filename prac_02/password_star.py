PASSWORD_LENGTH = 10
def main():
    password = get_password()
    method_name(password)


def get_password():
    password = input("Enter a password: ")
    while len(password) <= PASSWORD_LENGTH:
        print("Invalid Password ")
        password = input("Enter a password: ")
    return password


def method_name(password):
    length = len(password)
    print(length * "*")

main()