MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)

def main():
    choice = get_choice()

    while choice != "Q":
        if choice == "C":
            celsius = get_celsius()
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = get_fahrenheit()
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = get_choice()

    print("Thank you.")

def get_celsius():
    celsius = float(input("Celsius: "))
    return celsius

def get_fahrenheit():
    fahrenheit = float(input("Fahrenheit: "))
    return fahrenheit

def get_choice():
    choice = input(">>> ").upper()
    return choice

def celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)

main()