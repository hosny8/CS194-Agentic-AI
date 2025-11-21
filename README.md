# CTAE-Green: Commodity Trade Agent Evaluation

**Evaluating Multi-Agent Reasoning in Commodity Trade Operations**

## Overview

CTAE-Green is a benchmarking and evaluation agent designed to assess multi-agent performance in complex, data-driven decision environments such as commodity trade logistics and risk management. The Green Agent acts as an orchestrator and judge, simulating realistic trading workflows involving logistics updates, risk alerts, and coordination tasks.

## What This Benchmark Tests

### Task Description
The CTAE-Green Agent evaluates how well "white agents" handle reasoning in simulated commodity trade operations:

- **Environment**: Streams of logistics emails, shipment updates, market news, and risk alerts
- **Agent Capabilities**: Extract key details, link related events, suggest actions (e.g., rerouting cargo)
- **Evaluation Metrics**:
  - **Data Extraction Accuracy** (30%): Precision/recall of extracted facts from unstructured data
  - **Risk Reasoning Quality** (35%): Correctness of risk identification and severity assessment
  - **Recommendation Coherence** (25%): Actionability and clarity of suggestions
  - **Response Time** (10%): Speed of analysis

### Why This Matters

Existing benchmarks (τ-bench, BrowserGym, SWE-bench) assess reasoning and task automation but lack real-world data interdependencies typical in enterprise domains. CTAE-Green extends these by introducing:

- **Cross-modal evaluation**: Unstructured emails + structured CSVs + real-time alerts
- **Causal reasoning assessment**: Linking events across data sources (e.g., port delay → shipment impact → financial exposure)
- **Collaborative coordination tests**: Multi-agent scenarios requiring information synthesis

## Project Structure

```
ctae-green/
├── data/                          # Simulation data
│   ├── logistics_emails.json     # Logistics updates, delays, news
│   ├── shipment_manifest.csv     # Active shipments with details
│   └── risk_alerts.json          # Weather, geopolitical, operational risks
│
├── agents/                        # Agent implementations
│   ├── green_agent_card.toml     # Green Agent configuration
│   ├── green_agent.py            # Orchestrator/judge implementation
│   └── white_agent_card.toml     # Example White Agent config
│
├── run_demo.sh                    # Quick demo runner
└── README.md                      # This file
```

## Quick Start

### 1. Setup Environment

```bash
# Ensure you're in the ctae-green directory
cd /Users/mohamedhosny/cs194-agenticAI/ctae-green

# Create virtual environment (if not already done)
python3 -m venv ../venv
source ../venv/bin/activate

# Install dependencies (only agentbeats needed for full A2A integration)
pip install agentbeats
```

### 2. Run Demo (Standalone Mode)

For a quick demonstration without full AgentBeats infrastructure:

```bash
chmod +x run_demo.sh
./run_demo.sh
```

This will:
1. Load 3 evaluation scenarios from the data directory
2. Simulate white agent responses (mock responses for demo)
3. Evaluate responses against ground truth
4. Generate a detailed evaluation report

**Expected Output**: A comprehensive report showing scores for each scenario and aggregate performance.

### 3. View Results

The demo generates `ctae_evaluation_report.txt` with detailed scoring:

```
SCENARIO 1: Shanghai Port Delay - Oil Shipment Crisis
SCORES:
  Data Extraction Accuracy:    95.2/100
  Risk Reasoning Quality:      88.7/100
  Recommendation Coherence:    82.5/100
  Response Time Score:         94.3/100
  -------------------------------
  OVERALL SCORE:               89.1/100
```

## Evaluation Scenarios

### Scenario 1: Shanghai Port Delay - Oil Shipment Crisis
- **Difficulty**: Medium
- **Focus**: Single-shipment crisis management
- **Data Sources**: Port delay email, price update, shipment manifest, congestion alert
- **Key Challenge**: Extract impact of 5-day delay on $3.9M oil shipment

### Scenario 2: Hurricane Risk - Gulf Operations  
- **Difficulty**: Hard
- **Focus**: Weather-driven operational disruption
- **Data Sources**: Hurricane alert, risk bulletin, shipment data
- **Key Challenge**: Identify at-risk shipments and recommend mitigation

### Scenario 3: Multi-Risk Assessment - Global View
- **Difficulty**: Hard
- **Focus**: Synthesizing multiple concurrent risks
- **Data Sources**: All emails, shipments, and risk alerts
- **Key Challenge**: Prioritize top 3 risks across $50M+ portfolio

## How Green Agent Evaluates

### 1. Data Extraction Accuracy (0-100)
- Measures F1 score of extracted facts vs. ground truth
- Critical facts: shipment IDs, quantities, delays, financial values
- Example: "50,000 barrels", "5-day delay", "SHP-2025-1042"

### 2. Risk Reasoning Quality (0-100)
- Risk type identification (weather, port congestion, geopolitical)
- Severity assessment accuracy (low/medium/high/critical)
- Affected asset mapping (which shipments/routes impacted)

### 3. Recommendation Coherence (0-100)
- Alignment with optimal actions (reroute, delay, notify, hedge)
- Presence of clear rationale for each recommendation
- Actionability and specificity

### 4. Response Time Score (0-100)
- Normalized score based on time limit (30-45 seconds per scenario)
- Simulates operational urgency constraints

### 5. Overall Score
Weighted average: `0.30×Extraction + 0.35×Reasoning + 0.25×Recommendations + 0.10×Time`

## Integration with AgentBeats Platform

To run this with actual A2A agents on the AgentBeats platform:

### Step 1: Deploy White Agent

