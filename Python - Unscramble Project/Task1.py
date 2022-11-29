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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
tele_no_in_texts = set()
tele_no_in_calls = set()

for i in range(len(texts)):
    tele_no_in_texts.add(texts[i][0])
    tele_no_in_texts.add(texts[i][1])



for i in range(len(calls)):
    tele_no_in_calls.add(calls[i][0])
    tele_no_in_calls.add(calls[i][1])


different_telephone = len(tele_no_in_calls.union(tele_no_in_texts))

print('There are {} different telephone numbers in the records.'.format(different_telephone))