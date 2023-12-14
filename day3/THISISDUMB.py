from part1 import notworking
from dick import working

schematic_doc = open('day3/input.txt').read()
schematic_doc = list(schematic_doc.split('\n'))
i=0
while i < len(schematic_doc):
    if notworking('\n'.join(schematic_doc[i:i+3])) == working('\n'.join(schematic_doc[i:i+3])):
        print('SAME')
    else:
        print('NOT SAME', '\n'.join(schematic_doc[i:i+3]), notworking('\n'.join(schematic_doc[i:i+3])), working('\n'.join(schematic_doc[i:i+3])))
    i+=3