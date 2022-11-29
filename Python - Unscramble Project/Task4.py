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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""



"""These are calls from telemarketers"""

telemarketernumbers = set()

for numbers in calls:
    telemarketernumbers.add(numbers[0])

telemarketersreceiving = set()

for numbers in calls:
    telemarketersreceiving.add(numbers[1])      

texttelemarketers = set()
for numbers in texts:
    texttelemarketers.add(numbers[0])
    texttelemarketers.add(numbers[1])

numbers_to_avoid = telemarketersreceiving.union(texttelemarketers)

"""
if len(numbers_to_avoid) == 0:
    print("There were no telemarketers who have sent or received texts, or received calls \n")
else:
    print("numbers_to_avoid \n",numbers_to_avoid)
"""

if len(numbers_to_avoid) == 0:
    telemarketernumbers = telemarketernumbers
else:
    telemarketernumbers = telemarketernumbers.difference(numbers_to_avoid)

print("These numbers could be telemarketers: ", "\n")
for numbers in sorted(list(telemarketernumbers)):
    print(numbers)
    
    

    
    
    
    
    
    
    
    
    
    