class MyCalendar:

    def __init__(self):
        self.queue = []

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.queue:
            self.queue.append([startTime,endTime])
            return True
        for start,end in self.queue:
            if not(startTime >= end or endTime <= start):
                return False
        
        self.queue.append([startTime,endTime])
        return True
            

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)