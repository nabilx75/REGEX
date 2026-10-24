import re
text = "NLP is useful. NLP is interesting. Machine learning is useful."
print(re.findall(r"NLP", text))
print(re.findall(r"useful", text))
#----------------------------------

#Write a pattern that matches NLP only as a whole word (not as part of another word such as NLPs)
print(re.findall(r"\bNLP\b", text))

#Write a function count_occurrences(pattern, text) that returns the number of matches, and use it to count how many times useful OR interesting appears
def count_occurrences(pattern, text):
    return len(re.findall(pattern, text))
text = "NLP is useful. NLP is interesting. Machine learning is useful."

print(count_occurrences(r"NLP", text))
print(count_occurrences(r"useful|interesting", text))

#Make the search case-insensitive and test it on a version of the text where NLP is sometimes written nlp or Nlp

def count_occurrences(pattern, text):
    return len(re.findall(pattern, text,re.IGNORECASE))
text = "NLP is useful. NLP is interesting. Machine learning is useful."

print(count_occurrences(r"nLP", text))
print(count_occurrences(r"useful|interesting", text))


# the task is to count how many sentences mention either topic

text = "NLP is useful. NLP is interesting. Machine learning is useful."

pattern = r"[^.!?]*\b(?:NLP|machine learning)\b[^.!?]*[.!?]"

matches = re.findall(pattern, text, re.IGNORECASE)

print(len(matches))
print(len(matches) / 3 * 100, "%")