user_str = input()

binary_prefixes = {'b', '0b'}
for prefix in binary_prefixes:
    if user_str.startswith(prefix):
        user_str = user_str[len(prefix):]
if all(char in {'0', '1'} for char in user_str):
    print("да")
else:
    print("нет")

#0b11001
#да

#1b0101
#нет


#b11
#да

#bb0b0100111001
#нет