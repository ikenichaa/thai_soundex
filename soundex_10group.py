
import back
import num
import front

def main(wrd):

    start=1
    sara = ['ะ','า','ิ','ี','ึ','ื','ุ','ู','ใ','ๆ','ไ','่','้','๋','็','๊','ั','แ','เ','โ','\n','.',' ','ฯ','-','!','0','1', '2','3','4','5','6','7','8','9','/','ฺ','ๅ']
    sara2 = ['เ','ี','ื']
    garun = ['์']
    curse=['ห','อ','ฮ','ฅ','ฃ']
    trvocab=['ทรวด','ทรง','ทราบ','ทราม','ทราย','ทรุด','โทรม','อินทรี','มัทรี','อินทรีย์','เทริด','นนทรี','พุทรา','ทรวง','ไทร','ทรัพย์','แทรก','ทรุดโทรม','โทรมนัส','ฉะเชิงเทรา']

    word=wrd


    w=[]
    delete=[]
    addm=[]
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
        elif (w[i] in garun):
            #print (delete)
            if (i-1 not in delete):
                delete.append(i-1)
            #print (delete)
            if ((w[i-1] == 'ร') and (w[i-2] in ['ท','ต','ด'])):
                delete.append(i-2)
            if ((w[i-1] == 'น') and (w[i-2] in ['ท','จ'])):
                delete.append(i-2)

            if (w[i-1] in ['ิ','ุ']):
                delete.append(i-2)
            delete.append(i)
            #print (delete)



    #Delete sara
    delete.sort()
    for k in range(0,len(delete)):
        gone = delete[k]
        del w[gone-k]
    #print(w)

    # ำ -> ม
    for i in range(0,len(w)):
        if (w[i]=='ำ'):
            w[i]='ม'
    # 'ํ' -> ัง
    for i in range(0,len(w)):
        if (w[i]== 'ํ'):
            w[i]='ง'


    delete=[]
    for i in range (1,len(w)):
        if (w[i] in curse): #delete ห อ ฮ if not in front
            delete.append(i)
        if ((w[i]=='ร') and (i!=len(w)-1)): # delete รร
            if (w[i+1]=='ร'):
                delete.append(i)
                delete.append(i+1)
    for k in range(0,len(delete)):
        gone = delete[k]
        del w[gone-k]
    #print(w)

    #ทร --> ซ
    delete=[]
    addc=[]
    for i in range(0,len(w)):
        if (w[i]=='ท'):
            if (i!=len(w)-1):
                if ((w[i+1]=='ร') and (word in trvocab)):
                    w[i]='ซ'
                    delete.append(i+1)
    for k in range(0,len(delete)):
        gone = delete[k]
        del w[gone-k]
    #print(w)


    #Change to number
    for i in range (0,len(w)):
        if (i==0):
            ans=ans+front.main(w[i])

        else:
            find = back.main(w[i])
            ans=ans+num.main(find)


    if (len(ans)<4):
        length=4-len(ans)
        for i in range (0,length):
            ans=ans+'0'
    elif(len(ans)>4):
        length=len(ans)-4
        for i in range (0,length):
            ans=ans[:-1]


   # print(ans)
    return ans



l=[]
with open("wordlist.txt","r",encoding="utf8")as file:
    lines = file.readlines()
    last=lines[-1]
    for lines in lines:
        if lines is last:
            break
        else:
            l.append(lines)

#List for the 10 selected soundex
K=[]
ข=[]
จ=[]
ช=[]
ท=[]
น=[]
บ=[]
ป=[]
ว=[]
อ=[]

K_match=0
ข_match=0
จ_match=0
ช_match=0
ท_match=0
น_match=0
บ_match=0
ป_match=0
ว_match=0
อ_match=0

#list_match = []
for i in range (len(l)):
    word_match = main(l[i])
    if("ก500" in word_match):
        K.append(l[i])
        K_match=K_match+1

    if("ข523" in word_match):
        ข.append(l[i])
        ข_match=ข_match+1

    if("จ374" in word_match):
        จ.append(l[i])
        จ_match=จ_match+1

    if("ช535" in word_match):
        ช.append(l[i])
        ช_match=ช_match+1

    if("ท715" in word_match):
        ท.append(l[i])
        ท_match=ท_match+1

    if("น165" in word_match):
        น.append(l[i])
        น_match=น_match+1

    if("บ533" in word_match):
        บ.append(l[i])
        บ_match=บ_match+1

    if("ป315" in word_match):
        ป.append(l[i])
        ป_match=ป_match+1

    if("ว343" in word_match):
        ว.append(l[i])
        ว_match=ว_match+1

    if("อ135" in word_match):
        อ.append(l[i])
        อ_match=อ_match+1

print("ก500")
print("There are ",K_match," match")
print("Now, there are ",K," in the list that match")
print("\n")

print("ข523")
print("There are ",ข_match," match")
print("Now, there are ",ข," in the list that match")
print("\n")

print("จ374")
print("There are ",จ_match," match")
print("Now, there are ",จ," in the list that match")
print("\n")

print("ช535")
print("There are ",ช_match," match")
print("Now, there are ",ช," in the list that match")
print("\n")

print("ท715")
print("There are ",ท_match," match")
print("Now, there are ",ท," in the list that match")
print("\n")

print("น165")
print("There are ",น_match," match")
print("Now, there are ",น," in the list that match")
print("\n")

print("บ533")
print("There are ",บ_match," match")
print("Now, there are ",บ," in the list that match")
print("\n")

print("ป315")
print("There are ",ป_match," match")
print("Now, there are ",ป," in the list that match")
print("\n")

print("ว343")
print("There are ",ว_match," match")
print("Now, there are ",ว," in the list that match")
print("\n")

print("อ135")
print("There are ",อ_match," match")
print("Now, there are ",อ," in the list that match")
print("\n")
