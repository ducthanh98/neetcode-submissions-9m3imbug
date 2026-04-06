class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 1. Kết hợp và sắp xếp xe từ gần đích đến xa đích
        # reverse=True để xe có position lớn nhất đứng đầu
        cars = sorted(zip(position, speed), reverse=True)
        
        stack = []
        
        for p, s in cars:
            # 2. Tính thời gian xe này về đích (không bị cản trở)
            time = (target - p) / s
            
            # 3. Kiểm tra xem có tạo thành đoàn mới không
            # Nếu stack rỗng: Chắc chắn là 1 đoàn mới
            # Nếu time > stack[-1]: Xe này chậm hơn đoàn phía trước, 
            # nên nó sẽ tạo thành một đoàn riêng biệt phía sau.
            if not stack or time > stack[-1]:
                stack.append(time)
            
            # Nếu time <= stack[-1]: Xe này nhanh hơn hoặc bằng đoàn trước
            # Nó sẽ đâm vào đuôi đoàn trước và nhập bọn (không push vào stack)
            
        # 4. Số lượng đoàn xe chính là số phần tử trong stack
        return len(stack)