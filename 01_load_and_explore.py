# ==============================================================================
# Monique IWB Project - Step 1: Load, Convert, and Initial Exploration
#
# This script reads the custom Excel file, converts it into a litstudy
# DocumentSet, and performs a basic timeline analysis to verify the process.
# ==============================================================================

import pandas as pd
import litstudy
from pathlib import Path

# --- 1. Configuration ---
INPUT_EXCEL_FILE = Path("Analyse tabel scoping review MM.xlsx")
OUTPUT_DIR = Path("output")

# Ensure the output directory exists
OUTPUT_DIR.mkdir(exist_ok=True)


# --- 2. Define the Column Mapping (ACTION REQUIRED) ---
#
# EDIT THIS SECTION!
# Replace the placeholder strings on the RIGHT with the ACTUAL column names
# from your Excel file. For example, if your title column is named 'Article Title',
# change 'title': 'Column Name for Title' to 'title': 'Article Title'.
#
# If a field doesn't exist in your Excel file, you can remove that line.
#
COLUMN_MAPPING = {
    # --- Standard Bibliographic Fields ---
    'title':    'title',              # <-- EDIT THIS
    'authors':  'authors',            # <-- EDIT THIS
    'year':     'year',               # <-- EDIT THIS
    'abstract': 'abstract',           # <-- EDIT THIS (Optional but recommended)
    'keywords': 'keywords',           # <-- EDIT THIS (Optional)
    'doi':      'doi',                # <-- EDIT THIS (Optional)

    # --- Monique's Custom Research Columns ---
    # We map these to custom fields within litstudy for later analysis.
    'iwb_related_factors': 'Kolom G',  # <-- EDIT THIS (Factors related to IWB)
    'innovation_definitions': 'Kolom I',  # <-- EDIT THIS (Definitions of "innovation")
    'iwb_measurement': 'Kolom J',      # <-- EDIT THIS (IWB definitions, dimensions, questionnaires)
    'theoretical_foundations': 'Kolom K',# <-- EDIT THIS (Theories and disciplines)
}


# --- 3. Load Data with Pandas ---
print(f"Loading data from '{INPUT_EXCEL_FILE}'...")
if not INPUT_EXCEL_FILE.exists():
    print(f"ERROR: Data file not found! Please place '{INPUT_EXCEL_FILE}' in the project directory.")
    exit()

df = pd.read_excel(INPUT_EXCEL_FILE)
print("Data loaded successfully. Columns found:", list(df.columns))


# --- 4. Convert to litstudy DocumentSet ---
print("\nConverting DataFrame to litstudy.DocumentSet using custom mapping...")
try:
    doc_set = litstudy.sources.load_dataframe(df, mapping=COLUMN_MAPPING)
    print("Conversion successful.")
except KeyError as e:
    print(f"\nERROR: A column in your mapping was not found in the Excel file: {e}")
    print("Please check your COLUMN_MAPPING variable and the Excel file's column names.")
    exit()


# --- 5. Initial Analysis & Verification ---
print("\n--- Initial Analysis ---")
print(doc_set)  # Display a summary of the DocumentSet

# Create and save a timeline plot
print("\nGenerating publication timeline plot...")
fig = litstudy.plot_year_histogram(doc_set)
output_path = OUTPUT_DIR / "01_publication_timeline.png"
fig.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"✓ Timeline plot saved to: {output_path}")