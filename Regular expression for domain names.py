# Необходимо написать регулярное выражение, которое проверяет на корректность доменные имена.

import re

name = input("Please enter a domain name: ")
result = re.match(r"^(http[s]?://)([a-zA-Z0-9]([a-zA-Z0-9\.-]{0,61}[a-zA-Z0-9])?)\.([a-z]{1,6})(\/)?$", name)
if result:
    print("match")
else:
    print("no match")

# http://1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.ip6.arpa