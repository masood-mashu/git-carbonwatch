# Segregation of Duties (SOD) Policy: GitCarbonWatch

This document establishes the role boundaries and segregation of duties for the GitCarbonWatch agent.

## Role Separation

### 1. Maker
The Maker role is responsible for authoring carbon activity conversion factors, preparing emissions inventories, and generating automated sustainability diffs.
This role cannot approve or merge its own changes into protected ESG reporting branches.

### 2. Checker
The Checker role is responsible for reviewing, auditing, and validating incoming energy consumption logs, Scope 1/2 emissions, and SBTi trajectories.
This role operates as an impartial auditor to verify compliance with GHG Protocol and CSRD regulatory benchmarks.

### 3. Approver
The Approver role is strictly reserved for human Chief Sustainability Officers and independent ESG verification auditors.
Human approval is required for all public net-zero claims, annual carbon disclosures, and emissions factor overrides.
