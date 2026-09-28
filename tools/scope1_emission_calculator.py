"""
scope1_emission_calculator.py - Calculates metric tons CO2e from natural gas and stationary fuel combustion
"""
import sys
import json


def calculate_scope1(fuel_consumption_json: str):
    import json
    data = json.loads(fuel_consumption_json) if isinstance(fuel_consumption_json, str) else fuel_consumption_json
    diesel = data.get("gallons_diesel", 0.0)
    gas = data.get("therms_natural_gas", 0.0)
    
    # EPA factors: diesel ~ 0.01021 MTCO2e/gal, natural gas ~ 0.0053 MTCO2e/therm
    co2e_diesel = diesel * 0.01021
    co2e_gas = gas * 0.0053
    total_mt = round(co2e_diesel + co2e_gas, 2)
    return {
        "gallons_diesel": diesel,
        "therms_natural_gas": gas,
        "scope1_mt_co2e": total_mt,
        "status": "SCOPE1_CALCULATED"
    }


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "scope1-emission-calculator"}))
