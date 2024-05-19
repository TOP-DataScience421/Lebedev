def formatting_list(numbers: list, n: int = 1) -> list:
    repeat = 0
    while repeat < n:
        try:
            numbers.remove(max(numbers))
            numbers.remove(min(numbers))
        except ValueError:
            break
        repeat += 1
    return numbers
    
def numbers_strip(numbers: list, n: int = 1, *, flag: bool = False) -> list:
    if flag == False:
        return formatting_list(numbers, n)
    else:
        return formatting_list(numbers, n).copy()
        
#>>> sample = [1, 2, 3, 4]
#>>> sample_stripped = numbers_strip(sample)
#>>> sample_stripped
#[2, 3]
#>>> sample is sample_stripped
#True
#>>> 
#>>> sample = [10, 20, 30, 40, 50]
#>>> sample_stripped = numbers_strip(sample, 2, flag=True)
#>>> sample_stripped
#[30]
#>>> sample is sample_stripped
#False