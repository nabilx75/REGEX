# \d+ One or more digits
# [A-Z][a-z]+ one capital letter followed by one or more lowercase letters
# \b\w+\b a word

#2

# \d+ 1.5 1,5
# [A-Z][a-z]+ NLP McDo 
# \b\w+\b don't

#3
import re
s = "Dr. O'Brien met 3 students in New-York on 16/09/2026."
print(re.findall(r"\d+", s))
print(re.findall(r"[A-Z][a-z]+", s))
print(re.findall(r"\b\w+\b", s))

