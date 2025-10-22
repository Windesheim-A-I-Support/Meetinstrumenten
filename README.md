


# Psychometric Review of Innovative Work Behavior (IWB) Questionnaires for Nurses

## Project Title
Systematic Evaluation of Measurement Instruments for Innovative Work Behavior in Nursing Contexts

## Researcher
Monique Mensen  
Lecturer and Researcher, Lectoraat Supply Chain Finance  
Windesheim University of Applied Sciences

# Core Problems and Bottlenecks in Academic Data Extraction Projects

## Academic Challenges

### Semantic Ambiguity and Inconsistent Terminology

A pervasive challenge is that different researchers often use varied terms for the same concept, causing confusion and missed connections. For example, in an *Innovative Work Behavior (IWB)* literature review, one study might report a reliability metric as “Cronbach’s alpha” while another refers to the exact same statistic as “internal consistency” or “internal reliability.” In one case, three different papers used three different names for the **same** number – all referring to an identical measurement of reliability. 

This semantic inconsistency means an automated search or extraction can easily overlook relevant data if it doesn’t account for synonyms or variant phrasings. The problem generalizes to other fields as well; for instance, in Supply Chain Finance, the practice known as “Supply Chain Finance” might also be called “Supplier Finance” or “Reverse Factoring” – different names for the same solution. Such ambiguity makes it difficult to aggregate and compare findings across sources, since one must recognize when two terms actually refer to one shared concept.

### Manual, Labor-Intensive Workflows (Excel-Based Research)

Academic data extraction projects today often rely on painstaking manual effort. Researchers frequently collect data from papers by reading and copying values into spreadsheets or tables by hand. In the IWB case, key metrics were copied manually from each article into Excel. This is a common scenario in literature reviews and meta-analyses: dozens of PDF articles are combed through, and key statistics are transcribed into Excel or Word.

Not only is this tedious and time-consuming, it’s also error-prone. Typos or transcription errors can slip in unnoticed, and important context from the source may be lost. Even when done carefully, manual data entry carries a higher risk of mistakes and inconsistencies. For example, nearly **30%** of published papers with Excel gene lists were found to contain mangled gene names due to spreadsheet autocorrect errors — illustrating how fragile Excel workflows can be for data integrity.

Beyond accuracy, these manual processes don’t scale. A task feasible (if unpleasant) for 50 papers becomes virtually impossible for 500. Researchers often end up limiting the scope of their analysis or spending disproportionate effort on grunt work, which is a direct consequence of inefficient workflows.

### Lack of Provenance and Traceability

When data is extracted by hand and compiled in a custom spreadsheet, it often loses clear links to its original source. In academic workflows today, it’s uncommon to see each cell of a summary table explicitly tied to the paper and page it came from. This makes verification difficult: if a number looks surprising or needs double-checking, one must manually dig back through the papers to find it again.

It also undermines trust and transparency — without provenance, colleagues or peer reviewers have to trust that all numbers were transcribed correctly and pertain to the stated references. Anyone revisiting the data faces a time-intensive task to reconstruct the extraction context.

### Reproducibility and Update Challenges

Because of the issues above, academic data extraction projects often suffer from poor reproducibility. If another researcher (or even the original researcher, at a later date) tries to replicate the extracted dataset, there’s no guarantee they would end up with the same results. Minor differences in how a term is interpreted or which numbers are recorded can lead to divergent outcomes. 

For instance, if the inclusion criteria for which metrics to extract aren’t rigorously documented, two people summarizing the same set of papers might pick out slightly different statistics. Furthermore, manual extraction lacks an automatic “paper trail” of operations, so there is no log of steps to replay. This makes it laborious to incorporate new literature: adding one more study means repeating a lot of the manual steps, and potentially redoing analyses from scratch.

In fields where evidence is rapidly evolving (say, new financial regulations affecting supply chain finance, or new studies on a behavioral metric), this inability to seamlessly update the dataset can result in analyses going stale. The cost of re-gathering data is so high that many academic reviews simply freeze their dataset at a point in time.

