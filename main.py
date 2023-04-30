import random
import string

def generate_code():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f"https://discord.gift/{code}"

print("""
  _   _ _____ _______ _____   ____     _____ ______ _   _ 
 | \ | |_   _|__   __|  __ \ / __ \   / ____|  ____| \ | |
 |  \| | | |    | |  | |__) | |  | | | |  __| |__  |  \| |
 | . ` | | |    | |  |  _  /| |  | | | | |_ |  __| | . ` |
 | |\  |_| |_   | |  | | \ \| |__| | | |__| | |____| |\  |
 |_| \_|_____|  |_|  |_|  \_\\____/   \_____|______|_| \_|
                                                          
                                                          
""")

quantity = int(input("How many nitro codes would you like to generate? "))

with open("output.txt", "w") as f:
    for i in range(quantity):
        code = generate_code()
        f.write(f"{code}\n")

print(f"{quantity} Discord Nitro codes have been generated and saved to output.txt")
