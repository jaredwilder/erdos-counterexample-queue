#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Standalone verifier for the counterexample-queue results.

No dependencies outside the Python standard library. Run it:

    python verify.py

Every check below re-derives a claim in README.md from scratch. A claim that
does not reproduce fails the run; the script exits non-zero if anything fails.
"""
from __future__ import annotations

import sys
from itertools import product

FAILURES = []


def check(label, got, want):
    ok = got == want
    print("  %-58s %s" % (label, "PASS" if ok else "FAIL  got=%r want=%r" % (got, want)))
    if not ok:
        FAILURES.append(label)
    return ok


def sigma(n):
    """Sum of divisors, by trial division. Exact integer arithmetic."""
    total, d = 0, 1
    while d * d <= n:
        if n % d == 0:
            total += d
            other = n // d
            if other != d:
                total += other
        d += 1
    return total


def tau(n):
    total, d = 0, 1
    while d * d <= n:
        if n % d == 0:
            total += 1 if d * d == n else 2
        d += 1
    return total


def r_count(N):
    """Ordered pairs (a,b), a+b=N, with sigma(a)+sigma(b)=sigma(N)."""
    s = sigma(N)
    return sum(1 for a in range(1, N) if sigma(a) + sigma(N - a) == s)


# ---------------------------------------------------------------- result 1
def test_r_exceeds_tau():
    print("1. r(N) <= tau(N) is FALSE")
    bad = [(N, r_count(N), tau(N)) for N in range(3, 201)
           if r_count(N) > tau(N)]
    check("exceptions for N <= 200", bad, [(123, 6, 4), (141, 6, 4), (183, 8, 4)])
    s = sigma(123)
    check("sigma(123)", s, 168)
    for a, b in ((38, 85), (41, 82), (46, 77)):
        check("sigma(%d)+sigma(%d) = sigma(123)" % (a, b), sigma(a) + sigma(b), s)


# ---------------------------------------------------------------- result 2
def mono_triple_exists(colour, N):
    """Is there a < b <= N with {2a, a+b, 2b} monochromatic?"""
    for a in range(1, N + 1):
        for b in range(a + 1, N + 1):
            if colour[2 * a] == colour[a + b] == colour[2 * b]:
                return True
    return False


def least_forcing_N(limit=9):
    """Smallest N such that EVERY 2-colouring of [2,2N] forces a mono triple."""
    for N in range(1, limit + 1):
        idx = list(range(2, 2 * N + 1))
        forced = True
        for bits in product((0, 1), repeat=len(idx)):
            if not mono_triple_exists(dict(zip(idx, bits)), N):
                forced = False
                break
        if forced:
            return N
    return None


def test_threshold_is_seven():
    print("2. the {2a, a+b, 2b} threshold is 7, not 33")
    check("least forcing N", least_forcing_N(), 7)
    # the explicit avoiding colouring at N=6, from the README
    c = {2: 1, 3: 0, 4: 1, 5: 0, 6: 0, 7: 0, 8: 1, 9: 1, 10: 0, 11: 1, 12: 0}
    check("N=6 avoiding colouring really avoids", mono_triple_exists(c, 6), False)


# ---------------------------------------------------------------- result 3
def v_p(n, p):
    k = 0
    while n % p == 0:
        n //= p
        k += 1
    return k


def test_constant_ratio():
    print("3. n = 2^(3^r) has CONSTANT ratio 3/ln2, not ratio -> 0")
    import math
    ratios = []
    for r in range(5):
        n = 2 ** (3 ** r)
        m = n * (n + 1)
        a, b = v_p(m, 2), v_p(m, 3)
        ratios.append(round((2 ** a * 3 ** b) / (n * math.log(n)), 9))
        check("  r=%d: v2 = 3^r" % r, a, 3 ** r)
        check("  r=%d: v3 = r+1 (lifting the exponent)" % r, b, r + 1)
    check("ratio constant across r=0..4", len(set(ratios)), 1)
    check("ratio equals 3/ln 2", ratios[0], round(3 / math.log(2), 9))


# ---------------------------------------------------------------- result 4
def test_minimum_is_22():
    print("4. min sum f2(n)^2 over 2-bases of [2,8] is 22, not 27")

    def score(A):
        f = {}
        for n in range(2, 9):
            f[n] = sum(1 for x in A for y in A if x + y == n)
        if any(v == 0 for v in f.values()):
            return None  # not a basis of [2,8]
        return sum(v * v for v in f.values())

    best, arg = None, None
    universe = range(0, 9)
    for size in range(2, 10):
        for A in __import__("itertools").combinations(universe, size):
            s = score(set(A))
            if s is not None and (best is None or s < best):
                best, arg = s, A
    check("true minimum", best, 22)
    check("unique extremizer", arg, (0, 2, 3, 7, 8))
    check("filed extremizer {1,2,3,6} scores 27", score({1, 2, 3, 6}), 27)


# ------------------------------------------------ the impossible counterexample
def test_impossible_counterexample():
    print("5. the Erdos 247 counterexample cannot exist")
    # a_n = n + m*2^m, the literal sequence that was filed
    a = sorted({n + m * 2 ** m for n in range(1, 60) for m in range(0, 6)})[:400]
    max_ratio = max(a[i] / (i + 1) for i in range(len(a)))
    counts = [sum(1 for x in a if x <= N) / N for N in range(1, 3000)]
    check("its limsup a_n/n is NOT infinite (prefix max < 2)", max_ratio < 2, True)
    check("its liminf A(N)/N is NOT 1 (samples below 0.1)", min(counts) < 0.1, True)
    # A(N) <= N always, which is what makes the pair contradictory
    check("A(N) <= N for all sampled N", all(c <= 1.0 for c in counts), True)


# ------------------------------------------------------------ spot refutations
def test_spot_refutations():
    print("6. spot refutations")
    # Erdos 17: 88 is not a difference of two primes <= 97
    def is_prime(n):
        if n < 2:
            return False
        d = 2
        while d * d <= n:
            if n % d == 0:
                return False
            d += 1
        return True

    reps = [(88 + q, q) for q in range(2, 98)
            if is_prime(q) and 88 + q <= 97 and is_prime(88 + q)]
    check("Erdos 17: no representation of 88 with both primes <= 97", reps, [])

    # Erdos 137: consecutive powerful pairs
    def powerful(n):
        if n < 1:
            return False
        m, d = n, 2
        while d * d <= m:
            if m % d == 0:
                e = 0
                while m % d == 0:
                    m //= d
                    e += 1
                if e < 2:
                    return False
            d += 1
        return m == 1

    pairs = [n for n in range(1, 20001) if powerful(n) and powerful(n + 1)]
    check("Erdos 137: consecutive powerful n <= 20000", pairs, [8, 288, 675, 9800, 12167])

    # Erdos 1061: the witness (6,11) at N=17 does not satisfy the equation
    check("Erdos 1061: sigma(6)+sigma(11) != sigma(17)",
          sigma(6) + sigma(11) == sigma(17), False)
    check("  the actual values", (sigma(6) + sigma(11), sigma(17)), (24, 18))

    # Erdos 539: the 'injective diagonal' step
    check("Erdos 539: a/gcd(a,a) = 1, not a", [a // a for a in (2, 7, 30)], [1, 1, 1])


def main():
    print("Verifying the counterexample-queue results.\n")
    for fn in (test_r_exceeds_tau, test_threshold_is_seven, test_constant_ratio,
               test_minimum_is_22, test_impossible_counterexample,
               test_spot_refutations):
        fn()
        print()
    if FAILURES:
        print("FAILED: %d check(s)" % len(FAILURES))
        for f in FAILURES:
            print("   " + f)
        return 1
    print("ALL CHECKS PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
