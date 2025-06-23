# === PART A: Create and activate the virtual environment ===
echo "--- Setting up virtual environment named 'venv' ---"
python3 -m venv venv
source venv/bin/activate
echo "--- Environment 'venv' is now active ---"

# === PART B: Install the necessary libraries ===
echo "--- Installing pandas, openpyxl, matplotlib, and litstudy ---"
pip install pandas openpyxl matplotlib
pip install git+https://github.com/Windesheim-A-I-Support/litstudy.git
echo "--- All libraries installed successfully ---"

# === PART C: Run your Python program ===
echo "--- Running your Python script now... ---"
python3 "01_load_and_explore.py"