class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cycle = 0

        map_count = Counter(tasks)  
        max_heap = []
        for k,v in map_count.items():
            heapq.heappush(max_heap, (-v, k))

        cooldown = {}
        map_value = {}
        while len(max_heap) > 0 or len(cooldown) > 0:
            cycle += 1 
            if len(max_heap) >0 :
                pop_value = heapq.heappop(max_heap)
                cur_val = pop_value[0] + 1
                if cur_val < 0 :
                    cooldown[pop_value[1]] = n + 1
                    map_value[pop_value[1]] = cur_val 
            for k,v in list(cooldown.items()):
                cur = v - 1 
                if cur == 0:
                    del cooldown[k]
                    heapq.heappush(max_heap, (map_value[k], k))
                else:
                    cooldown[k] = cur
                
        return cycle





