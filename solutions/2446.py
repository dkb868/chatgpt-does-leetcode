"""solve in python3, just give a code block.

You are given two arrays of strings that represent two inclusive events that happened on the same day, event1 and event2, where:

event1 = [startTime1, endTime1] and
event2 = [startTime2, endTime2].
Event times are valid 24 hours format in the form of HH:MM.

A conflict happens when two events have some non-empty intersection (i.e., some moment is common to both events).

Return true if there is a conflict between two events. Otherwise, return false.

 

Example 1:

Input: event1 = ["01:15","02:00"], event2 = ["02:00","03:00"]
Output: true
Explanation: The two events intersect at time 2:00.
Example 2:

Input: event1 = ["01:00","02:00"], event2 = ["01:20","03:00"]
Output: true
Explanation: The two events intersect starting from 01:20 to 02:00.
Example 3:

Input: event1 = ["10:00","11:00"], event2 = ["14:00","15:00"]
Output: false
Explanation: The two events do not intersect.
 

Constraints:

evnet1.length == event2.length == 2.
event1[i].length == event2[i].length == 5
startTime1 <= endTime1
startTime2 <= endTime2
All the event times follow the HH:MM format.

---

class Solution:
  def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
"""


class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        # Convert start and end times to minutes
        start1, end1 = self.convertToMinutes(event1)
        start2, end2 = self.convertToMinutes(event2)


        # Check if there is any overlap between the two events
        if start1 <= start2 <= end1 or start1 <= end2 <= end1 or start2 <= start1 <= end2 or start2 <= end1 <= end2:
            return True
        return False


    def convertToMinutes(self, event: List[str]) -> Tuple[int, int]:
        # Convert HH:MM to minutes
        hours, minutes = event[0].split(':')
        start = int(hours) * 60 + int(minutes)
        hours, minutes = event[1].split(':')
        end = int(hours) * 60 + int(minutes)
        return start, end


