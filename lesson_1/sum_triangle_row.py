

def build_triangle_rows(n):
    rows = []
    last_val = 0
    for i in range(1, n+1):
        new_row = []
        for j in range(0, i):
            last_val += 2
            new_row.append(last_val)
        rows.append(new_row)
    return rows

def sum_triangle_row(n):
    rows = build_triangle_rows(n)
    return sum(rows[n-1])

def sum_triangle_row_v2(n):
    # We can picture the rows stacked into a single sequence
    # (can model as a range with step 2).
    # The length of the list will be equal to the sum of ints 1..n
    # We want to sum the last n elements of the list.

    # Figure out length of the list we need:
    # This is a standard formula for sum of integers 1 to n
    length_of_stacked_rows = (n * (n + 1)) // 2

    # For the range limit, need to multiply the length by the step size
    # and add 1 as range limit is exclusive.
    STEP = 2
    stacked_rows = range(STEP, (length_of_stacked_rows * STEP) + 1, STEP)

    # Sum the last n elements of this range.
    return sum(stacked_rows[-n:])

print(sum_triangle_row_v2(3))
