# ==============================================================================
# Monique IWB Project - Step 4: Geospatial Visualization
#
# This script loads the cleaned dataset, extracts the country for each study,
# and generates a world map shaded by the number of studies per country.
# ==============================================================================

import litstudy
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from pathlib import Path
from thefuzz import process # For fuzzy matching country names

# --- 1. Configuration ---
INPUT_DOCSET_PATH = Path("output/01_cleaned_doc_set.pkl")
OUTPUT_DIR = Path("output/04_geospatial_outputs")

# --- ACTION REQUIRED: CONFIGURE THIS VARIABLE ---
#
# Tell the script which column holds the country name for each study.
# This key must match one you defined in the COLUMN_MAPPING in script 01.
# If you don't have a country column, this script won't be able to run.
COUNTRY_COLUMN_KEY = 'country' # <-- EDIT THIS to your country column key
#
# ----------------------------------------------------

# Ensure the output directory exists
OUTPUT_DIR.mkdir(exist_ok=True, parents=True)


# --- 2. Helper function for fuzzy matching ---
def standardize_country_name(messy_name, correct_names):
    """Finds the best match for a messy country name from a list of correct names."""
    if not messy_name or pd.isna(messy_name):
        return None
    # process.extractOne returns the best match and its score
    best_match, score = process.extractOne(messy_name, correct_names)
    # Only accept a match if the similarity score is reasonably high (e.g., > 80)
    if score > 80:
        return best_match
    return None


# --- 3. Main Execution ---
def main():
    """Main function to run the entire analysis pipeline."""
    print("--- Starting Script 04: Geospatial Visualization ---")
    
    # Check for input file
    if not INPUT_DOCSET_PATH.exists():
        print(f"\nERROR: Input file not found: '{INPUT_DOCSET_PATH}'")
        print("Please run '01_load_and_explore.py' successfully before running this script.")
        exit()
        
    # Load the cleaned data
    print(f"Loading cleaned data from '{INPUT_DOCSET_PATH}'...")
    doc_set = litstudy.load_document_set(INPUT_DOCSET_PATH)
    
    # Convert to a pandas DataFrame
    df = doc_set.to_frame()

    # Check if the country column exists
    if COUNTRY_COLUMN_KEY not in df.columns:
        print(f"\nERROR: The specified country column '{COUNTRY_COLUMN_KEY}' was not found in the dataset.")
        print("Please configure the COUNTRY_COLUMN_KEY variable in this script.")
        exit()

    # --- Data Preparation ---
    print("\n--- Preparing geospatial data ---")
    # 1. Count studies per (messy) country name
    country_counts = df[COUNTRY_COLUMN_KEY].value_counts().reset_index()
    country_counts.columns = ['messy_country', 'study_count']
    
    # 2. Load the base world map from geopandas
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    # Get a clean list of official country names
    official_country_names = world['name'].tolist()

    # 3. Standardize country names using our fuzzy matching function
    print("Standardizing country names using fuzzy matching...")
    country_counts['standard_name'] = country_counts['messy_country'].apply(
        lambda x: standardize_country_name(x, official_country_names)
    )
    
    # Sum counts again in case multiple messy names mapped to one standard name
    final_counts = country_counts.groupby('standard_name')['study_count'].sum().reset_index()

    # 4. Merge our study data with the world map data
    merged_map = world.merge(final_counts, left_on='name', right_on='standard_name', how='left')

    # --- Visualization ---
    print("\n--- Generating world map plot ---")
    fig, ax = plt.subplots(1, 1, figsize=(20, 12))

    merged_map.plot(
        column='study_count',          # The value to shade the countries by
        ax=ax,
        legend=True,
        legend_kwds={
            'label': "Number of Studies",
            'orientation': "horizontal",
            'shrink': 0.6
        },
        missing_kwds={                  # How to color countries with no data
            "color": "lightgrey",
            "edgecolor": "white",
            "hatch": "///",
            "label": "No data"
        },
        cmap='viridis'                 # The color scheme
    )

    # --- Final Touches ---
    ax.set_title("Geographic Distribution of IWB Studies", fontsize=20, pad=20)
    ax.set_axis_off() # Remove the latitude/longitude axes for a cleaner look

    # Save the final map image
    output_path = OUTPUT_DIR / "world_map_study_distribution.png"
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"\n✓ World map saved to: {output_path}")

    print(f"\n{'='*60}\n✅ All geospatial analysis is complete.\n{'='*60}")
    print(f"Check the '{OUTPUT_DIR}' folder for your map.")


if __name__ == "__main__":
    main()