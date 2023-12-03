 # https://www.youtube.com/watch?v=OzFXiukhv8o&list=PLsMufJgu5933ZkBCHS7bQTx0bncjwi4PK&index=8&ab_channel=Chan-SuShin

class Stack:
    def __init__(self):
        self.items = []  # 스택을 위한 빈 리스트 초기화 (Initialize an empty list for the stack)

    def push(self, val):
        self.items.append(val)  # 스택에 원소 추가 (Add an element to the stack)

    def pop(self):
        # 스택이 비어있지 않으면 가장 위의 원소를 꺼내고 반환
        # 비어있으면 None 반환 (If the stack is not empty, remove and return the top element; if the stack is empty, return None)
        return self.items.pop() if self.items else None

    def top(self):
        # 스택이 비어있지 않으면 가장 위의 원소를 반환
        # 비어있으면 None 반환 (If the stack is not empty, return the top element; if the stack is empty, return None)
        return self.items[-1] if self.items else None

    def is_empty(self):
        # 스택이 비어있으면 True, 아니면 False 반환 (Return True if the stack is empty; otherwise, return False)
        return not self.items

    def __len__(self):
        # 스택의 원소 개수 반환 (Return the number of elements in the stack)
        return len(self.items)


def is_valid_parentheses(parSeg):
    stack = Stack()  # 괄호 검사를 위한 스택 생성 (Create a stack for parentheses validation)

    for p in parSeg:
        if p == '(':
            stack.push(p)
        elif p == ')':
            # 닫는 괄호를 만나면 스택에서 해당하는 여는 괄호를 빼냄
            # 여는 괄호가 없으면 불일치로 판단하고 False 반환 (When encountering a closing parenthesis, pop the corresponding opening parenthesis from the stack;
            # If there is no matching opening parenthesis, consider it a mismatch and return False)
            if not stack.pop():
                print("괄호 불일치 발생. (Mismatched parentheses occurred.)")
                return False
        else:
            print("알려지지 않은 기호 발견. (Unknown symbol encountered.)")
            return False

    # 모든 괄호를 검사한 후에도 스택에 여는 괄호가 남아있으면 불일치로 판단하고 False 반환
    # (If there are remaining opening parentheses in the stack, consider it a mismatch and return False)
    if not stack.is_empty():
        print("괄호 불일치 발생. (Mismatched parentheses occurred.)")
        return False
    else:
        # 모든 조건을 통과하면 괄호가 올바르게 맞춰진 것으로 판단하여 True 반환
        # (If all conditions are passed, consider the parentheses correctly balanced and return True)
        return True

# 예제 사용 (Example usage)
parSeg = "((()))"
result = is_valid_parentheses(parSeg)

if result:
    print("괄호가 올바르게 맞춰져 있습니다. (The parentheses are correctly balanced.)")
else:
    print("괄호가 올바르게 맞춰져 있지 않습니다. (The parentheses are not correctly balanced.)")



# 컨셉 코딩
# class Stack:
#     def __init__(self):
#         self.items = []                 # 데이터 저장을 위한 리스트 준비

#     def push(self, val):
#         self.items.append(val)

#     def pop(self):
#         try:                            # pop할 아이템이 없으면
#             return self.items.pop()
#         except IndexError:              # indexError 발생
#             print("Steck is empty")

#     def top(self):
#         try:
#             return self.items[-1]
#         except IndexError:
#             print("Steck is empty")

#     def __len__(self):                  # len()로 호출하면 stack의 item 수 반환
#         return len(self.items)
    
# # 괄호 맞추기    
# S = Stack()
# for p in parSeg :
#     if p == '(' : S.push(p)
#     elif p == ')' : S.pop()
#     else : print("Not albwed Symbol")
# if len(S) > 0 : return False
# else : return True