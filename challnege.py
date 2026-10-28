import re

announcement = (
 "Reminder: the NLP project (worth 12 points) is due on 30/09/2026 before 23:59.Send your report (max 2.5 MB) to nlp.lab@univ.dz or upload it at https://courses.univ.dz/submit. Late submissions lose -1.5 points per day.Contact +213 555 98 76 54 for questions.")
date = r"\b(?:\d{4}-\d{2}-\d{2}|\d{2}[/-]\d{2}[/-]\d{4})\b"
time = r"\b\d{1,2}[:h]\d{1,2}\b"
email = r"[\w.+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}"
url = r"https?://[^\s]+[^\s.,;:!?)]"
phone = r"(?<!\d)(?:\+213\s?|0)\d{3}(?:\s?\d{2}){3}(?!\d)"
number = r"-?\d+(?:\.\d+)?"
results = {
 "dates": re.findall(date, announcement),
 "times": re.findall(time, announcement),
 "emails": re.findall(email, announcement),
 "urls": re.findall(url, announcement),
 "phones": re.findall(phone, announcement),
}
# mask what we already found, then look for the remaining numbers
masked = announcement
for p in [email, url, date, time, phone]:
 masked = re.sub(p, " ", masked)
results["numbers"] = re.findall(number, masked)

print("_--------------------------------")
print("report :")
for category, values in results.items():
 print(f"{category.capitalize():8} ({len(values)}): {values}")
