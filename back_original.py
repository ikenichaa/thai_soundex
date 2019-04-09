def main(input):
    myDict = {}
    myDict['ก']='k'
    for key in ['ข','ค', 'ฆ']:
        myDict[key] = 'k'
    myDict['ง']='ng'
    myDict['จ']='t'
    for key in ['ฉ','ฌ', 'ช']:
        myDict[key] = 't'
    for key in ['ซ','ศ', 'ษ','ส']:
        myDict[key] = 't'
    for key in ['ญ', 'ย']:
        myDict[key] = 'j'
    for key in ['ฎ', 'ด']:
        myDict[key] = 't'
    for key in ['ฏ', 'ต']:
        myDict[key] = 't'
    for key in ['ฐ','ฑ', 'ฒ','ถ','ท','ธ']:
        myDict[key] = 't'
    for key in ['ณ', 'น']:
        myDict[key] = 'n'
    myDict['บ']='p'
    myDict['ป']='p'
    for key in ['ผ', 'พ','ภ']:
        myDict[key] = 'p'
    for key in ['ฝ', 'ฟ']:
        myDict[key] = 'p'
    myDict['ม']='m'
    myDict['ร']='n'
    for key in ['ล', 'ฬ']:
        myDict[key] = 'n'
    myDict['ว']='w'
    for key in ['ห', 'ฮ']:
        myDict[key] = ''
    myDict['อ']=''

    x=myDict.get(input)
    return x;
