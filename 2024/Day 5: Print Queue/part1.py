with open("Day 5: Print Queue/test cases.txt", 'r') as file:
    lines = file.readlines()

rules = []
updates = []
for line in lines:
    line = line.strip()
    if "|" in line:  
        rules.append(line)
    elif line:  
        updates.append(list(map(int, line.split(','))))


def is_correct_order(update, rules):
    for rule in rules:
        before, after = map(int, rule.split('|'))
        if before in update and after in update:
            if update.index(before) > update.index(after):
                return False
    return True




middle_page_sum = 0
for update in updates:
    if is_correct_order(update, rules):
        middle_page = update[len(update) // 2]  
        middle_page_sum += middle_page

print(middle_page_sum)

