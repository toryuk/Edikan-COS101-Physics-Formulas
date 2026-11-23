# The list of numbers
data = [4, 1, 2, 2, 3, 5]


# 1. Function for SUM
def get_sum(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total


# 2. Function for AVERAGE (Mean)
def get_average(numbers):
    total = get_sum(numbers)
    average = total / len(numbers)
    return average

     #function for median
def get_median(numbers):
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    middle_index = n // 2

    if n % 2 == 0:

        return (sorted_nums[middle_index - 1] + sorted_nums[middle_index]) / 2
    else:

        return sorted_nums[middle_index]

    #function for mode
def get_mode(numbers):
    counts = {}
    for num in numbers:
        if num in counts:
            counts[num] = counts[num] + 1
        else:
            counts[num] = 1

    #finding numbers with the highest count:
    highest_count = 0
    mode_num = numbers[0]
    for num, count in counts.items():
        if count > highest_count:
            highest_count = count
            mode_num = num
    return mode_num


print("The list is:", data)
print("Sum:", get_sum(data))
print("Average:", get_average(data))
print("Median:", get_median(data))
print("Mode:", get_mode(data))
