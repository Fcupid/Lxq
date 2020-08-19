#用类表示出链表
#建立节点node
class Node(object):
    '''初始化'''
    def __init__(self,elem):
        self.elem=elem
        self.next=None

#创建链表
class SingleCircleList(object):
    '''单链表'''
    def __init__(self,node=None):
        self._head=node
        if node:
            node.next=node#变量私有化，且头节点为空

    "关于链表的相关操作函数"
    def is_empty(self):
        '''链表是否为空'''
        return self._head==None

    def length(self):
        '''链表长度'''
        if self.is_empty():
            return 0
        count = 1
        cur=self._head
        # 建立指针，初始位置指向头结点,用于移动便利节点
        while cur.next != self._head:
            count+=1
            cur=cur.next
        return count

    def travel(self):
        '''遍历链表'''
        cur=self._head
        if self.is_empty():#什么语法？？？？
            return None
        else:
            while cur.next!= self._head:
                print(cur.elem,end=' ')
                cur=cur.next
            print(cur.elem)#由于cur在指向尾节点时，循环就退出了，未打印，因此在循环退出时要把尾节点加上

    def add(self,item):
        '''从头部添加元素——头插法'''
        node=Node(item)#函数第一步一定要新建一个Node用于添加。
        node.next=self._head
        self._head=node

    def append(self,item):
        '''尾插法'''
        node=Node(item)
        cur=self._head
        if self._head == None:
            self._head=node
        else:
            while cur.next != None:
                cur=cur.next
            cur.next=node

    def insert(self,pos,item):
        '''在中间任意位置添加元素'''
        node=Node(item)
        cur=self._head
        if pos<0:
            self.add(item)
        elif pos>=ls.length():
            self.append(item)
        else:
            count=1
            while count<pos:
                count+=1
                cur=cur.next
            node.next=cur.next
            cur.next=node

    def remove(self,item):
        '''移除链表元素'''
        if self.is_empty():
            return
        cur=self._head
        pre=None
        #判断是否为空
        while cur.next != None:
            if cur.elem==item:
                #头结点的情况，需要一个指针移动到尾部，在指向头部重新建立循环
                rear=self._head
                if rear.next!=cur:
                    rear=rear.next
                self._head=cur.next
                rear.next=self._head
            if cur.elem != item :
                pre=cur
                cur = cur.next
                if cur.elem==item:
                    pre.next=cur.next
            break
            #退出循环尾节点，cur指向为节点
        if cur.elem==item:
            if cur==self._head:#只有一个人节点的情况
                self._head=None
            else:
                pre.next=cur.next
        else:
            return

    def search(self,item):
        '''查找链表中元素是否存在'''
        if self.is_empty() :
            return False
        cur=self._head
        while cur.next!=self._head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        if cur.next==self.head:
            if cur.elem==item:
                return True
            else:
                return False

if __name__=="__main__":
    ls=SingleCircleList()
    ls.append(3)
    ls.append(5)
    ls.remove(3)
    #ls.insert(1,100)
    ls.travel()
    #ls.remove(100)
    #ls.travel()
