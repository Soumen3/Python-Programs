# In the world war, the denizens of the Marvel Universe are forced to pick sides when KingA and
# KingB come to blows over ideological differences. The government decides to push for the Hero
# Registration Act, a law that limits a hero’s actions. This results in a division in The
# Soldiers.KingB stands with this Act, claiming that their actions must be kept in check
# otherwise cities will continue to be destroyed, but KingA feels that saving the world is daring
# enough and that they cannot rely on the government to protect the world. And here the civil
# war begins. They are trying make their team stronger by adding more Soldiers to their team.
# There are N Soldiers lined up.

# Rules to add avenger to their team-
# É Any team can start first. But they will alternatively onlyÇ

# É They can select avenger from any side. But if they start from one side they can’t move to
# other side in current chance.

# Courses Screenshots
# from Courses 200+

# * They will stop only when all the Soldiers are part of either side3
# * Every Avenger has a power associated with hi
# * There are some spurious Soldiers who will decrease the overall power of the team.
# Constraints
# 1<= N <= 10^6
# -10^9 <= p[i] <= 10^9
# Both teams will select players optimally. Find the difference of powers of the two teams
# Input
# First line contains an integer denoting the number of Soldiers(N).
# Next lines contain N space separated values denoting power of every avenger(P[i]).
# Output
# Print the difference of the powers of teams –
# Time Limit (secs) 1
# Examples :
# Input
# 5
# 2 -7 8 -1 20
# Output
# 2
# Input
# 4
# 4 -21 30 31
# Output
# 24
# Input
# 6
# 1 5 -2 22 33 -7
# Output
# 4
# Input
# 4
# 2 -1 -2 -3
# Output
# 6










N = int(input())
powers = list(map(int, input().split()))

team_a_power = 0
team_b_power = 0

# Sort the powers
powers.sort(key=lambda x: (abs(x), -x), reverse=True)
print(powers)

# Assign Avengers to teams alternatively
ironman_turn = True

for power in powers:
    if ironman_turn:
        team_a_power += power
    else:
        team_b_power += power
    ironman_turn = not ironman_turn

power_difference = abs(team_a_power - team_b_power)
print(power_difference)