# .agents/ Directory Installation

## What You're Getting

The complete `.agents/` directory structure for the AI Orchestrator project, including:
- IDE configurations (Cursor, VS Code, Continue.dev, GitHub Copilot)
- Setup automation scripts
- Prompt templates
- Code templates
- Branding assets

## Installation Steps

### For Windows (File Explorer)

1. **Download** the `agents-directory.tar.gz` file
2. **Extract** using 7-Zip or WinRAR:
   - Right-click → 7-Zip → Extract Here
   - This will create a `.agents` folder
3. **Move** the `.agents` folder to your Orchestration directory:
   ```
   C:\Users\Eric Petross\Repos\Projects\Orchestration\.agents\
   ```

### For Windows (PowerShell/Git Bash)

```bash
# Navigate to your Orchestration directory
cd "C:\Users\Eric Petross\Repos\Projects\Orchestration"

# Extract the archive (use the path where you downloaded it)
tar -xzf ~/Downloads/agents-directory.tar.gz

# Verify extraction
ls -la .agents/
```

### For macOS/Linux

```bash
# Navigate to your Orchestration directory
cd ~/Repos/Projects/Orchestration

# Extract the archive
tar -xzf ~/Downloads/agents-directory.tar.gz

# Verify extraction
ls -la .agents/
```

## Verify Installation

After extraction, your Orchestration directory should contain:

```
Orchestration/
├── .agents/              # ← NEW!
│   ├── config/
│   │   ├── cursor/
│   │   ├── vscode/
│   │   ├── continue/
│   │   └── copilot/
│   ├── scripts/
│   ├── prompts/
│   ├── templates/
│   └── README.md
├── modules/
├── docs/
└── README.md
```

## Next Steps

Once installed:

1. **Run setup script:**
   ```bash
   cd Orchestration
   bash .agents/scripts/setup-env.sh
   ```

2. **Validate environment:**
   ```bash
   python .agents/scripts/validate-setup.py
   ```

3. **Configure your IDE:**
   ```bash
   python .agents/scripts/configure-ide.py
   ```

4. **Set up API keys:**
   - Copy `.env.example` to `.env`
   - Add your API keys (at minimum, `GEMINI_API_KEY`)

5. **Reload your IDE** to apply the new settings

## Troubleshooting

### "I don't see .agents/ after extraction"

On Windows, folders starting with `.` are hidden by default:
- File Explorer → View → Show → Hidden items (check the box)

### "Permission denied on setup-env.sh"

Make the scripts executable:
```bash
chmod +x .agents/scripts/*.sh
chmod +x .agents/scripts/*.py
```

### "tar command not found" (Windows)

Use 7-Zip, WinRAR, or install Git Bash which includes tar.

## What's Included

See `.agents/README.md` for complete documentation of all files and configurations.

---

**Created**: December 24, 2025  
**Version**: 1.0.0  
**Repository**: github.com/StrayDogSyn/Orchestration
