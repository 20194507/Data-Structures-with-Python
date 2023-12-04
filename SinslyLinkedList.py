# https://www.youtube.com/watch?v=kGZoEShMcSQ&list=PLsMufJgu5933ZkBCHS7bQTx0bncjwi4PK&index=13&ab_channel=Chan-SuShin

# 컨셉 코드
class Node:
    def __init__(self, key=None):
        # 노드의 초기화 함수입니다. Initializes a node.
        self.key = key  # 현재 노드에 저장되는 값 (Value stored in the current node)
        self.next = None  # 다음 노드를 가리키는 참조 (Reference to the next node)

    def __str__(self):
        # 노드의 문자열 표현을 반환합니다. 주로 디버깅과 출력에 사용됩니다. Returns the string representation of the node, mainly used for debugging and printing.
        return str(self.key)


class SinglyLinkedList:
    def __init__(self):
        # 단일 연결 리스트의 초기화 함수입니다. Initializes a singly linked list.
        self.head = None  # 리스트의 첫 번째 노드를 가리키는 참조 (Reference to the first node in the list)
        self.size = 0  # 리스트의 노드 개수를 나타내는 변수 (Variable indicating the number of nodes in the list)

    def pushFront(self, key):
        # 리스트의 맨 앞에 노드를 추가하는 함수입니다. Adds a node to the front of the list.
        new_node = Node(key)
        new_node.next = self.head  # 새로운 노드의 다음 노드를 현재 head로 설정 (Set the next node of the new node to the current head)
        self.head = new_node  # head를 새로운 노드로 업데이트 (Update the head to the new node)
        self.size += 1  # 리스트 크기 증가 (Increase the size of the list)

    def pushBack(self, key):
        # 리스트의 맨 뒤에 노드를 추가하는 함수입니다. Adds a node to the end of the list.
        new_node = Node(key)  # 수정: 변수 이름을 new_node로 변경했습니다.
        if self.size == 0:  # 리스트가 비어있을 경우 (If the list is empty)
            self.head = new_node
        else:
            tail = self.head
            while tail.next is not None:
                tail = tail.next
            tail.next = new_node  # 현재 마지막 노드의 다음을 새로운 노드로 설정 (Set the next of the current last node to the new node)
        self.size += 1  # 리스트 크기 증가 (Increase the size of the list)

    def popBack(self):
        # 리스트의 맨 뒤에 있는 노드를 제거하고 해당 노드의 키 값을 반환하는 함수입니다. Removes the node at the end of the list and returns its key value.
        if self.size == 0:
            return None  # 빈 리스트일 경우 None 반환 (Return None if the list is empty)
        elif self.size == 1:  # 리스트에 노드가 하나만 있는 경우 (If there is only one node in the list)
            key = self.head.key
            self.head = None  # head를 None으로 설정하여 리스트를 비움 (Set head to None to empty the list)
        else:
            prev, tail = None, self.head
            while tail.next is not None:
                prev, tail = tail, tail.next
            key = tail.key
            prev.next = None  # 마지막 노드를 삭제하기 위해 이전 노드의 다음을 None으로 설정 (Set the next of the previous node to None to delete the last node)
            del tail  # 불필요한 노드 삭제 (Delete the unnecessary node)
        self.size -= 1  # 리스트 크기 감소 (Decrease the size of the list)
        return key  # 삭제한 노드의 키 값을 반환 (Return the key value of the deleted node)

    def search(self, key):
        # 주어진 키 값을 갖는 노드를 찾아 반환합니다. 없으면 None을 반환합니다. Finds and returns the node with the given key value. Returns None if not found.
        v = self.head
        while v is not None:
            if v.key == key:
                return v
            v = v.next
        return None

    def __iter__(self):
        # 리스트의 각 노드를 반복적으로 반환하는 이터레이터 함수입니다. Iterator function that iterates over each node in the list.
        v = self.head
        while v is not None:
            yield v
            v = v.next

# Create three nodes with key values 3, 9, and -1.
# 키 값이 3, 9, -1인 세 개의 노드를 생성합니다.
a = Node(3)
b = Node(9)
c = Node(-1)

# Link the nodes to form a linked list: a -> b -> c
# 노드를 연결하여 연결 리스트를 형성합니다: a -> b -> c
a.next = b
b.next = c



# class SinslyLinkedList :
#     def __init__(self) :
#         self.head = None
#         self.size = 0
    
#     def pushFront(self, key) :
#         new_node = Node(key)
#         new_node.next = L.head
#         L.head = new_node
#         L.size += 1

#     def pushBack(self, key) :
#         v = Node(key)
#         if len(self) == 0 :
#             self.head = v
#         else :
#             tail = self.head
#             while tail.next != None :
#                 tail = tail.next
#             tail.next = v
#         self.size += 1
    
#     def popBack(self) :
#         if len(self) == 0 :
#             return None
#         else :      # running technique
#             prev, tail = None, self.head
#             while tail.next != None :
#                 prev = tailtail = tail.next
#             if len(self) == 1 :
#                 self.head == None
#             else :
#                 prev.next = tail.next
#             key = tail.key
#             del  tail
#             self.size -= 1
#             return key
    
#     def search(self, key) :
#         # key 값의 노드를 리턴, 없으면 None 리턴
#         v = self.head
#         while v != None :
#             if v.key == key :
#                 return v
#             v = v.next
#             return None
    
#     def __iterator__(self) :
#         v = self.head
#         while v != None :
#             yield v
#             v = v.next


 