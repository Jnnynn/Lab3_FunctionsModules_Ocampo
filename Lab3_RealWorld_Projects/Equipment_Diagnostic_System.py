# exercise1.py
import functools

LAST_NAME = "OCAMPO"
SEED_NUM = 9
FAVORITE_ARTIST = "lANA DEL REY"

execution_log = []

def diagnostic_logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        execution_log.append(f"{func.__name__}: {args}")
        return func(*args, **kwargs)
    return wrapper

def process_fault_trace(trace, index=0):
    global recursive_calls
    recursive_calls += 1

    if index >= len(trace):
        execution_log.append(f"base-case reached at index {index}")
        return 0

    current = trace[index]
    execution_log.append(f"call #{recursive_calls}: step {current['step']} = {current['value']}")
    return current["value"] + process_fault_trace(trace, index + 1)

@diagnostic_logger
def generate_readings():
    
    base = (len(LAST_NAME) * SEED_NUM) + len(FAVORITE_ARTIST)
    return [base + 15.2, "BINARY", base - 16.4, 18.7, base * 13.5]
@diagnostic_logger
def validate_reading(reading):
    
    try:
        val = float(reading)
        if val > 150.0:  
            raise ValueError("Reading exceeds maximum sensor capacity threshold.")
        return val, "VALID"
    except (TypeError, ValueError) as err:
        return None, f"INVALID_CRITICAL ({type(err).__name__})"
@diagnostic_logger
def classify_reading(val):
    if val < 40.0:
        return "Low (Sub-optimal)"
    elif val <= 100.0:
        return "Nominal (Safe Execution)"
    else:
        return "High Operational Stress"

if __name__ == "__main__":
    raw_stream = generate_readings()
    valid_data = []
    invalid_count = 0
    classifications = []
    for item in raw_stream:
        clean_val, status = validate_reading(item)
        if status == "VALID":
            valid_data.append(clean_val)
            classifications.append(classify_reading(clean_val))
        else:
            invalid_count += 1
    print("=== ASSESSMENT DATA (EXERCISE 1) ===")
    print(f"Generated Equipment Data: {raw_stream}")
    print(f"Validation Results: {len(valid_data)} Passed | {invalid_count} Failed")
    print(f"Diagnostic Results (Classifications): {classifications}")
    print("Execution log:")
for entry in execution_log:
    print("  -", entry)
    print(f"\nFinal Output: Processing terminated. Core Mean Temp: {sum(valid_data)/len(valid_data):.2f}°C")