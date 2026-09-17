# Counterexample library

A collection of explicit counterexamples and corrected finite calculations extracted from larger Erdős research logs. Every item promoted to this README was independently recomputed before publication.

The source sweep found 1,668 nonempty counterexample fields across 226 campaigns; 504 had not been routed into a findings document.

## Selected counterexamples and corrections

### A divisor-function bound fails

Let `r(N)` count ordered pairs satisfying

\[
\sigma(a)+\sigma(b)=\sigma(N).
\]

The proposed inequality `r(N)<=τ(N)` is false. The first failure found is

\[
N=123,
\qquad
r(123)=6>4=\tau(123).
\]

Indeed,

```text
sigma(38)+sigma(85) = 60+108 = 168
sigma(41)+sigma(82) = 42+126 = 168
sigma(46)+sigma(77) = 72+96  = 168
sigma(123) = 168.
```

Further failures occur at 141 and 183.

### Exact Ramsey-type threshold: 7

Consider 2-colorings and ask for `a<b` such that

\[
\{2a,a+b,2b\}
\]

is monochromatic. Exhaustive search gives the exact threshold

\[
\boxed{N=7}.
\]

Every coloring of `[2,14]` has such a triple, while an avoiding coloring exists for the corresponding `N=6` instance.

### A supposedly vanishing ratio is constant

For

\[
n=2^{3^r},
\]

one has

\[
v_2(n(n+1))=3^r,
\qquad
v_3(2^{3^r}+1)=r+1.
\]

The associated normalized quantity simplifies exactly to

\[
\frac{3}{\log2}=4.328085123\ldots,
\]

independent of `r`.

### Representation-energy minimum

Under the convention allowing `0` in the basis, a finite minimization previously recorded as 27 is actually

\[
\boxed{22},
\]

attained uniquely by

\[
A=\{0,2,3,7,8\}.
\]

For `n=2,...,8`, the representation counts are

```text
2,2,1,2,1,2,2
```

whose squared sum is 22.

## A false counterexample that killed a true lemma

For a strictly increasing sequence `a_n`, let

\[
A(N)=\#\{n:a_n\le N\}.
\]

The equivalence

\[
\limsup\frac{a_n}{n}=\infty
\iff
\liminf\frac{A(N)}N=0
\]

is true.

One archived route incorrectly discarded it using a purported counterexample whose two advertised asymptotic properties are themselves incompatible. The direct proof of both implications is elementary and is recorded with the source material.

This is an important category in the library: not only false lemmas with valid counterexamples, but also valid lemmas that were incorrectly killed by invalid examples.

## Arithmetic receipt corrections

The sweep also found many cases where the high-level verdict was right but the supporting arithmetic was wrong. Examples include:

- `47^2+1=2210=2·5·13·17`, not 2222;
- `2^11=2048=2210212_3`;
- `sigma(1764)=5187`, not 728;
- several mislabeled modular witnesses in Erdős #479;
- corrected admissible-pair counts in Erdős #1093;
- corrected Collatz stopping-time values in one finite table.

These matter because a correct conclusion with an incorrect certificate is not reusable evidence.

## Further explicit refutations

The source queue contains verified counterexamples for a number of proposed intermediate statements, including:

- consecutive powerful-number exclusions, with examples `(288,289)` and `(675,676)`;
- a local-window characterization in Erdős #413, failing at `n=8193`;
- a claimed WLOG reduction in a modular product problem, refuted at `p=11`;
- a pointwise bound in Erdős #158, already failing at small `N`;
- a composite-number lower bound in Erdős #700, failing at `n=6`;
- an incorrect large witness in Erdős #376.

The repository preserves the concrete witnesses and recalculations needed to check each one.

## Purpose

This is a counterexample and correction bank, not a theorem-status dashboard. A result that survives a counterexample belongs in its mathematical subject repository; a failed route remains here with the object that kills it.

Author: Jared Wilder. License: Apache-2.0.
