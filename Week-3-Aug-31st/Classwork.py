second = 7
hrs = second / 3600
print(hrs)
sec = second % 3600
print(sec)
minutes = sec // 60
print(minutes)

race = str(input("Enter your race: "))
defense = float(input("Enter your defense power: "))

if(race == 'Elf'):
    defense *= .75
    if(race == 'Elf'):
        print(f"Your defense power is {defense}")
elif(race == 'Dwarf'):
    defense *= 2
    if(race == 'Dwarf'):
        print(f"Your defense power is {defense}")
elif(race == 'Human'):
    defense *= 1.25
    if(race == 'Human'):
        print(f"Your defense power is {defense}")
else:
    print("Choose a valid race")




