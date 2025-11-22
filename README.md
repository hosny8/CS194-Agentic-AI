# CTAE-Green: Commodity Trade Agent Evaluation

A green agent benchmark for evaluating AI agents on commodity trade operations requiring cross-modal reasoning under operational constraints.

## Repository Information

- **Repository**: https://github.com/hosny8/CS194-Agentic-AI
- **Branch**: `main`
- **Status**: Public

## Overview

CTAE-Green evaluates white agents on their ability to:
- Extract structured data from unstructured logistics emails and CSV manifests
- Link causal event chains across data sources (e.g., port delay → shipment impact → financial risk)
- Assess risk severity and identify affected assets
- Generate actionable recommendations under time pressure (30-45 seconds)

The green agent scores white agents across four metrics:
- **Data Extraction Accuracy (30%)**: F1 score of extracted facts
- **Risk Reasoning Quality (35%)**: Correctness of risk identification and severity
- **Recommendation Coherence (25%)**: Actionability and rationale clarity
- **Response Time (10%)**: Speed under operational constraints

---

## Installation

### Prerequisites
- Python 3.11+
- pip

### Setup

```bash
# Clone repository
git clone https://github.com/hosny8/CS194-Agentic-AI.git
cd CS194-Agentic-AI/ctae-green

# Install dependencies
pip install -r requirements.txt
```

---

## Usage

### 1. List Available Agents and Scenarios

View all registered white agents and evaluation scenarios:

```bash
python3 launcher.py list
```

**Output**: Lists 3 white agents (Strong Analyst, Weak Extractor, Moderate Analyst) and 3 scenarios with descriptions.

---

### 2. Run Green Agent to Evaluate White Agents

#### Full Evaluation (All Agents × All Scenarios)

```bash
python3 launcher.py launch
```

**What it does:**
- Evaluates all 3 white agents on all 3 scenarios (9 total evaluations)
- Generates leaderboard with comparative rankings
- Displays aggregate performance metrics

**Expected Results:**
- Strong Analyst: ~45/100 (demonstrates strong extraction and reasoning)
- Weak Extractor: ~27/100 (shows poor performance on details)
- Moderate Analyst: ~22/100 (mid-level competence)

**Time**: ~10-15 seconds

---

#### Single Agent Evaluation

Evaluate a specific white agent:

```bash
python3 launcher.py evaluate --agent strong_analyst
```

**Available agents:**
- `strong_analyst` - High-quality reasoning and extraction
- `weak_extractor` - Poor extraction capabilities
- `moderate_analyst` - Mid-level performance

**Output**: Detailed scores for each scenario with performance tier (EXCELLENT/GOOD/FAIR/NEEDS IMPROVEMENT)

---

#### Specific Scenario Evaluation

Evaluate on specific scenarios only:

```bash
python3 launcher.py evaluate --agent strong_analyst --scenarios scenario_01 scenario_02
```

**Available scenarios:**
- `scenario_01` - Shanghai Port Delay (Medium difficulty)
- `scenario_02` - Hurricane Risk (Hard difficulty)
- `scenario_03` - Multi-Risk Assessment (Hard difficulty)

---

### 3. Test Green Agent Evaluation

#### Test Case 1: Strong Performance

Verify green agent correctly scores high-quality responses:

```bash
python3 launcher.py evaluate --agent strong_analyst --scenarios scenario_01
```

**Expected Output:**
```
  [Step 4/4] Scores:
            - Data Extraction:     80.0/100
            - Risk Reasoning:      100.0/100
            - Recommendations:     83.3/100
            - Response Time:       100.0/100
            --------------------------------
            - OVERALL SCORE:       89.8/100
            - Performance Tier:    EXCELLENT
```

**Validation**: Green agent correctly recognizes comprehensive fact extraction, accurate risk assessment, and actionable recommendations.

---

#### Test Case 2: Weak Performance

Verify green agent penalizes poor responses:

```bash
python3 launcher.py evaluate --agent weak_extractor --scenarios scenario_02
```

