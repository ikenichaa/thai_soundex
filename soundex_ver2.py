
import back
import num
import front

print ('Welcome to Soundex Version 2')

def main(wrd):
    start=1
    sara = ['ะ','า','า','ิ','ี','ึ','ื','ุ','ู','ใ','ๆ','ไ','่','้','๋','็','๊','ั','แ','เ','โ','.','','ฯ','-','!','0','1', '2','3','4','5','6','7','8','9','/','ฺ','\n',' ']
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
    if ('ฤา' in w):
        print("yes")
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
            if (i-1 not in delete):
                delete.append(i-1)
            if ((w[i-1] == 'ร') and (w[i-2] in ['ท','ต','ด'])):
                delete.append(i-2)
            if ((w[i-1] == 'น') and (w[i-2] in ['ท','จ'])):
                delete.append(i-2)

            if (w[i-1] in ['ิ','ุ']):
                delete.append(i-2)
            delete.append(i)




    #Delete sara
    delete.sort()
    for k in range(0,len(delete)):
        gone = delete[k]
        del w[gone-k]


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
                w[i+1]='น'
    for k in range(0,len(delete)):
        gone = delete[k]
        del w[gone-k]


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


    return(ans)

l=[]
with open("wordlist.txt","r",encoding="utf8")as file:
    lines = file.readlines()
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
