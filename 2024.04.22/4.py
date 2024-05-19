def countable_nouns(num: int, nouns: tuple[str, str, str]):
    if num % 10 == 1 and num % 100 != 11:
        return(nouns[0])
    elif num % 10 in range(2,5) and num %100 not in range(12,15):
        return(nouns[1])
    else:
        return(nouns[2])
        
#countable_nouns(1, ("год", "года", "лет"))
#'год'
#>>> countable_nouns(57, ("год", "года", "лет"))
#'лет'
#>>> countable_nouns(10939, ("год", "года", "лет"))
#'лет'
#>>> countable_nouns(2054, ("год", "года", "лет"))
#'года'
#>>> countable_nouns(2024, ("год", "года", "лет"))
#'года'
#>>> countable_nouns(2021, ("год", "года", "лет"))
#'год'