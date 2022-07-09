import sys
import re

# Get input
text = input("Text: ")

# Count stuff (spaces at the start and end count as words with simple '\s')
letters = len(re.findall("\w", text))
words = len(re.findall("\s(?!\s)(?=.)", re.sub("^\s+", "", text))) + 1
sentences = len(re.findall("\?|\.|!", text))

# Calculate L and S (also check for errors!)
try:
    L = letters / words * 100
    S = sentences / words * 100
except:
    print("Not enough words!")
    sys.exit(1)

# Calculate index
I = round(0.0588 * L - 0.296 * S - 15.8)

# Print grade
print("Before Grade 1") if I < 1 else (print("Grade 16+") if I > 16 else print(f"Grade {I}"))