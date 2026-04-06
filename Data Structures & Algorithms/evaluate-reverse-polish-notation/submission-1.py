class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            # Cách check số âm đơn giản nhất
            if token[-1].isdigit():
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:
                    # Dùng int(a / b) để xử lý số âm chuẩn xác
                    stack.append(int(a / b))


        return stack[0]