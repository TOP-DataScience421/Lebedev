cell1 = input()
cell2 = input()

if (ord(cell1[0]) + ord(cell2[0]) + int(cell1[1]) + int(cell2[1])) % 2 == 0:
    print('да')
else:
    print('нет')
    
#a1
#b1
#нет

#d4
#h7
#нет

#a6
#d4
#нет

#e7
#c5
#да