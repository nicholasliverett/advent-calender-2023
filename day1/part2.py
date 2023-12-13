# day 1 
# clean up "calibration document" and add first and last digits of each line - PART 2: consider numerical words in calculations, rather than ignoring them

from variables import calibration_doc, words2num_dict
import re

# convert long string to managable list of each line
calibration_doc = list(calibration_doc.split("\n"))
s = calibration_doc

# setup loop variables and such
i=0
total_of_digits = 0
pattern = '|'.join(sorted(re.escape(k) for k in words2num_dict))

# define numeric words to digits function
def words2num(text):
    for key, value in words2num_dict.items():
        text = text.replace(key, value)
    return text

while len(s) > i:

    # STEP 0.5: convert numeric words to digits so they are included before step 1 removes them
    s1 = words2num(s[i])

    # STEP 1: clean doc list item so it only includes digits
    s2 = re.sub("[^0-9]", "", s1)

    # STEP 2 take first and last digits of each list item and add together
    list_item_total = s2[0] + s2[len(s2)-1]
    print(list_item_total)

    # STEP 3 take list item total and add to total of the entire calibration sheet / list
    total_of_digits += int(list_item_total)

    i += 1




print("Sum of all of the Calibration Values: " + str(total_of_digits) + "\n\n :)")