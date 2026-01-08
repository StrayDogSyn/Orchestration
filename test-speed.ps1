Write-Host "`nModel Speed Comparison" -ForegroundColor Cyan
Write-Host "======================" -ForegroundColor Cyan

$models = @(
    "tinyllama",
    "llama3.2:1b", 
    "llama3.2:3b",
    "phi3:mini",
    "qwen2.5-coder:7b"
)

$prompt = "Explain recursion in one sentence."

foreach ($model in $models) {
    Write-Host "`n[Testing: $model]" -ForegroundColor Yellow
    $start = Get-Date
    ollama run $model "$prompt" | Out-Null
    $duration = ((Get-Date) - $start).TotalSeconds
    Write-Host "  ⏱️  $([math]::Round($duration, 2)) seconds" -ForegroundColor Green
}
