class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cycle = 0

        map_count = Counter(tasks)  
        max_heap = []
        for k,v in map_count.items():
            heapq.heappush(max_heap, (-v, k))

        cooldown = []
        while len(max_heap) > 0 or len(cooldown) > 0:
            cycle += 1 
            if len(max_heap) >0 :
                pop_value = heapq.heappop(max_heap)
                cur_val = pop_value[0] + 1
                if cur_val < 0 :
                    cooldown.append([pop_value[1],cur_val, cycle + n])
            if len(cooldown) > 0 and cooldown[0][2] == cycle:
                v = cooldown.pop(0)
                heapq.heappush(max_heap, (v[1], v[0]))
                
        return cycle





