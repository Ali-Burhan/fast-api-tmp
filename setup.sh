#!/bin/bash#!/bin/bash



# FastAPI Speech Translation API - Setup Script# FastAPI Speech Translation API - Setup Script

# For Linux and macOS# For Linux and macOS



set -e  # Exit on errorset -e  # Exit on error



echo "=========================================="echo "=========================================="

echo "FastAPI Speech Translation API Setup"echo "FastAPI Speech Translation API Setup"

echo "=========================================="echo "=========================================="

echo ""echo ""



# Color codes for output# Color codes for output

RED='\033[0;31m'RED='\033[0;31m'

GREEN='\033[0;32m'GREEN='\033[0;32m'

YELLOW='\033[1;33m'YELLOW='\033[1;33m'

NC='\033[0m' # No ColorNC='\033[0m' # No Color



# Function to print colored messages# Function to print colored messages

print_success() {print_success() {

    echo -e "${GREEN}✓ $1${NC}"    echo -e "${GREEN}✓ $1${NC}"

}}



print_error() {print_error() {

    echo -e "${RED}✗ $1${NC}"    echo -e "${RED}✗ $1${NC}"

}}



print_info() {print_info() {

    echo -e "${YELLOW}→ $1${NC}"    echo -e "${YELLOW}→ $1${NC}"

}}



# Initialize pyenv if it exists# Initialize pyenv if it exists

if command -v pyenv &> /dev/null; thenif command -v pyenv &> /dev/null; then

    print_info "Initializing pyenv..."    print_info "Initializing pyenv..."

    export PYENV_ROOT="$HOME/.pyenv"    export PYENV_ROOT="$HOME/.pyenv"

    export PATH="$PYENV_ROOT/bin:$PATH"    export PATH="$PYENV_ROOT/bin:$PATH"

    eval "$(pyenv init --path 2>/dev/null || true)"    eval "$(pyenv init --path 2>/dev/null || true)"

    eval "$(pyenv init - 2>/dev/null || true)"    eval "$(pyenv init - 2>/dev/null || true)"

fifi



# Check for Python 3.13# Check for Python 3.13

print_info "Checking for Python 3.13..."print_info "Checking for Python 3.13..."



# Try different Python commands# Try different Python commands

PYTHON_CMD=""PYTHON_CMD=""

PYTHON_VERSION=""PYTHON_VERSION=""

for cmd in python3.13 python3 python; dofor cmd in python3.13 python3 python; do

    if command -v $cmd &> /dev/null; then    if command -v $cmd &> /dev/null; then

        # Get version, handling different output formats        # Get version, handling different output formats

        version=$($cmd --version 2>&1 | grep -oP '\d+\.\d+(\.\d+)?' | head -1)        version=$($cmd --version 2>&1 | grep -oP '\d+\.\d+(\.\d+)?' | head -1)

        if [ -n "$version" ]; then        version=$($cmd --version 2>&1 | grep -oP '\d+\.\d+(\.\d+)?' | head -1)

            major=$(echo $version | cut -d. -f1)        if [ -n "$version" ]; then

            minor=$(echo $version | cut -d. -f2)            major=$(echo $version | cut -d. -f1)

                        minor=$(echo $version | cut -d. -f2)

            if [ "$major" -eq 3 ] && [ "$minor" -ge 13 ]; then            

                PYTHON_CMD=$cmd            if [ "$major" -eq 3 ] && [ "$minor" -ge 13 ]; then

                PYTHON_VERSION=$version                PYTHON_CMD=$cmd

                print_success "Found Python $version at $(which $cmd)"                PYTHON_VERSION=$version

                break                print_success "Found Python $version at $(which $cmd)"

            fi                break

        fi            fi

    fi        fi

done    fi

done

if [ -z "$PYTHON_CMD" ]; then

    print_error "Python 3.13 or higher is required but not found!"if [ -z "$PYTHON_CMD" ]; then

    echo ""    print_error "Python 3.13 or higher is required but not found!"

    echo "Please install Python 3.13+ from:"    echo ""

    echo "  - pyenv: pyenv install 3.13.0 && pyenv global 3.13.0"    echo "Please install Python 3.13+ from:"

    echo "  - macOS: brew install python@3.13"    echo "  - pyenv: pyenv install 3.13.0 && pyenv global 3.13.0"

    echo "  - Ubuntu/Debian: sudo apt install python3.13"    echo "  - macOS: brew install python@3.13"

    echo "  - Or download from: https://www.python.org/downloads/"    echo "  - Ubuntu/Debian: sudo apt install python3.13"

    echo ""    echo "  - Or download from: https://www.python.org/downloads/"

    echo "For pyenv users, see PYENV_GUIDE.md for detailed instructions."    echo ""

    exit 1    echo "For pyenv users, see PYENV_GUIDE.md for detailed instructions."

