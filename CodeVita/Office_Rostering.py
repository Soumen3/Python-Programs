def solve_rostering(N, friendships, K):
    # Initialize graph of friendships
    graph = [[] for _ in range(N)]
    for u, v in friendships:
        graph[u].append(v)
        graph[v].append(u)
    
    # Initial state: everyone works from office
    current_wfo = [1] * N
    total_rostering = N
    days = 1
    
    while total_rostering < K:
        next_wfo = [0] * N
        
        # Determine next day's work status
        for emp in range(N):
            office_friends = sum(current_wfo[friend] for friend in graph[emp])
            
            # WFO rule: continue if exactly 3 friends worked from office
            if current_wfo[emp] == 1 and office_friends == 3:
                next_wfo[emp] = 1
            # WFH rule: go to office if less than 3 friends worked from office
            elif current_wfo[emp] == 0 and office_friends < 3:
                next_wfo[emp] = 1
        
        # Update rostering value
        total_rostering += sum(next_wfo)
        current_wfo = next_wfo
        days += 1
        
        # Debugging output to trace the computation
        print(f"Day {days}: Current WFO: {current_wfo}, Total Rostering: {total_rostering}")

        # Check if we have reached or exceeded K
        if total_rostering >= K:
            break
    
    return days

def main():
    N, M = map(int, input().split())
    friendships = [tuple(map(int, input().split())) for _ in range(M)]
    K = int(input())
    
    print(solve_rostering(N, friendships, K))

if __name__ == "__main__":
    main()