"""Task 1: Lists and Slicing: Daily Rainfall Records."""

import time
import random

def moving_average_naive(readings, k=7):
    if len(readings) < k:
        return []
    result = []
    for i in range(len(readings) - k + 1):
        window = readings[i:i+k]
        result.append(sum(window) / k)
    return result

def moving_average_running(readings, k=7):
    if len(readings) < k:
        return []
    result = []
    current_sum = sum(readings[:k])
    result.append(current_sum / k)
    for i in range(len(readings) - k):
        current_sum = current_sum - readings[i] + readings[i + k]
        result.append(current_sum / k)
    return result

if __name__ == "__main__":
    random.seed(42)
    rain_year = [random.choice([0.0, 0.0, 2.5, 12.0, 45.5, 0.0, 5.0]) for _ in range(365)]
    
    print(f"Total readings: {len(rain_year)}")
    print(f"readings[7:14] (Week 2): {rain_year[7:14]}")
    print(f"readings[-7:] (Last 7 days): {rain_year[-7:]}")
    print(f"readings[::7] (Weekly sample): {rain_year[::7][:5]} ...")
    
    # Benchmarking
    for size in [365, 36500]:
        data = [random.uniform(0, 50) for _ in range(size)]
        
        start = time.perf_counter()
        moving_average_naive(data)
        t_naive = time.perf_counter() - start
        
        start = time.perf_counter()
        moving_average_running(data)
        t_running = time.perf_counter() - start
        
        print(f"Size {size:6d} | Naive: {t_naive:.6f}s | Running Sum: {t_running:.6f}s")
