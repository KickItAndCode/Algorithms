# Program for Tower of Hanoi
# Tower of Hanoi is a mathematical puzzle where we have three rods and n disks. The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:
# 1) Only one disk can be moved at a time.
# 2) Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack i.e. a disk can only be moved if it is the uppermost disk on a stack.
# 3) No disk may be placed on top of a smaller disk.


# Approach :

# Take an example for 2 disks :
# Let rod 1 = 'A', rod 2 = 'B', rod 3 = 'C'.

# Step 1 : Shift first disk from 'A' to 'B'.
# Step 2 : Shift second disk from 'A' to 'C'.
# Step 3 : Shift first disk from 'B' to 'C'.

# The pattern here is :
# Shift 'n-1' disks from 'A' to 'B'.
# Shift last disk from 'A' to 'C'.
# Shift 'n-1' disks from 'B' to 'C'.

# Image illustration for 3 disks :


NUMPEGS = 3


# def computeTowerHanoi(numrings):
#     def computeTowerHanoiSteps(numrings, src, dst, tmp):
#         if numrings > 0:
#             computeTowerHanoiSteps(numrings - 1, src, tmp, dst)
#             pegs[dst].append(pegs[src].pop())
#             results.append([src, dst])
#             computeTowerHanoiSteps(numrings - 1, tmp, dst, src)

#     results = []
#     pegs = [list(reversed(range(1, numrings, +1)))] + [[]
#                                                        for _ in range(1, numrings)]
#     computeTowerHanoiSteps(numrings, 0, 1, 2)
#     return results


# computeTowerHanoi(3)


def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print("Move disk 1 from rod", from_rod, "to rod", to_rod)
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)


# Driver code
n = 4
TowerOfHanoi(n, 'A', 'C', 'B')
# A, C, B are the name of rods
