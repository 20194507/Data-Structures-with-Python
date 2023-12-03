# https://www.youtube.com/watch?v=MYk4autDAJ0&list=PLsMufJgu5933ZkBCHS7bQTx0bncjwi4PK&index=10&ab_channel=Chan-SuShin


class Stack:
    def __init__(self):
        self.items = []  # 데이터 저장을 위한 리스트 준비 (Initialize an empty list for data storage)

    def push(self, val):
        self.items.append(val)  # 스택에 원소 추가 (Add an element to the stack)

    def pop(self):
        try:  # pop할 아이템이 없으면
            return self.items.pop()
        except IndexError:  # indexError 발생
            print("Stack is empty")

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")

    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):  # len()로 호출하면 stack의 item 수 반환 (Return the number of items in the stack when called with len())
        return len(self.items)


# 중위 표기식을 후위 표기식으로 변환
def infix_to_postfix(expr):
    opstack = Stack()  # 연산자를 저장할 스택 (Stack to store operators)
    outstack = []  # 출력을 위한 리스트 (List for output)

    # 연산자의 우선순위를 반환하는 함수 (Function to return the priority of an operator)
    def priority(operator):
        if operator == '(':
            return 0
        elif operator in ['+', '-']:
            return 1
        elif operator in ['*', '/']:
            return 2
        else:
            return -1

    for token in expr:
        if token.isdigit():
            outstack.append(token)
        elif token == '(':
            opstack.push(token)
        elif token == ')':
            # '('를 만날 때까지 스택에서 모든 연산자를 pop하고 outstack에 추가
            while opstack.top() != '(':
                outstack.append(opstack.pop())
            opstack.pop()  # '(' 제거
        elif token in "+-*/":
            # 현재 연산자의 우선순위가 스택의 top에 있는 연산자의 우선순위보다 낮거나 같으면 pop하고 outstack에 추가
            while not opstack.is_empty() and priority(opstack.top()) >= priority(token):
                outstack.append(opstack.pop())
            opstack.push(token)

    # 남은 연산자 모두 pop
    while not opstack.is_empty():
        outstack.append(opstack.pop())

    return outstack

# 후위 표기식을 계산
def calculate_postfix(postfix_exp):
    S = Stack()

    for token in postfix_exp:
        if token.isdigit():
            S.push(int(token))
        elif token in "+-*/":
            b = S.pop()
            a = S.pop()
            if token == '+':
                S.push(a + b)
            elif token == '-':
                S.push(a - b)
            elif token == '*':
                S.push(a * b)
            elif token == '/':
                S.push(a / b)

    return S.pop()

# 예제 사용
infix_expr = "3 + 5 * ( 2 - 8 ) / 2"
postfix_expr = infix_to_postfix(infix_expr.split())
result = calculate_postfix(postfix_expr)

print("Infix Expression:", infix_expr)
print("Postfix Expression:", " ".join(postfix_expr))
print("Calculation Result:", result)



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


# # infix -> posfix
# for token in expr :
#     if token == operand :
#         outstack.append(token)
#     if token == '(' :
#         opstack.push(token)
#     if token == ')' :
#         opstack에 저장된 연산자 '('를 pop할때까지 pop 
#         -> of outstack에 append
    
#     if token in "+*-/" : 
#         opstack에 token 우선 순위 높은
#         연산자 모두 pop, 자신이 push
#         opstack에 남은 연산자 모두 pop -> outstack
        
# # posfix -> calculation
# for token in postfix.exp :
#     if token == operand :
#         S.push(token)
#     if token in "+*-/" :
#         a = S.pop()
#         b = S.pop()
#         S.push( a token b)

