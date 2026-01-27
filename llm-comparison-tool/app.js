import { scenarios } from "./scenarios.js";

// State Management
const state = {
  currentStep: 0,
  responses: {},
  scores: {},
  exportData: null,
};

// DOM Elements
const app = document.getElementById("app");
const headerSteps = document.getElementById("stepper");

// Initialization
document.addEventListener("DOMContentLoaded", () => {
  initApp();
  setupModal();
  setupNav();
});

function initApp() {
  state.responses = JSON.parse(localStorage.getItem("llm_responses")) || {};
  state.scores = JSON.parse(localStorage.getItem("llm_scores")) || {};
  renderStepper();
  renderCurrentStep();
}

function setupNav() {
  // Navigation can be handled via renderStepper clicks
}

function setupModal() {
  const modal = document.getElementById("infoModal");
  const openBtn = document.getElementById("openModalBtn");
  const closeBtn = document.getElementById("closeModalBtn");

  if (openBtn && modal && closeBtn) {
    openBtn.addEventListener("click", () => modal.classList.add("open"));
    closeBtn.addEventListener("click", () => modal.classList.remove("open"));
    window.addEventListener("click", (e) => {
      if (e.target === modal) modal.classList.remove("open");
    });
  }
}

// Rendering Logic
function renderStepper() {
  const steps = [
    "Setup",
    ...scenarios.map((_, i) => `Test ${i + 1}`),
    "Analysis",
  ];
  headerSteps.innerHTML = steps
    .map((label, index) => {
      let className = "step-item";
      if (index === state.currentStep) className += " active";
      if (index < state.currentStep) className += " completed";
      return `
            <div class="${className}" onclick="goToStep(${index})">
                <div class="step-circle">${index + 1}</div>
                <div class="step-label">${label}</div>
            </div>
        `;
    })
    .join("");
}

window.goToStep = (index) => {
  state.currentStep = index;
  renderStepper();
  renderCurrentStep();
};

function renderCurrentStep() {
  app.innerHTML = "";

  // Step 0: Setup
  if (state.currentStep === 0) {
    renderSetup();
    return;
  }

  // Step 1-5: Tests
  if (state.currentStep > 0 && state.currentStep <= scenarios.length) {
    renderTest(state.currentStep - 1);
    return;
  }

  // Step 6: Analysis
  if (state.currentStep === scenarios.length + 1) {
    renderAnalysis();
    return;
  }
}

function renderSetup() {
  app.innerHTML = `
        <div class="card">
            <h2>Welcome to LLM Comparison Protocol</h2>
            <p class="subtitle" style="margin-bottom: 2rem;">Compare GLM 4.7 Cloud vs. Gemini Flash on pedagogical criteria.</p>
            
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; margin-bottom: 2rem;">
                <div class="rubric-section">
                    <h3>Step 1: Environment Check</h3>
                    <code style="display: block; background: rgba(0,0,0,0.3); padding: 1rem; border-radius: 0.5rem; margin-top: 1rem;">
                        ollama list<br>
                        # Should show glm-4.7:cloud
                    </code>
                </div>
                <div class="rubric-section">
                    <h3>Step 2: Testing Protocol</h3>
                    <ul style="margin-left: 1.5rem; margin-top: 1rem; color: var(--text-secondary);">
                        <li>Run tests sequentially</li>
                        <li>Paste full outputs raw</li>
                        <li>Score objectively based on rubric</li>
                        <li>Export JSON at the end</li>
                    </ul>
                </div>
            </div>

            <div class="flex-end">
                <button class="btn btn-primary" onclick="goToStep(1)">Start Testing &rarr;</button>
            </div>
        </div>
    `;
}

