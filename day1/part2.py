# day 1 
# clean up "calibration document" and add first and last digits of each line - PART 2: consider numerical words in calculations, rather than ignoring them

import re

calibration_doc = open('day1/input.txt').read()

# convert long string to managable list of each line
calibration_doc = list(calibration_doc.split("\n"))
s = calibration_doc

# setup loop variables and such
i=0
total_of_digits = 0
words2num_dict = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e"
}

while len(s) > i:

    # STEP 0.5: convert numeric words to digits so they are included before step 1 removes them
    s1 = s[i]
    for key, value in words2num_dict.items():
        s1 = s1.replace(key, value)

    # STEP 1: clean doc list item so it only includes digits
    s2 = re.sub("[^0-9]", "", s1)

    # STEP 2 take first and last digits of each list item and add together
    list_item_total = s2[0] + s2[-1]

    # STEP 3 take list item total and add to total of the entire calibration sheet / list
    total_of_digits += int(list_item_total)

    i += 1

print("Sum of all of the Calibration Values: " + str(total_of_digits) + "\n\n :) \n")