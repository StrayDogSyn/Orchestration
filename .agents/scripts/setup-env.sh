#!/bin/bash
set -e

echo "🔧 Setting up The AI Orchestrator development environment..."
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check Python version
echo "Checking Python version..."
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python 3 not found. Please install Python 3.10+${NC}"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
REQUIRED_VERSION="3.10"

if [ "$(printf '%s\n' "$REQUIRED_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" != "$REQUIRED_VERSION" ]; then
    echo -e "${RED}❌ Python 3.10+ required. Found: $PYTHON_VERSION${NC}"
    exit 1
fi

echo -e "${GREEN}✓ Python $PYTHON_VERSION${NC}"

# Create virtual environment
if [ ! -d "venv" ]; then
    echo ""
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo -e "${GREEN}✓ Virtual environment created${NC}"
else
    echo -e "${YELLOW}⚠️  Virtual environment already exists${NC}"
fi

# Activate virtual environment
echo ""
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo ""
echo "Upgrading pip..."
pip install --upgrade pip -q
echo -e "${GREEN}✓ Pip upgraded${NC}"

# Install dependencies
if [ -f "requirements.txt" ]; then
    echo ""
    echo "Installing dependencies..."
    pip install -r requirements.txt -q
    echo -e "${GREEN}✓ Dependencies installed${NC}"
else
    echo -e "${YELLOW}⚠️  No requirements.txt found${NC}"
fi

# Install dev dependencies
if [ -f "requirements-dev.txt" ]; then
    echo ""
    echo "Installing development dependencies..."
    pip install -r requirements-dev.txt -q
    echo -e "${GREEN}✓ Dev dependencies installed${NC}"
fi

# Setup git hooks
echo ""
echo "Configuring git hooks..."
mkdir -p .git/hooks

# Pre-commit hook
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/bash
# Pre-commit hook: Run linters before commit

echo "Running pre-commit checks..."

# Activate venv if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Run Black (formatting check)
if command -v black &> /dev/null; then
    echo "Checking formatting with Black..."
    black --check . || {
        echo "❌ Black formatting issues found. Run: black ."
        exit 1
    }
fi

# Run Flake8 (linting)
if command -v flake8 &> /dev/null; then
    echo "Linting with Flake8..."
    flake8 . || {
        echo "❌ Flake8 linting issues found"
        exit 1
    }
fi

# Run MyPy (type checking)
if command -v mypy &> /dev/null; then
    echo "Type checking with MyPy..."
    mypy . || {
        echo "⚠️  MyPy found type issues"
        # Don't fail on mypy errors, just warn
    }
fi

echo "✓ Pre-commit checks passed"
EOF

chmod +x .git/hooks/pre-commit
echo -e "${GREEN}✓ Pre-commit hook installed${NC}"

# Pre-push hook
cat > .git/hooks/pre-push << 'EOF'
#!/bin/bash
# Pre-push hook: Prevent direct push to main

current_branch=$(git symbolic-ref HEAD | sed -e 's,.*/\(.*\),\1,')

if [ "$current_branch" = "main" ]; then
    echo "❌ Cannot push directly to main branch"
    echo "Please create a pull request instead"
    exit 1
fi

echo "✓ Pushing to branch: $current_branch"
EOF

chmod +x .git/hooks/pre-push
echo -e "${GREEN}✓ Pre-push hook installed${NC}"

# Setup .env if not exists
echo ""
echo "Checking environment variables..."
if [ ! -f ".env" ]; then
    if [ -f ".env.example" ]; then
        echo -e "${YELLOW}⚠️  No .env file found. Copying .env.example...${NC}"
        cp .env.example .env
        echo -e "${YELLOW}⚠️  Please edit .env and add your API keys${NC}"
    else
        echo -e "${YELLOW}⚠️  No .env or .env.example found${NC}"
    fi
else
    echo -e "${GREEN}✓ .env file exists${NC}"
fi

# Copy IDE configurations
echo ""
echo "Applying IDE configurations..."

# VS Code
if [ -d ".agents/config/vscode" ]; then
    mkdir -p .vscode
    cp .agents/config/vscode/*.json .vscode/ 2>/dev/null || true
    echo -e "${GREEN}✓ VS Code config applied${NC}"
fi

# Cursor
if [ -d ".agents/config/cursor" ]; then
    cp .agents/config/cursor/.cursorrules .cursorrules 2>/dev/null || true
    echo -e "${GREEN}✓ Cursor config applied${NC}"
fi

# Continue.dev
if [ -d ".agents/config/continue" ]; then
    mkdir -p .continue
    cp .agents/config/continue/config.json .continue/ 2>/dev/null || true
    echo -e "${GREEN}✓ Continue.dev config applied${NC}"
fi

# Setup git aliases
echo ""
echo "Configuring git aliases..."
git config alias.new-feature '!f() { git checkout -b "feature/$1"; }; f'
git config alias.new-fix '!f() { git checkout -b "fix/$1"; }; f'
git config alias.new-docs '!f() { git checkout -b "docs/$1"; }; f'
echo -e "${GREEN}✓ Git aliases configured${NC}"

# Run validation
echo ""
echo "Running setup validation..."
if [ -f ".agents/scripts/validate-setup.py" ]; then
    python .agents/scripts/validate-setup.py
else
    echo -e "${YELLOW}⚠️  Validation script not found${NC}"
fi

# Summary
echo ""
echo "=========================================="
echo -e "${GREEN}✅ Setup complete!${NC}"
echo "=========================================="
echo ""
echo "Next steps:"
echo "1. Activate venv: source venv/bin/activate"
echo "2. Edit .env with your API keys"
echo "3. Run validation: python .agents/scripts/validate-setup.py"
echo "4. Open your IDE: cursor . (or code .)"
echo ""
echo "Git aliases available:"
echo "  git new-feature <name>  - Create feature branch"
echo "  git new-fix <name>      - Create fix branch"
echo "  git new-docs <name>     - Create docs branch"
echo ""
