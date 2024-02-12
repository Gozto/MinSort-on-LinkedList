class LinkedList:
    class Node:
        def __init__(self, data, next=None):
            self.data, self.next = data, next

    def __init__(self, seq=None):
        self.len = 0
        self.front = self.Node(None)
        if seq is not None:
            vrch = self.front
            if type(seq) == int:
                vrch.next = self.Node(seq)
                self.len += 1
            else:
                for prvok in seq:
                    vrch.next = self.Node(prvok)
                    vrch = vrch.next
                    self.len += 1

    def progress(self, first, reverse):
        vrch = first.next 
        if vrch is None: #ked je vrch posledny v zozname
            return 

        node1 = first.next
        node2 = node1.next
        while node2:
            if reverse is not True:
                if node1.data > node2.data:
                    self.vymen(node1, node2)
                    node1, node2 = node2, node1
            elif reverse is True:
                if node1.data < node2.data:
                    self.vymen(node1, node2)
                    node1, node2 = node2, node1
            node2 = node2.next

    def vymen(self, node1, node2):
        if node1 == node2:
            return

        pred_node1 = self.front
        while pred_node1.next != node1:
            pred_node1 = pred_node1.next

        pred_node2 = self.front
        while pred_node2.next != node2:
            pred_node2 = pred_node2.next

        if pred_node1 != None:
            pred_node1.next = node2
        else:
            self.front = node2

        if pred_node2 != None:
            pred_node2.next = node1
        else:
            self.front = node1

        pomocny_pointer = node1.next
        node1.next = node2.next
        node2.next = pomocny_pointer
        return node2

    def min_sort(self, reverse):
        first = self.front
        while first.next is not None:
            self.progress(first, reverse)
            print(self.get_list())
            first = first.next

    def get_list(self):
        lst = []
        vrch = self.front.next
        while vrch:
            lst.append(vrch.data)
            vrch = vrch.next
        return lst

    def __getitem__(self, index):
        vrch = self.front
        cnt = -1
        while vrch:
            if cnt == index:
                return vrch.data
            vrch = vrch.next
            cnt += 1

    def get_node(self, index):
        vrch = self.front
        cnt = -1
        while vrch:
            if cnt == index:
                return vrch
            vrch = vrch.next
            cnt += 1

def min_sort(seq, reverse=False):
    ll = LinkedList(seq)
    ll.min_sort(reverse)
    return ll.get_list()

if __name__ == '__main__':
    seq = (4,30,8,31,48,19)
    lst = min_sort(seq)
    print(lst)

    seq = 'kohutik jaraby nechod do zahrady'.split()
    lst = min_sort(seq, reverse=True)
    print(lst)


