import re
text="Regular Expression"
a=re.search("Regular",text)
if a:
    print("Word found")
else:
    print("Word not found")