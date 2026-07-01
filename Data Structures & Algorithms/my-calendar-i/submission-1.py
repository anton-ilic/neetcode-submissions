class MyCalendar:
    
    def __init__(self):
        self.calendar = []

    def book(self, startTime: int, endTime: int) -> bool:
        inserted = False
        for i in range(0, len(self.calendar)):
            item = self.calendar[i]
            current_start = item[0]
            current_end = item[1] # exclusive
            
            # THIS INTERVAL IS SMALLER; CONTINUE
            if current_end <= startTime:
                continue
            # THIS INTERVAL IS BIGGER; INSERT BEFORE
            elif current_start >= endTime: # end time is exclusive
                # insert here; o(n)
                self.calendar.insert(i, [startTime, endTime])
                inserted = True
                break
            else:
                # check if CONTAINED WITHIN 
                return False

        # optimizations TODO: merge intervals
        if not inserted:
            self.calendar.append([startTime, endTime])
        return True


        



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)