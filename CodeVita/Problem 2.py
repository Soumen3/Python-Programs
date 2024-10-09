# Problem 2 : Digital Time
 
# The objective is to form the maximum possible time in the HH:MM:SS format using any six of nine given single digits
# (not necessarily distinct)
# Given a set of nine single (not necessarily distinct) digits, say 0, 0, 1, 3, 4, 6, 7, 8, 9, it is possible to 
# form many distinct times in a 24 hour time format HH:MM:SS, such as 17:36:40 or 10:30:41 by using each of the digits only once. 
# The objective is to find the maximum possible valid time (00:00:01 to 24:00:00) that can be formed using some six of the nine  digits exactly
# once. In this case, it is 19:48:37.

# Input : A line consisting of a sequence of 9 (not necessarily distinct) single digits (any of 0-9) separated by commas. The sequence will
# be non-decreasing

# Output : The maximum possible time in a 24 hour clock (00:00:01 to 24:00:00) in a HH:MM:SS form that can be formed by using some
# six of the nine given digits (in any order) precisely once each. If no combination of any six digits will form a valid time, the
# output should be the word Impossible

# Example 1
# Input: 0,0,1,1,3,5,6,7,7
# Output: 17:57:36

# Explanation:

# The maximum valid time in a 24 hour clock that can be formed using some six of the 9 digits precisely once is 17:57:36

# Example 2

# Input: 3,3,3,3,3,3,3,3,3
# Output: Impossible

# Explanation:

# No set of six digits from the input may be used to form a valid time.

from itertools import permutations

class Solution:

    def is_valid_time(self, perm):
        hour_first, hour_second, minute_first, minute_second, second_first, second_second = perm
        hour = hour_first*10 + hour_second
        minute = minute_first*10 + minute_second
        second = second_first*10 + second_second
        if hour < 24 and hour >= 0 and minute < 60 and minute >= 0 and second < 60 and second >= 0:
            return True
        return False
    
    def format_time(self, perm):
        hour_first, hour_second, minute_first, minute_second, second_first, second_second = perm
        return f"{hour_first}{hour_second}:{minute_first}{minute_second}:{second_first}{second_second}"

    def find_maximum_time(self, data):
        self.digits = data
        self.valid_times = []
        # Generate all permutations of length 6 (for hour, minute, and second)
        for perm in permutations(self.digits, 6):
            # Check if the permutation is a valid time
            if self.is_valid_time(perm):
                self.valid_times.append(self.format_time(perm))

        if len(self.valid_times) == 0:  # No valid time found
            return "Impossible"
        else:
            return max(self.valid_times)


if __name__ == "__main__":
    data = [0,0,1,1,3,5,6,7,7]
    s = Solution()
    print(s.find_maximum_time(data))