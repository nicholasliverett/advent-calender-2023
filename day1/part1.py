# day 1 

# clean up list and add first and last digits of each line

from variables import calibration_doc
import re

# convert long string to managable list of each line
calibration_doc = list(calibration_doc.split("\n"))
s = calibration_doc

# while loop or whateer
i=0
total_of_digits = 0
while len(calibration_doc) > i:

    # STEP 1: clean doc list item so it only includes digits
    s1 = re.sub("[^0-9]", "", s[i])

    # STEP 2 take first and last digits of each list item and add together
    list_item_total = s1[0] + s1[len(s1)-1]

    # STEP 3 take list item total and add to total of the entire calibration sheet / list
    total_of_digits += int(list_item_total)

    i += 1




print("Sum of all of the Calibration Values: " + str(total_of_digits) + "\n\n :)")