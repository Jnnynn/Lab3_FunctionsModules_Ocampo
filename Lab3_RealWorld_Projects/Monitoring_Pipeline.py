# exercise3.py
import telemetry_generator as core

LAST_NAME = "OCAMPO"
SEED_NUM = 9
FAVORITE_ARTIST = "LANA DEL REY"


if __name__ == "__main__":
    stream = core.telemetry_generator(LAST_NAME, SEED_NUM, FAVORITE_ARTIST)
    scale_transformer = lambda x: float(x) * 1.05

    processed_count = 0
    valid_count = 0
    invalid_count = 0
    anomalies_detected = 0
    execution_log = []

    execution_log.append("Initialization of Pipeline Monitor Sequence.")

    for item in stream:
        processed_count += 1
        try:
            if isinstance(item, str):
                raise TypeError("Alpha values found in stream matrix.")

            clean_val = scale_transformer(item)
            valid_count += 1
            execution_log.append(f"Signal stream item {processed_count} verified: {clean_val:.2f}")

            if clean_val > 120.0:
                anomalies_detected += 1
                execution_log.append(f"  [ANOMALY TRIGGERED] Node item value {clean_val:.2f} bounds breached.")
                resolved_val, iterations = core.recursive_anomaly_analysis(clean_val)
                execution_log.append(f"  [ANOMALY RESOLVED] Stabilized to {resolved_val:.2f} after {iterations} recursions.")

        except (TypeError, ValueError) as err:
            invalid_count += 1
            execution_log.append(f"Skipped corrupt stream artifact at index {processed_count}: {err}")

    status_metric = "NOMINAL" if anomalies_detected < 2 else "WARNING: MAINTENANCE REQUIRED"

    print("=== ASSESSMENT DATA (EXERCISE 3) ===")
    print(f"Student-Specific Inputs: Surname={LAST_NAME} | Seed={SEED_NUM} | Artist={FAVORITE_ARTIST}")
    print(f"Generated Telemetry Data Metrics: Processed total of {processed_count} data nodes.")
    print(f"Valid/Invalid Results: {valid_count} Staged Valid | {invalid_count} Dropped Corrupt")
    print(f"Processed Results & Recursive Analysis Summary: Handled {anomalies_detected} out-of-bounds metrics.")
    print(f"Overall Equipment Status: {status_metric}")
    print("\nExecution Log:")
    for line in execution_log:
        print(f"  {line}")
    print("\nFinal Output: Core pipeline loop safely evaluated and finalized.")