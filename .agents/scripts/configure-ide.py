#!/usr/bin/env python3
"""
IDE Auto-Configuration Script
Detects and configures IDE settings for The AI Orchestrator project.

Copyright © 2025 Eric 'Hunter' Petross
StrayDog Syndications LLC | Second Story Initiative
Licensed under MIT License
"""

import os
import json
import shutil
from pathlib import Path
from typing import Optional, Dict, List

class IDEConfigurator:
    """Auto-configure IDE settings."""
    
    def __init__(self):
        self.project_root = Path.cwd()
        self.agents_dir = self.project_root / '.agents'
        self.config_dir = self.agents_dir / 'config'
        
    def detect_ide(self) -> List[str]:
        """Detect which IDEs are being used."""
        ides = []
        
        # Check for VS Code
        if (self.project_root / '.vscode').exists():
            ides.append('vscode')
        
        # Check for Cursor (same as VS Code but with .cursorrules)
        if (self.project_root / '.cursorrules').exists():
            ides.append('cursor')
        
        # Check for Continue.dev
        if (self.project_root / '.continue').exists():
            ides.append('continue')
        
        # Check for PyCharm
        if (self.project_root / '.idea').exists():
            ides.append('pycharm')
        
        return ides
    
    def configure_vscode(self) -> bool:
        """Configure VS Code settings."""
        print("Configuring VS Code...")
        
        source_dir = self.config_dir / 'vscode'
        target_dir = self.project_root / '.vscode'
        
        if not source_dir.exists():
            print("  ⚠️  VS Code config template not found")
            return False
        
        target_dir.mkdir(exist_ok=True)
        
        # Copy settings.json
        if (source_dir / 'settings.json').exists():
            shutil.copy(
                source_dir / 'settings.json',
                target_dir / 'settings.json'
            )
            print("  ✓ settings.json")
        
        # Copy extensions.json
        if (source_dir / 'extensions.json').exists():
            shutil.copy(
                source_dir / 'extensions.json',
                target_dir / 'extensions.json'
            )
            print("  ✓ extensions.json")
        
        print("  ✅ VS Code configured")
        return True
    
    def configure_cursor(self) -> bool:
        """Configure Cursor IDE."""
        print("Configuring Cursor...")
        
        source_dir = self.config_dir / 'cursor'
        
        if not source_dir.exists():
            print("  ⚠️  Cursor config template not found")
            return False
        
        # Copy .cursorrules
        if (source_dir / '.cursorrules').exists():
            shutil.copy(
                source_dir / '.cursorrules',
                self.project_root / '.cursorrules'
            )
            print("  ✓ .cursorrules")
        
        # Copy MCP servers config
        if (source_dir / 'mcp-servers.json').exists():
            target_dir = self.project_root / '.cursor'
            target_dir.mkdir(exist_ok=True)
            shutil.copy(
                source_dir / 'mcp-servers.json',
                target_dir / 'mcp-servers.json'
            )
            print("  ✓ mcp-servers.json")
        
        print("  ✅ Cursor configured")
        return True
    
    def configure_continue(self) -> bool:
        """Configure Continue.dev."""
        print("Configuring Continue.dev...")
        
        source_dir = self.config_dir / 'continue'
        target_dir = self.project_root / '.continue'
        
        if not source_dir.exists():
            print("  ⚠️  Continue.dev config template not found")
            return False
        
        target_dir.mkdir(exist_ok=True)
        
        # Copy config.json with environment variable substitution
        if (source_dir / 'config.json').exists():
            with open(source_dir / 'config.json') as f:
                config = f.read()
            
            # Replace environment variable placeholders
            config = config.replace('${GEMINI_API_KEY}', os.getenv('GEMINI_API_KEY', ''))
            config = config.replace('${ANTHROPIC_API_KEY}', os.getenv('ANTHROPIC_API_KEY', ''))
            config = config.replace('${OPENAI_API_KEY}', os.getenv('OPENAI_API_KEY', ''))
            
            with open(target_dir / 'config.json', 'w') as f:
                f.write(config)
            
            print("  ✓ config.json (with API keys)")
        
        print("  ✅ Continue.dev configured")
        return True
    
    def configure_pycharm(self) -> bool:
        """Configure PyCharm settings."""
        print("Configuring PyCharm...")
        
        idea_dir = self.project_root / '.idea'
        
        if not idea_dir.exists():
            print("  ⚠️  PyCharm project not initialized")
            return False
        
        # Create inspectionProfiles for code style
        profiles_dir = idea_dir / 'inspectionProfiles'
        profiles_dir.mkdir(exist_ok=True)
        
        profile = {
            "profile": {
                "name": "The AI Orchestrator",
                "inspection_tool": {
                    "class": "PyPep8Inspection",
                    "enabled": True
                }
            }
        }
        
        # PyCharm uses XML, this is simplified
        print("  ℹ️  Manual PyCharm configuration recommended")
        print("     - Set Python interpreter to venv/bin/python")
        print("     - Enable Black formatter")
        print("     - Enable Flake8 linting")
        
        return True
    
    def configure_all(self) -> None:
        """Configure all detected IDEs."""
        print("\n🔧 Auto-Configuring IDEs for The AI Orchestrator\n")
        
        # Always attempt to configure common IDEs
        configured = []
        
        if self.configure_vscode():
            configured.append('VS Code')
        
        if self.configure_cursor():
            configured.append('Cursor')
        
        if self.configure_continue():
            configured.append('Continue.dev')
        
        # Only configure PyCharm if .idea exists
        if (self.project_root / '.idea').exists():
            if self.configure_pycharm():
                configured.append('PyCharm')
        
        print("\n" + "="*60)
        if configured:
            print(f"✅ Configured: {', '.join(configured)}")
        else:
            print("⚠️  No IDE configurations applied")
        print("="*60 + "\n")
        
        # Instructions
        print("Next steps:")
        print("1. Reload your IDE to apply settings")
        print("2. Install recommended extensions (VS Code/Cursor)")
        print("3. Configure API keys in .env file")
        print("4. Run validation: python .agents/scripts/validate-setup.py")
        print()

def main():
    """Main entry point."""
    configurator = IDEConfigurator()
    configurator.configure_all()

if __name__ == '__main__':
    main()
