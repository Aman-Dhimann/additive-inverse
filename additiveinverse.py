stri = input("enter a string")
print(stri)
key = int(input("enter the key"))
encrypted = str("")
decrypted = str("")
for i in stri:
    if i.isupper():
        encrypted += (chr(((ord(i)-65+key) % 26)+65))
    else:
        encrypted += (chr(((ord(i)-97+key) % 26)+97))
print("encrypted cipher is: "+encrypted)
for i in encrypted:
    if i.isupper():
        decrypted += (chr(((ord(i)-65-key) % 26)+65))
    else:
        decrypted += (chr(((ord(i) - 97 - key) % 26) + 97))
print("decrypted cipher (Plain Text) is : "+decrypted)
