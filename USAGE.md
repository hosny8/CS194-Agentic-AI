# CTAE-Green Usage Guide

Complete guide to running the CTAE-Green evaluation system.

---

## 🚀 Quick Start (2 Commands)

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run full evaluation
python3 launcher.py launch
```

That's it! The launcher will evaluate 3 white agents across 3 scenarios and display a leaderboard.

---

## 📋 Available Commands

### **1. List Agents and Scenarios**

```bash
python3 launcher.py list
```

Shows:
- All available white agents (Strong Analyst, Weak Extractor, Moderate Analyst)
- All evaluation scenarios (Scenario 1, 2, 3)
- Descriptions and difficulty levels

---

### **2. Full Evaluation (All Agents × All Scenarios)**

```bash
python3 launcher.py launch
```

Runs:
- All 3 white agents
- On all 3 scenarios (9 total evaluations)
- Displays leaderboard with rankings

**Output:**
- Detailed scores for each scenario
- Aggregate performance metrics
- Leaderboard ranked by overall score

**Time:** ~10 seconds

---

### **3. Evaluate Single Agent (All Scenarios)**

```bash
python3 launcher.py evaluate --agent strong_analyst
```

Runs one agent on all scenarios.

**Available agents:**
- `strong_analyst` - High-quality reasoning
- `weak_extractor` - Poor extraction skills
- `moderate_analyst` - Mid-level performance

---

### **4. Evaluate Specific Scenarios**

```bash
python3 launcher.py evaluate --agent strong_analyst --scenarios scenario_01 scenario_02
```

Run specific scenarios only.

**Available scenarios:**
- `scenario_01` - Shanghai Port Delay (Medium)
- `scenario_02` - Hurricane Risk (Hard)
- `scenario_03` - Multi-Risk Assessment (Hard)

---

## 📊 Understanding the Output

### **Evaluation Flow**

```
[Step 1/4] Green Agent preparing scenario...
           ✓ Scenario prompt ready (3087 chars)

[Step 2/4] Sending to Strong Analyst...
           ✓ Response received in 0.00s

[Step 3/4] Green Agent evaluating response...
           ✓ Evaluation complete

[Step 4/4] Scores:
           - Data Extraction:     80.0/100
           - Risk Reasoning:      100.0/100
           - Recommendations:     83.3/100
           - Response Time:       100.0/100
           --------------------------------
           - OVERALL SCORE:       89.8/100
           - Performance Tier:    EXCELLENT
```

### **Metrics Explained**

1. **Data Extraction (30% weight)**
   - Measures F1 score of extracted facts
   - Example: Did agent catch "SHP-2025-1042", "50,000 barrels", "$3.9M"?

2. **Risk Reasoning (35% weight)**
   - Evaluates risk identification and severity assessment
   - Example: Did agent identify delay risk as HIGH, financial risk as MEDIUM?

3. **Recommendation Coherence (25% weight)**
   - Assesses actionability and rationale quality
   - Example: Did agent recommend "reroute" with clear justification?

4. **Response Time (10% weight)**
   - Normalized against time limit (30-45 seconds)
   - Fast responses score higher

### **Performance Tiers**

- **EXCELLENT**: 80-100
- **GOOD**: 60-79
- **FAIR**: 40-59
- **NEEDS IMPROVEMENT**: <40

---

## 🧪 Test Cases

The launcher includes 3 mock white agents demonstrating different performance levels:

### **Strong Analyst (Expected: 80-90/100)**
- Excellent data extraction
- Accurate risk assessment
- Clear, actionable recommendations
- **Use case:** Benchmark for top-tier performance

### **Weak Extractor (Expected: 20-30/100)**
- Poor extraction (misses critical facts)
- Generic risk assessment
- Vague recommendations
- **Use case:** Lower bound, tests Green Agent's ability to penalize poor performance

### **Moderate Analyst (Expected: 30-40/100)**
- Decent extraction but misses details
- Underestimates risk severity
- Incomplete recommendations
- **Use case:** Mid-range performance, tests scoring granularity

---

## 🔧 Advanced Usage

### **Standalone Green Agent (Legacy)**

If you prefer running without the launcher:

```bash
cd agents
python3 green_agent.py
```

Runs built-in demo with fixed mock responses.

---

### **A2A Server Mode (For AgentBeats Platform)**

Start Green Agent as HTTP server:

```bash
cd agents
python3 green_agent_server.py
```

Access:
- Health check: http://localhost:8000
- Agent card: http://localhost:8000/agent-card
- Task endpoint: http://localhost:8000/task
- Reset: http://localhost:8000/reset

**Example API call:**

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

## 📁 File Structure

```
ctae-green/
├── launcher.py              # Main entry point ⭐
├── agents/
│   ├── green_agent.py       # Core evaluation logic
│   ├── green_agent_server.py # A2A HTTP server
│   ├── green_agent_card.toml
│   └── white_agent_card.toml
├── data/
│   ├── logistics_emails.json
│   ├── shipment_manifest.csv
│   └── risk_alerts.json
├── requirements.txt
└── USAGE.md (this file)
```

---

## 🐛 Troubleshooting

### **"No module named 'green_agent'"**

Make sure you're running from the `ctae-green/` directory:
```bash
cd /path/to/ctae-green
python3 launcher.py launch
```

### **"FileNotFoundError: data/logistics_emails.json"**

The launcher handles this automatically by detecting the data directory.
If you see this, ensure `data/` directory exists with all files.

### **Scores seem wrong**

The mock agents use simplified logic for demonstration.
Scores are correct based on the mock responses they generate.
Real white agents would produce different scores.

---

## 🎯 For Your Submission

### **Demo Video Commands**

1. Show launcher listing agents:
```bash
python3 launcher.py list
```

2. Run single agent evaluation:
```bash
python3 launcher.py evaluate --agent strong_analyst
```

3. Show leaderboard:
```bash
python3 launcher.py launch
```

### **GitHub Repository Commands**

Document in README:

```bash
# Clone and setup
git clone https://github.com/hosny8/CS194-Agentic-AI.git
cd CS194-Agentic-AI/ctae-green
pip install -r requirements.txt

# Run evaluation
python3 launcher.py launch

# Test green agent
python3 launcher.py evaluate --agent strong_analyst --scenarios scenario_01

# View available options
python3 launcher.py list
```

---

## 🚀 Next Steps

1. **Record demo video** showing launcher in action
2. **Test on another machine** to verify reproducibility
3. **Add custom white agents** by modifying launcher
4. **Deploy A2A server** for AgentBeats platform integration

---

## 💡 Tips

- Use `python3 launcher.py list` to see all options
- Test with single scenario first: `--scenarios scenario_01`
- The leaderboard shows comparative performance clearly
- Mock agents demonstrate scoring granularity
- Launcher handles all orchestration automatically

---

**For more details, see:**
- `README.md` - Project overview
- `QUICK_RECORDING_GUIDE.md` - Demo recording help
- `EVALUATION_FLOW.md` - Detailed metric explanations

