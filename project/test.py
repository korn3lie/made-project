import os
import subprocess
import pytest

# Define expected output files
EXPECTED_FILES = [
    "../data/electric_car_population.csv",
    "../data/CO.csv",
    "../data/NO2.csv",
    "../data/PM10_Speciation.csv",
    "../data/PM25_Speciation.csv"
]
@pytest.fixture(scope="module", autouse=True)
def run_pipeline():
    """
    Run the pipeline script before tests.
    """
    print("Running pipeline...")
    # Remove any existing output files to ensure a clean state
    for file in EXPECTED_FILES:
        if os.path.exists(file):
            os.remove(file)
    
    # Execute the pipeline script
    subprocess.run(["python", "pipeline.py"], check=True)

def test_output_files_exist():
    """
    Verify that the pipeline generates all expected files.
    """
    print("Running pipeline2...")
    for file in EXPECTED_FILES:
        assert os.path.exists(file), f"Output file {file} was not created."

def test_cleanup_after_execution():
    """
    Test cleanup: Ensure tests can remove generated files if needed.
    """
    for file in EXPECTED_FILES:
        os.remove(file)
        assert not os.path.exists(file), f"Output file {file} was not removed."
