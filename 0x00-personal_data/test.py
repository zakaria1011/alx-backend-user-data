import re

string = "Hello. How are you? (I'm fine, thanks!)"
escaped_string = re.escape(string)

print("Original string:", string)
print("Escaped string:", escaped_string)