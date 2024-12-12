def get_factors(n):
    """Efficiently find all factors of a number."""
    factors = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
    return sorted(list(factors))

def solve_buzz_day_sale(N, item_ids, item_costs, budget):
    if not item_ids or not item_costs or N == 0 or budget <= 0:
        return 0, 0
    
    item_map = {item_ids[i]: (item_costs[i], i) for i in range(N)}
    
    max_free_items = 0
    max_free_worth = 0
    
    factor_cache = {}
    
    for buy_id in item_ids:
        if item_map[buy_id][0] > budget:
            continue
        
        if buy_id not in factor_cache:
            factor_cache[buy_id] = set(get_factors(buy_id))
        
        max_qty = budget // item_map[buy_id][0]
        
        for qty in range(1, max_qty + 1):
            total_cost = qty * item_map[buy_id][0]
            
            free_items = []
            for potential_free_id in item_ids:
                if (potential_free_id != buy_id and 
                    potential_free_id in factor_cache[buy_id]):
                    free_items.append(potential_free_id)
            
            free_worth = sum(item_map[free_id][0] * qty for free_id in free_items)
            free_count = len(free_items) * qty

            if free_count > max_free_items or \
               (free_count == max_free_items and free_worth > max_free_worth):
                max_free_items = free_count
                max_free_worth = free_worth
    
    return max_free_items, max_free_worth

def main():
    try:
        N = int(input())
        
        item_ids = list(map(int, input().split()))
        
        item_costs = list(map(int, input().split()))
        
        budget = int(input())
        
        if len(item_ids) != N or len(item_costs) != N:
            print("0 0")
            return
        
        result = solve_buzz_day_sale(N, item_ids, item_costs, budget)
        print(*result, end="")
    
    except (ValueError, IndexError) as e:
        print("0 0")

if __name__ == '__main__':
    main()