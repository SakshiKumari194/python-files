def find_min(numbers):
    minimum=numbers[0] #assume first element is minimum

    for num in numbers:
        if num<minimum:
            minimum=num

    return minimum        