with open("Day 5: If You Give A Seed A Fertilizer/test cases.txt") as fin:
    lines = fin.read().strip().split("\n")

seeds = list(map(int, lines[0].split(" ")[1:]))

# Generate all the mappings
maps = []

i = 2
while i < len(lines):
    maps.append([])

    i += 1
    while i < len(lines) and not lines[i] == "":
        disStart, disEnd, rangeBw = map(int, lines[i].split())
        maps[-1].append((disStart, disEnd, rangeBw))
        i += 1

    i += 1


def findLoc(seed):
    currentSeed = seed

    for m in maps:
        for disStart, disEnd, rangeBw in m:
            if disEnd <= currentSeed < disEnd + rangeBw:
                currentSeed = disStart + (currentSeed - disEnd)
                break

    return currentSeed


locs = []
for seed in seeds:
    locs.append(findLoc(seed))

print(min(locs))