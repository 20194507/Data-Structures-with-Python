# https://www.youtube.com/watch?v=nqCNk_DmPio&list=PLsMufJgu5933ZkBCHS7bQTx0bncjwi4PK&index=11&ab_channel=Chan-SuShin

class Queue :
    def __init__(self) :
        self.items = []     # 빈리스트
        self.front_index = 0

    def enqueue(self, val) :
        self.items.append(val)

    def dequeue(self) :
        if self.front_index == len(self.items) :
            print("Q is empty")
            return None
        else :
            x = self.items[self.front_index]
            self.front_index += 1
            return x
        
# 테스트 코드
my_queue = Queue()

# enqueue 테스트
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)

# dequeue 테스트
print(my_queue.dequeue())  # 출력: 1
print(my_queue.dequeue())  # 출력: 2
print(my_queue.dequeue())  # 출력: 3
print(my_queue.dequeue())  # 출력: Queue is empty, None

# 컨셉 코드
