print("Matriz Leida:")
for line in open("matriz.txt", "r").readlines(): print line.split()


def caracol(array):
    if not len(array): return []
    return array[0] + \
           [row[-1] for row in array[1:]] + \
           array[-1][-2::-1] + \
           [row[0] for row in array[-2:0:-1]] + \
           caracol([row[1:-1] for row in array[1:-1]])

print("Recorrido Caracol: ")
print caracol([x.split() for x in open("matriz.txt").readlines()])

