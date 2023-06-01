#6
def get_even_numbers(input_list):
    numbers = []
    for num in input_list:
        if num % 2 == 0:
            numbers.append(num)
    return numbers
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_list = get_even_numbers(input_list)
print(numbers_list)
