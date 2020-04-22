fil = open("D:\\ForPythonBeginners\\for-python-beginners\\我的成语接龙\\成语大全（31648个成语解释）.Txt",'rb')

lis = fil.readlines()

# print(lis[0])
# print(lis[501][0:5])
# print(lis[5001][0:5])
# print(lis[20001][0:5])

inFil = open("D:\\ForPythonBeginners\\for-python-beginners\\我的成语接龙\\words.txt","a")

ll = []

for i in lis:
    if i.strip() == "":
        pass
    else:
        i = i.decode("gbk","ignore")
        # s = i.replace(" ","")
        word = i[0:5]
        ll.append(word)
        # ss = s.decode()
        # inFil.write(word)

print(len(ll))

wordSet = set(ll)
wordLis = list(wordSet)

for i in wordLis:
    if i.strip()!="" and i != " ":
        inFil.write(i.strip()+"\n")

fil.close()
inFil.close()

