"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

"""These are calls from bangalore"""

callsfrombang = []    
for call in calls:
    if call[0].startswith('(080)'):
        callsfrombang.append(call)

#print("These are the calls from bangalore", callsfrombang, "\n")

"""These are calls from bangalore to Fixed lines"""
fixedlines = set()
for codes in callsfrombang:
    if codes[1].startswith('(0'):
        fixedlines.add(codes[1])

#print("These are the calls to fixed line numbers", fixedlines, "\n")

"""These are the fixed line codes"""
fixedlinecodes = set()

for codes in fixedlines:
    start = codes.find('(')+1
    end = codes.find(')', start)
    fixedlinecodes.add(codes[start:end])

    
#print("These are the fixed line codes", fixedlinecodes, "\n")

"""These are calls from bangalore to Mobiles"""

Mobilenumbers = set()

for mobiles in callsfrombang:
    if mobiles[1].startswith('7'):
        Mobilenumbers.add(mobiles[1])
    elif mobiles[1].startswith('8'):
        Mobilenumbers.add(mobiles[1])
    elif mobiles[1].startswith('9'):
        Mobilenumbers.add(mobiles[1])

#print("These are the calls to mobile numbers", Mobilenumbers, "\n")

"""These are the mobile number prefixes - codes"""
mobilecodes = set()

for codes in Mobilenumbers:
    mobilecodes.add(codes[0:4])

#print("These are the mobile prefix codes", mobilecodes, "\n")

"""These are calls from telemarketers"""

telemarketernumbers = set()

for numbers in calls:
    if numbers[0].startswith('140'):
        telemarketernumbers.add(numbers[0])

#print("These are the telemarketers", telemarketernumbers , "\n")

telemarketercalls = set()

for numbers in calls:
    if numbers[0].startswith('140'):
        telemarketercalls.add(numbers[1])

#print("These are the calls made by telemarketers", telemarketercalls, "\n")



"PART A ANSWER - Calling Codes in Lexicographical order"

callingcodes = mobilecodes.union(fixedlinecodes)
sortedcallingcodes = sorted(list(callingcodes))

print("The numbers called by people in Bangalore have codes: ", "\n")

for codes in sortedcallingcodes:
    print(codes)

"PART B ANSWER - Percentage of bangalore fixed line calls to bangalore fixed lines"

"Total calls from bangalore fixed lines"

callsfrombangfixedline = 0

for callsmade in callsfrombang:
    callsfrombangfixedline +=1

#print(f"These are total calls made from bangalore fixed lines, {callsfrombangfixedline}")


"Total calls from bangalore fixed lines(BFL) to BFL"

callsfrombfltobfl = 0

for callsmade in callsfrombang:
    if callsmade[1].startswith('(080)'):
        callsfrombfltobfl +=1

#print(f"These are total calls made from BFL to BFL, {callsfrombfltobfl}")


bfltobflcallspercent = round(((callsfrombfltobfl/callsfrombangfixedline)*100),2)

print(f"\n {bfltobflcallspercent} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
























