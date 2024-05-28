import time

def linearCongruentialGenerator(modulus, a, c, seed):
    while True:
        seed = (a * seed + c) % modulus
        yield seed


def generateRandomList(n : int):
    maxVal = 2**n - 1
    requiredNo = 2*n

    modulus = maxVal + 1  # The modulus for the LCG
    a = 1103515245  # Multiplier
    c = 12345  # Increment
    seed = int(time.time())  # Use current time as the seed
    rng = linearCongruentialGenerator(modulus, a, c, seed)

    uniqueIntSet = set()
    while len(uniqueIntSet) < requiredNo:
        num = next(rng)
        if num > 0:  # Ensure it is a positive integer
            uniqueIntSet.add(num)
    uniqueIntList = list(uniqueIntSet)

    k = next(rng)
    while k == 0 or k > maxVal: # Ensure 0 < k <= 2^n-1
        k = next(rng)

    return k, uniqueIntList

def searchK(k: int, list_n: list[int]):
    stepCount = 0
    for each in list_n:
        stepCount += 1
        if k == each:
            return True, stepCount
    return False, stepCount


def lessThanK(k: int, list_n: list[int]):
    stepCount = 0
    list_nk = list()
    for each in list_n:
        stepCount += 1
        if each < k:
            list_nk.append(each)
    return list_nk, stepCount


# Example:
listN = generateRandomList(5)
print(listN)
# k_exist = searchK(k, list_n)
# list_nk = lessThanK(k, list_n)
# print(k, list_n)
# print(k_exist)
# print(list_nk)

# Output
# 5, [3, 2, 5, 1, 6, 7]
# (True, 3)
# ([2, 1], 6)