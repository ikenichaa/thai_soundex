def main(input):
    myDict = {}
    myDict['ก']='ก'
    for key in ['ข','ค', 'ฆ','ฅ','ฃ']:
        myDict[key] = 'ข'
    myDict['ง']='ง'
    myDict['จ']='จ'
    for key in ['ฌ', 'ช']:
        myDict[key] = 'ช'
    for key in ['ศ', 'ษ','ส']:
        myDict[key] = 'ส'
    for key in ['ญ', 'ย']:
        myDict[key] = 'ย'
    for key in ['ฎ', 'ด']:
        myDict[key] = 'ด'
    for key in ['ฏ', 'ต']:
        myDict[key] = 'ต'
    for key in ['ฑ', 'ฒ','ท','ธ']:
        myDict[key] = 'ท'
    for key in ['ฐ','ถ']:
        myDict[key] = 'ถ'
    for key in ['ณ', 'น']:
        myDict[key] = 'น'
    myDict['บ']='บ'
    myDict['ป']='ป'
    for key in ['พ','ภ']:
        myDict[key] = 'พ'
    myDict['ม']='ม'
    for key in ['ร','ฤ']:
        myDict[key] = 'ร'

    for key in ['ล', 'ฬ','ฦ']:
        myDict[key] = 'ล'
    myDict['ว']='ว'
    for key in ['ห', 'ฮ']:
        myDict[key] = 'ห'
    myDict['อ']='อ'
    myDict['ผ']='ผ'
    myDict['ฝ']='ฝ'
    myDict['ฟ']='ฟ'
    myDict['ซ']='ซ'
    myDict['ฉ']='ฉ'

    x=myDict.get(input)
    return x;
