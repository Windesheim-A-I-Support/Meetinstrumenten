# create-issues.ps1

$issues = @(
    "Clean up the Excel file from Monique - standardize column names, fix formatting, make it script-ready.",
    "Check and define what each column means - especially G, I, J, K. Label them clearly for scripting.",
    "Convert Excel to a structured format - e.g. CSV or Pandas DataFrame for Python analysis.",
    "Write a script to analyze the number of studies over time - create a bar chart of study count per year.",
    "Write a script to map study locations - produce a world map with number of studies per country.",
    "Cluster the definitions of innovation (column I) using AI - group definitions and compare similarities.",
    "Analyze how IWB is defined and measured (column J) - extract number of dimensions and questionnaires used.",
    "Extract the influencing factors from each study (column G) - list positively and negatively related factors.",
    "Map the theories used (column K) - identify which theories are used and from which disciplines.",
    "Create a scoring system to evaluate questionnaires against COSMIN criteria - use psychometric values from studies.",
    "Score each questionnaire on COSMIN domains - excluding criterion validity.",
    "Create a heatmap or comparison table of all instruments across COSMIN criteria.",
    "Make a summary table of all questionnaires - include name, context, COSMIN score, strengths/weaknesses.",
    "Draft a narrative summary of how IWB is conceptualized - definitions, models, and constructs across studies.",
    "Write a short report or notebook summary - include cleaned data, visuals, and findings for Monique’s article.",
    "Ensure all data stays local - no cloud or uploads, document the local-only workflow.",
    "Prepare for the June 10 hands-on session - bring cleaned data and first visuals."
)

foreach ($task in $issues) {
    gh issue create --title "$task" --body "Auto-generated from project kickoff list"
}