The broader implication is a reproducibility crisis in microcosm – if these projects aren’t overhauled, the findings may not hold up as reliable because they are built on fragile, non-repeatable extraction processes.

## Technical Challenges

### Brittleness of Regex and Rule-Based Extraction

Many early attempts at automating data extraction rely on regular expressions or hard-coded rules tailored to known document layouts. While these methods can work for very structured sources (e.g., a data table in a consistent format), they struggle with the variability found in academic papers.

Research articles come in a multitude of formats – different publishers, column layouts, fonts, and phrasing styles – so a regex that detects a metric in one paper might fail completely on another. For example, a simple regex to find “Cronbach’s α = …” will miss cases where the author wrote “(alpha)”, or formatted the value in a table cell, or used a synonym like “reliability = …”.

Template-based approaches assume a constant structure, but academic documents rarely adhere to one uniform template. As a result, a rule-based script often needs constant maintenance, adding new patterns for each new paper encountered – a brittle and unsustainable approach.

Moreover, PDFs themselves encode text in sometimes unpredictable ways (columns, hyphenation, encoding issues), so regex patterns might not even see the content in the expected order. This technical bottleneck means that purely rule-based automation hits a ceiling in effectiveness, often catching only the low-hanging fruit and requiring human intervention for anything that deviates from the norm.

### Unstructured Source Data and Document Complexity

Academic documents (and many business documents in fields like finance) are fundamentally unstructured from a machine’s point of view. They mix narrative text with tables, figures, and references. Important data might be buried in a paragraph, inside a table, or even in an image (like a chart or scanned form).

Parsing PDFs – which were designed for faithful human viewing, not data interchange – is notoriously hard. In fact, creating a universal algorithm to perfectly convert arbitrary PDFs into clean text or data is sometimes compared to the difficulty of achieving full self-driving cars in complexity. Tools exist to extract text, but they can mangle the order or lose context (for example, mixing columns out of sequence or misreading special characters).

If some papers are scanned images (common in older literature or certain fields), then OCR is needed, introducing another layer of potential errors (misrecognized characters, etc.). All these factors mean that technical solutions face an uphill battle just to *read* the source material correctly. 

Data extraction systems must be robust to myriad formatting idiosyncrasies, or risk silently dropping or scrambling key information. Without addressing this, any automated pipeline will have blind spots – portions of the data that it simply can’t handle without manual cleanup.

### Scalability and Performance Constraints

Even if basic extraction can be automated on a small scale, scaling up to large document sets is a significant technical challenge. Processing 80 PDFs one by one might be manageable, but what about 800 or 8,000? The computational load (and time required) grows with each document, and naive approaches could become unbearably slow or expensive.

Large-scale text extraction may require distributed computing or specialized indexing to avoid bottlenecks. There’s also the challenge of scaling the *accuracy*: a method that works 90% of the time still yields errors in 10% of documents – across thousands of papers that means many problematic outputs to manually fix.

In supply chain finance use-cases, one might have to ingest streams of contracts or invoices continuously; the extraction system needs to cope with throughput and not fall behind. If the current approach is manual or semi-manual, scaling at all is nearly impossible – adding manpower linearly is often not feasible in academic contexts due to limited research assistance.

Thus, without technical advancement, projects remain stuck in “pilot scale.” The inability to scale means valuable data trapped in literature or documents stays inaccessible at larger volumes, and analyses that require big samples or comprehensive coverage can’t be performed reliably.

### Tooling Fragmentation and Integration Gaps

The technology ecosystem for these projects is often fragmented, forcing researchers to juggle multiple tools and formats. One person’s workflow might involve a PDF reader for highlighting text, an Excel sheet for storing extracted numbers, a statistical software (like SPSS or R) for analysis, and maybe a reference manager for citations – none of which talk to each other seamlessly.

