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
    # go through each game and remove "Game #:" and split each set into list items
    for id, games in enumerate(inputgames):
        ig = games.replace(f"Game {id + 1}:", "")
        ig = list(ig.split(";"))
        cubecolor = []
        # find respective color's amount in each set and add to a list
        for games in ig:
            colorindex = games.find(key)
            ig3 = games[colorindex - 3:colorindex - 1]
            if colorindex == -1:
                cubecolor += "0"
            else:
                cubecolor += [ig3.replace(" ", "")]
        # take max color of game append list, red is first, then the rest are multiplied to create the "power" of each game
        colormax = int(max(list(map(int, cubecolor))))
        if key == 'red':
            minreq += [colormax]
        else:
            minreq[id] = minreq[id] * colormax

# for loop setup and such
sumtotal = 0

# power's of each game are added together to create a total sum of all the powers
for games in minreq:
    sumtotal += games

print(sumtotal)