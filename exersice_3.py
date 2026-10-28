import re
text = "The course has 20 hours, 3 labs and 12 exercises."
print(re.findall(r"\d+", text))

receipt = ("2 apples, 1.5 kg of rice, 3 juices at $2.50 each, ""total: $12.75 (-$1.00 discount).")
 
print(re.findall(r"-?\$?\d+(?:\.\d+)?", receipt)) 

#3

print("-----------------")
r=re.findall(r"-?\$\d+(?:\.\d+)?",receipt)
print(r)
amount= [float(d.replace("$","")) for d in r]
#4
print(f"the sum is : {sum(amount)}")

#challenge
m=re.findall(r"-?\$\d+(?:\.\d+)?", receipt)
q= re.findall(r"(?<![$\d.])\d+(?:\.\d+)?", receipt)
print("quantities:", q)
print("money:", m)