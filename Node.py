# https://www.youtube.com/watch?v=sMpsvA5O0xU&list=PLsMufJgu5933ZkBCHS7bQTx0bncjwi4PK&index=12&ab_channel=Chan-SuShin

# Define a class named Node to represent a node in a linked list.
# 연결 리스트의 노드를 표현하기 위한 Node 클래스를 정의합니다.
class Node:
    # Constructor to initialize a node with a key and a reference to the next node.
    # key와 다음 노드에 대한 참조로 노드를 초기화하는 생성자입니다.
    def __init__(self, key=None):
        self.key = key  # Key value stored in the node.
                        # 노드에 저장된 키 값입니다.
        self.next = None  # Reference to the next node in the linked list.
                          # 연결 리스트에서 다음 노드에 대한 참조입니다.

    # String representation of the node, useful for debugging and printing.
    # 디버깅 및 출력에 유용한 노드의 문자열 표현입니다.
    def __str__(self):
        return str(self.key)  # Convert the key to a string for easy printing.
                              # 키를 문자열로 변환하여 쉽게 출력할 수 있도록 합니다.

# Create three nodes with key values 3, 9, and -1.
# 키 값이 3, 9, -1인 세 개의 노드를 생성합니다.
a = Node(3)
b = Node(9)
c = Node(-1)

# Link the nodes to form a linked list: a -> b -> c
# 노드를 연결하여 연결 리스트를 형성합니다: a -> b -> c
a.next = b
b.next = c