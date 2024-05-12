scores_letters = {
    1: 'АВЕИНОРСТ',
    2: 'ДКЛМПУ',
    3: 'БГЬЯ',
    4: 'ЙЫ',
    5: 'ЖЗХЦЧ',
    8: 'ФШЭЮ',
    10: 'Щ',
    15: 'Ъ'
}

user_word = input()
user_word_upper = user_word.upper()

if 'Ё' in user_word_upper:
    user_word_upper = user_word_upper.replace('Ё', 'Е')

user_word_upper_list = list(user_word_upper)
    
total = 0

for key, value in scores_letters.items():
    for i in value:
        if i in user_word_upper_list:
            total += user_word_upper_list.count(i) * key
           
print(total)

    