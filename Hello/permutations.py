# all permutations of ABC
# start with  AB => BA swap and iteration
# iteration is still faster!

def permute(string, pocket=""):
    if len(string) == 0:
        print(pocket)
    else:
        for i in range(len(string)):
            letter = string[i]
            front = string[0:i]
            back = string[i+1:]
            together = front + back
            permute(together, letter + pocket)


print(permute("ABC", ""))

# BCA, CAB, ACB, BAC, ABC, None

# TODO Iteration code here