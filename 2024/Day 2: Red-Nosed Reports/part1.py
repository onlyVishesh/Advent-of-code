import fileinput

# Read and parse reports
reports = []
for line in fileinput.input(files='test cases.txt'):
    reports.append(list(map(int, line.strip().split())))

def is_safe(diffs):
    if diffs[0] > 0:
        sign = "positive"
    elif diffs[0] < 0:
        sign = "negative"
    else:
        return False 

    for diff in diffs:
        if diff >= 0 and sign == "negative":
            return False
        if diff <= 0 and sign == "positive":
            return False
        if abs(diff) > 3:
            return False
    return True


# Count safe reports
safe_reports = 0
for report in reports:
    # Calculate differences for the original report
    diffs = [report[i] - report[i - 1] for i in range(1, len(report))]
    if is_safe(diffs):
        safe_reports += 1

print(safe_reports)
