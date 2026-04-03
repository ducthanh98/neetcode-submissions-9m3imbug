class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        res = len(s1)
        for s in s1:
            if s in count:
                count[s] += 1 
            else:
                count[s] = 1 
        l, r = 0, 0
        while(r < len(s2)):
            # 1. Xử lý ký tự bên phải (r)
            if s2[r] in count:
                if count[s2[r]] > 0:
                    res -= 1
                # Luôn trừ count, kể cả khi nó về âm (để đánh dấu là đang dư ký tự)
                count[s2[r]] -= 1
            
            if res == 0:
                return True

            # 2. Xử lý thu hẹp cửa sổ khi đạt độ dài s1
            if r - l + 1 >= len(s1):
                if s2[l] in count:
                    # Nếu count >= 0 nghĩa là ký tự này thực sự quan trọng (không phải loại dư thừa)
                    # nên khi bỏ nó ra, ta phải tăng res (tức là cần thêm ký tự này)
                    if count[s2[l]] >= 0:
                        res += 1
                    count[s2[l]] += 1
                l += 1
            
            r += 1 # Luôn tăng r ở cuối vòng lặp
            
        return False