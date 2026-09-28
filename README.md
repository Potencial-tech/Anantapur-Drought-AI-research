# Multimodal AI-Assisted Drought and Water-Security Assessment — Anantapur

This repository accompanies the research manuscript:

**Multimodal AI-Assisted Drought and Water-Security Assessment of Anantapur District, Andhra Pradesh, India: Climate, Groundwater and Landsat Evidence with a Reproducible ML Pipeline**

## Contents
- `paper/` — manuscript in PDF and DOCX
- `data/` — supporting CSV tables used in the current manuscript
- `figures/` — groundwater and exploratory multimodal visualizations
- `src/` — space for the full reproducible analysis pipeline
- `docs/` — web visualization assets

## Important data-status note
The current version distinguishes reported observations from proposed/future multimodal analysis. The exploratory surface-stress fusion index is explicitly labelled exploratory and should not be interpreted as a validated drought index.

## Planned full pipeline
CHIRPS rainfall → ERA5-Land climate/land-surface variables → Sentinel-2 vegetation indicators → Landsat/MODIS thermal indicators → CGWB groundwater observations → drought indices → machine-learning comparison → temporal validation → spatial drought-risk maps.

## Reproducibility
The final journal version should include the exact data-download dates, processing scripts, model parameters, train/test splits, and validation metrics before publication.
