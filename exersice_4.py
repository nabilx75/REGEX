import re
text = "The exam is on 16/09/2026 at 14:30."
print(re.findall(r"\d{2}/\d{2}/\d{4}", text))
print(re.findall(r"\d{2}:\d{2}", text))
time = ("Lab 1: 16/09/2026, Lab 2: 2026-09-23, Lab 3: 30-09-2026, "
 "exam at 9:00, revision session at 14:30, office hours 09h30.")
#-------------------------------------------------------------------
#1
dmy = r"\d{1,2}[/-]\d{1,2}[/-]\d{4}"
print(re.findall(dmy, time))

#2 iso format 
ydm=r"\d{4}-\d{1,2}-\d{1,2}"
print(re.findall(ydm, time))

#3 all formats

print(re.findall(r"\b\d{4}-\d{1,2}-\d{1,2}|\d{1,2}[/-]\d{1,2}[/-]\d{4}\b", time))

#4 Write a pattern that matches both time formats 9:00 / 14:30 and 09h30
times = r"\b\d{1,2}[:h]\d{1,2}\b"
print(re.findall(times, time))