**Expected Output:**
```
  [Step 4/4] Scores:
            - Data Extraction:     0.0/100
            - Risk Reasoning:      0.0/100
            - Recommendations:     50.0/100
            - Response Time:       100.0/100
            --------------------------------
            - OVERALL SCORE:       22.5/100
            - Performance Tier:    NEEDS IMPROVEMENT
```

**Validation**: Green agent correctly penalizes missing facts and lack of detailed analysis.

---

#### Test Case 3: Comparative Evaluation

Verify green agent differentiates performance levels:

```bash
python3 launcher.py launch
```

**Expected Leaderboard:**
```
Rank   Agent Name                Overall    Extract    Reason     Recommend 
----------------------------------------------------------------------
1      Strong Analyst              44.9/100    26.7/100    33.3/100    61.1/100
2      Weak Extractor              27.4/100     0.0/100    13.9/100    50.0/100
3      Moderate Analyst            21.7/100     8.3/100     8.3/100    25.0/100
```

**Validation**: Green agent produces consistent rankings with clear score differentiation.

---

## Running White Agents

### Mock Agents (Demonstration)

The repository includes 3 mock white agents for demonstration purposes. These are automatically invoked by the launcher and require no separate setup.

**Mock Agent Qualities:**
- **Strong Analyst**: Excellent extraction, accurate risk assessment, clear recommendations
- **Weak Extractor**: Misses critical facts, generic analysis
- **Moderate Analyst**: Decent extraction but underestimates severity

---

### Custom White Agents

To evaluate your own white agent:

1. **Implement A2A Protocol**: Your agent must respond to task requests via HTTP
2. **Deploy Agent**: Run your agent on a public URL or localhost
3. **Modify Launcher**: Update `launcher.py` to include your agent:

```python
self.white_agents["your_agent"] = {
    "name": "Your Agent Name",
    "description": "Description",
    "quality": "custom",
    "url": "http://your-agent-url:port"
}
```

4. **Evaluate**:
```bash
python3 launcher.py evaluate --agent your_agent
```

---

## AgentBeats Platform Integration

### Running as A2A Server

Start the green agent as an HTTP server for AgentBeats platform:

```bash
cd agents
python3 green_agent_server.py
```

**Endpoints:**
- **GET** `/` - Health check
- **GET** `/agent-card` - Agent capabilities (A2A protocol)
- **POST** `/task` - Evaluate white agents
- **POST** `/reset` - Reset green agent state

**Example API Call:**

```bash
curl -X POST http://localhost:8000/task \
  -H "Content-Type: application/json" \
  -d '{
    "task": "evaluate_agent",
    "metadata": {
      "white_agent_url": "http://localhost:8001",
      "scenario_id": "scenario_01"
    }
  }'
```

---

### Deploying on AgentBeats

1. **Register Green Agent**:
   - Agent URL: `http://your-server:8000`
   - Launcher URL: `http://your-server:9000` (for reset endpoint)

2. **Register White Agents**: Deploy your white agents and register their URLs

3. **Create Battle**: Configure green agent as orchestrator, white agents as participants

4. **Run Evaluation**: Platform will coordinate full evaluation and display results

---

## Project Structure

```
ctae-green/
├── launcher.py              # Main orchestration script
├── agents/
│   ├── green_agent.py       # Core evaluation logic
│   ├── green_agent_server.py # A2A HTTP server
│   ├── green_agent_card.toml
│   └── white_agent_card.toml
├── data/
│   ├── logistics_emails.json    # 4 logistics emails
│   ├── shipment_manifest.csv    # 5 shipments ($50M+ portfolio)
│   └── risk_alerts.json         # 3 risk alerts
├── requirements.txt
├── README.md
├── EVALUATION_FLOW.md      # Detailed metric explanations
└── USAGE.md                # Extended usage guide
```

---

## Evaluation Scenarios

### Scenario 1: Shanghai Port Delay - Oil Shipment Crisis
- **Difficulty**: Medium
- **Focus**: Single-event crisis management
- **Data**: Port delay email, price update, shipment manifest, congestion alert
- **Challenge**: Extract impact of 5-day delay on $3.9M oil shipment

