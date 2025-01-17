class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #counter
        #maxheap [(freq, A)]
        #time
        #heap not empty
            #curr_time
            #type, time = pop the top element
            # if currtime == time:
            #curr_time = time + n
            #push to heap
        count = Counter(tasks)
        maxHeap = [ -cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        q = deque()
        time = 0
        while maxHeap or q:
            time+=1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time+n])
            while q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time