In the IWB case study, even the guidance on tools was fragmented: Monique’s advisor suggested she use a note-taking app (Microsoft OneNote) to organize her data, while a support engineer pointed her towards writing code in a Jupyter Notebook. Meanwhile, she was already working in Excel. This kind of disjointed tooling leads to constant friction: exporting data from one tool and importing into another, re-formatting outputs, copying and pasting between applications.

Every handoff is an opportunity for error (e.g., copying the wrong cell range, or a formatting issue causing data misalignment). It also raises the technical barrier – a researcher has to be proficient in several environments or rely on others for help. The lack of an integrated platform means there’s no single source of truth for the project’s data; updates or corrections in one place may not propagate to others.

Without solving this, any attempt at automation will be only partial – like automating one step of a pipeline that still breaks when the output is manually fed into the next tool. Fragmentation ultimately slows down progress and makes the entire process fragile.

### Data Fidelity and Quality Concerns with Advanced Tools

A tempting solution to some of the above is to use AI or machine learning (for example, employing a language model to read papers and extract values). However, current AI tools come with their own reliability issues. Large language models can *appear* very competent at reading text, but they are known to hallucinate or make up content, especially when asked to extract structured data they weren’t explicitly trained to handle.

In a discussion about applying AI, the support engineer cautioned that using a GPT-like model to fill a table is “not a good option” because the model might **guess** or alter the data rather than accurately report it. In one example, simply asking an AI to reproduce a numeric table without changes led it to output altered numbers – a disastrous outcome for data fidelity.

This highlights a technical pitfall: many AI systems lack a notion of provenance or verification, so their answers cannot be trusted in a critical data pipeline without additional checks. Ensuring quality and correctness of extracted data is therefore a big technical hurdle.

### Implications

Ignoring these technical challenges means any attempt to modernize academic workflows will remain brittle and unreliable. Automation might work in demos but break down in real-world variability. Projects will struggle to move beyond small-scale prototypes, and the dream of AI-assisted literature analysis or document processing will keep hitting practical roadblocks.

In the worst case, flawed automation could introduce new errors into research rather than eliminating them. Overall, not overcoming these bottlenecks leaves us stuck with the status quo: fragmented tools and manual effort, with all the inefficiency and risk that entails.


## Objective
Systematically analyze and compare existing questionnaires used to measure Innovative Work Behavior (IWB) among nurses, with the goal of identifying valid and reliable instruments and building a foundation for a new context-specific questionnaire for community nursing.

## Dataset
- 85 peer-reviewed articles (1990–June 2025)
- Focus: studies measuring IWB in nursing using structured instruments

## Research Questions
1. Which questionnaires have been used to measure IWB among nurses?
2. What psychometric properties are reported for each questionnaire?
3. Are these properties sufficiently strong according to COSMIN criteria?
4. What definitions and dimensional structures of IWB are used across studies?
5. Which influencing factors are statistically associated with IWB?

## Methodology

### Data Structure
Analyzed variables include:
- Study objectives  
- Definitions of IWB  
- Dimensions and scales used  
- Psychometric properties (e.g. RMSEA, SRMR, Cronbach’s alpha)  
- Statistically significant relationships (positive/negative)  
- Theoretical frameworks used

### Evaluation Framework
Using COSMIN 2.0 criteria to assess:
- Content validity  
- Structural validity  
- Internal consistency  
- Cross-cultural validity / measurement invariance  
- Reliability  
- Measurement error  
- Hypotheses testing for construct validity  
- Responsiveness  
(Note: Criterion validity excluded)

### Tooling
- Excel: cleaned and structured database of extracted study data
- Python (Jupyter Notebook): visualization and comparison scripts
- AI (Perplexity): clustering of textual content (study goals, definitions)
- Local-only processing: no cloud or third-party storage

## Planned Outputs
- Overview tables of IWB measurement instruments
- Visualizations (e.g., timeline, world map by study location)
- Psychometric comparison of instruments across contexts
- Thematic summary of IWB definitions and theoretical bases
- Final recommendation of suitable IWB scales for use in district nursing

