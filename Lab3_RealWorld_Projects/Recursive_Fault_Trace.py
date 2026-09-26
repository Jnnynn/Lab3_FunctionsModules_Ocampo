LAST_NAME = "OCAMPO"
SEED_NUM = 9
FAVORITE_ARTIST = "lANA DEL REY"

recursive_calls = 0
fault_trace = []


def generate_fault_code(last_name, seed_num, favorite_artist):
    """Generate a unique numeric fault code from student data."""
    name_value = sum(ord(char) for char in last_name.upper())
    artist_value = sum(ord(char) for char in favorite_artist.upper() if char.isalpha())
    fault_code = ((len(last_name) * seed_num) + name_value + artist_value) % 250 + 50
    return fault_code


def trace_fault(fault_code, level=1):
    """Recursively trace the fault until it reaches the termination condition."""
    global recursive_calls

    recursive_calls += 1
    current_step = f"Level {level}: fault code = {fault_code} -> diagnostic in progress"
    fault_trace.append(current_step)
    print(current_step)

    if fault_code <= SEED_NUM:
        base_step = (
            f"Base condition reached at Level {level}: code {fault_code} is below the "
            "fault threshold. Diagnostic sequence complete."
        )
        fault_trace.append(base_step)
        print(base_step)
        return f"Final Result: Fault stabilized at {fault_code}."

    next_code = fault_code - (SEED_NUM + (level % 3))
    if next_code <= 0:
        next_code = 0

    print(f"  Next step: {fault_code} -> {next_code}")
    return trace_fault(next_code, level + 1)


if __name__ == "__main__":
    fault_code = generate_fault_code(LAST_NAME, SEED_NUM, FAVORITE_ARTIST)

    print("=" * 60)
    print("RECURSIVE FAULT TRACE")
    print(f"Student surname: {LAST_NAME}")
    print(f"SEED_NUM: {SEED_NUM}")
    print(f"Favorite artist: {FAVORITE_ARTIST}")
    print(f"Generated fault code: {fault_code}")
    print("=" * 60)

    final_result = trace_fault(fault_code, 1)

    print("\nComplete diagnostic sequence:")
    for step in fault_trace:
        print(f"  - {step}")

    print(f"\nRecursive calls performed: {recursive_calls}")
    print(final_result)
    print("=" * 60)
