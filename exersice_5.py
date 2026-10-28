import re
text = "Contact ali@example.com or student.name@univ.dz."
pattern = r"[\w.-]+@[\w.-]+\.\w+"
print(re.findall(pattern, text))

#1
emails = ['ali@example.com','student.name@univ.dz','a.b-c@sub.univ.dz','not-an-email','missing@domain','double@@example.com',
 '@no-local-part.com', 'ok.name+lab@example.co.uk']
for email in emails:
 print(f"{email:28} -> {'valid' if re.findall(pattern, email) else 'invalid'}")
#The 28 specifies the minimum width of the field
print("-----------------------------------")

#2
updated_pattern=r"[\w.+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}"
#{2,} — at least two letters.
for email in emails:
 print(f"{email:28} -> {'valid' if re.fullmatch(updated_pattern, email) else 'invalid'}")
 
 
 #4
print("-----------------------------------")
def is_valid_email(emails):
  return re.fullmatch(updated_pattern, emails) is not None
valid = [email for email in emails if is_valid_email(email)]
invalid = [email for email in emails if not is_valid_email(email)]
print("valid :", len(valid))
print("invalid:", len(invalid))
print("valid emails :", valid)
print("invalid emails:", invalid)
