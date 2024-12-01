import fileinput

# Read and parse reports
reports = []
for line in fileinput.input(files='test cases.txt'):
    reports.append(list(map(int, line.strip().split())))

# Function to determine if a list of differences is safe
def is_safe(diffs):
    if diffs[0] > 0:
        sign = "positive"
    elif diffs[0] < 0:
        sign = "negative"
    else:
        return False  # First difference can't be zero

    for diff in diffs:
        if diff >= 0 and sign == "negative":
            return False
        if diff <= 0 and sign == "positive":
            return False
        if abs(diff) > 3:
            return False
    return True

# Function to check if a report becomes safe with one level removed
def is_safe_with_dampener(report):
    for i in range(len(report)):
        # Remove one level and recalculate differences
        modified_report = report[:i] + report[i + 1:]
        diffs = [modified_report[j] - modified_report[j - 1] for j in range(1, len(modified_report))]
        if is_safe(diffs):
            return True
    return False

# Count safe reports
safe_reports = 0
for report in reports:
    # Calculate differences for the original report
    diffs = [report[i] - report[i - 1] for i in range(1, len(report))]
    if is_safe(diffs) or is_safe_with_dampener(report):
        safe_reports += 1

print(safe_reports)
