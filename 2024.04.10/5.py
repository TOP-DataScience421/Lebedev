user_str = input()

symbol_cost = 30
price = 0

for item in user_str:
    if item == " ":
        continue
    else:
        price += symbol_cost

print(f"{price // 100} руб. {price % 100} коп.")
    
#Программа выводит в stdout стоимость в рублях и копейках, согласно формату в примере ниже.
#23 руб. 10 коп.
