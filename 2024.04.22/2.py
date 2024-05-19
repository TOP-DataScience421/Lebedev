def taxi_cost(distance: int, waiting_time: int = 0) -> int | None:
    total_price = 0
    base_price = 80
    cost_per_minute = 3
    cost_per_meter = 6
    
    if distance < 0 or waiting_time < 0:
        return None
    
    if distance == 0:
        total_price = base_price * 2 + waiting_time * cost_per_minute
        return round(total_price)

    total_price = base_price + (distance / 150) * cost_per_meter + waiting_time * cost_per_minute
    
    return round(total_price)
    
# >>> print(taxi_cost(-300))
# None
# >>> taxi_cost(1500)
# 140
# >>> taxi_cost(2560)
# 182
# >>> taxi_cost(0, 5)
# 175
# >>> taxi_cost(42130, 8)
# 1789
# >>>