## Final Goal
Publish a peer-reviewed article that:
- Summarizes existing IWB instruments in nursing contexts
- Assesses their psychometric quality
- Recommends the most robust tools or highlights gaps for development

## Data Governance
- All data remains under the researcher's ownership
- No cloud storage or external uploads
- Full transparency and reproducibility guaranteed

- 24-06-2025

# Project Statusrapport: Systematische Review IWB

### Samenvatting
Het project heeft een cruciale transitie doorgemaakt: van een serie losse ideeën naar een **volledig functionerende, geautomatiseerde data-analyse pijplijn**. De technische fundering en het volledige machinepark zijn succesvol gebouwd en getest. De focus kan nu verschuiven van technische implementatie naar inhoudelijke verfijning.


### Wat We Hebben Gebouwd en Bereikt

*   **✅ 1. Robuuste Projectomgeving**
    *   Er is een geïsoleerde Python-omgeving (`venv`) opgezet.
    *   Alle benodigde softwarebibliotheken worden beheerd via een `requirements.txt`-bestand, wat het project reproduceerbaar maakt.

*   **✅ 2. Automatische PDF-Verzamelaar**
    *   Het `download_pdfs.py`-script kan op basis van een lijst met URL's automatisch bronartikelen downloaden.

*   **✅ 3. Intelligente Index-Assistent**
    *   Het `update_index.py`-script scant de `documenten`-map, herkent nieuwe PDF's, en werkt automatisch de `iwb_data.csv` index bij.

*   **✅ 4. Automatische Data-Extractor**
    *   Het `01_extract_from_pdfs.py`-script leest de PDF's en kan op basis van zoekpatronen (Reguliere Expressies) automatisch relevante tekstfragmenten extraheren.
    *   **Status:** Het mechanisme werkt, maar de zoekpatronen vereisen verdere verfijning voor een completere extractie.

*   **✅ 5. Werkende Analyse-Pijplijn**
    *   De scripts `03_psychometric_analysis.py` en `04_geospatial_visualization.py` zijn succesvol getest. Zodra er data is, kunnen zij:
        *   Psychometrische data analyseren en visualiseren.
        *   Een geografische wereldkaart genereren.

*   **✅ 6. Professioneel Rapportage-Systeem**
    *   Er is een `report.qmd`-template opgezet.
    *   Technische problemen met het genereren van een PDF/Word-document zijn opgelost. Het systeem kan met één klik een rapport genereren.


### Volgende Stappen: De Weg Vooruit

De technische fase is voorbij. De weg vooruit is inhoudelijk, iteratief en gefocust.

*   ### Stap A: De Extractie Perfectioneren
    1.  **Focus op een kleine, beheersbare set:** Kies 3 tot 5 representatieve PDF's.
    2.  **Identificeer formuleringen:** Zoek handmatig in deze PDF's naar de exacte formuleringen voor de te extraheren data.
    3.  **Verfijn de `SEARCH_PATTERNS`:** Werk de `SEARCH_PATTERNS`-dictionary in `01_extract_from_pdfs.py` bij met de gevonden formuleringen totdat de extractie voor de test-set optimaal is.

 technische fundering is gebouwd en getest. De focus verschuift nu naar inhoudelijke verfijning van de data-extractie.


## Wat We Hebben Gebouwd en Bereikt

#### 1. Robuuste Projectomgeving
-   Een geïsoleerde Python-omgeving (`venv`) is opgezet.
-   Softwarebibliotheken worden beheerd via een `requirements.txt`-bestand voor reproduceerbaarheid.

#### 2. Automatische PDF-Verzamelaar
-   Een `download_pdfs.py`-script is ontwikkeld om artikelen te downloaden op basis van een URL-lijst.

#### 3. Intelligente Index-Assistent
-   Het `update_index.py`-script scant de `documenten`-map, herkent nieuwe PDF's, en werkt automatisch de `iwb_data.csv` index bij.

#### 4. Automatische Data-Extractor
-   Het `01_extract_from_pdfs.py`-script leest de inhoud van de PDF's en extraheert tekstfragmenten op basis van zoekpatronen (Reguliere Expressies).
-   **Status:** De functionaliteit is bewezen. De zoekpatronen vereisen verdere verfijning voor compleetheid.

