# Problem 1 : Date Time

# Arun and his sister Usha are challenging each other with some mathematical puzzles. Usha, the cleverer one, 
# has come up with the idea of Giving Arun 12 distinct digits from 0 to 9, and have him from the largest date 
# time in 2018 with them. Arun is a little nervous, and asks you to help him with a computer program.
# Usha will give Arun 12 distinct digits. He needs to create a date time combination in the year 2018: 
# the date in the MM/DD form (all four digits must be present), and the time in the format HH:MM (all 
# four digits must be present). The date may be from 01/01 to 12/31 and the time may be from 00:00 to
# 23:59 (in the 24 hour format).

# The digits provided may be used only once in the answer that Arun gives.
# If more than one date time combination may be formed, Arun needs to give the latest valid date time possible
# in the year 2018.
# Constraints
# Single digits (any of 0-9)

# Input Format

# A line consisting of a sequence of 12 (not necessarily distinct) single digits (any of 0-9) separated by commas. 
# The sequence will be non-decreasing.

# Output

# The maximum possible valid date time in the year 2018. The output must be in the format
# MM/DD HH:MM
# If no date time can be constructed, the output should be 0.

# Example1 :

# Input 0,0,1,2,2,2,3,5,9,9,9,9
# Output 12/30 22:59

# Explanation:

# The 12 digits to be used by Arun are given.
# The maximum valid date time using only the digits given, and with each digit used at most once is 12/30 22:59
# This is the output.

# Example 2

# Input:  3,3,3,3,3,3,3,3,3,3,3,3
# Output: 0

# Explanation

# As no digit less than 3 is present in the input, a valid month cannot be formed. Hence no valid Date time can be 
# formed with the input digits.



# Solution:
from itertools import permutations

class Solution:

    def __init__(self):
        self.days_in_month = {
            1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
            7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
        }

    def find_maximum_date_and_time(self, digits):
        valid_dates_times = []

        # Generate all permutations of length 8 (for month, day, hour, and minute)
        for perm in permutations(digits, 8):
            month_first, month_second, day_first, day_second, hour_first, hour_second, minute_first, minute_second = perm

            # Form the month, day, hour, and minute from the digits
            month = month_first * 10 + month_second
            day = day_first * 10 + day_second
            hour = hour_first * 10 + hour_second
            minute = minute_first * 10 + minute_second

            # Check if the month is valid (between 1 and 12)
            if 1 <= month <= 12:
                max_days = self.days_in_month[month]  # Get max days in the month

                # Check if the day is valid for the given month
                if 1 <= day <= max_days:
                    # Check if the hour and minute are valid
                    if 0 <= hour <= 23 and 0 <= minute <= 59:
                        valid_dates_times.append((month, day, hour, minute))

        # If valid dates and times exist, find the maximum one
        if valid_dates_times:
            max_date_time = max(valid_dates_times)
            return f"{max_date_time[0]:02d}/{max_date_time[1]:02d} {max_date_time[2]:02d}:{max_date_time[3]:02d}"
        else:
            return 0





if __name__ == "__main__":
    data = [0, 0, 1, 2, 2, 2, 3, 5, 9, 9, 9, 9]
    s = Solution()
    print(s.find_maximum_date_and_time(data))