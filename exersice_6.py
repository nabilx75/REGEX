import re
text = "Visit https://www.univ.dz or http://example.org."
pattern = r"https?://[^\s]+"
print(re.findall(pattern, text))
#--------------------------------------------
#1
parag = ("See https://www.univ.dz/lab1?page=2, http://example.org,"
        " https://docs.python.org/3/library/re.html and ftp://old-server.com "
       " (not a web link).")

print(re.findall(pattern, parag))

#2
print("the real dmain names :")
for u in (re.findall(pattern, parag)):
 
 print(re.search(r"https?://([^/?#:,\s]+)", u).group(1))
 
 #3
with_ftp = r"(?:https?|ftp)://[^\s]+[^\s.,;:!?)]"
print(re.findall(with_ftp, parag))

#4
https = sum(bool(re.match(r"https://", u)) for u in (re.findall(pattern, parag)))
http = sum(bool(re.match(r"http://", u)) for u in (re.findall(pattern, parag)))

print("HTTPS:", https, " HTTP:", http)
