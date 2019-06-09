
def binaryToStr(bs):
    res=''
    for i in bs:
        temp=''
        for j in range(0,8):
            temp=str(int(i)%2)+temp
            i=i//2
        res=res+temp
    return res
def readZip():
    fileName=input('enter zip file name :')
    source=open(fileName,'rb')
    binarys=source.read()
    source.close()
    return binaryToStr(binarys)
def readHufmmanTxt():
    fileName=input('enter huffman txt file name :')
    source=open(fileName,'r')
    txt=source.read()
    source.close()
    return txt
def txtToArr(txt):
    txt='^'+txt
    res=[['','']]
    flag=1
    for i in range(0,len(txt)):
        print(i,len(txt))
        if i>(len(txt)-2):
            return res
        else:
            if txt[i]=='\t' and txt[i+1]=='\t':
                i=i+4
                pass
            if txt[i]=='\n' and txt[i+1]=='\n':
                i=i+1
                pass
        
        if txt[i]=='\t' and flag:
            temp=[txt[i-1],'']
            flag=0
        if txt[i]=='\t' and  not flag:
            for j in txt[i:]:
                if j=='\n':
                    break
                if j=='0' or j=='1':
                    temp[1]+=j
            res=res+[temp]
            flag=1
    return res
def spl(txt):
    arr=txt.split("\t")
    return arr
ziptxt=readZip()
htxt=readHufmmanTxt()
huffmanArr=spl(htxt)

def writeRes(strRes):
    with open('input.txt','w') as f:
        f.write(strRes)
    f.close()
res=''

for i in range (0,len(huffmanArr)):
    if  huffmanArr[i]==chr(0):
        EOF=huffmanArr[i+2]
        break

while(not ziptxt.startswith(EOF)):
    for i in range (0,len(huffmanArr)):
        temp=huffmanArr[i]
        if (ziptxt.startswith(temp)):
            if (huffmanArr[i-2]=="\n\\t"):
                res+='\t'
            else:
                res+=huffmanArr[i-2][1]
            ziptxt=ziptxt[len(temp):]
            break
print(res)
writeRes(res)