# ==============================================================================
# Monique IWB Project - Step 2: Text Analysis and Clustering
#
# This script loads the cleaned DocumentSet from Step 1 and uses BERTopic
# to identify and visualize themes within the key text columns.
# ==============================================================================

import litstudy
import pandas as pd
from pathlib import Path
from bertopic import BERTopic
from sentence_transformers import SentenceTransformer

# --- 1. Configuration ---
INPUT_DOCSET_PATH = Path("output/01_cleaned_doc_set.pkl")
OUTPUT_DIR = Path("output/02_nlp_outputs")

# Define which custom columns from our dataset we want to analyze.
# These keys must match the ones you defined in the COLUMN_MAPPING in script 01.
COLUMNS_TO_ANALYZE = [
    'innovation_definitions',
    'iwb_measurement',
    'theoretical_foundations',
]

# Ensure the output directory exists
OUTPUT_DIR.mkdir(exist_ok=True, parents=True)


# --- 2. Function to Perform Topic Modeling ---
def analyze_text_column(doc_set, column_key):
    """
    Performs BERTopic analysis on a specified text column of the DocumentSet.
    """
    print(f"\n{'='*60}\n--- Analyzing Column: '{column_key}' ---\n{'='*60}")

    # Create a DataFrame with document IDs and the text from the target column
    records = []
    for doc in doc_set:
        records.append({
            'id': doc.id,
            'title': doc.title,
            'text': getattr(doc, column_key, None) # Safely get the custom attribute
        })
    df = pd.DataFrame(records)

    # --- Data Preparation ---
    # Drop documents where the text is missing or empty for this column
    df.dropna(subset=['text'], inplace=True)
    df = df[df['text'].str.strip() != '']

    if len(df) < 10:
        print(f"WARNING: Not enough data for '{column_key}' (found {len(df)} documents). Skipping.")
        return

    docs_to_analyze = df['text'].tolist()
    print(f"Found {len(docs_to_analyze)} documents with text to analyze for this column.")

    # --- Topic Modeling ---
    print("Initializing topic model (this may download a model on first run)...")
    # Using a multilingual model is robust for scientific literature
    embedding_model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
    
    # We set min_topic_size to 3 to avoid creating tiny, meaningless topics.
    topic_model = BERTopic(
        embedding_model=embedding_model,
        min_topic_size=3,
        verbose=True
    )

    print("Fitting model and identifying topics... (This can take several minutes)")
    topics, _ = topic_model.fit_transform(docs_to_analyze)

    # --- Save Results ---
    print("Analysis complete. Saving results...")
    
    # 1. Save the full topic model itself
    model_path = OUTPUT_DIR / f"{column_key}_model"
    topic_model.save(model_path, serialization="safetensors")

    # 2. Save an interactive HTML chart of the topics
    viz_path = OUTPUT_DIR / f"{column_key}_interactive_topics.html"
    fig = topic_model.visualize_topics()
    fig.write_html(viz_path)
    
    # 3. Save a CSV file with the topic keywords and information
    info_path = OUTPUT_DIR / f"{column_key}_topic_summary.csv"
    topic_info_df = topic_model.get_topic_info()
    topic_info_df.to_csv(info_path, index=False)
    
    # 4. Save a CSV mapping each document to its assigned topic
    doc_path = OUTPUT_DIR / f"{column_key}_document_topic_map.csv"
    df['topic_id'] = topics
    # Merge with topic names for clarity
    df = df.merge(topic_info_df[['Topic', 'Name']], left_on='topic_id', right_on='Topic', how='left')
    df.to_csv(doc_path, index=False)
    
    print(f"✓ Results for '{column_key}' saved in '{OUTPUT_DIR}'")


# --- 3. Main Execution ---
if __name__ == "__main__":
    print("--- Starting Script 02: Text Analysis and Clustering ---")
    
    # Check if the input file from script 01 exists
    if not INPUT_DOCSET_PATH.exists():
        print(f"\nERROR: Input file not found: '{INPUT_DOCSET_PATH}'")
        print("Please run '01_load_and_explore.py' successfully before running this script.")
        exit()
        
    # Load the cleaned data
    print(f"Loading cleaned data from '{INPUT_DOCSET_PATH}'...")
    main_doc_set = litstudy.load_document_set(INPUT_DOCSET_PATH)

    # Run the analysis for each configured column
    for col in COLUMNS_TO_ANALYZE:
        analyze_text_column(main_doc_set, col)
        
    print(f"\n{'='*60}\n✅ All text analysis is complete.\n{'='*60}")
    print(f"Check the '{OUTPUT_DIR}' folder for interactive plots and CSV files.")