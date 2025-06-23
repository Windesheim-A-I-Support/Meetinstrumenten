# ==============================================================================
# Monique IWB Project - Step 3: Psychometric Analysis
#
# This script extracts quantitative psychometric data (e.g., Cronbach's Alpha)
# from text fields, saves the clean data, and generates comparative plots.
# ==============================================================================

import litstudy
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import re
from pathlib import Path

# --- 1. Configuration ---
INPUT_DOCSET_PATH = Path("output/01_cleaned_doc_set.pkl")
OUTPUT_DIR = Path("output/03_psychometric_outputs")

# --- ACTION REQUIRED: CONFIGURE THESE VARIABLES ---

# 1. Tell the script which column holds the NAME of the questionnaire/instrument.
#    This key must match one you defined in the COLUMN_MAPPING in script 01.
INSTRUMENT_NAME_COLUMN = 'iwb_measurement' # <-- EDIT THIS if needed

# 2. Tell the script which column contains the TEXT describing the psychometric properties.
#    This is the column we will be searching inside.
PSYCHOMETRIC_TEXT_COLUMN = 'iwb_measurement' # <-- EDIT THIS if needed

# 3. Define the metrics to extract.
#    The key is the name of our new clean column.
#    The value is a Regular Expression (Regex) pattern to find the number.
#    I have provided robust examples for common metrics.
METRICS_TO_EXTRACT = {
    "cronbach_alpha": r"(?:cronbach|alpha)\'?(?:s)?\s*(?:is|=|\:)\s*(\.?\d{1,3})",
    "rmsea": r"RMSEA\s*(?:is|=|\:)\s*(\.?\d{1,3})",
    "srmr": r"SRMR\s*(?:is|=|\:)\s*(\.?\d{1,3})",
    "cfi": r"CFI\s*(?:is|=|\:)\s*(\.?\d{1,3})",
    "tli": r"TLI\s*(?:is|=|\:)\s*(\.?\d{1,3})",
}
# ----------------------------------------------------

# Ensure the output directory exists
OUTPUT_DIR.mkdir(exist_ok=True, parents=True)


# --- 2. Main Execution ---
def main():
    """Main function to run the entire analysis pipeline."""
    print("--- Starting Script 03: Psychometric Analysis ---")
    
    # Check for input file
    if not INPUT_DOCSET_PATH.exists():
        print(f"\nERROR: Input file not found: '{INPUT_DOCSET_PATH}'")
        print("Please run '01_load_and_explore.py' successfully before running this script.")
        exit()
        
    # Load the cleaned data from script 01
    print(f"Loading cleaned data from '{INPUT_DOCSET_PATH}'...")
    doc_set = litstudy.load_document_set(INPUT_DOCSET_PATH)
    
    # Convert to a pandas DataFrame for easier manipulation
    df = doc_set.to_frame()

    # --- Data Extraction ---
    print("\n--- Extracting psychometric values using Regex ---")
    
    # Create a results DataFrame with the unique ID and instrument name
    try:
        results_df = df[['id', 'title', INSTRUMENT_NAME_COLUMN]].copy()
        results_df.rename(columns={INSTRUMENT_NAME_COLUMN: 'instrument'}, inplace=True)
    except KeyError as e:
        print(f"\nERROR: The column '{e}' was not found in your dataset.")
        print("Please check the INSTRUMENT_NAME_COLUMN and PSYCHOMETRIC_TEXT_COLUMN variables.")
        exit()

    # Iterate through each metric defined in the configuration
    for metric, pattern in METRICS_TO_EXTRACT.items():
        print(f"Searching for '{metric}'...")
        # Use .str.extract() with the regex pattern to find the first matching number
        # We ensure the source column is treated as a string to avoid errors.
        extracted_series = df[PSYCHOMETRIC_TEXT_COLUMN].astype(str).str.extract(pattern, flags=re.IGNORECASE)
        
        # Convert the extracted text to a numeric value
        results_df[metric] = pd.to_numeric(extracted_series[0], errors='coerce')

    # Drop rows where no psychometric data was found at all
    metrics_only = results_df.drop(columns=['id', 'title', 'instrument'])
    results_df.dropna(subset=metrics_only.columns, how='all', inplace=True)

    if results_df.empty:
        print("\nWARNING: No psychometric data could be extracted with the current patterns.")
        print("Please check your source data and the regex patterns in METRICS_TO_EXTRACT.")
        exit()

    # Save the clean, extracted data to a CSV file
    extracted_data_path = OUTPUT_DIR / "extracted_psychometric_data.csv"
    results_df.to_csv(extracted_data_path, index=False)
    print(f"\n✓ Clean extracted data saved to: {extracted_data_path}")

    # --- Visualization ---
    print("\n--- Generating comparison plots ---")
    for metric in METRICS_TO_EXTRACT.keys():
        # Create a plot only if we found data for that metric
        if results_df[metric].notna().sum() > 1:
            plt.figure(figsize=(12, 8))
            
            # Use Seaborn for beautiful box plots
            sns.boxplot(data=results_df, x=metric, y='instrument', palette="viridis")
            
            plt.title(f"Comparison of '{metric.replace('_', ' ').title()}' Across Instruments", fontsize=16)
            plt.xlabel(metric.upper(), fontsize=12)
            plt.ylabel("Instrument", fontsize=12)
            plt.tight_layout()
            
            plot_path = OUTPUT_DIR / f"plot_{metric}_comparison.png"
            plt.savefig(plot_path, dpi=300)
            print(f"✓ Comparison plot saved to: {plot_path}")
            plt.close() # Close the figure to free up memory

    print(f"\n{'='*60}\n✅ All psychometric analysis is complete.\n{'='*60}")
    print(f"Check the '{OUTPUT_DIR}' folder for the data file and plots.")


if __name__ == "__main__":
    main()