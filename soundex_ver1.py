#import
import back_original
import num

def main(wrd):
    start=1
    sara = ['ะ','า','ิ','ี','ึ','ื','ุ','ู','ใ','ๆ','ไ','่','้','๋','็','๊','ั','แ','เ','โ','\n','.',' ','ฯ','-','!','0','1', '2','3','4','5','6','7','8','9','/','ฺ','ๅ','ํ','ำ','ฺ','์','ฤ','ฦ']
    sara2 = ['เ','ี','ื']
    none=['ฃ','ฅ','ห','อ','ฮ']

    word=wrd
    w=[]
    delete=[]
    ans=''
    count=0

    for i in range(0,len(word)):
        w.append(word[i])

    #Find position of sara
    for i in range (0,len(w)):
        if (w[i] in sara):
            delete.append(i)
            if (w[i] in sara2):
                count=count+1
                if (count==2):
                    yak=i+1
                    if (w[yak]=='ย'):
                        delete.append(yak)
                    count=0
        elif (w[i] in none):
            delete.append(i)


    #Delete sara
    for k in range(0,len(delete)):
        gone = delete[k]
        del w[gone-k]


    #Change to number
    for i in range (0,len(w)):
        if (i==0):
            ans=ans+w[i]
        else:
            find = back_original.main(w[i])
            ans=ans+num.main(find)


    if (len(ans)<4):
        length=4-len(ans)
        for i in range (0,length):
            ans=ans+'0'
    elif(len(ans)>4):
        length=len(ans)-4
        for i in range (0,length):
            ans=ans[:-1]



    return(ans)

l=[]
with open("TWC_Dict.txt","r",encoding="utf8")as file:
    lines = file.readlines()
    #lines.rstrip("\n")
    last=lines[-1]
    for lines in lines:
        if lines is last:
            break
        else:
            l.append(lines)
# Dictionary = open('TWC_Dict.txt',encoding='utf8',errors='ignore')
# l = list(set([d.rstrip() for d in Dictionary.readlines()]))


#List for the selected soundex
K=[]
K_match=0

print("Soundex Version 1")
print("Select 1 to input word to see its group")
print("Select 2 to input group to see its group")
n=int(input("Select 1 or 2: "))
if (n==1):
    w=str(input("Word: "))
    wmatch=str(main(w))
elif(n==2):
    wmatch=str(input("Group: "))


list_match = []
for i in range (len(l)):
    word_match = str(main(l[i]))
    if(word_match == wmatch):
        K.append(l[i])
        K_match=K_match+1



print(wmatch)
print("There are ",K_match," match")
print(K)
