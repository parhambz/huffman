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
        return "count: "+str(self.count)+'  val:  '+self.val
    def __ge__(self,other):
        return self.count >= other.count
    def __gt__(self,other):
        return self.count > other.count
    def __lt__(self,other):
        return self.count < other.count
    def __le__(self,other):
        return self.count <= other.count
class MinHeap:
    arr=[Node("aa")]
    def upHeapify(self,x):
        if x<=1:
            return
        if self.arr[x//2]>self.arr[x]:
            self.arr[x//2],self.arr[x]=self.arr[x],self.arr[x//2]
            return self.upHeapify(x//2)
        else:
            return
    def downHeapify(self,x):
        if (x*2>=len(self.arr)):
            return
        if (x*2+1>=len(self.arr) or self.arr[x*2]< self.arr[x*2+1]):
            if (self.arr[x]>self.arr[x*2]):
                self.arr[x],self.arr[x*2]=self.arr[x*2],self.arr[x]
                return self.downHeapify(x*2)
        else:
            if (self.arr[x]>self.arr[x*2+1]):
                self.arr[x],self.arr[x*2+1]=self.arr[x*2+1],self.arr[x]
                return self.downHeapify(x*2+1)
        return
    def add(self,x):
        self.arr.append(x)
        self.upHeapify(len(self.arr)-1)
    def removeMin(self):
        self.arr[1]=self.arr[len(self.arr)-1]
        self.arr.pop()
        self.downHeapify(1)
    def getMin(self):
        return self.arr[1]
    def __str__(self):
        res=''
        j=0
        for i in self.arr:
            res=res+str(j)+str(i)+'\n'
            j=j+1
        return res
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
def createHuffman(minHeap):
    while (len(minHeap.arr)!=2):
        temp = Node('')
        temp.addLeft(minHeap.getMin())
        minHeap.removeMin()
        if (len(minHeap.arr)>1):
            temp.addRight(minHeap.getMin())
            minHeap.removeMin()
        minHeap.add(temp)
    return minHeap.arr[1]
def createMinHeap(alphabet):
    m=MinHeap()
    for i in alphabet :
        m.add(i)
    return m

def writeFile(res,huffmanTxtStr):
    bstr = [res[i:i + 8] for i in range(0, len(res), 8)]
    bs = [int(b, 2) for b in bstr]
    with open('zip.txt', 'wb') as f:
        f.write(bytearray(bs))  # convert to bytearray before writing
    f.close()
    with open('Huffman.txt','w') as f:
        f.write(huffmanTxtStr)
    f.close()
def huffmanTxt(huffTree,fileStr):
    res=''
    for i in range(0,127):
        if (chr(i) in fileStr):
            if(chr(i)=="\t"):
                temp=findNode(huffTree,chr(i))
                res=res+'\\t'+'\t'+str(len(temp))+'\t'+str(temp)+'\t'+'\n'
            else:
                temp=findNode(huffTree,chr(i))
                res=res+chr(i)+'\t'+str(len(temp))+'\t'+str(temp)+'\t'+'\n'
    return res

fileName=input('enter file name :')
source=open(fileName,'r')
fileStr=source.read()
fileStr=fileStr+chr(0)
alphabet=countChar(fileStr)

minHeapTree=createMinHeap(alphabet)
tree=createHuffman(minHeapTree)
res=''
resSize=0
for i in range(0,len(fileStr)):
    temp=findNode(tree,fileStr[i])
    resSize+=len(temp)
    res+=temp
res=res+(8-len(res)%8)*'0'
huffmanTxtStr=huffmanTxt(tree,fileStr)
writeFile(res,huffmanTxtStr)
print("old size is (bits) : "+str(len(fileStr)*8))
print("new size is (bits) : "+str(resSize))

