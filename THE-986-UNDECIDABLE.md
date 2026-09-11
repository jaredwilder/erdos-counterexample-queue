# The 986 a matcher could not judge

The harvest tool that produced this repository classified counterexamples by looking for
**distinctive tokens**: multi-digit numbers, fractions, witness tuples, set literals. It asked one
question of each, "does this exact token appear in the findings corpus", because prose matching had
already produced false positives.

682 of the 1,668 counterexample fields carried such a token. **986 carried none**, and the tool
correctly refused to call them present or absent.

Those 986 have now been read rather than matched. **Every claim below was re-verified by direct
computation.**

---

## The measurement first

| bucket | count | share |
|---|---|---|
| **No mathematical object at all** | **877** | **88.9%** |
| Pure back-pointer ("the above", "the same instance") | 16 | 1.6% |
| **Self-contained mathematical object** | **93** | **9.4%** |

**Roughly 89% are vacuous, and that is the answer to why a matcher could not decide them: there is
no token because there is no object.** The dominant shape is the machine reporting that it found no
counterexample.

A useful refinement: **272 of the 877** are "none, and here is the scope" — negative results with a
boundary note, which is not noise but is not a counterexample either.

Of the 93 real objects, about **20 carry a result worth banking**. That is **2% of the pool**, and it
prices the remaining work honestly: a second full pass is not worth it, but a targeted read of the
93 captures essentially everything.

---

## Three campaign verdicts are wrong

### A banked kill that rests on false arithmetic [verified]

A node was marked `CLAIM_STATUS FALSE` on the grounds that the machine record contained a
representation of **87 as a sum of at most three powerful numbers**.

The powerful numbers up to 87 are

```
1, 4, 8, 9, 16, 25, 27, 32, 36, 49, 64, 72, 81
```

**Exhaustive enumeration of all one-, two- and three-term sums finds no representation of 87.** The
kill is false and the lemma it struck down was correct.

Extending the search, the complete non-representable set for `n <= 2000` is

```
{7, 15, 23, 87, 111, 119}
```

which is the known exceptional set for the three-powerful-numbers theorem. **This also extends a
result published earlier in this release**, which recorded `{7, 15, 23, 87}` from a shorter range:
111 and 119 belong to it as well, and the set is stable from 119 to 2000.

A second audit in the same campaign is right that the filed witness set `{7}` is incomplete, but its
proposed replacement `{7, 15, 23}` is also incomplete.

### A correction that was false, filed against a parenthetical that was right [verified]

A row corrects an extremizer count: *"N=6 distinct-gap extremizers = 22, not 14"*.

Exhaustive enumeration over all subsets of `[1,6]`: `F(6) = 3`, and there are **exactly 14**
extremizers.

```
{1,2,4} {1,2,5} {1,2,6} {1,3,4} {1,3,6} {1,4,5} {1,4,6}
{1,5,6} {2,3,5} {2,3,6} {2,4,5} {2,5,6} {3,4,6} {3,5,6}
```

Independent cross-check: `C(6,3) = 20`, minus the 6 three-term progressions, is **14**. The same code
reproduces that campaign's own `F(9)=4` and `F(12)=5`, so the definitions agree. **The original
number was right and the correction is the error.**

### Two boundary instances that are not boundary instances [verified]

A row files *"n=32 has m=30 and 30+omega(30) = 33 > 32"* and elsewhere *"n=42 is not in B1 since
40+omega(40) = 43 > 42"*.

**`omega(40) = |{2,5}| = 2`, so `40 + omega(40) = 42`, not 43.** That error is independent of any
definitional reading.

And both values are in the image of `m -> m + omega(m)`:

```
32 = 31 + omega(31) = 31 + 1
42 = 41 + omega(41) = 41 + 1     (and also 40 + 2)
```

The jump-over test examined only `m=30` and `m=40` and never checked the prime one step up. Genuine
non-image values below 100 are `{2,7,11,13,15,19,21,25,27,29,31,34,39,43,49,51,55,61,66,75,83,85,86,91,92,99}`,
and neither 32 nor 42 is among them.

---

## A lemma far more dead than its record says [verified]

A lemma filed at `COMPUTATION_SUPPORTED` asserts: **if `n-1` is prime then `f(n) = n-1`**, where
`f(n)` is the least `m` whose sorted-divisor prefix sums hit `n`.

An audit retracted the *argument* and called one bad value a "table defect". **The conclusion itself
is false, on an infinite constructible family.**

