
def max_expertise_team(n, c, conflicts, expertise):
    # Build conflict map for each employee
    conflict_map = {i: set() for i in range(n)}  # Employees are 0-indexed internally

    # Populate conflict relationships
    for u, v in conflicts:
        conflict_map[u - 1].add(v - 1)  # Convert to 0-indexed
        conflict_map[v - 1].add(u - 1)  # Convert to 0-indexed

    # Combine employees and their expertise into a list of tuples
    employees = [(expertise[i], i) for i in range(n)]

    # Sort employees based on expertise in descending order
    employees.sort(reverse=True, key=lambda x: x[0])  # Sort by expertise descending

    max_expertise = 0
    selected_employees = set()  # To track employees already in the team

    # Iterate through sorted employees
    for exp, emp in employees:
        # Check if this employee conflicts with any already selected employee
        if not any(conflict in selected_employees for conflict in conflict_map[emp]):
            # No conflicts, so add this employee's expertise
            max_expertise += exp
            # Mark this employee as selected
            selected_employees.add(emp)

    return max_expertise

n, c = map(int, input().split())  # n = number of employees, c = number of conflicts
conflicts = [tuple(map(int, input().split())) for _ in range(c)]  # conflict pairs
expertise = list(map(int, input().split()))  # expertise values of employees


# Solve the problem
result = max_expertise_team(n, c, conflicts, expertise)
print(result)
