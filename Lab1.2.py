import re

text = "Contact us at support@example.com or sales@example.org for assistance."

email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

emails = re.findall(email_pattern, text)

print(emails)
