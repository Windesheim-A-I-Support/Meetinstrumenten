#!/bin/bash

# =================================================================================
#  Project Provisioning Script for Ubuntu 24.04
#
#  This script transforms a bland Ubuntu 24.04 system into a complete
#  development environment for the IWB literature review project.
#
#  It installs:
#    1. Core system tools (git, curl, build-essential).
#    2. Visual Studio Code IDE.
#    3. Miniconda for Python environment management.
#    4. A dedicated Conda environment ('iwb-env') with all required libraries.
#    5. Quarto and TinyTeX for scientific publishing and reporting.
#
#  Usage: chmod +x provision_ubuntu.sh && ./provision_ubuntu.sh
# =================================================================================

# --- Configuration ---
CONDA_ENV_NAME="iwb-env"
PYTHON_VERSION="3.10"
QUARTO_VERSION="1.4.553" # Check for the latest version if needed

# Use ANSI escape codes for colored output
GREEN='\033[1;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${YELLOW}Starting full system provisioning for the IWB Project...${NC}"
echo "This will install all necessary tools from system packages, Conda, and Pip."
echo "You will be prompted for your password for 'sudo' commands."

# --- PART 1: SYSTEM-LEVEL DEPENDENCIES ---
echo -e "\n${YELLOW}--- Part 1: Installing Core System Dependencies via APT ---${NC}"
sudo apt-get update
sudo apt-get install -y \
  git \
  curl \
  wget \
  build-essential \
  software-properties-common \
  apt-transport-https

echo -e "${GREEN}✓ Core system dependencies installed.${NC}"


# --- PART 2: VISUAL STUDIO CODE (IDE) ---
echo -e "\n${YELLOW}--- Part 2: Installing Visual Studio Code ---${NC}"
# Add Microsoft GPG key
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg
# Add VS Code repository
sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
rm -f packages.microsoft.gpg
# Install VS Code
sudo apt-get update
sudo apt-get install code -y

echo -e "${GREEN}✓ Visual Studio Code installed successfully.${NC}"


# --- PART 3: MINICONDA & PYTHON ENVIRONMENT ---
echo -e "\n${YELLOW}--- Part 3: Installing Miniconda and the Python Environment ---${NC}"
# Download and install Miniconda
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh
bash ~/miniconda.sh -b -p $HOME/miniconda
rm ~/miniconda.sh

# Initialize Conda in the current shell
eval "$($HOME/miniconda/bin/conda shell.bash hook)"
# And ensure it's initialized for future sessions
conda init

echo -e "${GREEN}✓ Miniconda installed and initialized.${NC}"

# Create the Conda environment
echo -e "\n${YELLOW}Creating Conda environment '${CONDA_ENV_NAME}'...${NC}"
conda create --name "$CONDA_ENV_NAME" python="$PYTHON_VERSION" -y

# Install core libraries via Conda (best for complex dependencies)
echo -e "\n${YELLOW}Installing Python libraries via Conda... (This is the longest step)${NC}"
conda install -n "$CONDA_ENV_NAME" -c conda-forge -y \
  pandas \
  openpyxl \
  matplotlib \
  seaborn \
  plotly \
  geopandas \
  sentence-transformers \
  bertopic \
  scikit-learn \
  jupyterlab

# Install litstudy via Pip from within the Conda environment
echo -e "\n${YELLOW}Installing 'litstudy' from GitHub via Pip...${NC}"
conda run -n "$CONDA_ENV_NAME" pip install git+https://github.com/Windesheim-A-I-Support/litstudy.git

echo -e "${GREEN}✓ Python environment '${CONDA_ENV_NAME}' is fully provisioned.${NC}"


# --- PART 4: QUARTO & LATEX (PUBLISHING TOOLS) ---
echo -e "\n${YELLOW}--- Part 4: Installing Quarto and TinyTeX for Publishing ---${NC}"
# Download and install Quarto
wget "https://github.com/quarto-dev/quarto-cli/releases/download/v${QUARTO_VERSION}/quarto-${QUARTO_VERSION}-linux-amd64.deb"
sudo dpkg -i "quarto-${QUARTO_VERSION}-linux-amd64.deb"
rm "quarto-${QUARTO_VERSION}-linux-amd64.deb"

# Install TinyTeX (LaTeX distribution managed by Quarto)
echo -e "\n${YELLOW}Installing TinyTeX via Quarto...${NC}"
# This command needs to run as the user, not sudo
quarto install tinytex

echo -e "${GREEN}✓ Quarto and TinyTeX installed successfully.${NC}"


# --- PART 5: FINAL SETUP & INSTRUCTIONS ---
echo -e "\n${YELLOW}--- Part 5: Finalizing Setup ---${NC}"
# Create the reproducibility file for the environment
conda env export -n "$CONDA_ENV_NAME" > environment.yml
echo -e "${GREEN}✓ 'environment.yml' file created for reproducibility.${NC}"

echo -e "\n${GREEN}===================================================================${NC}"
echo -e "${GREEN}   ✅  SYSTEM PROVISIONING COMPLETE! ✅   ${NC}"
echo -e "${GREEN}===================================================================${NC}"
echo -e "\n${YELLOW}IMPORTANT: You must CLOSE and REOPEN your terminal for all changes to take effect.${NC}"
echo -e "\nYour next steps are:"
echo -e "  1.  ${YELLOW}Close and reopen your terminal.${NC}"
echo -e "  2.  Clone the project repository: ${GREEN}git clone https://github.com/Windesheim-A-I-Support/litstudy.git${NC} (or your project's repo)"
echo -e "  3.  Navigate into the project folder: ${GREEN}cd litstudy${NC}"
echo -e "  4.  Open the project in VS Code: ${GREEN}code .${NC}"
echo -e "  5.  When VS Code opens, it should auto-detect your '${CONDA_ENV_NAME}' environment."
echo -e "      It will also suggest installing the 'Python' and 'Jupyter' extensions. Please accept."
echo ""
