from itertools import takewhile

colours = ["blue", "green", "yellow", "red", "black", "", "white"]
has_red = "red" in colours

print(f' Colours contains green: {"green" in colours}')

numbers = [2, 43, 23, 4, 1, 9, 44]
print(f'any number above 40: {any (number > 40 for number in numbers)}')

short_colours = (colour
                 for colour in colours
                 if len(colour) < 4)
#print(f'first short colour: {next(short_colours, None)}')
print(short_colours.__next__())

col_b4_dud = list(takewhile(bool, colours))
print(col_b4_dud)

squared = list(number **2 for number in numbers)
squares = (number ** 2 for number in numbers)
print(squared)
print(next(squares))

badminton_group = {}
badminton_group["bassey"] = "pro"
badminton_group["hui"] = "pro"
badminton_group["kashp"] = "beginner"
print(*badminton_group)
print(badminton_group)