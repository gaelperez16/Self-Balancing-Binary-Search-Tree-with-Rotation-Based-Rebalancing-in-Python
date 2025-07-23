class OurCSCE310Tree:
    # Class constructor
    def __init__(self, value=0, parent=None, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    # Class Destructor
    def __del__(self):
        self.value = 0
        del self.left
        self.left = None
        del self.right
        self.right = None

    def getParent(self):
        return self.parent

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getValue(self):
        return self.value

    def setParent(self, par):
        self.parent = par
        return

    def setLeft(self, lft):
        self.left = lft
        return

    def setRight(self, rght):
        self.right = rght
        return

    def setValue(self, val):
        self.value = val
        return

    def insert(self, val):
        if not self.getValue():
            self.setValue(val)
        elif (val < self.getValue() and not self.getLeft()) or (
                val < self.getValue() and not self.getLeft().getValue()):
            self.left = OurCSCE310Tree()
            self.left.setParent(self)
            self.left.setValue(val)
        elif ((val > self.getValue() and not self.getRight()) or (
                val > self.getValue() and not self.getRight().getValue())):
            self.right = OurCSCE310Tree()
            self.right.setParent(self)
            self.right.setValue(val)
        elif val < self.getValue():
            self.getLeft().insert(val)
        else:
            self.getRight().insert(val)

        if self.getLeft() and self.getLeft().getRight() and not self.getRight() or self.getLeft() and self.getLeft().getRight() and self.getRight() and self.getLeft().getHeight() > self.getRight().getHeight() + 1 and self.getLeft().getRight().getHeight() > self.getLeft().getLeft().getHeight() + 1:
            self.rotateLeftRight()
        elif self.getRight() and self.getRight().getLeft() and not self.getLeft() or self.getRight() and self.getRight().getLeft() and self.getLeft() and self.getRight().getHeight() > self.getLeft().getHeight() + 1 and self.getRight().getLeft().getHeight() > self.getRight().getRight().getHeight() + 1:
            self.rotateRightLeft()
        elif self.getLeft() and not self.getRight() and self.getLeft().getHeight() > 1 or self.getLeft() and self.getRight() and self.getLeft().getHeight() > self.getRight().getHeight() + 1:
            self.rotateRight()
        elif self.getRight() and not self.getLeft() and self.getRight().getHeight() > 1 or self.getRight() and self.getLeft() and self.getRight().getHeight() > self.getLeft().getHeight() + 1:
            self.rotateLeft()
        return

    def printPreorder(self):
        if self.getValue():
            print(self.getValue(), end='')
        if self.getLeft() and self.getLeft().getValue():
            print(",", end='')
            self.getLeft().printPreorder()
        if self.getRight() and self.getRight().getValue():
            print(",", end='')
            self.getRight().printPreorder()
        return

    def printInorder(self):
        if self.getLeft() and self.getLeft().getValue():
            self.getLeft().printInorder()
            print(",", end='')
        if self.getValue():
            print(self.getValue(), end='')
        if self.getRight() and self.getRight().getValue():
            print(",", end='')
            self.getRight().printInorder()
        return

    def printPostorder(self):
        if self.getLeft() and self.getLeft().getValue():
            self.getLeft().printPostorder()
            print(",", end='')
        if self.getRight() and self.getRight().getValue():
            self.getRight().printPostorder()
            print(",", end='')
        if self.getValue():
            print(self.getValue(), end='')
        return

    def getHeight(self):
        if self.getLeft() and self.getLeft().getValue() and (not self.getRight() or not self.getRight().getValue()):
            return self.getLeft().getHeight() + 1
        elif self.getRight() and self.getRight().getValue() and (not self.getLeft() or not self.getLeft().getValue()):
            return self.getRight().getHeight() + 1
        elif self.getRight() and self.getLeft() and self.getRight().getValue() and self.getLeft().getValue():
            return max(self.getRight().getHeight(), self.getLeft().getHeight()) + 1
        elif self.getValue() and (not self.getLeft() or not self.getLeft().getValue()) and (
                not self.getRight() or not self.getRight().getValue()):
            return 1
        return 0

    def deleteNode(self, key): #fails test11???
        if self.getValue() == key:
        #if self.getValue() = val
            if self.getLeft() is None:
                return self.getRight()
            elif self.getRight() is None:
                return self.getLeft()
            else:
                tempR = self.getRight()
                while tempR.getLeft() is not None:
                    tempR = tempR.getLeft()

                self.setValue(tempR.getValue())
               #deletes
                self.setRight(self.getRight().deleteNode(tempR.getValue()))
        elif key < self.getValue():#less than
            if self.getLeft() is not None:
                self.setLeft(self.getLeft().deleteNode(key))
        else:
            if self.getRight() is not None:
            #if self.getRight() == is not None
                self.setRight(self.getRight().deleteNode(key))
        return self

    def rotateLeft(self):
        left_child = self.getLeft()
        right_child = self.getRight()

        new_node = OurCSCE310Tree() #tree
        new_node.setParent(self) #parent

        self.setLeft(new_node)
        new_node.setLeft(left_child)
        Value = self.getValue()
        new_node.setValue(Value)

        RightValue = right_child.getValue()
        self.setValue(RightValue)
        RightLeft = right_child.getLeft()

        if RightLeft != None:
        #if RightLeft == None: //wrong
            new_node.setRight(RightLeft)
            RightLeft.setParent(new_node)
        RRight = right_child.getRight()
        if RRight != None:
            RRight.setParent(self)
            self.setRight(RRight)
        return

    def rotateRight(self):
        left_child = self.getLeft()
        right_child = self.getRight()
        
        new_node = OurCSCE310Tree()
        new_node.setParent(self)
        self.setRight(new_node)
        new_node.setRight(right_child)
        Value = self.getValue()
        new_node.setValue(Value)

        LeftVal = left_child.getValue()
        self.setValue(LeftVal)
        LeftRight = left_child.getRight()
        if LeftRight != None:
            new_node.setLeft(LeftRight)
            LeftRight.setParent(new_node)
        LL = left_child.getLeft()
        #LL = right_child.getLeft()
        if LL != None:
            LL.setParent(self)
            self.setLeft(LL)
        return

    def rotateLeftRight(self):
        self.getLeft().rotateLeft()
        self.rotateRight()
        return

    def rotateRightLeft(self):
        self.getRight().rotateRight()
        self.rotateLeft()
        return

    def getElevation(self):
        if not self.getParent():
            return self.getHeight()
        else:
            return self.getParent().getElevation() - 1

