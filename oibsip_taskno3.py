import random

def generate_password(len):

    list_of_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*"

    selected_char = random.sample(list_of_chars,len)
    pass_str = "".join(selected_char)

    return pass_str

if_name_="main"

len = int(input("Enter the length of the Password: "))

pass_str = generate_password(len)

print("A randomly generated password is: ",pass_str)