### Scenario 2: Hurricane Risk - Gulf Operations
- **Difficulty**: Hard
- **Focus**: Weather-driven operational disruption
- **Data**: Hurricane alert, risk bulletin, shipment data
- **Challenge**: Identify at-risk shipments and recommend mitigation

### Scenario 3: Multi-Risk Assessment - Global View
- **Difficulty**: Hard
- **Focus**: Synthesizing multiple concurrent risks
- **Data**: All emails, shipments, and risk alerts
- **Challenge**: Prioritize top 3 risks across $50M+ portfolio

---

## Metrics

### 1. Data Extraction Accuracy (0-100)
- **Method**: F1 score (precision × recall)
- **Ground Truth**: Pre-defined critical facts per scenario
- **Example**: "SHP-2025-1042", "50,000 barrels", "$3.9M", "5-day delay"

### 2. Risk Reasoning Quality (0-100)
- **Method**: Risk type recall + severity accuracy
- **Ground Truth**: Expected risks with severity levels
- **Example**: Delay risk (HIGH), Financial risk (MEDIUM)

### 3. Recommendation Coherence (0-100)
- **Method**: Action coverage + rationale quality
- **Ground Truth**: Optimal actions per scenario
- **Example**: "Reroute to Ningbo port" with clear justification

### 4. Response Time Score (0-100)
- **Method**: Normalized against time limit (30-45s)
- **Calculation**: max(0, 100 - (time / limit × 100))

### Overall Score
Weighted average: `0.30×Extraction + 0.35×Reasoning + 0.25×Recommendations + 0.10×Time`

**Performance Tiers:**
- EXCELLENT: 80-100
- GOOD: 60-79
- FAIR: 40-59
- NEEDS IMPROVEMENT: <40

---

## Reproducibility

All evaluations are deterministic:
- Same white agent response → same scores (100% reproducible)
- Ground truth is fixed and version-controlled
- No randomness in scoring functions

**Verification:**
Run the same evaluation twice and compare outputs:
```bash
python3 launcher.py evaluate --agent strong_analyst --scenarios scenario_01 > run1.txt
python3 launcher.py evaluate --agent strong_analyst --scenarios scenario_01 > run2.txt
diff run1.txt run2.txt  # Should be identical
```

---

## Troubleshooting

### "No module named 'green_agent'"
Ensure you're in the `ctae-green/` directory:
```bash
cd /path/to/CS194-Agentic-AI/ctae-green
python3 launcher.py list
```

### "FileNotFoundError: data/logistics_emails.json"
The launcher auto-detects data directory. Ensure `data/` exists with all files.

### Scores seem incorrect
Mock agents use simplified logic for demonstration. Scores are correct based on mock responses. Real white agents would produce different scores.

---

## Development

### Adding New Scenarios

1. Edit `agents/green_agent.py`
2. Add scenario in `load_scenarios()` method
3. Add ground truth in `load_ground_truth()` method
4. Test: `python3 launcher.py evaluate --agent strong_analyst --scenarios your_scenario_id`

### Adding New Metrics

1. Edit `evaluate_response()` in `agents/green_agent.py`
2. Define scoring logic
3. Update weight calculation in overall score
4. Test with mock agents

---

## Citation

If you use CTAE-Green in your research, please cite:

```
@misc{ctae-green-2025,
  title={CTAE-Green: Evaluating Multi-Agent Reasoning in Commodity Trade Operations},
  author={Mohamed Hosny and Matheus [Last Name]},
  year={2025},
  url={https://github.com/hosny8/CS194-Agentic-AI}
}
```

---

## License

MIT License

---

## Authors

- **Mohamed Hosny** - Green agent architecture, evaluation metrics, AgentBeats integration
- **Matheus [Last Name]** - Data generation, environment setup, validation testing

---

## Support

For issues or questions:
- Open an issue on GitHub: https://github.com/hosny8/CS194-Agentic-AI/issues
- Contact: [your email]

---

## Acknowledgments

Built for CS194 Agentic AI course project. Thanks to the AgentBeats team for the evaluation platform framework.
