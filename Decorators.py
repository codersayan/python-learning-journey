import time

def execution_time_logger(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@execution_time_logger
def sample_function(n):
    return sum(i for i in range(n))

# Test the decorator
sample_function(1000000)