#### 5. Werkende Analyse-Pijplijn
-   De scripts `03_psychometric_analysis.py` en `04_geospatial_visualization.py` zijn functioneel en genereren de beoogde outputs (grafieken, kaarten) op basis van de geëxtraheerde data.

#### 6. Professioneel Rapportage-Systeem
-   Een `report.qmd`-template is opgezet met Quarto.
-   Technische problemen met het genereren van PDF/Word-documenten, inclusief citatie-fouten, zijn opgelost. Het systeem kan met één commando een rapport genereren.

---

## Volgende Stappen

#### Stap A: Extractie Optimaliseren
1.  **Selecteer een focus-set:** Kies 3-5 representatieve PDF's.
2.  **Identificeer formuleringen:** Zoek handmatig in de focus-set naar de exacte formuleringen die auteurs gebruiken voor de te extraheren concepten.
3.  **Verfijn zoekpatronen:** Werk de `SEARCH_PATTERNS`-dictionary in `01_extract_from_pdfs.py` bij met de gevonden formuleringen om de extractie-accuraatheid te verhogen.

#### Stap B: Volledige Analyse Uitvoeren
-   Voer het masterscript `./run_full_project.sh` uit nadat de zoekpatronen zijn verfijnd. Dit genereert een complete set van inhoudelijk rijke resultaten in de `output`-map.

#### Stap C: Rapportage Afronden
-   Vul het `report.qmd`-bestand met de interpretatie, discussie en conclusies op basis van de outputs uit Stap B.

CTT (Classical Test Theory)

A theory of measurement based on the idea that an observed score is the sum of a true score and an error component (Observed Score = True Score + Error). It focuses on the reliability of the total test.

IRT (Item Response Theory)

A modern measurement theory that models the relationship between a person's underlying ability and their probability of getting an individual item correct. It focuses on item-level statistics.

RASCH Model

The simplest form of IRT. It is a one-parameter model that characterizes each item only by its difficulty, assuming all items discriminate equally.

INFIT and OUTFIT Mean Squares

Fit statistics used in the Rasch model to check if individual items fit the model's expectations.

INFIT: Inlier-sensitive fit, focusing on responses from people whose ability is near the item's difficulty.

OUTFIT: Outlier-sensitive fit, more influenced by unexpected responses.

Acceptable Range: Values for both should be between 0.5 and 1.5.

EFA (Exploratory Factor Analysis)

A statistical method used to uncover the underlying factor structure of a set of variables when you do not have a prior hypothesis about that structure.

PFA (Principal Factor Analysis)

A specific extraction method used to perform an Exploratory Factor Analysis. It focuses on shared variance among variables to identify latent factors.

CFA (Confirmatory Factor Analysis)

A statistical method used to test a pre-specified hypothesis about the factor structure of a set of variables. It confirms if the data fits a proposed model.

CFI (Comparative Fit Index)

An incremental fit index used in CFA. It compares the fit of a target model to the fit of a null model where variables are uncorrelated.

Cut-off for good fit: > 0.95

TLI (Tucker-Lewis Index)

An incremental fit index similar to the CFI. It also compares the proposed model to a null model, with an added penalty for model complexity.

Cut-off for good fit: > 0.95

RMSEA (Root Mean Square Error of Approximation)

An absolute fit index that measures the discrepancy between the proposed model and the population covariance matrix, adjusted for model complexity.

Cut-off for good fit: < 0.06

SRMR (Standardized Root Mean Square Residual)

Represents the average standardized difference between the observed correlations in the data and the correlations predicted by the model.

Cut-off for good fit: < 0.08

Z-Standardized Values (Z-scores)

A value that has been rescaled to indicate how many standard deviations it is from the mean of its dataset. The new mean is 0 and the standard deviation is 1.

EVA

This is not a standard acronym in this context and is likely a typo for EFA.
