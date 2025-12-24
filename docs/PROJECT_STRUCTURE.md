# Project Structure & File Organization Rules

**Project**: The AI Orchestrator
**Last Updated**: December 23, 2025
**Status**: Enforced

---

## 🎯 Purpose

This document establishes **mandatory** rules for directory structure and file
organization as the codebase scales. These rules ensure consistency,
maintainability, and clarity across all contributors and AI assistants.

---

## 📁 Root Directory - PROTECTED

### ✅ ALLOWED in Root

Only these file types belong in the project root:

```
Orchestration/
├── README.md                 # Project overview (REQUIRED)
├── LICENSE                   # MIT License (REQUIRED)
├── .gitignore               # Git ignore rules (REQUIRED)
├── .cursorrules             # Cursor IDE rules (auto-generated)
├── .env.example             # Environment template (REQUIRED)
├── .env                     # Local env vars (git-ignored)
├── .markdownlint.json       # Markdown linting config
├── requirements.txt         # Python dependencies (REQUIRED)
├── requirements-dev.txt     # Dev dependencies (REQUIRED)
└── pyproject.toml           # Python project config (optional)
```

### ❌ FORBIDDEN in Root

**NEVER place these in root:**

- ❌ Documentation files (→ `docs/`)
- ❌ Scripts (→ `scripts/`)
- ❌ Test files (→ `tests/`)
- ❌ Lab materials (→ `modules/`)
- ❌ Assets (→ `assets/`)
- ❌ Templates (→ `templates/`)
- ❌ Build artifacts (→ `.gitignore` them)
- ❌ Archive/backup files (→ `backup-docs/` and git-ignore)
- ❌ Setup instructions (→ `docs/setup/`)
- ❌ Installation archives (→ `docs/setup/`)

---

## 📂 Mandatory Directory Structure

### `/docs` - All Documentation

```
docs/
├── README.md                       # Docs index
├── CONTRIBUTING.md                 # How to contribute
├── setup/                          # Setup & installation
│   ├── INSTALLATION_INSTRUCTIONS.md
│   ├── AGENTS_IMPLEMENTATION_COMPLETE.md
│   └── agents-directory.tar.gz
├── technical/                      # Technical documentation
│   ├── README.md
│   ├── API.md
│   ├── ARCHITECTURE.md
│   └── DATABASE_SCHEMA.md
├── pedagogy/                       # Teaching methodology
│   ├── README.md
│   ├── LEARNING_OBJECTIVES.md
│   └── ASSESSMENT_RUBRICS.md
├── research/                       # Research & analysis
│   ├── README.md
│   ├── RESEARCH_PROMPTS.md
│   ├── gemini-responses/
│   ├── perplexity-responses/
│   └── synthesis/
├── prompts/                        # AI prompt templates
│   ├── code-review.md
│   └── documentation.md
├── assessment/                     # Grading & evaluation
│   └── rubrics/
└── archive/                        # Deprecated docs (with dates)
```

### `/modules` - Course Content (Strict Hierarchy)

```
modules/
├── README.md                       # Module index
├── 01-foundations/
│   ├── README.md                   # Module overview
│   ├── lectures/                   # Lecture notes/slides
│   │   ├── 01-architects-advantage.md
│   │   └── 02-prompts-are-functions.md
│   ├── labs/                       # Hands-on labs
│   │   ├── lab-01-fix-ai-homework/
│   │   │   ├── README.md
│   │   │   ├── starter.ipynb
│   │   │   ├── solution.ipynb
│   │   │   ├── BETA_TEST_PROTOCOL.md
│   │   │   └── tracker_original.py
│   │   └── lab-02-prompt-engineering/
│   ├── projects/                   # Module capstone projects
│   │   └── job-tracker-refactor/
│   └── resources/                  # Additional materials
│       ├── readings.md
│       └── cheat-sheets/
├── 02-prompting/
├── 03-orchestration/
├── 04-memory/
├── 05-agents/
└── 06-capstone/
```

