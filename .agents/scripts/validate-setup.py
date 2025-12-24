#!/usr/bin/env python3
"""
Setup Validation Script
Validates that The AI Orchestrator development environment is properly configured.

Copyright © 2025 Eric 'Hunter' Petross
StrayDog Syndications LLC | Second Story Initiative
Licensed under MIT License
"""

import os
import sys
import subprocess
from pathlib import Path
from typing import Tuple, List

# Colors for terminal output
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    END = '\033[0m'

def print_header(text: str) -> None:
    """Print section header."""
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{text}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.END}\n")

def check_status(name: str, passed: bool, message: str = "") -> None:
    """Print check status."""
    if passed:
        print(f"{Colors.GREEN}✓{Colors.END} {name}")
        if message:
            print(f"  {Colors.GREEN}{message}{Colors.END}")
    else:
        print(f"{Colors.RED}✗{Colors.END} {name}")
        if message:
            print(f"  {Colors.RED}{message}{Colors.END}")

def check_python_version() -> Tuple[bool, str]:
    """Check Python version >= 3.10."""
    version = sys.version_info
    if version.major == 3 and version.minor >= 10:
        return True, f"Python {version.major}.{version.minor}.{version.micro}"
    return False, f"Python {version.major}.{version.minor} (3.10+ required)"

def check_venv() -> Tuple[bool, str]:
    """Check if running in virtual environment."""
    in_venv = hasattr(sys, 'real_prefix') or (
        hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix
    )
    if in_venv:
        return True, f"Active at {sys.prefix}"
    return False, "Not in virtual environment (recommended)"

def check_package(package: str) -> Tuple[bool, str]:
    """Check if Python package is installed."""
    try:
        __import__(package)
        return True, "Installed"
    except ImportError:
        return False, "Not installed"

def check_env_file() -> Tuple[bool, str]:
    """Check if .env file exists."""
    if Path('.env').exists():
        return True, ".env file found"
    return False, ".env file missing (copy from .env.example)"

def check_api_key(key_name: str) -> Tuple[bool, str]:
    """Check if API key is configured."""
    value = os.getenv(key_name)
    if value and not value.startswith('your_'):
        return True, "Configured"
    return False, "Not configured"

def check_git() -> Tuple[bool, str]:
    """Check if git is initialized."""
    if Path('.git').exists():
        return True, "Repository initialized"
    return False, "Not a git repository"

def check_git_hooks() -> Tuple[bool, str]:
    """Check if git hooks are installed."""
    hooks = ['.git/hooks/pre-commit', '.git/hooks/pre-push']
    installed = all(Path(hook).exists() for hook in hooks)
    if installed:
        return True, "Pre-commit and pre-push hooks installed"
    return False, "Git hooks not installed"

def check_ide_config(ide: str) -> Tuple[bool, str]:
    """Check if IDE configuration exists."""
    configs = {
        'vscode': '.vscode/settings.json',
        'cursor': '.cursorrules',
        'continue': '.continue/config.json'
    }
    
    if ide not in configs:
        return False, "Unknown IDE"
    
    if Path(configs[ide]).exists():
        return True, f"{ide.capitalize()} configured"
    return False, f"{ide.capitalize()} config missing"

def check_command(command: str) -> Tuple[bool, str]:
    """Check if command is available."""
    try:
        subprocess.run([command, '--version'], 
                      capture_output=True, 
                      check=True,
                      timeout=5)
        return True, "Available"
    except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired):
        return False, "Not found"

def run_validation() -> int:
    """Run all validation checks."""
    print(f"\n{Colors.BOLD}The AI Orchestrator - Setup Validation{Colors.END}")
    print(f"{Colors.BOLD}{'='*60}{Colors.END}")
    
    errors = 0
    warnings = 0
    
    # Python Environment
    print_header("Python Environment")
    
    passed, msg = check_python_version()
    check_status("Python 3.10+", passed, msg)
    if not passed:
        errors += 1
    
    passed, msg = check_venv()
    check_status("Virtual Environment", passed, msg)
    if not passed:
        warnings += 1
    
    # Required Packages
    print_header("Required Packages")
    
    required_packages = [
        ('anthropic', True),
        ('google.generativeai', True),
        ('chromadb', True),
        ('openai', False),  # Optional
    ]
    
    for package, required in required_packages:
        passed, msg = check_package(package.replace('.', '/').split('/')[0])
        check_status(package, passed, msg)
        if not passed:
            if required:
                errors += 1
            else:
                warnings += 1
    
    # Development Tools
    print_header("Development Tools")
    
    dev_tools = [
        ('black', True),
        ('flake8', True),
        ('mypy', False),
        ('pytest', True),
    ]
    
    for tool, required in dev_tools:
        passed, msg = check_command(tool)
        check_status(tool, passed, msg)
        if not passed:
            if required:
                errors += 1
            else:
                warnings += 1
    
    # Environment Configuration
    print_header("Environment Configuration")
    
    passed, msg = check_env_file()
    check_status(".env file", passed, msg)
    if not passed:
        errors += 1
    
    if Path('.env').exists():
        # Load .env
        try:
            with open('.env') as f:
                for line in f:
                    if '=' in line and not line.startswith('#'):
                        key, value = line.strip().split('=', 1)
                        os.environ[key] = value
        except Exception:
            pass
        
        api_keys = [
            ('GEMINI_API_KEY', True),
            ('ANTHROPIC_API_KEY', False),
            ('OPENAI_API_KEY', False),
        ]
        
        for key, required in api_keys:
            passed, msg = check_api_key(key)
            check_status(key, passed, msg)
            if not passed:
                if required:
                    errors += 1
                else:
                    warnings += 1
    
    # Git Configuration
    print_header("Git Configuration")
    
    passed, msg = check_git()
    check_status("Git Repository", passed, msg)
    if not passed:
        warnings += 1
    
    if Path('.git').exists():
        passed, msg = check_git_hooks()
        check_status("Git Hooks", passed, msg)
        if not passed:
            warnings += 1
    
    # IDE Configuration
    print_header("IDE Configuration")
    
    for ide in ['vscode', 'cursor', 'continue']:
        passed, msg = check_ide_config(ide)
        check_status(ide.capitalize(), passed, msg)
        # IDE configs are optional, just inform
    
    # Summary
    print_header("Summary")
    
    if errors == 0 and warnings == 0:
        print(f"{Colors.GREEN}{Colors.BOLD}✅ All checks passed!{Colors.END}\n")
        print("Your environment is properly configured.")
        return 0
    
    if errors == 0:
        print(f"{Colors.YELLOW}{Colors.BOLD}⚠️  {warnings} warning(s) found{Colors.END}\n")
        print("Environment is functional but could be improved.")
        return 0
    
    print(f"{Colors.RED}{Colors.BOLD}❌ {errors} error(s) and {warnings} warning(s) found{Colors.END}\n")
    print("Please fix the errors above before proceeding.")
    print("\nNext steps:")
    print("1. Install missing packages: pip install -r requirements.txt")
    print("2. Configure .env: cp .env.example .env && edit .env")
    print("3. Run setup: bash .agents/scripts/setup-env.sh")
    return 1

if __name__ == '__main__':
    sys.exit(run_validation())
