"""
sbti_trajectory_verifier.py - Verifies whether annual emission reductions meet the SBTi 1.5C minimum 4.2% annual reduction rate
"""
import sys
import json


def verify_sbti_trajectory(reduction_data_json: str, min_annual_reduction_pct: float = 4.2):
    import json
    data = json.loads(reduction_data_json) if isinstance(reduction_data_json, str) else reduction_data_json
    base = max(data.get("baseline_year_emissions", 1000.0), 0.1)
    curr = data.get("current_year_emissions", 1000.0)
    reduction_pct = ((base - curr) / base) * 100.0
    on_track = reduction_pct >= min_annual_reduction_pct
    return {
        "baseline_emissions": base,
        "current_emissions": curr,
        "reduction_pct": round(reduction_pct, 2),
        "on_track": on_track,
        "status": "SBTI_ON_TRACK" if on_track else "OFF_TRACK_TRAJECTORY"
    }


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "sbti-trajectory-verifier"}))
