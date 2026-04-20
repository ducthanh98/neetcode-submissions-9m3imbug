class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0 # Biến nhớ
        
        # Chạy khi còn node ở l1, l2 HOẶC còn biến nhớ
        while l1 or l2 or carry:
            # Lấy giá trị an toàn (nếu node None thì coi là 0)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Tính tổng và biến nhớ mới
            total = val1 + val2 + carry
            carry = total // 10  # Lấy phần chục (ví dụ 15 // 10 = 1)
            digit = total % 10   # Lấy phần đơn vị (ví dụ 15 % 10 = 5)
            
            # Tạo node mới với 1 chữ số duy nhất
            current.next = ListNode(digit)
            current = current.next
            
            # Di chuyển sang node tiếp theo
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return dummy.next