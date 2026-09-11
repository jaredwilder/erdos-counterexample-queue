# The counterexample queue

**504 counterexamples that a machine produced, argued from, and then lost.**

Author: Jared Wilder. Worked and published 2026-09-11.

A promotion pipeline in this estate reads `LEMMA_VERDICT` lines. But the machine does its
constructing inside `BOUNDARY_AUDIT` / `TESTS` / `COUNTEREXAMPLES` prose, which carries no verdict
line. So the single most valuable class of output it produces, a refutation with its counterexample
attached, was invisible to the thing whose job is to promote it.

A tool written for this release swept all 226 transcript-bearing campaigns and found **1,668
non-empty `COUNTEREXAMPLES` fields**. Of those, **504 had never reached any findings document**.

This repository is that queue, worked.

**Every claim below was re-verified by direct computation before publication.** Where my check
disagreed with the machine, my check is what is published, and several entries below are
corrections to the counterexamples themselves.

---

## What the queue turned out to be

| slice | rows | carrying a real object | distinct findings |
|---|---|---|---|
| top six campaigns | 117 | ~37 (32%) | ~22 |
| problems 1-499 | 265 | 75 (28%) | ~40 |
| problems 500+ | 199 | ~51 | ~18 |

**Roughly two thirds is filler**, rows reading `NONE`, or `NONE - [tests that passed]`. Erdos 400 is
the extreme: 18 of its 19 rows restate that `n!*1! | n!`. One row does real work.

That ratio is the first useful finding, because it prices the remaining work honestly.

---

## The four results that are new mathematics

### 1. `r(N) <= tau(N)` is false, the compute request nobody ran

A route filed `r(N) <= tau(N)` as its load-bearing lemma, where `r(N)` counts ordered pairs with
`sigma(a) + sigma(b) = sigma(N)`, and **requested an exact table for `3 <= N <= 200`**. The route was
retracted for an unrelated defect before the table was ever computed.

The table has now been computed. **The bound is false.**

| N | r(N) | tau(N) |
|---|---|---|
| **123** | **6** | 4 |
| 141 | 6 | 4 |
| 183 | **8** | 4 |

First failure at `N = 123`:

```
sigma(38) + sigma(85) =  60 + 108 = 168 = sigma(123)
sigma(41) + sigma(82) =  42 + 126 = 168 = sigma(123)
sigma(46) + sigma(77) =  72 +  96 = 168 = sigma(123)
```

By `N <= 400`, `r` reaches 10. The proposed upper-bound mechanism is dead independently of the
defect the route was actually retracted for.

### 2. A Ramsey-type threshold that is 7, not 33

A route needed: every 2-colouring of `[1,N]` contains `a < b` with `{2a, a+b, 2b}` monochromatic. It
routed through van der Waerden `W(2,3)=9` and two affine maps to land on **N = 33**, window `[1,66]`.

The detour is unnecessary. Put `d(n) = c(2n)` and apply `W(2,3)=9` directly: a monochromatic 3-term
progression `a < m < b` in `d` gives `A = {a,b}` with `A+A = {2a, 2m, 2b}` monochromatic. That alone
gives N=9.

**Exhaustive search gives the exact answer: `N = 7` is minimal.** Every 2-colouring of `[2,14]`
contains a monochromatic triple, and `N = 6` does not suffice. Here is an avoiding colouring of
`[2,12]`:

```
c(2)=1  c(3)=0  c(4)=1  c(5)=0  c(6)=0  c(7)=0
c(8)=1  c(9)=1  c(10)=0  c(11)=1  c(12)=0
```

all 15 pairs `a < b <= 6` non-monochromatic. **The filed bound was nearly five times too weak.**

### 3. A family called "ratio tends to 0" has a constant ratio

An audit dismissed the family `n = 2^(3^r)` as not even witnessing its own branch, on the grounds
that its ratio tends to 0. For that family, `v_2(n(n+1)) = 3^r`, and by lifting-the-exponent
`v_3(2^(3^r)+1) = r+1`. So

```
2^k 3^l / (n log n)  =  n*3^(r+1) / (n ln n)  =  3/ln 2  =  4.328085123...
```

**constant in r**, verified digit-identical at r = 0, 1, 2, 3, 4. The family is a uniform lower
bound, not a null family, and any constant for the branch must satisfy `B >= 4.3281`.

The same audit row recorded `n=8` as "ratio ~ 0.48", having dropped the 3-part of `72 = 2^3 * 3^2`
entirely.

### 4. A minimum that is 22, not 27

A repaired lemma asserts `min sum f_2(n)^2 = 27` over 2-bases of `[2,8]`. Under the `0 in N` reading
the route itself invokes, the true minimum is **22**, uniquely at `A = {0,2,3,7,8}`:

```
f_2(2..8) = (2, 2, 1, 2, 1, 2, 2)      sum f_2^2 = 4+4+1+4+1+4+4 = 22
```

The campaign considered 0-inclusion, probed it with a set that **is not a basis at all**, and
concluded 27 survived.

