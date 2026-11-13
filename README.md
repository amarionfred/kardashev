# Kardashev

**Lunar helium-3 and the industrial base beneath the Kardashev curve.** A technical white paper.

Live site: https://kardashev.aft.page/ (canonical)
This repository is the public artifact: the paper, the reproducible arithmetic, and the print PDF.

## What is here

- `kardashev-white-paper.md` — the paper (canonical source).
- `kardashev-white-paper.pdf` — the print build, 15 pages.
- `scripts/reproduce.py` — recomputes every number a reader can check from public constants plus the paper's labelled assumptions.
- `REPRODUCTION.md` — the exact boundary between what you can verify here and what stays internal.

## Verify

```sh
python3 scripts/reproduce.py
```

No dependencies.

## What is not here

The F1/F2 engineering design basis (parameterised models, quantity records, CAD/STEP snapshots, review records) is internal to the programme. This repository publishes the white paper and the arithmetic that does not depend on it. Questions about a specific claim in the paper should be answerable from the paper plus `scripts/reproduce.py` plus the named public sources; when they are not, the paper labels the number an assumption or an unknown.

## Review status

All numbered sections had internal fresh-context reviews (requirement fit, citation screening, prose, technical pass) on 12–13 November 2026. The document has not been independently verified, peer-reviewed, or checked against hardware. It is a working document, not an offer or a solicitation.

## Rights

All rights reserved. Contact via the site.
