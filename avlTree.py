class Node:
    def __init__(self,key,value = None):
        self.key = key
        self.value = value
        self.right = None
        self.left = None

    def __str__(self):
        return str((self.key,self.value),)

class TreeAVL:
    def __init__(self):
        self.root = None
        self.height = -1
        self.balance = 0

    def str(self):
        if self.root is None:
            return ''
        string = str(self.root.key) + ',' + self.root.left.str() + ',' + self.root.right.str()
        string2 = ''
        flag = ''
        for x in string:
            if x != ',':
                flag += x
            else:
                if flag != '':
                    string2 += flag + ','
                    flag = ''
        return string2

    def __str__(self):
        string = self.str()
        return string[:len(string)-1]

    def __repr__(self):
        if self.root is None:
            return []
        
        listt = []

        l = self.root.left.__repr__()
        for x in l:
            listt.append(x)

        listt.append(self.root.key)

        l = self.root.right.__repr__()
        for x in l:
            listt.append(x)
        
        return listt

    def _height_(self):
        if self.root is not None:
            return self.height
        else:
            return 0
    
    def folha(self):
        return (self.height == 0)
    
    def insert(self,key,value=None):
        pointer = self.root
        if pointer is None:
            self.root = Node(key,value)
            self.root.left = TreeAVL()
            self.root.right = TreeAVL()
        elif key < pointer.key:
            return self.root.left.insert(key,value)
        elif key > pointer.key:
            return self.root.right.insert(key,value)
        else:
        self.balanced()

    def heightUpdate(self):
        if self.root is not None:
            if self.root.left is not None:
                self.root.left.heightUpdate()
            if self.root.right is not None:
                self.root.right.heightUpdate()
            self.height = max(self.root.left.height,self.root.right.height) + 1
        else:
            self.height = -1

    def balanceUpdate(self):
        if self.root is not None:
            if self.root.left is not None:
                self.root.left.balanceUpdate()
            if self.root.right is not None:
                self.root.right.balanceUpdate()
            self.balance = self.root.left.height - self.root.right.height
        else:
            self.balance = 0
    
    def leftRotate(self):
        x = self.root
        y = self.root.right.root
        z = y.left.root
        self.root = y
        y.left.root = x
        x.right.root = z
    
    def rightRotate(self):
        x = self.root
        y = self.root.left.root
        z = y.right.root
        self.root = y
        y.right.root = x
        x.left.root = z
    
    def balanced(self):
        while abs(self.balance) > 1:
            if self.balance > 1:
                if self.root.left.balance < 0:
                    self.root.left.leftRotate()
                    self.heightUpdate()
                    self.balanceUpdate()
                self.rightRotate()
            if self.balance < -1:
                if self.root.right.balance > 0:
                    self.root.right.rightRotate()
                    self.heightUpdate()
                    self.balanceUpdate()
                self.leftRotate()

            self.heightUpdate()
            self.balanceUpdate()

    def successor(self,root):
        root = root.right.root
        if root is not None:
            while root.left:
                if root.left.root is None:
                    return root
                else:
                    root = root.left.root
        return root
    
    def predecessor(self,root):
        root = root.left.root
        if root is not None:
            while root.right:
                if root.right.root is None:
                    return root
                else:
                    root = root.right.root
        return root

    def remove(self,key):
        if self.root:
            if self.root.key == key:
                if self.root.left is None and self.root.right is None:
                    self.root = None
                elif self.root.left is None:
                    self.root = self.root.right.root
                elif self.root.right is None:
                    self.root = self.root.left.root
                else:
                    s = self.successor(self.root)
                    if s:
                        self.root.key = s.key
                        self.root.value = s.value
                        self.root.right.remove(s.key)
                self.balanced()
                return

            elif key < self.root.key:
                self.root.left.remove(key)
            elif key > self.root.key:
                self.root.right.remove(key)
            self.balanced()
        else:
            return

    def checkBalance(self):
        if self.root is None or self is None:
            return True
        self.heightUpdate()
        self.balanceUpdate()
        return (abs(self.balance)<2) and self.root.left.checkBalance() and self.root.right.checkBalance()

    