Take `m = 2q` with `q` an odd prime. Its divisors are `1, 2, q, 2q`, with prefix sums
`1, 3, q+3, 3q+3`. So `n = 3q+3` is attained at `m = 2q`, and `2q < 3q+2 = n-1` always. Whenever
`3q+2` is prime, the lemma predicts `f(n) = n-1` and is wrong.

**Of the 46 values `n <= 200` with `n-1` prime, the lemma fails on 29.** The minimal witness:

| n | f(n) | n-1 |
|---|---|---|
| **12** | **6** | 11 |
| 18 | 10 | 17 |
| 24 | 14 | 23 |
| 32 | 21 | 31 |
| 42 | 20 | 41 |
| 48 | 33 | 47 |

---

## A five-point isosceles set in the plane [verified]

A row files `d=2, max = 4` with the unit square as extremizer, for sets in which every triple is
isosceles.

**The regular pentagon has exactly two distinct squared distances**, `(5 - sqrt5)/2` and
`(5 + sqrt5)/2`, verified symbolically over `Q(sqrt5)`. With only two distance values among five
points, **all 10 of its 10 triples are isosceles.**

So the maximum is at least 5. The retraction reason recorded is correct: a bounded-grid enumeration
was read as a universal bound over the plane.

---

## Structural objects a token matcher can never see

These are the reason the 986 were worth reading. None contains a distinctive number, and each kills
something.

**A quantifier shape that is void by Dirichlet.** A lemma argues: all `q <= 2^31` excluded within a
window of `2^-63` at each level, therefore the sum is irrational. **Dirichlet's approximation theorem
guarantees that for every irrational and every `Q` there is `q <= Q` with `|alpha - p/q| < 1/(qQ)`.**
The convergents of `sqrt2` — `3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408` — every one satisfies
`|alpha - p/q| < 1/q^2`, and `sqrt2` is irrational. A finite `q`-window is consistent with both
rationality and irrationality, so the lemma form has no content. To say anything it must cover all
`q` below an explicit level-dependent bound.

**Bezout kills an entire mechanism.** A construction claims `n^2/24 - O(n)` 4-rich lines with no 5
collinear, and the only named mechanism is the group law on a cubic. **A line meets an irreducible
cubic in at most 3 points, so the count of 4-rich lines is identically zero on any such point set.**
Demonstrated on 60 points of `y^2 = x^3 + 2x + 3` over `F_1009`: the richness histogram is
`{2-rich: 1674, 3-rich: 32, 4-or-more: 0}`. This refutes the attribution, not the existence of some
other construction.

**An identity read where only monotonicity holds.** A filed dyadic layer-cake is not an identity and
not even an upper bound: it **undercounts**. The ungrouped form is exact, but the correct level
weight is `3*4^j - 2^(j+1)`, not the filed `3*2^(j-1)`:

| y | true S | ungrouped layer cake | filed dyadic |
|---|---|---|---|
| 6 | 20 | **20** | 15 |
| 12 | 72 | **72** | 36 |
| 30 | 148 | **148** | 61.5 |

**A non-integral increment.** An increment formula `(k+1)(2k-3)/2` is filed for an integer sequence.
It is **half-integral at every even `k`** (3/2 at k=2, 25/2 at k=4, 63/2 at k=6), which alone kills
it. The true increment is `k^2 - 2`, and the two agree at `k=1` only. The filed positivity claim also
fails immediately: the first three values are `-3, -4, -2`.

## One conclusion that is right for the wrong reason

A node reports its instance set empty by a **parity contradiction**, claiming the left side is even
and the right side odd. Over 384 admissible triples the right side was **even in 384 of 384**. The
reason is elementary: `2N` is even and `a+b+c` is even, so `2N + a + b + c` is even, so the product
is even. The transcript read `2N` as odd.

**The emptiness holds anyway, by a different mechanism.** `N(qr + pr + pq) = pqr` with `p, q, r`
distinct primes forces `p | N*qr`, hence `p | N`; but `1/p < 1/N` forces `p > N`. Contradiction.
Brute force over all distinct odd primes `p < q < r <= 4000` with `N <= 1300` found no solutions.

## And a minimality nobody established

The failure of the coverage lemma at `p = 97, n = 88` is published in this repository's main README.
Sweeping all primes shows **`p = 97` is the smallest prime admitting such a failure**. The witness is
minimal, which the original audit did not establish.

---

## What this says about the rest of the work

The yield is 2%, concentrated in about twenty campaigns. That is low, and it is the right number to
plan against.

But the items it did yield are disproportionately **structural**: a quantifier shape, a Bezout
degree bound, a parity claim that runs backwards, an increment that cannot be an integer. Those are
exactly the objects a token matcher is blind to, and exactly the ones that kill a route permanently
rather than correcting a digit.
