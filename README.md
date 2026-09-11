# AI-Enabled OpEx toolkit — public familiarisation site

**Live site: https://nova-reperta-consulting.github.io/opex-toolkit-demo/**

A read-only look at Nova Reperta's AI-enabled OpEx delivery system, published so colleagues can get familiar with it before running an analysis on a real client.

**Everything on this site is sample data.** Northwind Assurance is an insurer we invented. Every figure, quote and finding in the worked examples was written for this site. No real engagement material belongs in this repository.

## Where to start

Three links, in this order:

1. **[The dashboard](https://nova-reperta-consulting.github.io/opex-toolkit-demo/engagement-dashboard.html)** — where the work is configured and run. Set up the wave, decide which analyses run on which team, then read the findings back. It opens on the filled-in Northwind wave; *Clear the demo data* in the sidebar turns it into an empty tool you can configure yourself.
2. **[The map](https://nova-reperta-consulting.github.io/opex-toolkit-demo/opex-constellation.html)** — every analysis in the toolkit, what it measures, what state it is in, and the three steps to run it.
3. **[The worked example](https://nova-reperta-consulting.github.io/opex-toolkit-demo/sandbox/)** — the Northwind engagement read end to end: thirteen analyses on one team, one set of facts.

## What is here

| Page | What it is |
| --- | --- |
| `index.html` | The front door |
| `engagement-dashboard.html` | The engagement dashboard — configure a wave, run the analyses, read the findings |
| `opex-constellation.html` | The map of the toolkit: every analysis, its state, and the three steps to run it |
| `sandbox/index.html` | The Northwind Assurance engagement, read end to end |
| `sandbox/*.html` | Thirteen finished analyses, as the client sees them |
| `sandbox/*.WORKING.html` | The working copy of eleven of them — the unlocked build you edit live in a workshop |

The thirteen: executive summary, hypothesis tree, OTE waterfall, MAE, AI opportunity heatmap, org baseline, process map, service blueprint, RACI diagnostic, data readiness, performance wheel, skills wheel, team barometer.

## Why this repo is separate from the marketplace

GitHub Pages will not serve a private repository below Enterprise Cloud, so publishing means a public repository. The private marketplace repo carries real client output and must never be published. This repo holds only generated, invented material — that separation is the safeguard, not a review step.

## Before every commit

```
python3 check_public.py
```

It refuses names from real engagements and the confidentiality mark that private deliverables carry. A push cannot be undone, so run it even when the change looks trivial.

## Updating the site

These pages are generated, not hand-edited:

- the worked examples come from `sandbox-northwind/` in the Quickscan Builder project. Author a capture, render it with the instrument's own script, then swap the confidentiality mark.
- the constellation is built from the private working copy by `build_public.js`, which keeps only the regenerated examples and clears every other example path.
- the type scale and the read mode that keeps the artefacts legible on a phone live in the shared brand layer. Change `brand.css` and run `sync-brand.sh`; do not patch an individual file.

Editing a page here by hand means the next regeneration silently overwrites it.

Files go up through GitHub's web upload page, one folder at a time. Drop them **into the folder they belong to** — starting the drag from the parent folder puts everything one level too deep.
