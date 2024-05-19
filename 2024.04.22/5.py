def central_tendency(num_1: float, num_2: float, *numbers: float) -> dict[str, float]:
    turple_of_numbers = (num_1, num_2) + numbers
    
    sorted_numbers = sorted(turple_of_numbers, reverse = True)
    n = len(sorted_numbers)
    
    median = ((n + 1) / 2 if n % 2 != 0 else (n / 2 + n / 2 + 1) / 2)
    
    arithmetic = sum(turple_of_numbers) / n
    
    multiply_tuple = 1
    
    for num in turple_of_numbers:
        multiply_tuple *= num
    
    geometric = multiply_tuple ** (1 / n)
    
    harmonic = n / sum(1 / num for num in turple_of_numbers)
    
    return {'median': median,
            'arithmetic': arithmetic,
            'geometric': geometric,
            'harmonic': harmonic}

#>>> central_tendency(1, 2, 3, 4, 5)
#{'median': 3.0, 'arithmetic': 3.0, 'geometric': 2.605171084697352, 'harmonic': 2.18978102189781}
#>>> central_tendency(1, 2, 3, 4, 5, 7, 9)
#{'median': 4.0, 'arithmetic': 4.428571428571429, 'geometric': 3.5815790597564954, 'harmonic': 2.7588364091335627}
#>>> central_tendency(101, 92, 3, 34, 55, 7, 98)
#{'median': 4.0, 'arithmetic': 55.714285714285715, 'geometric': 32.18311117111581, 'harmonic': 12.618098733969909}
#>>>