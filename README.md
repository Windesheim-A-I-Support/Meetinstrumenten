


# Psychometric Review of Innovative Work Behavior (IWB) Questionnaires for Nurses

## Project Title
Systematic Evaluation of Measurement Instruments for Innovative Work Behavior in Nursing Contexts

## Researcher
Monique Mensen  
Lecturer and Researcher, Lectoraat Supply Chain Finance  
Windesheim University of Applied Sciences

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
