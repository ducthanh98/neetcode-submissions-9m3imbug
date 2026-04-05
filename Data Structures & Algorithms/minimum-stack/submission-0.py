class MinStack:
    def __init__(self):
        # Stack chính để lưu dữ liệu
        self.stack = []
        # Stack phụ để lưu các giá trị nhỏ nhất
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Nếu min_stack rỗng hoặc val nhỏ hơn/bằng giá trị nhỏ nhất hiện tại
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            # Nếu phần tử bị lấy ra là phần tử nhỏ nhất, phải cập nhật cả min_stack
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()

    def top(self) -> int:
        # Lấy phần tử trên cùng (mới nhất), không phải max
        return self.stack[-1]

    def getMin(self) -> int:
        # Giá trị nhỏ nhất luôn nằm ở đầu min_stack
        return self.min_stack[-1]