from binarytree import Node

class BT(Node):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, new_node):
        if self.left == None:
            self.left = BT(new_node)
        else:
            t = BT(new_node)
            t.left = self.left
            self.left = t

    def insert_right(self, new_node):
        if self.right== None:
            self.right= BT(new_node)
        else:
            t = BT(new_node)
            t.right = self.right
            self.right = t

    def get_right(self):
        return self.right

    def get_left_child(self):
        return self.left
    
    def set_root_val(self, obj):
        self.key = obj

    def get_root_val(self):
        return self.key

r = BT('a')
r.insert_left('b')
r.insert_left('c')
r.insert_right('10')
print(r)