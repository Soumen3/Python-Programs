# Problem 6: Seating Arrangement
# You are a caretaker of a waiting room and you have to take care of empty seats such that all the people should sit together. Imagine the seats are in a straight line like in a movie theatre. People are seated on random seats initially. Your task is to make them sit together so that minimum number of people change their position. Also, they can be made to sit together in many ways. Find the number of ways you can make them sit together by requiring only minimal people movement.
# “E” depicts an empty seat and “O” depicts an occupied seat. Input will be given in the form of a string.
# Example: OEOEO
# As we can see, only seat number 1, 3, 5 are occupied and 2 and 4 are empty.
# Case 1: If we move 5th person to 2nd position, they can all be together with only one person moving his/her place.
# Case 2: If we movement 1st person to 4th position, they can all be together with only one person moving his/her place.
# They can all be together with only one movement and this can be done in 2 ways. Print the minimum number of movements required and the number of ways this minimum movement can help achieve the objective.
# Note: If they are already sitting together, Print “00” as output.
# Constraints
# 0 <N <= 100000
# Input
# First line contains an integer N which depicts the number of seats
# Second line contains N characters each of which are either “O” or “E”. “O” denotes an occupied seat and “E” denotes an empty seat.
# Output
# Print minimum number of movements required and the number of ways in which all people can be made to sit together without exceeding minimum number of movements by space
# Time Limit (secs)
# 1
# Examples
# Input
# 5
# OEOEO
# Output
# 1 2
# Explanation:
# Given data of 5 seats in the queue,
# Seat number 2 and 4 are unoccupied and all the other seats are occupied.
# We can make them sit together by moving only one person near to the other. It can be done in 2 ways:
# OOOEE (Moving 4 person to 2º position)
# EE000 (Moving 1 person to 4 position)



# Solution

class Solution:
    def seatingArrangement(self, N, seats):
        occupied = seats.count("O")
        if occupied == 0 or occupied == len(seats):
            return 0, 0
        empty_counts = []
        current_available = 0
        for seat in seats:
            if seat == "E":
                current_available += 1
            else:
                if current_available > 0:
                    empty_counts.append(current_available)
                current_available = 0
        min_empty_seats = min(empty_counts)
        min_moves = min_empty_seats - 1
        ways = empty_counts.count(min_empty_seats)
        return min_moves * occupied +1, ways





if __name__ == '__main__':
    N = 5
    seats = "OEOEO"
    s = Solution()
    print(s.seatingArrangement(N, seats))