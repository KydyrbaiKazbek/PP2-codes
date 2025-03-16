import re

pattern = "[*@*\.*]"
text = "hi@kbtu.kz"
if re.search(pattern, text):
    print(True)