import random

sandi = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
panjang = int(input("berapa pang karakter untuk katasandi"))
hasil = ""

for i in range(panjang):
    hasil += random.choice(sandi)
print("kata sandi adalah", hasil)