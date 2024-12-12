def maxSubstringRemoval(substrings, main_string):
    # Memoization to store previously computed states
    memo = {}
    
    def removeSubstring(s, sub):
        """Remove first occurrence of substring."""
        idx = s.find(sub)
        return s[:idx] + s[idx+len(sub):] if idx != -1 else s
    
    def solved(current_string, remaining_subs):
        key = (current_string, tuple(sorted(remaining_subs)))
        
        if key in memo:
            return memo[key]
        
        max_removals = 0
        
        for i, sub in enumerate(remaining_subs):
            if sub in current_string:
                new_subs = remaining_subs[:i] + remaining_subs[i+1:]
                
                new_string = removeSubstring(current_string, sub)
                
                current_removals = 1 + solved(new_string, new_subs)
                
                max_removals = max(max_removals, current_removals)
        
        memo[key] = max_removals
        return max_removals
    
    return solved(main_string, substrings)

def main():
    N = int(input())
    
    substrings = input().split()
    
    main_string = input()

    
    print(maxSubstringRemoval(substrings, main_string))


if __name__ == '__main__':
    main()