**Module Naming Rules:**
- Format: `{number}-{kebab-case-name}/`
- Numbers: `01`, `02`, ..., `10`, `11`, etc. (always 2 digits)
- Names: lowercase, hyphens only, descriptive

### `/scripts` - Automation & Utilities

```
scripts/
├── README.md                       # Script documentation
├── setup/                          # Environment setup
│   ├── install-dependencies.py
│   └── configure-env.sh
├── validation/                     # Testing & validation
│   ├── validate-setup.py
│   └── check-links.py
├── deployment/                     # Deploy scripts
│   └── deploy-to-vercel.sh
└── utils/                          # Utility scripts
    ├── generate-toc.py
    └── format-notebooks.py
```

### `/assets` - Media & Branding

```
assets/
├── README.md                       # Asset catalog
├── branding/                       # Logos, colors, fonts
│   ├── logo.svg
│   ├── logo-dark.svg
│   ├── colors.json
│   └── typography.json
├── diagrams/                       # Architecture diagrams
│   ├── system-overview.svg
│   └── module-flow.mmd
├── icons/                          # UI icons (SVG only)
│   └── *.svg
└── images/                         # Screenshots, photos
    ├── screenshots/
    └── tutorials/
```

**Asset Rules:**
- ✅ SVG for logos, icons, diagrams (vector, small)
- ✅ PNG for screenshots (optimized, <500KB)
- ❌ No PSD, AI, Sketch files (source files in separate repo)
- ❌ No videos in git (use external hosting + links)

### `/templates` - Code Templates

```
templates/
├── README.md                       # Template index
├── python-module/
│   ├── template.py
│   └── test_template.py
├── lecture/
│   └── lecture-template.md
├── lab/
│   ├── README-template.md
│   └── starter-template.ipynb
└── documentation/
    ├── ADR-template.md
    └── API-template.md
```

### `/resources` - External References

```
resources/
├── README.md                       # Resource catalog
├── articles/                       # External articles (links)
│   └── recommended-reading.md
├── videos/                         # Video links (not files)
│   └── tutorial-links.md
└── code-templates/                 # Community templates
```

### `/.agents` - IDE Configuration (Source)

```
.agents/                            # Template configurations
├── README.md                       # Configuration guide
├── config/                         # IDE configs
│   ├── cursor/
│   ├── vscode/
│   ├── continue/
│   └── copilot/
├── prompts/                        # Prompt templates
├── scripts/                        # Setup automation
├── templates/                      # Code templates
└── mcp/                           # MCP server configs
```

**Note**: Active configs (.cursorrules, .continue/, etc.) are git-ignored.
This is the SOURCE for regenerating them.

---

## 📝 File Naming Conventions

### Documentation Files

```
✅ CORRECT:
- README.md                 # Always uppercase
- CONTRIBUTING.md           # Always uppercase
- CHANGELOG.md              # Always uppercase
- LICENSE                   # Always uppercase (no extension)
- 01-lecture-title.md       # Numbered, kebab-case
- api-reference.md          # Lowercase, kebab-case

❌ INCORRECT:
- readme.md                 # Lowercase README
- contributing.txt          # Wrong extension
- Lecture-Title.md          # PascalCase
- api_reference.md          # Snake_case
```

### Python Files

```
✅ CORRECT:
- module_name.py            # Snake_case
- ClassName.py              # PascalCase (only for classes)
- test_module.py            # Test files
- __init__.py               # Dunder files

❌ INCORRECT:
- moduleName.py             # camelCase
- Module-Name.py            # Kebab-case
- MODULE_NAME.py            # SCREAMING_SNAKE
```

### JavaScript/TypeScript Files

