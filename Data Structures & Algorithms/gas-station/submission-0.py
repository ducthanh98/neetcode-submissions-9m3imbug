class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        total_tank = 0
        curr_tank = 0
        start = 0
        
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total_tank += diff
            curr_tank += diff
            
            # Nếu hết xăng tại trạm i, thử xuất phát lại từ trạm i + 1
            if curr_tank < 0:
                start = i + 1
                curr_tank = 0
                
        return start if total_tank >= 0 else -1