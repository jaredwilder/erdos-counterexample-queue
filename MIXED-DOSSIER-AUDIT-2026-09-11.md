# Mixed dossier audit — six refuted claims

This file preserves a cross-problem audit that was briefly published inside the dedicated Erdős #930 repository. It does **not** belong to #930 mathematically; it is kept here because this repository is the forensic home for rechecked counterexamples, false lemmas, and corrected receipts.

## 1. False consecutive-block scaling family

A dossier claimed that, for every `k>=2`,

- `I1=[k,2k-1]`,
- `I2=[4k,5k-1]`

produce a square product because `I2` is supposedly obtained by multiplying `I1` by 4.

That step is false: `4*I1` has spacing 4, whereas `I2` is consecutive. Already at `k=2`,

- `4*{2,3}={8,12}`,
- `I2={8,9}`,
- the combined product is `432=2^4*3^3`, not a perfect power.

The same failure persists for the checked values `k=3,4,5`.

## 2. False claim `gcd(n!-1,m!-1)=1`

The proof correctly observes that a prime `p | n!-1` satisfies `p>n`, then incorrectly assumes `p<=m` for every `m>n`.

First failure:

- `4!-1=23`,
- `8!-1=40319=23*1753`,
- hence `gcd(4!-1,8!-1)=23`.

Nine failures occur for `2<=n<m<=25`:

`(4,8),(4,11),(4,21),(5,11),(5,15),(8,11),(8,21),(11,15),(11,21)`.

A correct statement from the same source survives: `gcd(n!-1,m!-1)` divides `(n+1)(n+2)...m - 1`; the preserved exact check found no violation for `2<=n<m<=21`.

The same dossier also gave the enclosure

`S in (1.253498755679455, 1.253498755679566)`,

while the audited value was recorded as `1.2534987556999534716...`, above the stated upper endpoint.

## 3. False infinite-graph transfer

A dossier argued that every subgraph of `K_m` is complete and concluded a claimed obstruction for an infinite-chromatic problem. This is false: subgraphs can delete edges.

The finite salvage is correct: a graph `H` on at most `n` vertices with chromatic number `n` must be `K_n`. The analogous inference fails at infinite cardinality. A disjoint union of `K_1,K_2,K_3,...` embeds in `K_{aleph_0}`, has chromatic number `aleph_0`, and is neither complete nor connected.

## 4. Partition values shifted to the wrong indices

The dossier stated `p(7)=22` and `p(11)=101`. The correct values are

- `p(7)=15`, while `p(8)=22`;
- `p(11)=56`, while `p(13)=101`.

Thus the claimed prime-entry points based on those values were not valid.

## 5. Coverage lemma false at its smallest tested instance

A claimed inequality for every greedy sequence and every `k>=1` asserted

`partial reciprocal sum >= 1 - (k+1)/(a_{k+1}-1)`.

For start `n=4`, `k=1`, the sequence begins `4,5`, so the left side is `1/4` and the right side is `1/2`.

The proof assumed every integer below `a_{k+1}` was representable as a consecutive sum; that is false for starts `n>=2` because integers below `n` are not represented.

## 6. False lemma accompanied by a non-counterexample

A dossier asserted `v_0(n)>=2` for every `n>=5` and supplied `n=15` as a counterexample because `15=3*5` was incorrectly read as having one prime factor. In fact `omega(15)=2`.

The lemma is nevertheless false; the surviving witnesses recorded in the audit are `n=7,8,16`.

## Provenance and verification

The original mixed verifier was temporarily stored in `jaredwilder/erdos930-consecutive-block-square/verify.py`. It independently rechecked the #930 length-4 witness plus the first, second, and fourth audit items above. The #930 repository has since been cleaned so that its verifier concerns #930 only.

This forensic note preserves the cross-problem correction record without allowing those failures to become the public identity of an unrelated mathematical result.
