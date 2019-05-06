import shutil
import os

concent = input("source: ")
final = input("destination: ")

os.chdir('D:\\jane\\'+ concent)

songs = []

songs = os.listdir('D:\\jane\\'+ concent +'\\')

alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

total = 0
newSongs = []

for song in songs:
    newSongs.append(alpha[total] + song)
    total+=1

order = input("What order would you like?")

new_order = order.split()

back = []

for new in newSongs:
    total = 0
    back.append(new[total])
    total += 1

total = len(new_order)
print(total)


for y in new_order:
    for t in back:
        if y == t:
            u = back.index(t)
            shutil.copy('D:\\jane\\'+ concent +'\\'+ songs[u], 'E:\\'+ final)
