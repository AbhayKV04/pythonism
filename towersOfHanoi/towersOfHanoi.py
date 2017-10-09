def printMove(fr, to):
    print("Move from " + str(fr) + " to " + str(to))

def towersOfHanoi(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        towersOfHanoi(n - 1, fr, spare, to)
        towersOfHanoi(1, fr, to, spare)
        towersOfHanoi(n - 1, spare, to, fr)

n = int(input("Number of discs: "))
towersOfHanoi(n, "S1", "S2", "S3")