---

## The inverse error: a true lemma killed by an impossible counterexample

Everything else here is a false claim that survived. This is the opposite, and it is worse.

Erdos 247, route R013, retired with `ROUTE_STATUS KILLED_BY_THEOREM`. The lemma it was killed for
contradicting, with `A(N) = #{n : a_n <= N}`:

```
limsup a_n/n = infinity   <=>   liminf A(N)/N = 0
```

**That lemma is true, and both directions are two lines.**

- take `a_{n_k}/n_k -> infinity` and set `N_k = a_{n_k}`; then `A(N_k)/N_k = n_k/a_{n_k} -> 0`
- take `A(N_k)/N_k -> 0` and `n_k = A(N_k)`; then `a_{n_k+1} > N_k`, so
  `a_{n_k+1}/(n_k+1) > N_k/(A(N_k)+1) -> infinity`

**The counterexample that killed it cannot exist.** It claimed a sequence with
`limsup a_n/n = infinity` AND `liminf A(N)/N = 1`. But `A(N) <= N` always, so `liminf A(N)/N = 1`
forces `A(N)/N -> 1`; at `N = a_n` that gives `n/a_n -> 1`, hence `limsup a_n/n = 1`. **The two
conditions are contradictory.**

The literal sequence proposed, `a_n = n + m*2^m`, does neither: its maximum `a_n/n` on a prefix is
**1.2984**, and `liminf A(N)/N` samples to **0.0607**.

A correct route was retired on a fabricated object, and that failure leaves no trace: the route
simply stops, and the record says a theorem killed it.

---

## The dominant pattern: receipts that fail re-derivation

Across the slice for problems 1-499, the most common real finding is **not** a refutation of an
Erdos statement. It is a campaign's own exact-arithmetic receipt failing re-computation, in cases
its own boundary audit did not catch.

| problem | what the receipt says | what it is |
|---|---|---|
| **383** | `47^2+1 = 2222 = 2*11*101`, filed as a non-survivor | `47^2+1 = 2210 = 2*5*13*17`, so `P = 17 <= 47`. It is a **survivor**, filed as its own opposite |
| **406** | `2^11 = 221212` base 3, "corrected" to `2112002` | those are **698** and **1838**; `2^11 = 2048 = 2210212` base 3. Both rounds wrong, and the audit's list of bad certificates omits k=11 |
| **243** | sixth term `1133904362`; partial sums `.., 11/14, 205/256, ..` | term is **1133904604**; sums are `1/2, 3/4, 23/28, 1065/1288, 17932049/21686056` |
| **313** | `sigma(1764) = sigma(4)sigma(9)sigma(7) = 728` | `1764 = 2^2 * 3^2 * 7^2`, so `sigma = 7*13*57 = 5187`. Conclusion survives, witness line does not |
| **479** | 15-row witness table for `2^n = k (mod n)` | **7 rows mislabelled.** `66, 946` are `k=-2` not `k=4`; `513` is `k=-1` not `8`; all three `k=-1` and both `k=-2` rows wrong |
| **238** | `K(59;2)=K(59;4)=2, K(97;6)=1, K(100;8)=0` | **all four wrong** under the definition as written: 4, 3, 2, 1. The audit caught one |
| **385** | bad-witness set "exact and complete", 10 members | **29 members** on `[2,200]`. The audit named six then wrote "..." |
| **386** | `15*16 = 240 != 2*(2*3*5) = 420` | `2*30 = 60`; 420 was copied from a different line |
| **1065** | 43-row sieve certificate | **39 rows.** Both prime tables also wrong. Form 1 has 23 primes not 16, missing `3, 5, 17, 41, 89, 97, 193` |
| **1135** | Collatz stopping times `k = (2,1,5,2,3,6,10)` | `k = (2,1,5,2,4,6,11)`, orbits recomputed in full |
| **1093** | 221 admissible pairs; deficiency-1 set of 7 | **224** pairs (`n = 76, 77, 79` omitted); deficiency-1 set has **5**, since `(22,4)` and `(23,4)` are deficiency 0: `20 = 2^2 * 5` is not 4-smooth |
| **1203** | `9*g(223092870)` in `[1.38413, 1.38424]` | `= 1.38401274083`, below the stated lower endpoint. Two more enclosures in the same node also miss |

In every case the **verdict** survived and only the **annotation** was wrong. That is precisely the
failure mode that makes a filed certificate unusable downstream: you cannot re-check it, you cannot
reuse it, and it cannot stop the error recurring.

---

## Refutations that stand, with witnesses

- **Erdos 17.** The "for every prime p" strengthening dies at **p = 97, n = 88**: `q1 = 88 + q2 <= 97`
  forces `q2 <= 9`, so `q1` lies in `{90, 91, 93, 95}`, all composite. Non-cluster primes below 400
  agree with OEIS A038133.
