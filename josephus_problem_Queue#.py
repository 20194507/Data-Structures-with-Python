# https://www.youtube.com/watch?v=MYk4autDAJ0&list=PLsMufJgu5933ZkBCHS7bQTx0bncjwi4PK&index=10&ab_channel=Chan-SuShin

class Queue:
    class EmptyQueueError(Exception):
        """Custom exception for empty queue error (큐가 비어있는 경우의 사용자 정의 예외)"""
        pass

    def __init__(self):
        self.items = []     # Create an empty list to store queue elements (큐의 원소를 저장하기 위한 빈 리스트)
        self.front_index = 0

    def enqueue(self, val):
        """Enqueue (insert) an element into the queue (요소를 큐에 추가합니다)."""
        self.items.append(val)

    def dequeue(self):
        """Dequeue (remove) an element from the front of the queue (큐의 맨 앞에서 요소를 제거합니다)."""
        if self.front_index == len(self.items):
            raise self.EmptyQueueError("Q is empty (큐가 비어있습니다)")
        else:
            x = self.items[self.front_index]
            self.front_index += 1
            return x



    def josephus_problem(self, n, k):
        """
        Solve the Josephus problem for a given number of people (n) and elimination interval (k)
        (특정한 인원 수 (n)와 제거 간격 (k)에 대한 요셉스 문제를 해결합니다).

        Parameters:
        - n (int): Number of people (사람 수).
        - k (int): Elimination interval (제거 간격).

        Returns:
        - list: Order in which people are eliminated (제거된 사람들의 순서).
        """
        # Create a circular queue to represent the circle of people (원형을 이루는 큐를 생성합니다.)
        for i in range(1, n + 1):
            self.enqueue(i)

        # List to store the order of eliminated people (제거된 사람들의 순서를 저장할 리스트를 생성합니다.)
        eliminated_people = []

        try:
            # Continue until only one person is left in the queue (큐에 한 명의 사람만 남을 때까지 반복합니다.)
            while len(self.items) > 1:
                # Move (k-1) people to the back of the queue ((k-1)명의 사람을 큐의 뒤로 이동합니다.)
                for _ in range(k - 1):
                    self.enqueue(self.dequeue())

                # Remove the k-th person and add to the list (k번째 사람을 제거하고 리스트에 추가합니다.)
                eliminated_person = self.dequeue()
                eliminated_people.append(eliminated_person)
                print(f"Person {eliminated_person} eliminated ({eliminated_person} 번째 사람이 제거되었습니다).")

            # The last person remains in the queue (마지막으로 남은 사람은 큐에 그대로 남아 있습니다.)
            last_person = self.items[self.front_index - 1]
            print(f"The last person remaining is {last_person} ({last_person} 번째로 남은 사람입니다).")

            print("Elimination order (제거 순서):", eliminated_people)
            return eliminated_people
        except self.EmptyQueueError as e:
            print(e)
            return eliminated_people

# Example of solving the Josephus problem (요셉스 문제 해결의 예시)
queue_instance = Queue()
result = queue_instance.josephus_problem(7, 3)
print("Elimination order (제거 순서):", result)
