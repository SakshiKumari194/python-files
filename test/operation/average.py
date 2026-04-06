def find_average(numbers):
    total=0

    for num in numbers:
        total+=num
    average = total / len(numbers)
    return average    