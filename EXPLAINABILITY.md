# GitCarbonWatch Explainability Specification

This document provides a transparent, verifiable architectural breakdown of how **GitCarbonWatch** operates, processes input, makes decisions, and enforces security boundaries.

---

## 1. Input Data and Data Sources Used

GitCarbonWatch consumes facility utility electric bills, corporate fleet fuel card receipts, natural gas smart meter logs, and regional grid carbon intensity tables. These data sources include kilowatt-hours consumed, gallons of diesel and therms of natural gas combusted, flight mileage registries, and EPA eGRID emission coefficients. The agent ingests these inputs in raw JSON, CSV, and utility XML format and parses them into standardized carbon activity ledgers for downstream sustainability analysis. Corporate net-zero baseline registries and Science Based Targets initiative (SBTi) criteria are also monitored as sensitive data sources to ensure ESG disclosure accuracy is strictly maintained.

---

## 2. How It Decides and Reasoning Process

The decision making process follows a deterministic, five-stage analytical pipeline designed to eliminate ambiguity and hallucination. When facility energy activity data is received, the agent first evaluates direct stationary combustion using the scope1-emission-calculator tool to compute metric tons of CO2 equivalent. Next, the reasoning engine invokes the scope2-grid-calculator tool to calculate indirect electricity emissions using regional grid intensity coefficients. Furthermore, enterprise decarbonization trajectory is evaluated using the sbti-trajectory-verifier tool against 1.5°C annual reduction requirements. Finally, the agent correlates all emissions findings against predefined GHG Protocol standards to issue a conclusive verdict of APPROVED, BLOCKED, or NEEDS_REVIEW alongside an automated ESG audit disclosure.

---

## 3. Constraints, Limitations, and Known Issues

GitCarbonWatch operates under strict operational constraints to prevent false positives and non-deterministic behavior across different agent frameworks. GitCarbonWatch operates under strict operational constraints to prevent inaccurate emissions claims and corporate greenwashing across sustainability disclosures. The agent is deliberately limited to GHG Protocol conversion calculations and decarbonization trajectory auditing and cannot physically calibrate physical facility utility meters. Another known issue and limitation is that complex unmetered Scope 3 upstream supply chain estimates may require secondary human review rather than autonomous blocking. Furthermore, the agent enforces a low temperature constraint of 0.1 to maintain strict predictability across all supported export frameworks.
