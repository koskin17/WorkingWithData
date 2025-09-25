sequence = '1 2 3 3 1 5 9 22 3 5'

def even_odd_numbers(sequence):    
    even_numbers = []
    odd_numbers = []
    
    for number in sequence.split(' '):
        if int(number) % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)

    if len(even_numbers) >= len(odd_numbers):
        print('Чётных чисел больше')
        print(sequence.index(odd_numbers[0]))
    else:
        print('Нечётных чисел больше')
        print(sequence.index(even_numbers[0]))
        
    return even_numbers, odd_numbers

even_odd_numbers(sequence)
    
