class Stack:
    def __init__(self):
        self.items = []                 # 데이터 저장을 위한 리스트 준비

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:                            # pop할 아이템이 없으면
            return self.items.pop()
        except IndexError:              # indexError 발생
            print("Steck is empty")

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Steck is empty")

    def __len__(self):                  # len()로 호출하면 stack의 item 수 반환
        return len(self.items)


S = Stack()
parSeq = ['(', ')']
for p in range(0, len(parSeq)) :
    if parSeq[p] =='(' :
        S.push('(')
#       print(S.items)
    elif parSeq[p] == ')' :
        S.pop()
#       print(S.items)
    else :
        print("Not albwed Symbol")
        print(S)
if len(S) > 0 :
    print(False)
#   print(S.items)
else :
    print(True)
#   print(S.items)


    # https://www.youtube.com/watch?v=OzFXiukhv8o&list=PLsMufJgu5933ZkBCHS7bQTx0bncjwi4PK&index=8&ab_channel=Chan-SuShin