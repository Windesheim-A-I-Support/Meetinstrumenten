#!/usr/bin/env python3
import argparse
import logging
import pandas as pd
import json
from pathlib import Path
import litstudy

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
log = logging.getLogger(__name__)

def find_excel_file(directory: Path):
    exts = ("*.xlsx", "*.xls", "*.xlsm")
    files = []
    for ext in exts:
        files.extend(directory.glob(ext))
    names = [f for f in files if f.is_file()]
    if len(names) == 0:
        log.error("No Excel files found in %r", directory)
        return None
    if len(names) > 1:
        log.error("Multiple Excel files found in %r: %s", directory, [f.name for f in names])
        return None
    return names[0]

def main():
    # → 1. Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--docs", type=Path, default=Path("documenten"), help="Folder with Excel")
    parser.add_argument("--out",  type=Path, default=Path("output"), help="Output folder")
    parser.add_argument("--save-mapping", action="store_true", help="Save COLUMN_MAPPING to JSON")
    args = parser.parse_args()

    args.out.mkdir(exist_ok=True, parents=True)

    # → 2. Locate file
    log.info("Searching for Excel in %r...", args.docs)
    excel = find_excel_file(args.docs)
    if not excel:
        return

    log.info("Found Excel file: %s", excel.name)

    # → 3. Load DataFrame
    try:
        df = pd.read_excel(excel)
    except Exception as e:
        log.error("Failed to load Excel: %s", e)
        return

    # → 4. Setup mapping
    COLUMN_MAPPING = get_mapping_example()  # Replace with your actual mapping

    # Validate mapping
    dfcols = set(df.columns)
    mapped = set(COLUMN_MAPPING.values())
    missing = mapped - dfcols
    if missing:
        log.error("Mapping references missing columns: %s", missing)
        log.info("Available columns: %s", dfcols)
        return
    log.info("Column mapping validated!")

    if args.save_mapping:
        outmap = args.out / "column_mapping.json"
        json.dump(COLUMN_MAPPING, open(outmap, "w"), indent=2)
        log.info("Saved mapping to %s", outmap)

    # → 5. Convert to litstudy
    try:
        docs = litstudy.sources.load_dataframe(df, mapping=COLUMN_MAPPING)
    except KeyError as e:
        log.error("Column mapping error: %s", e)
        return
    log.info("Loaded %d documents via litstudy", len(docs))

    # → 6. Generate plots
    plotters = {
        "01_timeline": litstudy.plot_year_histogram,
        "02_affiliations": litstudy.plot_affiliation_histogram,
        "03_authors": litstudy.plot_author_histogram,
    }
    for fname, fn in plotters.items():
        try:
            fig = fn(docs)
            p = args.out / f"{fname}.png"
            fig.savefig(p, dpi=300, bbox_inches="tight")
            log.info("Saved %s", p)
        except Exception as e:
            log.warning("Plot %s failed: %s", fname, e)

    # → 7. Optional: Topic modeling
    try:
        corpus = litstudy.build_corpus(docs, ngram_threshold=0.8)
        tm = litstudy.train_nmf_model(corpus, num_topics=8)
        litstudy.plot_word_distribution(corpus, limit=30, title="Top words in corpus")
        p = args.out / "04_word_dist.png"
        import matplotlib.pyplot as plt; plt.savefig(p, dpi=300, bbox_inches="tight")
        log.info("Saved word distribution: %s", p)
    except Exception as e:
        log.warning("Topic modeling skipped: %s", e)

if __name__ == "__main__":
    main()

# (This goes at the end of your 01_load_and_explore.py script)

# --- 8. Save the Cleaned DocumentSet for the next script ---
print("\nSaving cleaned DocumentSet for the next script...")
output_docset_path = OUTPUT_DIR / "01_cleaned_doc_set.pkl"
litstudy.save_document_set(doc_set, output_docset_path)
print(f"✓ Clean data saved to: {output_docset_path}")