

def calculate_efficiency(monsters, gold, stage):
    list=[]
    if stage == 0:
        # Prepare circle
        if len(monsters) == 0 or len(monsters) == 1:
            return gold
        else:
            #go stage 1
            temp=monsters.copy()
            temp.pop(0)

            nextstage1=calculate_efficiency(temp,gold - monsters[0],1)
            list.append(nextstage1)
            #stay stage 0
            temp=monsters.copy()
            temp.pop(0)
            staystage0=calculate_efficiency(temp,gold,0)
            list.append(staystage0)
    elif stage == 1:
        # Attack
        if len(monsters) == 1:
            return gold + monsters[0]
        elif len(monsters) == 0:
            return gold
        else:
            #now attack
            temp = monsters.copy()
            temp.pop(0)
            nowattack = calculate_efficiency(temp, gold + monsters[0], 2)
            list.append(nowattack)
            #later attack
            temp = monsters.copy()
            temp.pop(0)
            laterattack = calculate_efficiency(temp, gold, 1)
            list.append(laterattack)
    elif stage == 2:
        # Rest
        if (len(monsters) == 0) or (len(monsters) == 1):
            return gold
        else:
            temp = monsters.copy()
            temp.pop(0)
            return calculate_efficiency(temp,gold,0)
    else:
        # Add handling for other stages
        pass

    max_gold = max(list)

    return max_gold


if __name__ == "__main__":
    guess = {"guess": 1}
    print(type(guess))
