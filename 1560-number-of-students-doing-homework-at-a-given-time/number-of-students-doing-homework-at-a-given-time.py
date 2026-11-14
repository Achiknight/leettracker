class Solution:
    def busyStudent(self, startTime: list[int], endTime: list[int], queryTime: int) -> int:
        study = 0

        for i in range(len(startTime)):
            if queryTime >= startTime[i] and queryTime <= endTime[i]:
                study += 1
        return study