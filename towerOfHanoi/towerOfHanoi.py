def printMove(fr, to):
    print("Move from " + str(fr) + " to " + str(to))

def towerOfHanoi(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        towerOfHanoi(n - 1, fr, spare, to)
        towerOfHanoi(1, fr, to, spare)
        towerOfHanoi(n - 1, spare, to, fr)

n = int(input("Number of discs: "))
towerOfHanoi(n, "S1", "S2", "S3")