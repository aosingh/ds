from typing import List

class FenwickTree:
    """
    Let f be some reversible function and A be an array of integers of length N.

    Fenwick tree is a data structure which:
        1. Calculates the value of the function f in a given range [l:r] in O(logn) time.
        2. Updates the value of an element of A in O(logn) time.
        3. Requires 0(N) memory.
        4. Easy to code especially in multidimensional array.

    Fenwick Tree is also called as Binary Indexed Tree or BIT

    Given an array A[0:N-1] as input, fenwick tree is just an array T[0:N-1] where each of the elements
    is equal to
                f(A[g(i): i])

    here g is some function which satisfies 0 <= g(i) <= i


    Approach: Consider an example for the sum of elements in the range A[0:r]

    def sum(int r):
        # jumps in the direction of decreasing indices.
        res = 0
        while r >= 0:
            res += t[r]
            r = g(r) - 1
        return res

    The function sum works as follows
    1. First it adds the sum of the range [g(r):r] = t[r] to the result
    2. Then it jumps to the range [g(g(r) - 1):g(r)-1] and adds this to the result
    3. And so on until it jumps from [0:g(g(...g(r) - 1 ... -1)-1)] to [g(-1):-1] and this is where the sum function stops
       working.


    def increase(int i, int delta):
        # jumps in the direction of increasing indices
        for all j with g(j) <= i <= j:
            t[j] += delta

    The function inc works as follows:
    1. sums of the ranges that satisfy the condition g(j) <= i <= j are increased by delta i.e. t[j] += delta. Therefore
       we updated all elements of T that correspond to the ranges in which Ai lies.

    The complexity of the methods depends on the choice of the function g(i). For example if g(i) = 0 then we
    store the prefix sums [0:i] in the tree. This gives us constant time for sum, but updates will be slower.

    The clever part done by Fenwick is in choosing this function which allowed O(logn) time for both the methods.

    DEFINITION of g(i)

    g(i) <= j <= i

    We replace all trailing 1 bits in the binary representation of i with 0 bits.

    g(11) = g(1011) = 1000 = 8
    g(12) = g(1100) = 1100 = 12
    g(13) = g(1101) = 1100 = 12

    Using a simple bitwise technique, we can achieve this. g(i) = i & i+1

    Now, how to iterate over all the j's such that g(j) <= i <= j
    To do this, we start with i and flip the last unset bit.


    """
    def __init__(self,
                 nums: List[int]):
        self.tree = [0] * len(nums)
        for i, x in enumerate(nums):
            self.add(i, x)
        print(self.tree)


    def add(self, i: int, delta: int):
        # Increasing indices.
        if i < 0 or i >= len(self.tree):
            raise IndexError(f"Invalid index {i}")
        n = len(self.tree)
        while i < n:
            self.tree[i] += delta
            i = i | i + 1


    def sum(self, r:int):
        # Decreasing indices.
        ret = 0
        while r >= 0:
            ret += self.tree[r]
            r = (r & (r+1))-1 # g(r) -1
        return ret

    def range_sum(self, l, r):
        return self.sum(r) - self.sum(l)



if __name__ == '__main__':
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    ft =FenwickTree(nums=nums)
    print(ft.sum(8))
    print(ft.range_sum(0, 8))