function renderTest(scenarioIndex) {
  const scenario = scenarios[scenarioIndex];
  const savedResponses = state.responses[scenario.id] || {
    modelA: "",
    modelB: "",
  };
  const savedScores = state.scores[scenario.id] || {};

  const rubricHtml = scenario.rubric
    .map((item, i) => {
      const checked = savedScores[i] ? "checked" : "";
      return `
            <div class="rubric-item">
                <label class="checkbox-wrapper">
                    <input type="checkbox" onchange="updateScore('${scenario.id}', ${i}, ${item.weight}, this.checked)" ${checked}>
                    <span class="custom-checkbox">
                        <svg width="12" height="12" viewBox="0 0 12 12" fill="none" class="check-icon" style="opacity: ${checked ? 1 : 0}">
                            <path d="M10 3L4.5 8.5L2 6" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                    </span>
                    <span>${item.text}</span>
                </label>
                <span class="weight-badge">${item.weight} pts</span>
            </div>
        `;
    })
    .join("");

  app.innerHTML = `
        <div class="card">
            <div class="test-header">
                <div>
                    <h2>${scenario.title}</h2>
                    <p class="subtitle">${scenario.description}</p>
                </div>
                <div class="score-display">Score: <span id="score-${scenario.id}">${calculateTotal(scenario.id)}</span>%</div>
            </div>

            <div class="prompt-box">
                <button class="btn btn-secondary btn-small copy-btn" onclick="copyPrompt('${scenario.id}')">Copy Prompt</button>
                <div id="prompt-${scenario.id}">${scenario.prompt}</div>
            </div>

            <div class="comparison-grid">
                <div class="model-column">
                    <h3>Gemini Flash (Baseline)</h3>
                    <textarea class="input-area" placeholder="Paste Gemini response here..." 
                        oninput="saveResponse('${scenario.id}', 'modelA', this.value)">${savedResponses.modelA || ""}</textarea>
                </div>
                <div class="model-column">
                    <h3>GLM 4.7 Cloud (Challenger)</h3>
                    <textarea class="input-area" placeholder="Paste GLM 4.7 response here..." 
                        oninput="saveResponse('${scenario.id}', 'modelB', this.value)">${savedResponses.modelB || ""}</textarea>
                </div>
            </div>

            <div class="rubric-section">
                <div class="rubric-header">
                    <h3>Scoring Rubric (Applies to GLM 4.7)</h3>
                    <span class="subtitle" style="font-size: 0.9rem">Evaluation for GLM 4.7</span>
                </div>
                ${rubricHtml}
            </div>

            <div class="flex-end">
                ${scenarioIndex > 0 ? `<button class="btn btn-secondary" onclick="goToStep(${state.currentStep - 1})">&larr; Previous</button>` : ""}
                <button class="btn btn-primary" onclick="goToStep(${state.currentStep + 1})">Next Test &rarr;</button>
            </div>
        </div>
    `;
}

function renderAnalysis() {
  const totalScore = Object.values(state.scores).reduce((acc, scoreObj) => {
    return acc + Object.values(scoreObj).reduce((sum, val) => sum + val, 0);
  }, 0);

  // Calculate average % (each test is 100pts)
  const avgScore = Math.round(totalScore / scenarios.length);

  let recommendation = "";
  let statusColor = "";

  if (avgScore >= 85) {
    recommendation = "Equal Alternative";
    statusColor = "var(--success)";
  } else if (avgScore >= 70) {
    recommendation = "Specialized Tool";
    statusColor = "var(--warning)";
  } else {
    recommendation = "Local Fallback Only";
    statusColor = "var(--danger)";
  }

  const rows = scenarios
    .map((s) => {
      const score = calculateTotal(s.id);
      const color =
        score >= 85
          ? "text-green-400"
          : score >= 70
            ? "text-yellow-400"
            : "text-red-400"; // Utility classes not defined but keeping logic simple
      return `
            <tr>
                <td>${s.title}</td>
                <td style="font-weight: bold; color: ${score >= 80 ? "var(--success)" : "var(--warning)"}">${score}/100</td>
            </tr>
        `;
    })
    .join("");

  app.innerHTML = `
        <div class="card">
            <h2>Analysis Summary</h2>
            <div class="dashboard-grid">
                <div class="stat-card">
                    <h3>Overall Score</h3>
                    <div class="stat-value" style="color: ${statusColor}">${avgScore}%</div>
                </div>
                <div class="stat-card">
                    <h3>Recommendation</h3>
                    <div class="stat-value" style="font-size: 1.5rem; color: ${statusColor}">${recommendation}</div>
                </div>
            </div>

            <div class="rubric-section">
                <h3>Detailed Breakdown</h3>
                <table class="result-table">
                    <thead>
                        <tr>
                            <th>Test Scenario</th>
                            <th>Score</th>
                        </tr>
                    </thead>
                    <tbody>
                        ${rows}
                    </tbody>
                </table>
            </div>

            <div class="flex-end">
                <button class="btn btn-secondary" onclick="exportResults()">Export Results (JSON)</button>
            </div>
        </div>
    `;
}

// Logic Helpers
window.copyPrompt = (id) => {
  const text = scenarios.find((s) => s.id === id).prompt;
  navigator.clipboard.writeText(text);
  // Could add toaster here
};

window.saveResponse = (testId, model, value) => {
  if (!state.responses[testId]) state.responses[testId] = {};
  state.responses[testId][model] = value;
  persist();
};

window.updateScore = (testId, index, weight, isChecked) => {
  if (!state.scores[testId]) state.scores[testId] = {};
  state.scores[testId][index] = isChecked ? weight : 0;

  // Update local display
  document.getElementById(`score-${testId}`).innerText = calculateTotal(testId);
  persist();
};

function calculateTotal(testId) {
  if (!state.scores[testId]) return 0;
  return Object.values(state.scores[testId]).reduce((a, b) => a + b, 0);
}

window.exportResults = () => {
  const data = {
    timestamp: new Date().toISOString(),
    scores: state.scores,
    responses: state.responses,
  };
  const blob = new Blob([JSON.stringify(data, null, 2)], {
    type: "application/json",
  });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = `llm-comparison-${new Date().toISOString().slice(0, 10)}.json`;
  a.click();
};

function persist() {
  localStorage.setItem("llm_responses", JSON.stringify(state.responses));
  localStorage.setItem("llm_scores", JSON.stringify(state.scores));
}
