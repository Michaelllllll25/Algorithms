pokeParty = ["PIKACHU", "CHARMELEON", "GEODUDE", "GYARADOS", "BUTTERFREE", "MANKEY"]
enemy = "STARMIE"

print("Misty sent out " + enemy + "!")

print("\n" + enemy + "\t\t Lv21")
print("   HP [================]\n")

print("What will " + pokeParty[0] + " do?")
print("\t1. Fight")
print("\t2. Swap Pokemon")
print("\t3. Run")

choice = int(input("> "))

if choice == 1:
    print(pokeParty[0] + " used THUNDERSHOCK!  It's super effective.")

    print("\nSTARMIE\t\t Lv21")
    print("   HP [===========     ]\n")

    print(enemy + " used WATER PULSE!")
    print(pokeParty[0] + " fainted.")
elif choice == 2:
    print("\n" + pokeParty[0] + " swaps out with " + pokeParty[3] + "!\n")

    pokeParty[0], pokeParty[3] = pokeParty[3], pokeParty[0]  #--------   

    print(pokeParty)  #--------
    print(pokeParty[0] + " used BITE!  It's super effective.")

    print("\nSTARMIE\t\t Lv21")
    print("   HP [                ]\n")

    print(enemy + " fainted.\n")
    print(pokeParty[0] + " gained 155 EXP. Points!")
    print(pokeParty[3] + " gained 155 EXP. Points!")
    print("Received TM03 - WATER PULSE.")
    print("Received CASCADEBADGE.")
    print("Received $2100")
elif choice == 3:
    print(pokeParty[0] + " couldn't run. Skip a turn, coward.")

    print("\nSTARMIE\t\t Lv21")
    print("   HP [================]\n")

    print(enemy + " used WATER PULSE!")
    print(pokeParty[0] + " fainted.")
