def carFleet(target, position, speed):
    if len(position) == 1:
        return 1

    pairs = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)

    fleets = []
    for p, s in pairs:
        fleets.append((target-p)/s)
        if len(fleets) > 1 and fleets[-1] <= fleets[-2]:
            fleets.pop()

    return len(fleets)


print(carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))

print(carFleet(100, [0, 2, 4], [4, 2, 1]))