```
✅ CORRECT:
- ComponentName.jsx         # PascalCase (React components)
- utility-functions.js      # Kebab-case (utilities)
- api-client.ts             # Kebab-case
- index.js                  # Lowercase (special)

❌ INCORRECT:
- component_name.jsx        # Snake_case
- UtilityFunctions.js       # PascalCase non-component
```

### Jupyter Notebooks

```
✅ CORRECT:
- 01-data-exploration.ipynb      # Numbered, kebab-case
- starter.ipynb                  # Lowercase, descriptive
- solution.ipynb                 # Lowercase, descriptive

❌ INCORRECT:
- Data Exploration.ipynb         # Spaces
- dataExploration.ipynb          # camelCase
- STARTER.ipynb                  # UPPERCASE
```

---

## 🚫 Forbidden Practices

### 1. No Random Files in Root

**Problem**: `analysis.py`, `temp.txt`, `test.ipynb` cluttering root

**Solution**:
- Scripts → `/scripts/utils/`
- Experiments → `/sandbox/` (git-ignored)
- Tests → `/tests/`
- Notes → `/docs/notes/` (git-ignored)

### 2. No Deeply Nested Directories

**Problem**: `modules/01/lectures/week1/day1/morning/intro.md`

**Solution**: Maximum 4 levels deep
```
modules/01-foundations/lectures/01-intro.md  ✅
modules/module1/content/lectures/week1/intro.md  ❌
```

### 3. No Duplicate Files

**Problem**: `README.md` and `readme.txt` in same directory

**Solution**: One README per directory, always `.md` extension

### 4. No Generic Names

**Problem**: `file.py`, `test.py`, `module.py`, `utils.py`

**Solution**: Descriptive names
- `file.py` → `file_validator.py`
- `test.py` → `test_validator.py`
- `utils.py` → `string_utils.py`

### 5. No Version Suffixes in Filenames

**Problem**: `module_v2.py`, `api-final-FINAL.js`, `backup-20250123.md`

**Solution**: Use git for versioning, not filenames
- Delete old versions or archive in `/backup-docs/` (git-ignored)

### 6. No Special Characters

**Problem**: `module#1.py`, `file (copy).js`, `data@2024.csv`

**Solution**: Only alphanumeric, hyphens, underscores
- `module#1.py` → `module-01.py`
- `file (copy).js` → `file-backup.js`
- `data@2024.csv` → `data-2024.csv`

---

## 🔒 Protection Mechanisms

### 1. Git Hooks (Pre-Commit)

Automatically enforced via `.git/hooks/pre-commit`:

```bash
# Check for forbidden files in root
if [[ $(git diff --cached --name-only | grep -E '^[^/]+\.(md|txt|pdf)$' | grep -v README.md | grep -v LICENSE) ]]; then
    echo "❌ Documentation files in root. Move to docs/"
    exit 1
fi

# Check for spaces in filenames
if [[ $(git diff --cached --name-only | grep ' ') ]]; then
    echo "❌ Filenames with spaces detected"
    exit 1
fi
```

### 2. Cursor Rules (AI Enforcement)

In `.cursorrules`:

```plaintext
## File Creation Rules
- NEVER create files in root except: README.md, LICENSE, requirements*.txt
- All documentation → docs/
- All scripts → scripts/
- All tests → tests/
- Labs → modules/{module-name}/labs/
```

### 3. Code Review Checklist

**Before PR approval, verify:**

- [ ] No new files in root (except allowed types)
- [ ] All files follow naming conventions
- [ ] Directory structure follows hierarchy
- [ ] No spaces in filenames
- [ ] No generic names (file.py, test.js)
- [ ] README exists in new directories
- [ ] Assets are optimized (<500KB per file)

---

## 📊 Directory Size Limits

To prevent repository bloat:

| Directory | Max Size | Notes |
|-----------|----------|-------|
| `/docs` | 50 MB | Use external links for large PDFs |
| `/assets/images` | 20 MB | Optimize PNGs, use SVG when possible |
| `/modules` | 100 MB | Keep notebooks clean (clear output) |
| `/scripts` | 5 MB | Scripts only, no data |
| Root | 10 MB | Config files only |

