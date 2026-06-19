import re

text = "My phone number is 9876543210"

pattern = r"\d+"

match = re.search(pattern, text)

if match:
    print("Number found:", match.group())
else:
    print("No match found")