```bash
cd agents

# Run white agent on port 8001
agentbeats run white_agent_card.toml \
    --launcher_host localhost \
    --launcher_port 9001 \
    --agent_host localhost \
    --agent_port 8001 \
    --model_type openai \
    --model_name gpt-4o-mini
```

### Step 2: Deploy Green Agent

```bash
# Run green agent on port 8000
agentbeats run green_agent_card.toml \
    --launcher_host localhost \
    --launcher_port 9000 \
    --agent_host localhost \
    --agent_port 8000 \
    --model_type openai \
    --model_name gpt-4o
```

### Step 3: Register on AgentBeats.org

1. Login to [agentbeats.org](https://agentbeats.org)
2. Register agents:
   - **Green Agent**: `http://YOUR_IP:8000` (launcher: port 9000)
   - **White Agent**: `http://YOUR_IP:8001` (launcher: port 9001)
3. Create a battle with:
   - **Green Agent**: CTAE-Green Orchestrator (judge role)
   - **White Agent**: Your trade analyst agent (participant role)

## Demo Video Script (3 minutes)

### Part 1: Task Introduction (60 seconds)

**Show**: `data/` directory with files

**Narration**: 
> "CTAE-Green evaluates agents in commodity trade operations. The environment provides three data sources: logistics emails with shipping updates, a CSV manifest tracking active shipments worth $50M+, and real-time risk alerts for weather, port congestion, and geopolitical events. Agents must extract structured data, assess risks, and recommend actions like rerouting cargo or hedging positions."

### Part 2: Demonstration (90 seconds)

**Show**: Terminal running `./run_demo.sh`

**Narration**:
> "Let's see the Green Agent in action. It loads three scenarios of increasing difficulty. In Scenario 1, a $3.9M oil shipment is delayed 5 days at Shanghai port. The Green Agent sends this scenario to the White Agent, which must extract key facts like the shipment ID, delay duration, and financial impact. The White Agent identifies the delay, assesses it as high-risk, and recommends rerouting to an alternative port. The Green Agent scores this response on four dimensions: data extraction accuracy at 95%, risk reasoning quality at 89%, recommendation coherence at 83%, and response time. The overall score is 89 out of 100—excellent performance."

**Show**: Scroll through evaluation report

**Narration**:
> "Scenario 2 introduces a Category 3 hurricane threatening Gulf operations. The White Agent must identify which shipments are at risk and suggest immediate mitigation. Scenario 3 tests multi-risk synthesis across all concurrent threats. The final report shows aggregate performance: this White Agent scored 87/100 overall, with strong data extraction but room for improvement in complex recommendation synthesis."

### Part 3: Design Notes (30 seconds)

**Show**: `green_agent.py` code (evaluation functions)

**Narration**:
> "Test cases are generated from real-world trade patterns: port delays, weather disruptions, and market volatility. Ground truth includes critical facts, expected risks, and optimal actions. The Green Agent uses F1 scoring for extraction, rubric-based evaluation for reasoning, and LLM-as-judge for recommendation quality. This ensures fair, reproducible, and reliable agent assessment in high-stakes decision environments."

## Recording Your Demo

### Option 1: Screen Recording (Recommended)

**Tools**: QuickTime (macOS), OBS Studio, or Loom

1. Open Terminal and position it prominently
2. Have `README.md` and `data/logistics_emails.json` open in editor
3. Start recording
4. Follow the script above:
   - Show data files (10-15 seconds)
   - Run `./run_demo.sh` (60 seconds)
   - Scroll through report (30 seconds)
   - Show evaluation code (30 seconds)
5. Add voiceover narration (record separately and overlay if needed)

### Option 2: Edited Video

1. Record terminal session: `asciinema record demo.cast`
2. Record separate voiceover audio
3. Use video editor (iMovie, Final Cut, DaVinci Resolve) to combine
4. Add captions for clarity

### Tips for Great Demo
- **Keep it concise**: 3 minutes max
- **Show, don't tell**: Let the code run, show real output
- **Explain metrics**: Briefly clarify what each score measures
- **Highlight uniqueness**: Cross-modal data, causal reasoning, operational constraints

## Extending the Benchmark

### Adding New Scenarios

Edit `green_agent.py` in the `load_scenarios()` method:

```python
scenarios.append({
    "id": "scenario_04",
    "name": "Your Scenario Name",
    "difficulty": "medium",
    "data": {...},
    "task": "Your task description",
    "time_limit": 30
})
```

Add corresponding ground truth in `load_ground_truth()`.

### Customizing Metrics

Modify the `evaluate_response()` method to add new scoring dimensions:

```python
# Example: Add cost optimization metric
cost_savings = calculate_cost_savings(response)
scores["cost_optimization"] = cost_savings
```

### Integrating Real White Agents

Replace `mock_white_agent_response()` with actual A2A calls:

```python
import requests

def send_to_white_agent(agent_url: str, prompt: str) -> Dict[str, Any]:
    response = requests.post(
        f"{agent_url}/task",
        json={"task": prompt}
    )
    return response.json()
```

## Troubleshooting

### "File not found" errors
- Ensure you're running scripts from the `ctae-green/` directory
- Check that `data/` directory exists with all JSON/CSV files

### Import errors
- Activate virtual environment: `source ../venv/bin/activate`
- Install dependencies: `pip install agentbeats`

### Empty or incorrect scores
- Verify ground truth in `green_agent.py` matches your scenarios
- Check that white agent responses follow the expected JSON format

## Team

- **Mohamed**: Green Agent architecture, orchestration logic, evaluation metrics
- **Matheus**: Data generation, environment setup, demo preparation

## License

MIT License - see LICENSE file for details

## Contact

For questions or contributions, please open an issue on the repository.




