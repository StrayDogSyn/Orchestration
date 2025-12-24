# .agents/ - AI Development Configuration

This directory contains IDE configurations, prompt templates, automation scripts, and branding assets for The AI Orchestrator project.

## 📁 Directory Structure

```
.agents/
├── config/           # IDE-specific configurations
│   ├── cursor/       # Cursor IDE settings
│   ├── vscode/       # VS Code settings
│   ├── continue/     # Continue.dev configuration
│   ├── copilot/      # GitHub Copilot instructions
│   └── windsurf/     # Windsurf IDE (future)
├── prompts/          # Reusable prompt templates
├── mcp/              # Model Context Protocol servers
│   ├── filesystem/   # File system MCP configs
│   ├── github/       # GitHub integration MCP
│   └── memory/       # Persistent memory MCP
├── scripts/          # Automation and setup scripts
├── templates/        # Code and branding templates
│   ├── branding/     # Colors, typography, logos
│   ├── python-module/# Python code templates
│   ├── react-component/ # React templates
│   └── documentation/# Doc templates
└── README.md         # This file
```

## 🚀 Quick Start

### 1. Initial Setup

```bash
# Run the automated setup script
bash .agents/scripts/setup-env.sh
```

This will:
- Create Python virtual environment
- Install dependencies
- Set up git hooks
- Configure IDE settings
- Create .env from template

### 2. Validate Setup

```bash
# Check that everything is configured correctly
python .agents/scripts/validate-setup.py
```

### 3. Configure IDE

```bash
# Auto-configure your IDE
python .agents/scripts/configure-ide.py
```

## 🔧 Configuration Files

### Cursor IDE

- `.agents/config/cursor/.cursorrules` - Project-specific AI rules
- `.agents/config/cursor/mcp-servers.json` - MCP server configuration

**Features:**
- Token optimization (Gemini Flash → Claude Sonnet → GPT-4)
- Auto-approved commands (black, flake8, pytest, etc.)
- Branch protection (no direct commits to main)
- Memory management guidelines
- Pedagogy-focused code generation

### VS Code

- `.agents/config/vscode/settings.json` - Editor settings
- `.agents/config/vscode/extensions.json` - Recommended extensions

**Features:**
- Black formatter (line length 88)
- Flake8 linting
- MyPy type checking
- Continue.dev integration
- Git configuration

### Continue.dev

- `.agents/config/continue/config.json` - AI assistant configuration

**Features:**
- Multiple model support (Gemini, Claude, GPT)
- Custom commands (/review, /optimize, /explain, etc.)
- Context providers (diff, open, terminal, problems)
- Tab autocomplete with Gemini Flash

### GitHub Copilot

- `.agents/config/copilot/.github/copilot-instructions.md` - Coding guidelines

**Note:** Continue.dev is the primary AI assistant. Copilot is a fallback.

## 📝 Prompt Templates

### Code Review

```bash
# See .agents/prompts/code-review.md for templates
```

Templates for:
- Standard review (correctness, performance, readability)
- Quick review (fast feedback)
- Deep review (security, architecture, testing)
- Student code review (pedagogical focus)

### Documentation

```bash
# See .agents/prompts/documentation.md for templates
```

Templates for:
- Function/method documentation (Google style)
- Module documentation
- README files
- Architecture Decision Records (ADR)
- API documentation
- Tutorials

## 🎨 Branding

### Colors

```bash
# See .agents/templates/branding/colors.json
```

- Primary: Deep Blue (#1E3A8A)
- Secondary: Electric Teal (#14B8A6)
- Accent: Sunset Orange (#F59E0B)
- Semantic colors (success, error, warning, info)

### Typography

```bash
# See .agents/templates/branding/typography.json
```

- Primary: Inter (body text)
- Headings: Poppins (headings)
- Monospace: JetBrains Mono (code)

## 🔌 MCP Servers

Model Context Protocol (MCP) servers provide external capabilities to AI assistants.

### Available Servers

1. **Filesystem** - File system operations
2. **GitHub** - GitHub API integration
3. **Memory** - Persistent conversation memory

### Configuration

MCP servers are configured in:
- Cursor: `.agents/config/cursor/mcp-servers.json`
- Continue.dev: `.agents/config/continue/config.json`

### Environment Variables

```bash
# Required for GitHub MCP server
GITHUB_TOKEN=your_token_here
```

## 📜 Scripts

### setup-env.sh

Automated environment setup:
- Python environment
- Dependencies installation
- Git hooks configuration
- IDE settings

```bash
bash .agents/scripts/setup-env.sh
```

### validate-setup.py

Validates development environment:
- Python version
- Required packages
- API keys configuration
- Git setup
- IDE configuration

```bash
python .agents/scripts/validate-setup.py
```

### configure-ide.py

Auto-configures IDE settings:
- Detects which IDEs are installed
- Copies appropriate configuration files
- Substitutes environment variables

```bash
python .agents/scripts/configure-ide.py
```

## 🔐 Security

### API Keys

Never commit API keys to version control!

- Store keys in `.env` file
- `.env` is in `.gitignore`
- Use `.env.example` as template

### Git Hooks

Pre-commit hook prevents:
- Unformatted code (Black)
- Linting errors (Flake8)
- Type errors (MyPy)

Pre-push hook prevents:
- Direct pushes to main branch

## 📚 Usage Examples

### Using Custom Commands (Continue.dev)

```bash
# In your IDE, use slash commands:
/review          # Rigorous code review
/optimize        # Analyze Big O complexity
/explain         # Educational explanation
/test            # Generate pytest tests
/doc             # Add Google-style docstrings
/refactor        # Comprehensive refactoring
/debug           # Systematic debugging
/curriculum      # Pedagogy-focused help
```

### Using Prompt Templates

```python
# Example: Code review
# Copy template from .agents/prompts/code-review.md
# Fill in the [FILE] and [FOCUS] placeholders
# Paste into your AI assistant
```

### Creating New Modules

```bash
# Use Python module template
cp .agents/templates/python-module/template.py modules/my_module.py

# Fill in placeholders:
# - {module_name}
# - {module_description}
# - {ClassName}
# - {class_description}
```

## 🛠️ Customization

### Adding New IDE Configuration

1. Create directory: `.agents/config/your-ide/`
2. Add configuration files
3. Update `configure-ide.py` to detect and configure your IDE

### Adding New Prompt Templates

1. Create file: `.agents/prompts/your-template.md`
2. Follow existing template format
3. Document in this README

### Adding New MCP Servers

1. Create directory: `.agents/mcp/your-server/`
2. Add server configuration
3. Update IDE configs to include server

## 📖 Documentation

- **Main README**: `/README.md` - Project overview
- **Contributing**: `/CONTRIBUTING.md` - Contribution guidelines
- **Setup Guide**: `/docs/QUICKSTART.md` - Getting started
- **Project Setup**: `/PROJECT_SETUP.md` - Development workflow

## 🤝 Contributing

When contributing to `.agents/` configuration:

1. Test changes thoroughly
2. Update this README
3. Follow existing patterns
4. Document new features
5. Consider backward compatibility

## 📄 License

Copyright © 2025 Eric 'Hunter' Petross  
StrayDog Syndications LLC | Second Story Initiative  
Licensed under MIT License

---

**Last Updated**: December 24, 2025  
**Version**: 1.0.0  
**Status**: Production Ready
