import random

lower = "qwertyuiopasdfghjklzxcvbnm"
upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
numbers = "1234567890"
symbols = "!@#$%^&*(){}[]<>.,-=_/`~"

all = lower + upper + numbers + symbols
length = 16

password = "".join(random.sample(all , length))

print(password)