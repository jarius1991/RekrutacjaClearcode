def battle(soldiers):
    """
    This function count which fraction win.
    :param soldiers: Table of numbers which represents soldiers from Odds and Evens fraction.
    :return: String with information who win.
    """
    odds_list, evens_list = assign_squads(soldiers)
    odds_power = odds(odds_list)
    evens_power = evens(evens_list)
    result = choose_winner(odds_power, evens_power)
    return result


def assign_squads(soldiers):
    """
    This function assign soldiers to right fractions.
    :param soldiers: Table of numbers which represents soldiers from Odds and Evens fraction.
    :return: Two tables with Odds soldiers and Evens soldiers.
    """
    odds_list = []
    evens_list = []
    for squad in soldiers:
        if squad == 0:
            pass
        elif squad % 2 == 0:
            evens_list.append(squad)
        else:
            odds_list.append(squad)
    return odds_list, evens_list


def choose_winner(odd_num, even_num):
    """
    This function compare which fraction have more power.
    :param odd_num: Power of Odds fraction.
    :param even_num: Power of Evens fraction.
    :return: String with result of battle.
    """

    if odd_num > even_num:
        result = "odds win"
    elif odd_num < even_num:
        result = "evens win"
    else:
        result = "tie"

    return result


def odds(soldiers):
    """
    This function count power of Odds soldiers.
    :param soldiers: Table of numbers symbolizing Odds soldiers.
    :return: Power of Odds fraction.
    """
    return count_soldiers_power(soldiers, 1)


def evens(soldiers):
    """
    This function count power of Evens soldiers.
    :param soldiers: Table of numbers symbolizing Evens soldiers.
    :return: Power of Evens fraction
    """
    return count_soldiers_power(soldiers, 0)


def count_soldiers_power(soldiers, war_number):
    """
    Count how many soldiers and spies/saboteurs have given squad.
    :param soldiers: Table of numbers symbolizing soldiers.
    :param war_number: Number which symbolize fighting symbol.
    :return: Power of soldiers squads.
    """
    power = 0
    for soldier in soldiers:
        power += count_power(soldier, war_number)
    return power


def count_power(soldier, war_number):
    """
    Count power of given soldier.
    :param soldier: Number which symbolise soldier in squad.
    :param war_number: Number which symbolize fighting symbol.
    :return:  Power of given squad.
    """
    if soldier < 0:
        return - bin(soldier)[3:].count(str(war_number))  # Solve saboteur and spies problem
    else:
        return bin(soldier)[2:].count(str(war_number))


if __name__ == "__main__":
    print(battle([21, -3, 20]))
    print(battle([7, -3, -14, 6]))
    print(battle([23, -3, 32, -24]))