**Enforcement**: Pre-push hook checks directory sizes

---

## 🔄 Migration Path for Existing Files

If you have files in wrong locations:

```bash
# 1. Identify misplaced files
find . -maxdepth 1 -type f ! -name "README.md" ! -name "LICENSE" ! -name ".gitignore" ! -name "requirements*.txt"

# 2. Move to correct locations
mv SETUP_GUIDE.md docs/setup/
mv analyze_data.py scripts/utils/
mv logo.png assets/branding/

# 3. Update any broken links
# Use scripts/utils/check-links.py
```

---

## 🆘 Decision Tree: Where Does This File Go?

```
Is it a Python dependency list?
├─ YES → requirements.txt or requirements-dev.txt (root)
└─ NO ↓

Is it documentation?
├─ YES → docs/{category}/
│   ├─ Setup/install docs → docs/setup/
│   ├─ API docs → docs/technical/
│   ├─ Teaching guides → docs/pedagogy/
│   └─ Research → docs/research/
└─ NO ↓

Is it course content?
├─ YES → modules/{module-number}-{name}/
│   ├─ Lecture notes → lectures/
│   ├─ Labs → labs/
│   ├─ Projects → projects/
│   └─ Resources → resources/
└─ NO ↓

Is it a script or automation?
├─ YES → scripts/{category}/
└─ NO ↓

Is it media (image, logo, diagram)?
├─ YES → assets/{category}/
└─ NO ↓

Is it a code template?
├─ YES → templates/{language-or-type}/
└─ NO ↓

Is it a test file?
├─ YES → tests/{matching-source-structure}/
└─ NO ↓

Is it configuration?
├─ YES → 
│   ├─ IDE config → .agents/config/
│   ├─ Project config → root (.gitignore, .markdownlint.json)
│   └─ Environment → .env.example (root)
└─ NO ↓

If none of above, ask before creating!
```

---

## 🎓 Examples: Correct Placement

### Example 1: New Lecture

**Task**: Add "Lecture 03: Memory Systems"

**Correct**:
```
modules/01-foundations/lectures/03-memory-systems.md
```

**Incorrect**:
```
❌ Lecture-03.md (root)
❌ modules/lectures/memory.md (missing module)
❌ docs/lectures/03-memory-systems.md (wrong top-level)
```

### Example 2: API Documentation

**Task**: Document the API endpoints

**Correct**:
```
docs/technical/API.md
```

**Incorrect**:
```
❌ API_DOCS.md (root)
❌ docs/API.md (missing category)
❌ api-docs.txt (wrong extension)
```

### Example 3: Setup Script

**Task**: Script to install dependencies

**Correct**:
```
scripts/setup/install-dependencies.py
```

**Incorrect**:
```
❌ install.py (root)
❌ setup.py (root - reserved for Python packages)
❌ scripts/install-dependencies.py (missing category)
```

---

## 🚨 Enforcement Level

| Rule Type | Enforcement | Violation Response |
|-----------|-------------|-------------------|
| Root file restrictions | **BLOCKING** | Pre-commit hook fails |
| Naming conventions | **WARNING** | Code review comment |
| Directory structure | **BLOCKING** | PR rejected |
| File size limits | **BLOCKING** | Pre-push hook fails |
| Missing READMEs | **WARNING** | Code review comment |

---

## 📞 Questions?

If unclear where a file belongs:

1. Check this document's decision tree
2. Look for similar existing files
3. Ask in PR review before merging
4. When in doubt: **docs/notes/** (can reorganize later)

---

## 🔄 Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2025-12-23 | Initial structure rules |

---

**Status**: Active & Enforced
**Review Frequency**: Monthly
**Next Review**: 2026-01-23
