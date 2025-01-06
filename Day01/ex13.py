input_numbers = input("Enter numbers (number1,number2,...): ")
numbers = input_numbers.split(",")
int_numbers = []

for number in numbers:
    int_numbers.append(int(number))

sorted_numbers = sorted(int_numbers)
print(sorted_numbers)