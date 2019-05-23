from array import *
class Node:
    left = 0
    right = 0
    val = ""
    address = ""
    count = 0
    def __init__(self,val):
        self.val=val
        return
    '''def __init__(self,left,right):
        self.addLeft(left)
        self.addRight(right)
        return'''

    def updateAddress(self, c):
        self.address = c + self.address
        if (self.right != 0):
            self.right.updateAddress(c)
        if (self.left != 0):
            self.left.updateAddress(c)

    def addLeft(self, n):
        self.left = n
        n.updateAddress('0')
        self.val+=n.val
        self.count+=n.count
        return

    def addRight(self, n):
        self.right = n
        n.updateAddress('1')
        self.val+=n.val
        self.count+=n.count
        return
    def __str__(self):
        return self.val + str(self.count)

def findNode(n,val):
    if (len(n.val)==1):
        return n.address
    if(val in n.right.val):
        return findNode(n.right,val)
    if (val in n.left.val):
        return findNode(n.left, val)
def sort(xs):
    if(len(xs)==0):
        return []
    min=0
    for i in range (0,len(xs)):
        if(xs[i].count<xs[min].count):
            min=i
    minMember=xs[min]
    xs=xs[0:min]+xs[min+1:]
    return [minMember] + sort(xs)

def countChar(fileStr):
    alphabet=[Node(chr(i)) for i in range(0,127)]
    for i in range(0, len(fileStr)):
        alphabet[ord(fileStr[i])-0].count += 1
    return alphabet

def createTree(alphabet):
    while (len(alphabet) != 1):
        alphabet = sort(alphabet)
        temp = Node('')
        temp.addLeft(alphabet[0])
        temp.addRight(alphabet[1])
        alphabet = [temp] + alphabet[2:]
    return alphabet[0]

def writeFile(res):
    res
    bstr = [res[i:i + 8] for i in range(0, len(res), 8)]
    bs = [int(b, 2) for b in bstr]
    with open('res.bin', 'wb') as f:
        f.write(bytearray(bs))  # convert to bytearray before writing
    f.close()
fileName=input('enter file name :')
source=open(fileName,'r')
fileStr=source.read()
alphabet=countChar(fileStr)
tree=createTree(alphabet)
res=''
for i in range(0,len(fileStr)):
    res+=findNode(tree,fileStr[i])
writeFile(res)
print("old size is (bits) : "+str(len(fileStr)*8))
print("new size is (bits) : "+str(len(res)))

'''
dest=open('res.txt','b')
dest.write(res)
dest.close()
source.close()
'''