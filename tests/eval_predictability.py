"""
eval_predictability.py - Checkpoint 02 Benchmark Suite for GitCarbonWatch.
"""
import os, sys, unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tools.scope1_emission_calculator import *
from tools.scope2_grid_calculator import *
from tools.sbti_trajectory_verifier import *

class TestGitCarbonWatchPredictability(unittest.TestCase):

    def test_scope1_emission_calculator(self):
        res = calculate_scope1('{"gallons_diesel": 1000, "therms_natural_gas": 500}')
        self.assertGreater(res["scope1_mt_co2e"], 0.0)
        self.assertEqual(res["status"], "SCOPE1_CALCULATED")

    def test_scope2_grid_calculator(self):
        res = calculate_scope2('{"kwh_consumed": 50000, "grid_factor_kg_per_kwh": 0.4}')
        self.assertEqual(res["scope2_mt_co2e"], 20.0)
        self.assertEqual(res["status"], "SCOPE2_CALCULATED")

    def test_sbti_trajectory_verifier(self):
        res = verify_sbti_trajectory('{"baseline_year_emissions": 1000, "current_year_emissions": 950}')
        self.assertTrue(res["on_track"])
        self.assertEqual(res["status"], "SBTI_ON_TRACK")


if __name__ == "__main__":
    unittest.main()
