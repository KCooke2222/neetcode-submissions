class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # sort from time and heap to time
        # simulate the number of passengers as time increments
        # pop from list as time aligns: add passengers
        # pop to heap as time aligns: remove passengers
        
        
        # remove time tracking to improve performance

        trips.sort(key=lambda trip: trip[1])
        toHeap = []

        time = 0
        passengers = 0
        for trip in trips:
            passengers += trip[0]
            time = trip[1]
            heapq.heappush(toHeap, [trip[2], trip[0], trip[1]])

            while toHeap and toHeap[0][0] <= time:
                trip = heapq.heappop(toHeap)
                passengers -= trip[1]

            if passengers > capacity:
                return False



        return True

