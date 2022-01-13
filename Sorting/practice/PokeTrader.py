poke_party = ["PIKACHU", "CHARMELEON", "GEODUDE", "GYARADOS", "BUTTERFREE", "MANKEY"]

while True:
    print("EXCHANGE POKEMON\n")
    print("0. " + poke_party[0])
    for i in range(1, len(poke_party)):
        print(f"\t{i}. {poke_party[i]}")

    print(f"\nChoose a Pokemon to exchange with {poke_party[0]}. (Or enter 0 to quit.)")
    x = int(input("> "))

    poke_party[0], poke_party[x] = poke_party[x], poke_party[0] # ------
    print(poke_party) # ------

    if x == 0:
        break
