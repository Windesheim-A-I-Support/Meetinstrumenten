#!/bin/bash

# ------------------------
# Monique Project Setup Script (Ubuntu 24.04)
# Prepares tools for Excel analysis, NLP, visualization, reporting
# Author: Christiaan Verhoef
# ------------------------

# Exit on error
set -e

# 1. Update system
sudo apt update && sudo apt upgrade -y

# 2. Install system packages
sudo apt install -y \
    python3 python3-pip python3-venv \
    git build-essential libssl-dev libffi-dev python3-dev \
    libgeos-dev gdal-bin libgdal-dev libproj-dev \
    libsqlite3-dev libspatialindex-dev libxml2-dev libxslt1-dev \
    libjpeg-dev zlib1g-dev curl unzip pandoc texlive-xetex texlive-fonts-recommended texlive-plain-generic

# 3. Install VSCode (optional, good editor)
sudo snap install code --classic

# 4. Install Quarto (optional, for PDF / HTML reports)
# Check if quarto is installed first
if ! command -v quarto &> /dev/null
then
    echo "🔹 Installing Quarto CLI..."
    curl -LO https://quarto.org/download/latest/quarto-linux-amd64.deb
    sudo dpkg -i quarto-linux-amd64.deb
    rm quarto-linux-amd64.deb
else
    echo "✅ Quarto already installed."
fi

# 5. Create project folder
mkdir -p ~/monique-project
cd ~/monique-project

# 6. Create Python venv
python3 -m venv .venv
source .venv/bin/activate

# 7. Upgrade pip
pip install --upgrade pip

# 8. Install Python libraries
pip install \
    pandas openpyxl xlrd \
    matplotlib seaborn plotly geopandas \
    scikit-learn sentence-transformers \
    jupyterlab notebook tqdm \
    nbconvert jupyterlab-git

# 9. Optional: Install OpenAI client (for GPT use)
pip install openai

# 10. Freeze requirements for reproducibility
pip freeze > requirements.txt

# 11. Final message
echo ""
echo "✅✅ ALL DONE ✅✅"
echo "To start working:"
echo "----------------------------------"
echo "cd ~/monique-project"
echo "source .venv/bin/activate"
echo "jupyter lab"
echo "----------------------------------"

# End of script
