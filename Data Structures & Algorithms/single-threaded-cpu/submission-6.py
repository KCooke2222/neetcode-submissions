class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # sort tasks by enqueue time, maintain current time
            # check this before adding to heap after a task is processed
        # store in min heap
        # pop from min heap, process and increment time


        time = 0
        tasks = [(task[0], task[1], i) for i, task in enumerate(tasks)]
        tasks.sort(reverse=True) # stack
        taskHeap = []
        res = []

        while tasks or taskHeap:
            # adding new tasks
            while tasks and tasks[-1][0] <= time:
                task = tasks.pop()
                heapq.heappush(taskHeap, (task[1], task[0], task[2]))

            # if no tasks ready at time idle until next task
            if not taskHeap:
                task = tasks.pop()
                time = task[0]
                heapq.heappush(taskHeap, (task[1], task[0], task[2]))

            run = heapq.heappop(taskHeap)
            time += run[0]

            res.append(run[2])

        
        return res