"""
scope2_grid_calculator.py - Calculates Scope 2 electricity indirect emissions based on kWh usage and grid factor
"""
import sys
import json


def calculate_scope2(electricity_data_json: str):
    import json
    data = json.loads(electricity_data_json) if isinstance(electricity_data_json, str) else electricity_data_json
    kwh = data.get("kwh_consumed", 10000.0)
    grid_factor = data.get("grid_factor_kg_per_kwh", 0.38) # default US average ~0.38 kg CO2e/kWh
    mt_co2e = (kwh * grid_factor) / 1000.0
    return {
        "kwh_consumed": kwh,
        "grid_factor": grid_factor,
        "scope2_mt_co2e": round(mt_co2e, 2),
        "status": "SCOPE2_CALCULATED"
    }


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "scope2-grid-calculator"}))
