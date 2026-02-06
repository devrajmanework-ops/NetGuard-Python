numbers = [1,2,3,4,5]

def calculate_sum(numbers):

    total = 0

    for n in numbers:
        total = total + n
    return total
    
result = calculate_sum(numbers)
print("sum is:",result)
    