# https://www.youtube.com/watch?v=nQhzNRmnmt8&list=PLsMufJgu5933ZkBCHS7bQTx0bncjwi4PK&index=15&ab_channel=Chan-SuShin

class Node:
    def __init__(self, key=None):
        # 노드의 초기화 함수입니다.
        # Initializes a node.
        self.key = key
        self.next = self
        self.prev = self

    def __str__(self):
        # 노드의 문자열 표현을 반환합니다. 주로 디버깅과 출력에 사용됩니다.
        # Returns the string representation of the node, mainly used for debugging and printing.
        return str(self.key)

class DoublyLinkedList:
    def __init__(self):
        # 양방향 연결 리스트의 초기화 함수입니다.
        # Initializes a doubly linked list.
        self.head = Node()
        self.size = 0

    def __iter__(self):
        # 리스트의 각 노드를 반복적으로 반환하는 이터레이터 함수입니다.
        # Iterator function that iterates over each node in the list.
        v = self.head.next
        while v != self.head:
            yield v
            v = v.next

    def __str__(self):
        # 리스트의 문자열 표현을 반환합니다.
        # Returns the string representation of the list.
        nodes = [str(node) for node in self]
        return " <-> ".join(nodes)

    def __len__(self):
        # 리스트의 노드 개수를 반환합니다.
        # Returns the number of nodes in the list.
        return self.size

    def Splice(self, a, b, x):
        # 조건1 : a -> ... -> b
        # 조건2 : a와 b 사이에 head가 있으면 안된다.
        # 조건3 : a와 b 사이에 x node가 있으면 안된다.

        # 주어진 노드들 간의 연결을 조작하여 Splice 연산을 수행합니다.

        # 조건2 확인
        if a.next == b or b.prev == a or a == b or a == x or b == x:
            # 조건2를 위배할 경우 아무 작업도 수행하지 않고 함수를 종료합니다.
            # If condition 2 is violated, no operation is performed, and the function exits.
            return
        
        ap, bn, xn = a.prev, b.next, x.next

        # 조건3 확인
        if x != a and x != b and xn != a and xn != b and ap != b and bn != a:
            # 주어진 조건을 만족하면 연결을 수정합니다.
            # If the given conditions are satisfied, modify the connections.
            ap.next = bn  # cut
            bn.prev = ap  # cut

            x.next = a
            a.prev = x
            b.next = xn
            xn.prev = b

    def move_After(self, a, x):
        # 노드 a를 노드 x 다음으로 이동합니다.
        # Moves node a after node x.
        self.Splice(a, a, x)

    def move_Before(self, a, x):
        # 노드 a를 노드 x 전으로 이동합니다.
        # Moves node a before node x.
        self.Splice(a, a, x.prev)

    def insert_After(self, x, key):
        # 노드 x 다음에 새로운 노드를 삽입합니다.
        # Inserts a new node after node x.
        new_node = Node(key)
        self.move_After(new_node, x)

    def insert_Before(self, x, key):
        # 노드 x 전에 새로운 노드를 삽입합니다.
        # Inserts a new node before node x.
        new_node = Node(key)
        self.move_Before(new_node, x)

    # 탐색 연산
    def search(self, key):
        # 주어진 키 값을 갖는 노드를 찾아 반환합니다. 없으면 None을 반환합니다.
        # Finds and returns the node with the given key value. Returns None if not found.
        v = self.head.next  # dummy node 다음부터 시작 (Start from the node after the dummy node)
        while v != self.head:
            if v.key == key:
                return v
            v = v.next
        return None

    # 삭제 연산
    def remove(self, x):
        # 노드 x를 삭제합니다.
        # Removes node x.
        if x == None or x == self.head:
            return
        x.prev.next = x.next
        x.next.prev = x.prev
        del x

    def popFront(self):
        # 리스트의 맨 앞 노드를 삭제하고 그 노드의 key를 반환합니다.
        # Removes the front node of the list and returns its key.
        if self.head.next == self.head:
            return None
        front_key = self.head.next.key
        self.remove(self.head.next)
        return front_key

    def popBack(self):
        # 리스트의 맨 뒤 노드를 삭제하고 그 노드의 key를 반환합니다.
        # Removes the back node of the list and returns its key.
        if self.head.prev == self.head:
            return None
        back_key = self.head.prev.key
        self.remove(self.head.prev)
        return back_key

    def join(self, other_list):
        # 두 양방향 연결 리스트를 결합하여 현재 리스트에 추가합니다.
        # Joins two doubly linked lists and appends the second list to the current list.
        
        # 다른 리스트가 비어 있으면 아무 작업도 수행하지 않습니다.
        # If the other list is empty, no operation is performed.
        if other_list.head.next == other_list.head:
            return

        # 현재 리스트가 비어 있을 경우 다른 리스트의 첫 노드를 현재 리스트의 head 뒤에 연결합니다.
        # If the current list is empty, connect the first node of the other list after the head of the current list.
        if self.head.next == self.head:
            self.head.next = other_list.head.next
            other_list.head.next.prev = self.head
        else:
            # 현재 리스트가 비어 있지 않을 경우, 현재 리스트의 맨 뒤 노드와 다른 리스트의 첫 노드를 연결합니다.
            # If the current list is not empty, connect the last node of the current list and the first node of the other list.
            last_node = self.head.prev
            last_node.next = other_list.head.next
            other_list.head.next.prev = last_node

        # 다른 리스트의 head를 초기화하여 두 리스트를 결합합니다.
        # Initialize the head of the other list to combine the two lists.
        other_list.head = Node()
        self.size += other_list.size
        other_list.size = 0

    def split(self):
        # 양방향 연결 리스트를 현재 노드를 중심으로 두 개로 분할합니다.
        # Splits the doubly linked list into two lists centered around the current node.

        # 현재 리스트가 비어 있거나 노드가 하나밖에 없으면 아무 작업도 수행하지 않습니다.
        # If the current list is empty or has only one node, no operation is performed.
        if self.size <= 1:
            return None, None

        # 두 번째 리스트의 head를 현재 리스트의 중간 지점 뒤로 설정합니다.
        # Set the head of the second list to the point after the middle of the current list.
        mid = self.size // 2
        second_list_head = self.head
        for _ in range(mid + 1):
            second_list_head = second_list_head.next

        # 첫 번째 리스트의 tail과 두 번째 리스트의 head를 연결해 분할을 수행합니다.
        # Connect the tail of the first list with the head of the second list to perform the split.
        first_list_tail = second_list_head.prev
        first_list_tail.next = self.head
        self.head.prev = first_list_tail

        # 두 번째 리스트의 head와 tail을 연결해 리스트를 완성합니다.
        # Connect the head and tail of the second list to complete the lists.
        second_list_tail = self.head.prev
        second_list_tail.next = second_list_head
        second_list_head.prev = second_list_tail

        # 첫 번째 리스트의 size를 업데이트하고 두 번째 리스트의 size를 초기화합니다.
        # Update the size of the first list and initialize the size of the second list.
        first_list_size = mid + 1
        second_list_size = self.size - first_list_size
        self.size = first_list_size

        return first_list_size, second_list_size



