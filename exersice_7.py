import re
text = "The course has 20 hours and 12 exercises."
result = re.sub(r"\d+", "<NUM>", text)
print(result)
#--------------------------------------------------------

#1
print(re.sub(r"\d+", "<NUMBER>", text))

#2
email_pattern = r"[\w.+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}"
date_pattern = r"\b\d{2}[/-]\d{2}[/-]\d{4}\b"
phone_pattern = r"(?<!\d)(?:\+213\s?|0)\d{3}(?:\s?\d{2}){3}(?!\d)"
#formats  0555 12 34 56, 0555123456, or +213 555 12 34 56.
def anonymize(text):
 text = re.sub(email_pattern,"<EMAIL>",text)
 text = re.sub(date_pattern,"<DATE>",text)
 text = re.sub(phone_pattern,"<PHONE>",text)
 return text

comment = ("Contact me at ali.ben@example.com or call 0555 12 34 56 if you have questions about the 20-hour course. - Ali, 16/09/2026.")
print(anonymize(comment))
