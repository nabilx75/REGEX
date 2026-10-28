import re
text = "cat bat eaii SKN rat dog hot"
print(re.findall(r"[cb]at", text))
print(re.findall(r"[aeiou]", text))
#----------------------------------

#1 Modify the pattern to find every word ending in at, regardless of the letter before it.
print(re.findall(r"\b\w*at\b", text))

#2 Write a pattern that matches any three-letter word made only of consonants (no a, e, i, o, u).
print(re.findall(r"\b[aeiou]{3}\b", text))#V
print(re.findall(r"\b[b-df-hj-np-tv-z]{3}\b", "cat bat eai sknl skn rat dog hot"))#C

#3 username validator:
def username_validator(username):
   if(re.fullmatch(r"[a-z0-9_]{4,12}", username)):
    print(" valid")
   else :
       print(" invalid")  
 
   if(len(username) < 4):
     
    print(" * too short")
   if(len(username) > 12):
        
    print(" * too long")  
   if(re.search(r"[^a-z0-9_]", username)):
        
    print(" * wrong character") 

print("-----------------------------------")
print("ali_92 :")
username_validator("ali_92")
print("-----------------------------------")
print("A :")
username_validator("A")
print("-----------------------------------")
print("student.name :")
username_validator("student.name")
print("-----------------------------------")
print("nlp_lab_2026 :")
username_validator("nlp_lab_2026")