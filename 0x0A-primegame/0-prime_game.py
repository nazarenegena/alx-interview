#!/usr/bin/python3
"""the prime game.
"""


def isWinner(rounds, nums):
    """function determines the winner of a 
       prime game session with `x` rounds.
    """
    if rounds < 1 or not nums:
        return None
    marias_wins, bens_wins = 0, 0
    """generating primes with a max limit"""
    z = max(nums)
    primes = [True for _ in range(1, z + 1, 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, z + 1, i):
            primes[j - 1] = False
            """filtering the num of primes < z"""
    for _, z in zip(range(rounds), nums):
        primes_count = len(list(filter(lambda rounds: rounds, primes[0: z])))
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1
    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'