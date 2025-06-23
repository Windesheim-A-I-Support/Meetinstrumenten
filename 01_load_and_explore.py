# ==============================================================================
# Monique IWB Project - Step 1: Load, Convert, and Initial Exploration
#
# v4: Automatically finds the single Excel file in the 'documenten' folder.
#     No more manual filename edits required.
# ==============================================================================

import pandas as pd
import litstudy
from pathlib import Path

# --- 1. Configuration ---
# The script will search for your Excel file in this subfolder
DOCUMENTS_DIR = Path("documenten")
OUTPUT_DIR = Path("output")

# Ensure the output directory exists
OUTPUT_DIR.mkdir(exist_ok=True)


# --- 2. Smart File Finder ---
print(f"--- Searching for Excel file in '{DOCUMENTS_DIR}' folder... ---")

# Look for any files ending in .xlsx or .xls
excel_files = list(DOCUMENTS_DIR.glob('*.xlsx')) + list(DOCUMENTS_DIR.glob('*.xls'))

# Handle all possible cases
if len(excel_files) == 0:
    print(f"\nERROR: No Excel files found in the '{DOCUMENTS_DIR}' folder.")
    print("Please make sure your Excel file is placed inside that folder.")
    exit()

if len(excel_files) > 1:
    print(f"\nERROR: Multiple Excel files found in the '{DOCUMENTS_DIR}' folder:")
    for f in excel_files:
        print(f"  - {f.name}")
    print("\nPlease ensure only ONE Excel file is present in the folder and run again.")
    exit()

# If we get here, we found exactly one file. This is our target.
INPUT_EXCEL_FILE = excel_files[0]
print(f"✓ Automatically detected Excel file: '{INPUT_EXCEL_FILE.name}'")


# --- 3. Define the Column Mapping (ACTION REQUIRED) ---
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


# --- 4. Load and Validate Data ---
print(f"\nLoading data from '{INPUT_EXCEL_FILE.name}'...")
df = pd.read_excel(INPUT_EXCEL_FILE)

# --- 5. SMART CHECK: Find column names and give instructions ---
print("\n--- Validating Column Mapping ---")
is_still_placeholder = COLUMN_MAPPING.get('title') == 'title' and COLUMN_MAPPING.get('authors') == 'authors'

if is_still_placeholder:
    print("\nACTION REQUIRED: Please configure the COLUMN_MAPPING in this script.")
    print("I have found the following columns in your Excel file:")
    print("----------------------------------------------------")
    for col in df.columns:
        print(f"'{col}'")
    print("----------------------------------------------------")
    print("\nINSTRUCTIONS:")
    print("1. Open this Python script in an editor.")
    print("2. Find the 'COLUMN_MAPPING' section (around line 40).")
    print("3. Replace the placeholder names (like 'title') with the correct names from the list above.")
    print("4. Save the script and run it again.")
    exit()
else:
    print("✓ Column mapping has been edited. Proceeding to analysis.")


# --- 6. Convert to litstudy DocumentSet ---
print("\nConverting DataFrame to litstudy.DocumentSet...")
try:
    # Note: Corrected a typo here from "nutty" to "MAPPING"
    doc_set = litstudy.sources.load_dataframe(df, mapping=COLUMN_MAPPING)
    print("✓ Conversion successful.")
except KeyError as e:
    print(f"\nERROR: A column in your mapping is still incorrect: {e}")
    print("Please double-check your COLUMN_MAPPING variable against the column list.")
    exit()


# --- 7. Final Analysis ---
print("\n--- Initial Analysis ---")
print(doc_set)

print("\nGenerating publication timeline plot...")
fig = litstudy.plot_year_histogram(doc_set)
output_path = OUTPUT_DIR / "01_publication_timeline.png"
fig.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"✓ SUCCESS! Timeline plot saved to: {output_path}")