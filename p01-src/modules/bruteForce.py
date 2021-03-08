def closestPointsBF(data):
    minimum = 0
    c1 = []
    c2 = []
    first = True
    for i in range(len(data)):
        for j in range(len(data)):
            if i != j:
                if first == True:
                    minimum = distance(data[i], data[j])
                    c1 = data[i]
                    c2 = data[j]
                    first = False
                else:
                    current = distance(data[i], data[j])
                    if current < minimum:
                        minimum = current
                        c1 = data[i]
                        c2 = data[j]
    return minimum, c1, c2


def distance(p1, p2):
    total = 0
    total += (p1[0] - p2[0]) ** 2
    total += (p1[1] - p2[1]) ** 2
    return (total ** (1/2))
