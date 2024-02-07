import random
chrs = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
lght = int(input("Podaj długość hasła: "))
chrs_ct = 0
passw = ""
for i in range(len(chrs)): chrs_ct += 1
for i in range(lght): passw += chrs[random.randint(0, chrs_ct - 1)]
print(passw)