fi    exit 1

fi

# For pyenv users, set the local version to ensure consistency

if command -v pyenv &> /dev/null; then# For pyenv users, set the local version to ensure consistency

    # Check if the version is actually installed in pyenvif command -v pyenv &> /dev/null; then

    if pyenv versions --bare | grep -q "^${PYTHON_VERSION}$"; then    # Check if the version is actually installed in pyenv

        print_info "Setting pyenv local version to $PYTHON_VERSION..."    if pyenv versions --bare | grep -q "^${PYTHON_VERSION}$"; then

        pyenv local $PYTHON_VERSION        print_info "Setting pyenv local version to $PYTHON_VERSION..."

        print_success "Pyenv local version set to $PYTHON_VERSION"        pyenv local $PYTHON_VERSION

    else        print_success "Pyenv local version set to $PYTHON_VERSION"

        print_info "Note: Python $PYTHON_VERSION found but not managed by pyenv"    else

        print_info "Skipping pyenv local version setting"        print_info "Note: Python $PYTHON_VERSION found but not managed by pyenv"

    fi        print_info "Skipping pyenv local version setting"

fi    fi

fi

echo ""

echo ""

# Check if virtual environment already exists

if [ -d "venv" ]; then# Check if virtual environment already exists

    print_info "Virtual environment already exists."if [ -d "venv" ]; then

    read -p "Do you want to recreate it? (y/N): " -n 1 -r    print_info "Virtual environment already exists."

    echo ""    read -p "Do you want to recreate it? (y/N): " -n 1 -r

    if [[ $REPLY =~ ^[Yy]$ ]]; then    echo ""

        print_info "Removing existing virtual environment..."    if [[ $REPLY =~ ^[Yy]$ ]]; then

        rm -rf venv        print_info "Removing existing virtual environment..."

    else        rm -rf venv

        print_info "Using existing virtual environment."    else

    fi        print_info "Using existing virtual environment."

fi    fi

fi

# Create virtual environment if it doesn't exist

if [ ! -d "venv" ]; then# Create virtual environment if it doesn't exist

    print_info "Creating virtual environment..."if [ ! -d "venv" ]; then

    $PYTHON_CMD -m venv venv    print_info "Creating virtual environment..."

    print_success "Virtual environment created"    $PYTHON_CMD -m venv venv

fi    print_success "Virtual environment created"

fi

echo ""

echo ""

# Activate virtual environment

print_info "Activating virtual environment..."# Activate virtual environment

source venv/bin/activateprint_info "Activating virtual environment..."

source venv/bin/activate

# Upgrade pip

print_info "Upgrading pip..."# Upgrade pip

pip install --upgrade pip --quietprint_info "Upgrading pip..."

pip install --upgrade pip --quiet

echo ""

echo ""

# Install dependencies

print_info "Installing dependencies from requirements.txt..."# Install dependencies

pip install -r requirements.txtprint_info "Installing dependencies from requirements.txt..."

pip install -r requirements.txt

print_success "All dependencies installed successfully!"

print_success "All dependencies installed successfully!"

echo ""

echo "=========================================="echo ""

echo "Setup Complete! 🎉"echo "=========================================="

echo "=========================================="echo "Setup Complete! 🎉"

echo ""echo "=========================================="

echo "Next steps:"echo ""

echo "  1. Activate the virtual environment:"echo "Next steps:"

echo "     source venv/bin/activate"echo "  1. Activate the virtual environment:"

echo ""echo "     source venv/bin/activate"

echo "  2. Configure your environment variables:"echo ""

echo "     cp .env.example .env"echo "  2. Configure your environment variables:"

echo "     Then edit .env with your API keys"echo "     cp .env.example .env"

echo ""echo "     Then edit .env with your API keys"

echo "  3. Start the application:"echo ""

echo "     uvicorn app.main:app --reload"echo "  3. Start the application:"

echo ""echo "     uvicorn app.main:app --reload"

echo "  4. Visit the API documentation:"echo ""

echo "     http://localhost:8000/docs"echo "  4. Visit the API documentation:"

echo ""echo "     http://localhost:8000/docs"

echo "For detailed instructions, see INSTALLATION.md"echo ""

echo ""echo "For detailed instructions, see INSTALLATION.md"

echo ""
