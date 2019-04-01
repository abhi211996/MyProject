f1=open("C:\\Users\\320052863\\Desktop\\info.txt","r")
f2=open("C:\\Users\\320052863\\Desktop\\info1.txt","r")
for word1 in f1:
    for word2 in f2:
        if word1==word2:
            print("SAME\n")
        else:
            print(word1 + word2)
        break
f1.close()
f2.close()
