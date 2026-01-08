Write-Host "`n===== Setup Verification =====" -ForegroundColor Cyan

# 1. Ollama models
Write-Host "`n[1] Ollama Models" -ForegroundColor Yellow
$models = ollama list | Out-String
if ($models -match "llama3.2:3b") {
    Write-Host "   ✓ llama3.2:3b" -ForegroundColor Green
}
if ($models -match "codellama:13b") {
    Write-Host "   ✓ codellama:13b" -ForegroundColor Green
}
if ($models -match "nomic-embed-text") {
    Write-Host "   ✓ nomic-embed-text" -ForegroundColor Green
}

# 2. Python environment
Write-Host "`n[2] Python Environment" -ForegroundColor Yellow
if (Test-Path "venv") {
    Write-Host "   ✓ Virtual environment" -ForegroundColor Green
}

# 3. Dependencies
Write-Host "`n[3] Python Packages" -ForegroundColor Yellow
try {
    python -c "import anthropic, google.generativeai, openai, chromadb; print('   ✓ All packages installed')"
} catch {
    Write-Host "   ✗ Some packages missing" -ForegroundColor Red
}

# 4. Config files
Write-Host "`n[4] Configuration" -ForegroundColor Yellow
if (Test-Path ".env") {
    Write-Host "   ✓ .env file" -ForegroundColor Green
}
if (Test-Path "$env:USERPROFILE\.continue\config.json") {
    Write-Host "   ✓ Continue.dev config" -ForegroundColor Green
}

# 5. Ollama service
Write-Host "`n[5] Ollama Service" -ForegroundColor Yellow
try {
    $null = curl.exe -s http://localhost:11434/api/tags
    if ($LASTEXITCODE -eq 0) {
        Write-Host "   ✓ Running on :11434" -ForegroundColor Green
    }
} catch {
    Write-Host "   ✗ Not responding" -ForegroundColor Red
}

Write-Host "`n===== Verification Complete =====`n" -ForegroundColor Cyan
