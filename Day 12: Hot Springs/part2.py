from functools import cache

with open("Day 12: Hot Springs/test cases.txt") as f:
    lines = f.read().split("\n")


@cache
def solve(springs, m):
    if springs == "":
        return 1 if m == () else 0

    if m == ():
        return 0 if "#" in springs else 1

    tmp = 0

    if springs[0] in ".?":
        tmp += solve(springs[1:], m)

    if springs[0] in "#?":
        enough_springs_to_next_block = len(springs) >= m[0]
        no_workings_springs_in_the_next_block_length = "." not in springs[: m[0]]
        exactly_last_block = m[0] == len(springs)
        not_broken_spring_after_next_block = m[0] < len(springs) and springs[m[0]] != "#"
        good_conditions_for_next_block = exactly_last_block or not_broken_spring_after_next_block

        if (
            enough_springs_to_next_block
            and no_workings_springs_in_the_next_block_length
            and good_conditions_for_next_block
        ):
            tmp += solve(springs[m[0] + 1:], m[1:])

    return tmp


ans = 0
for line in lines:
    springs, m = line.split()
    m = tuple(int(x) for x in m.split(","))

    springs = "?".join([springs] * 5)
    m *= 5

    ans += solve(springs, m)

print(ans)
