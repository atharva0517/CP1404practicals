name = input("Enter your name: ")
out_file = open('name.txt', 'w')
print(name, file=out_file)
out_file.close()

in_file = open('name.txt', 'r')
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}!")

out_file = open('numbers.txt', 'w')
out_file.write("17\n42\n400\n")
out_file.close()


in_file = open('numbers.txt', 'r')
first_number = int(in_file.readline())
second_number = int(in_file.readline())
in_file.close()
result = first_number + second_number
print(result)

in_file = open('numbers.txt', 'r')
total = 0
for line in in_file:
    total += int(line)
in_file.close()
print(total)
