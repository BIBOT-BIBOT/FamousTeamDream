import random

s = "123456798*)(*&Y^&!F:LKJHGNVKCIJDMKFJ GHHTHUGHFRJ, ifjjndjijirnvdmijornsenrjernsdggfgfjkgfjkgfjkfgkgfkjgfkjgfkjfgkjgfkfgkkfkfkj"
psw = ''
for x in range(7):
    psw += random.choice(s)

print(psw)

f = open('password', 'a')

f = open('password', 'w')

f.writelines(psw)
f.close()