# 컨셉 코딩
# class Node:
#     def __init__(self, key=None):
#         self.key = key
#         self.next = self
#         self.prev = self
   
#     def __str__(self):
#         return str(self.key)

# class Doubly_Linked_List :
#     def __init__(self) :
#         self.head = Node()
#         self.size = 0
    
#     def __iter__() :
    
#     def __str__() :
    
#     def __len__() :

#     def Splice(self, a, b, x) :
#         # 조건1 : a -> ... -> b
#         # 조건2 : a와 b 사이에 head가 있으면 안된다.
#         # 조건3 : a와 b 사이에 x node가 있으면 안된다.
#         ap = a.prev, bn = b.next, xn = x.next

#         ap.next = bn    # cut
#         bn.prev = x     # cut

#         x.next = a
#         a.prev = x
#         b.next = xn
#         xn.prev = b
    
#     def move_After(self, a, x) :
#         # 노드 a를 노드 x 다음으로 이동
#         Splice(a, a, x)
#     def move_Before(a, x) :
#         # a를 x 전으로 이동
#         Splice(a, a, x.prev)
#     def insert_After(x, key) :
#         move_After(Node(key), x) 
#     def insert_Before(x, key) :
#         move_Before(Node(key), x)

#     # 탐색연산
#     def search(self, key) :
#         v = self.head   #dummy node
#         while v.next != self.head :
#             if v.key == key :
#                 return v
#             v = v.next
#         return None
    
#     # 삭제연산
#     def remove(x) :   # 노드 x를 삭제
#         if x == None or x == self.head :
#             return
#         x.prev.next = x.next
#         x.next.prev = x.prev
#         del x
    
#     def popFront :
#     def popBack :
    