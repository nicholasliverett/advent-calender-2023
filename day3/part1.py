# day3
# get numbers next to symbols and find sum

import re, math

schematic_doc = open('day3/input.txt').read()
schematic_doc = list(schematic_doc.split('\n'))

special_chars = re.compile('[@_!#$%^&*()<>?/\|}{~:=+-]')
sum_total = 0

# find numbers that are exceptions and remove them from each list item
# take all these numbers and add them all together by list or combine all of them into one massive string or something

for i, line in enumerate(schematic_doc): 
    digitsdex = {}
    numsdex_to_delete = []
    nums_in_line = re.findall(r'\d+', line)
    print(nums_in_line)
    lastnumdex = -1
    for num in nums_in_line:
        digitsdex[line.find(num, lastnumdex+1)] = int(math.log10(int(num)) + 1)
        lastnumdex = line.find(num, lastnumdex)+int(math.log10(int(num)))
    print(digitsdex)
    for id, (key, value) in enumerate(digitsdex.items()):
        ub = 1
        lb = 1
        rb = 1
        db = 1
        if key == 0:
            # this is special case #1 where the number is on the left edge and analysis of the line on, above, and below is slightly different
            lb = 0
        if key + value == len(line):
            # this is special case #2 where the number is on the right edge and analysis of the line on, above, and below is slightly different
            rb = 0
        if i == 0:
            # this is special case #3 where the number is on the first line and analysis of the line above is not possible
            ub = 0
        if i == len(schematic_doc)-1:
            # this is special case #4 where the number is on the last line and analysis of the line below is not possible
            db = 0

        upbound = special_chars.search(schematic_doc[i-ub][key-lb:key+value+rb])
        bound = special_chars.search(line[key-lb:key+value+rb])
        downbound = special_chars.search(schematic_doc[i+db][key-lb:key+value+rb])

        if upbound != None or bound != None or downbound != None:
            pass
        else:
            numsdex_to_delete += [id]
 
    numsdex_to_delete.reverse()
    for nums in numsdex_to_delete:
        del nums_in_line[nums]

    print(nums_in_line)
    pretotal = sum_total
    for nums in nums_in_line:
        sum_total += int(nums)

    print(sum_total-pretotal)
print(sum_total)