- **Erdos 137.** "No two consecutive powerful numbers" dies at **(288, 289)** = `2^5*3^2, 17^2` and
  **(675, 676)** = `3^3*5^2, 2^2*13^2`. Complete list to 20000: `8, 288, 675, 9800, 12167`.
- **Erdos 413.** The local-window characterisation dies at **n = 8193**: both nearest predecessors
  pass, but `m = 8190 = 2*3^2*5*7*13` has `omega = 5` and `8190 + 5 > 8193`. Killed from distance 3.
- **Erdos 445.** "WLOG `a = b`" is not a WLOG. At `p = 11, c = 0.6, n = 5` the window is `{6,7,8,9}`,
  the self-inverses `1, 10` are outside it, yet **`7*8 = 56 = 1 (mod 11)`** with both in the window.
- **Erdos 158.** The pointwise bound `M(N) <= sqrt(2N)` dies at **M(8) = 6** with `{1,2,3,4,6,8}`, and
  in fact already at `N = 3`.
- **Erdos 509.** `[-2,2]` is not inside the lemniscate at its own endpoint: `f_n(2) = 2^n * T_n(1) = 2^n > 1`
  for every `n >= 1`.
- **Erdos 1057.** The construction's exponent goes to **0**, not 1: `C(s,s/2) <= 2^s` against scale
  `s^s` gives `beta(s) <= log 2 / log s`. Measured: `0.5, 0.286, 0.240, 0.166, 0.128, 0.0998, 0.0813`.
- **Erdos 700.** A dossier's "Corollary C1", `f(n) >= n/2` for composite `n`, inverts a min into a
  lower bound. **`f(6) = 2 < 3`, and 152 of the composite `n <= 200` violate it.** The dossier claims
  this "resolves the entire multi-part contract, every clause."
- **Erdos 376.** The witness `n = 850` is false: `850 = 11400` base 5 has digit `4 > 2`, and
  `gcd(C(1700,850), 105) = 5`. True list for `n < 3*10^6`: **`{1, 10, 756, 757, 3160, 3186, 3187,
  3250, 7560, 7561, 7651, 20007}`**.
- **Erdos 539.** A node filed `PROVED` on the step `a/(a,a) = a`. **`gcd(a,a) = a`, so `a/(a,a) = 1`.**
  The diagonal contributes one value, not `n`. The conclusion survives on tested ranges; the proof
  does not exist.

## Corrections I am making to the counterexamples

Several kills fired correctly and mis-stated the corrected value. Published because a wrong
correction is what a later reader inherits.

- **Erdos 1061 census.** The kill says "12 unordered". It is **13**: 12 is the count of distinct `N`,
  and `N = 32` carries two unordered pairs, `(4,28)` and `(14,18)`.
- **`S(60)`.** The kill concludes `>= 36`. It is exactly **40**; the enumeration missed `r(55) = 4`
  and `r(57) = 4`.
- **Erdos 1192 at N=5.** The kill takes down both the `N=6` and `N=5` values. **The `N=5` value 18 is
  correct**; only its extremizer was wrong. True minima for `N = 2..6`: `6, 10, 14, 18, 27`.
- **Erdos 1210.** The lemma dies correctly on composite shifts, but the attached inequality is
  backwards: `23/12 = 1.91667` and `31/30 + 1 = 2.03333`, so `23/12 < 31/30 + 1`.
- **Erdos 1101.** The filed "counterexample" family is the odd primes, declared to satisfy
  `sum 1/u_i < infinity`. **That sum diverges.** The family refutes nothing.
- **Erdos 1094.** A probe reported two exceptions. There are **12** for `k <= 12, n <= 600`, and the
  reported `(3,2)` is not one: it violates `n >= 2k`.

## Objects that simply do not exist

- **Erdos 1061** lists `N=17` with witness `(6,11)`. `sigma(6)+sigma(11) = 24`, `sigma(17) = 18`. A
  witness pattern-fit and never evaluated.
- **Erdos 11** files `53, 89, 95, 97` as extremal. All four are one step from squarefree:
  `53 = 51+2`, `89 = 87+2`, `95 = 94+1`, `97 = 95+2`. The genuine extremizer is **n = 29**.

## One coincidence worth keeping

Erdos 1093's corrected deficiency-1 set and Erdos 1094's exception set are **the same five pairs**
for `k <= 6`: `(7,3), (13,4), (14,4), (23,5), (62,6)`. Both conditions say "`C(n,k)` has no small
prime factor relative to the window". **Neither campaign noticed the other**, and they were wrong in
complementary directions: 1093 over-listed by two, 1094 under-listed by ten.

---

## What remains

Roughly 387 of the 504 rows are worked here. The rest, plus **986 counterexamples the tool marked
UNDECIDABLE** because their text carries no distinctive token, need reading rather than matching.

Expect about a third to carry an object. Expect those objects to be right about *firing* and
unreliable about the *corrected value*. And expect at least one more of the inverse kind, because a
pipeline that retires routes on counterexamples nobody re-derives will retire correct routes.

## License

Apache-2.0.
