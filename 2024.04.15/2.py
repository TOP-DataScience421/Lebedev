user_fruit = input()
fruit_list = []

while user_fruit:
    fruit_list.append(user_fruit)
    user_fruit = input()

fruit_str = ', '.join(fruit_list)

print(' и'.join(fruit_str.rsplit(',', 1)))

#яблоко
#груша
#апельсин

#яблоко, груша и апельсин

#апельсин
#груша

#апельсин и груша

#апельсин
#яблоко
#груша
#апельсин
#яблоко
#груша
#банан
#яблоко

#апельсин, яблоко, груша, апельсин, яблоко, груша, банан и яблоко    