# AI-Enabled OpEx toolkit — public familiarisation site

A read-only look at Nova Reperta's OpEx Quickscan toolkit, published so colleagues can get
familiar with it before running an analysis on a real client.

**Everything on this site is sample data.** Northwind Assurance is an insurer we invented. Every
figure, quote and finding in the worked examples was written for this site. No real engagement
material belongs in this repository.

## What is here

| Page | What it is |
| --- | --- |
| `index.html` | The front door |
| `opex-constellation.html` | The map of the toolkit: every analysis, its state, and the three steps to run it |
| `sandbox/index.html` | The Northwind Assurance engagement, read end to end |
| `sandbox/*.html` | Five finished analyses, each as a client build and a working copy |

## Why this repo is separate from the marketplace

GitHub Pages will not serve a private repository below Enterprise Cloud, so publishing means a
public repository. The private marketplace repo carries real client output and must never be
published. **This repo holds only generated, invented material** — that separation is the
safeguard, not a review step.

## Before every commit

    python3 check_public.py

It refuses names from real engagements and the confidentiality mark that private
deliverables carry. A push cannot be
undone, so run it even when the change looks trivial.

## Updating the site

These pages are generated, not hand-edited:

- the worked examples come from `sandbox-northwind/` in the Quickscan Builder project. Author a
  capture, render it with the instrument's own script, then swap the confidentiality mark.
- the constellation is built from the private working copy by `build_public.js`, which keeps only
  the regenerated examples and clears every other example path.

Editing a page here by hand means the next regeneration silently overwrites it.

## Still to come

Six analyses are being built on the same engagement and will appear in the sandbox as they land:
the org baseline, the OTE waterfall, the service blueprint, the RACI diagnostic, the executive
summary and the hypothesis tree.
