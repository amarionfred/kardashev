# Reproduction guide

This document states the exact boundary between what you can reproduce from this repository and what cannot be reproduced without the internal programme records.

## Reproducible here (public constants + labelled assumptions)

Run `scripts/reproduce.py`. Every claim in the paper of this type is recomputed:

| Claim in the paper | Reproduces as |
|---|---|
| Feed ratio at 10/5 ppb, 100%/50% recovery | 100,000 t / 200,000 t / 400,000 t per kg |
| Heat per gram, 10 ppb 50%, 0.5–0.7 MJ/kg | 100–140 GJ (28–39 MWh) |
| Net heat at 85% recuperation (Mark-III claim) | 4.2–5.8 MWh |
| Night storage, 1.4 MW, 14.75 days | 496 MWh; ~1,982 t of batteries at 250 Wh/kg |
| Radiator at 300 K, ε=0.9, two-sided | ~827 W/m²; ~1,210 m² per MW |
| Break-even product per tonne of hardware | 50 kg @ $1M launch, 25 kg @ $500k, 5 kg @ $100k |
| Aluminium vs helium-3 per tonne of feed | $198.5 Al (50 kg @ $3.97) vs $100 He-3 (5 mg) |
| He-3 vs Al revenue per kg of product | $20,000,000 vs $3.97 (~5.0×10⁶) |
| Primary energy vs Sagan Type I | 1.96×10^13 W; K ≈ 0.73; ~509× to Type I |
| Lunation length | 2,551,443 s day / 1,275,721 s night |

## Not reproducible here (internal, labelled as such in the paper)

- The 226,744 J/kg integral of the FJS-1 simulant heat-capacity fit (313–570 K). The fit itself is published (Nakayama et al. 2025, DOI 10.11395/jjsem.25.14); the numerical route check (relative difference 3.19×10⁻⁹) lives in the internal design basis and is repeated here as an internal result. The figure is an internal model output, not a public measurement.
- "157 traced quantities" and "716 of 716 CAD/STEP pinned snapshots hash-verified at file scope." These describe the internal design basis. They are stated as scope descriptors, not as invariants you can re-derive from this repository.
- The 0.263 s failure timing. Internal deterministic simulation record.
- Apollo 17 sample ppb values (72501,27: 4.656; 70011,18: 11.209). These are assay records of the internal design basis, traceable to Apollo archives but not re-derivable here.
- Release fraction of ~95% at 800 °C on Apollo sample 10084 (Olson 2021, NASA NTRS 20210022801) — publicly verifiable at that citation; the paper's use of it remains a sample-specific point.

## Public sources the paper leans on

Everything cited as [1]–[7], [9]–[11], [14]–[24] in the bibliography is public and verifiable at the cited link. Internal citations are labelled "Internal, versioned."
