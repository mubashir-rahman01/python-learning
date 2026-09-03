# write a program to find the most repeated characters in the string
from pprint import pprint
sentence = "This is a common interview question"

frequency = {}
for char in sentence:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
        
char_freqency = (sorted(
    frequency.items(),
    key = lambda kv: kv[1],
    reverse = True       
));

print("The highest ocurrence:", char_freqency[0]);