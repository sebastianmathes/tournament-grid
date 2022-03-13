#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_schedule(list):
    """Create a schedule for the teams in the list and return it

    Shamelessly stolen from: https://gist.github.com/Makistos/7192777
    """
    s = []

    if len(list) % 2 == 1:
        list = list + ["BYE"]

    for i in range(len(list) - 1):
        mid = int(len(list) / 2)
        l1, l2 = list[:mid], list[mid:]
        l2.reverse()

        # Switch sides after each round
        s = s + [zip(l1, l2)] if i % 2 == 1 else s + [zip(l2, l1)]

        list.insert(1, list.pop())

    return s


def get_players():
    player_list = []
    player_list.append(input("Enter first player: "))

    while True:
        answer = input("Enter another player? [Y/N] ")

        if answer == "N" or answer == "n":
            print("")
            break
        elif answer == "Y" or answer == "y" or answer == "":
            player_list.append(input("Enter player name: "))
        else:
            print(answer)
            print("Try again, sucker")

    return player_list


def get_main():
    i = 1
    for round in get_schedule(get_players()):
        print(f"Round #{i}:")
        for match in round:
            print(match[0] + " - " + match[1])
        print("----")
        i += 1


if __name__ == "__main__":
    get_main()
