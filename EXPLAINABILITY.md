# Explainability & Governance Statement

## Decision Architecture
GitCarbonWatch calculates greenhouse gas emissions using deterministic emissions factors from EPA, DEFRA, and IPCC standards. Multiplying activity data (kWh or gallons) by standard carbon intensity coefficients generates metric tons CO2 equivalent (MTCO2e). If annual reductions fail to meet SBTi 4.2% annual linear reduction gates, the agent flags an off-track trajectory.

## Input Data Provenance
Data inputs include utility smart meter data, fleet fuel card receipts, flight booking records, and EPA eGRID regional emission factor tables.

## Operational Limits & Non-Goals
GitCarbonWatch quantifies reported consumption metrics; it cannot physically verify on-site factory meter calibration without sensor integrity validation.
