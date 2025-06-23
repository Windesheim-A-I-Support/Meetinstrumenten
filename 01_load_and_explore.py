# ==============================================================================
# Monique IWB Project - Step 1: Load, Convert, and Initial Exploration
#
# This script reads the custom Excel file, converts it into a litstudy
# DocumentSet, and performs a basic timeline analysis to verify the process.
#
# v3: Corrected the exact Excel filename.
# ==============================================================================

import pandas as pd
import litstudy
from pathlib import Path

# --- 1. Configuration ---
# The script will look for your files in this subfolder
DOCUMENTS_DIR = Path("documenten")

# UPDATED: Using the exact filename you provided.
# Make sure to add the .xlsx extension if your file has one.
INPUT_EXCEL_FILE = DOCUMENTS_DIR / "06-06-2025 Analyse tabel scoping review MM (2).xlsx"

OUTPUT_DIR = Path("output")

# Ensure the output directory exists
OUTPUT_DIR.mkdir(exist_ok=True)


# --- 2. Define the Column Mapping (ACTION REQUIRED) ---
#
# This is a PLACEHOLDER. The script will help you fill this out.
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


# --- 3. Load and Validate Data ---
print(f"Loading data from '{INPUT_EXCEL_FILE}'...")
if not INPUT_EXCEL_FILE.exists():
    print(f"\nERROR: Data file not found at the specified path!")
    print(f"Please double-check the filename and folder structure.")
    print(f"I am looking for: {INPUT_EXCEL_FILE}")
    exit()

df = pd.read_excel(INPUT_EXCEL_FILE)

# --- 4. SMART CHECK: Find column names and give instructions ---
print("\n--- Validating Column Mapping ---")

# Check if the user has updated the mapping from its default placeholder state
is_still_placeholder = COLUMN_MAPPING.get('title') == 'title' and COLUMN_MAPPING.get('authors') == 'authors'

if is_still_placeholder:
    print("\nACTION REQUIRED: Please configure the COLUMN_MAPPING in this script.")
    print("I have found the following columns in your Excel file:")
    print("----------------------------------------------------")
    for col in df.columns:
        print(f"'{col}'")
    print("----------------------------------------------------")
    print("\nINSTRUCTIONS:")
    print("1. Open this Python script (`01_load_and_explore.py`) in an editor.")
    print("2. Find the 'COLUMN_MAPPING' section (around line 30).")
    print("3. Replace the placeholder names (like 'title', 'authors') with the correct names from the list above.")
    print("4. Save the script and run it again.")
    exit() # Stop the script gracefully until the user configures it.
else:
    print("✓ Column mapping has been edited. Proceeding to analysis.")


# --- 5. Convert to litstudy DocumentSet ---
print("\nConverting DataFrame to litstudy.DocumentSet...")
try:
    doc_set = litstudy.sources.load_dataframe(df, mapping=COLUMN_M nutty)
    print("Conversion successful.")
except KeyError as e:
    print(f"\nERROR: A column in your mapping is still incorrect: {e}")
    print("Please double-check your COLUMN_MAPPING variable against the column list.")
    exit()


# --- 6. Final Analysis ---
print("\n--- Initial Analysis ---")
print(doc_set)  # Display a summary of the DocumentSet

print("\nGenerating publication timeline plot...")
fig = litstudy.plot_year_histogram(doc_set)
output_path = OUTPUT_DIR / "01_publication_timeline.png"
fig.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"✓ SUCCESS! Timeline plot saved to: {output_path}")