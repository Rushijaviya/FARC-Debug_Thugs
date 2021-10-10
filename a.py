import glob

a = glob.glob('./media/Images/*')

c = []
for i in a:

    if "OPEN" in i:
        c.append(i[15:-15])

print(c)
