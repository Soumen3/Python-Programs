# Problem 5: Possible Legal Subsets
# You are given N comma-separated Strings. You need to form all possible legal subsets of these N strings. These subsets will be a combination of zero or more of these N Strings After forming the subsets, they will be ranked in a particular onder. The legal subset formation and ranking logic is as described below
# Rank 1 will always be an empty set
# Next N ranks will be the N Strings that appear in the order they are provided in the input
# After N + 1 ranks, you need to combine N strings such that all legal combinations are formed
# Legal combination simply means that while combinations are formed, the string that appears to the left of a particular string in the input, can never appear to the right of that particular string, when subsets are formed
# A subset with less elements will be ranked higher than a subset with more elements (NOTE-Rank 1 is higher than rank 2)
# Refer Example 2 to get a better understanding of how subsets are formed and ranked
# It is guaranteed that
# N>=1
# All N strings are unique
# Example: you are having an input string “aa,cc,bb” in this string we can see we have three strings which are comma separated. Now from this group of string we have to create all possible subset of strings. 8 subsets can be formed from these strings. And they are as follows:
# {}
# {aa}
# {cc}
# {bb}
# {aa,}
# Note: here we can see the ranks given to the subsets are first by size i.e., the subset with lesser number of strings is ranked higher than the subset with higher size. If the subsets have equal number of strings then, the combination which is formed earlier (by virtue of combining strings in order they appear in input), gets a higher rank.
# For example, rank of su bset (aa,cc) > rank of (aa,bb) because string cc is appearing prior to string bb in the input. Similarly, rank of (cc) > rank of (bb).
# You are provided one rank R and for that you have to print the Rth subset from all legal subsets.
# Constraints:
# 0<N<=10^2
# 0<R<=10^18
# Input
# First line contains an integer N which is number of strings in group.
# Second line contains an integer R, for which you have to find Rth subset from all legal subsets.
# Third line contains N comma-separated strings basis which the subsets should be formed
# Output:
# From all possible legal subsets find the subset whose rank is R
# Time Limit (secs)
# 1
# Input
# 2
# 4
# a,b
# Output
# a,b
# Explanation:
# Given that N = 2, given
# Second line: Rank to be find: 4th
# Third line: Given group of strings: a,b
# Possible subsets & Rank
# {}-1
# {a} -2
# {b}-3
# {a, b}-4
# Output – a,b (4th rank corresponds to a,b)


# Solution
from itertools import combinations

class Solution:
    def findRank(self, N, R, String):
        self.String = String.split(',')
        self.N = N
        self.R = R
        self.subsets = [""]
         # Generate all possible subsets
        for i in range(1, N+1):
            for combo in combinations(self.String, i):
                self.subsets.append(','.join(combo))
        # print(self.subsets)

        return self.subsets[R-1]




if __name__ == "__main__":
    N = 2
    R = 4
    String = 'a,b'
    S = Solution()
    print(S.findRank(N, R, String))
    