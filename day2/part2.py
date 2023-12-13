# day 2
# sum of game ids that would have been possible if the bag contained 12 red, 13 green, and 14 blue cubes - PART 2: multiply amt of min required cubes of each game together and find sum

games = open("day2/input.txt").read()

rules = {
    "red": 12,
    "green": 13,
    "blue": 14
}

# listify input
inputgames = list(games.split("\n"))

# setup and such - working games is not used, kinda of a placeholder
minreq = []

# go through each color of cube and their respective rule to determine games that do not work
for key, value in rules.items():
    i = 0
    # go through each game and remove "Game #:" and split each set into list items
    for games in inputgames:
        ig = inputgames[i].replace(f"Game {i+1}:", "")
        ig = list(ig.split(";"))
        ii = 0
        cubecolor = []
        # find respective color's amount in each set and add to a list
        for games in ig:
            colorindex = ig[ii].find(key)
            ig3 = ig[ii][colorindex - 3:colorindex - 1]
            if colorindex == -1:
                cubecolor += "0"
            else:
                cubecolor += [ig3.replace(" ", "")]
            ii += 1
        # take max color of game append list, red is first, then the rest are multiplied to create the "power" of each game
        colormax = int(max(list(map(int, cubecolor))))
        if key == 'red':
            minreq += [colormax]
        else:
            minreq[i] = minreq[i] * colormax

        i += 1

# for loop setup and such
i = 0
sumtotal = 0

# power's of each game are added together to create a total sum of all the powers
for games in minreq:
    sumtotal += minreq[i]
    i += 1

print(sumtotal)