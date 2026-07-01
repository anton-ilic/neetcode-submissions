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
                break
            else:
                # check if CONTAINED WITHIN 
                return False

        
        if not inserted:
            self.calendar.append([startTime, endTime])
        return True

            
            # 1. event is before current_start
            # 2. event is after current_end
            # 3. WITHIN the current_start and current_end ==> False

        



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)