# 🎬 CTAE-Green Demo Recording Script
## Quick Reference Card - Keep this open while recording!

---

## ⏱️ Timing Targets
- **Part 1 (Intro)**: 0:00-0:50 (50 sec)
- **Part 2 (Demo)**: 0:50-2:20 (90 sec)  
- **Part 3 (Design)**: 2:20-3:00 (40 sec)
- **Total**: 3:00 max

---

## 📝 Part 1: Introduction (50 seconds)

### Actions:
1. Show file browser OR `ls data/`
2. Open `data/logistics_emails.json` in editor
3. Scroll through emails slowly
4. Open `data/shipment_manifest.csv`
5. Open `data/risk_alerts.json`

### Script:
```
"Hello! I'm presenting CTAE-Green, a benchmark for evaluating AI agents 
in commodity trade operations.

The task environment simulates real-world trade scenarios. Agents receive 
logistics emails with shipping updates...

...like this urgent alert about a 5-day port delay affecting a 
$3.9 million oil shipment.

They also get structured shipment data with commodity types, quantities, 
origins, destinations, and financial values.

And real-time risk alerts for weather events like hurricanes, port 
congestion, and geopolitical disruptions.

Agents must extract critical facts, assess risks, and recommend actions—
like rerouting cargo or hedging positions. The Green Agent evaluates 
them on four metrics: data extraction accuracy, risk reasoning quality, 
recommendation coherence, and response time."
```

---

## 🎮 Part 2: Demonstration (90 seconds)

### Actions:
1. Show terminal in `ctae-green/` directory
2. Type and run: `./run_demo.sh`
3. Let demo run, narrate over it
4. Show scores as they appear
5. Show final report

### Script:
```
"Let's see it in action. I'll run the Green Agent demo.

[Type ./run_demo.sh]

The Green Agent initializes and loads three evaluation scenarios. 
Here's Scenario 1: Shanghai Port Delay—a crisis involving the 
delayed oil shipment we just saw.

It sends this scenario to a White Agent—the agent being evaluated. 
The White Agent has 30 seconds to analyze the situation.

[Wait for response]

The White Agent extracts key facts: shipment ID SHP-2025-1042, 
50,000 barrels of crude oil, delayed 5 days, value $3.9 million. 
It assesses the delay as high-risk and recommends rerouting to 
an alternative port.

[Scores appear]

The Green Agent evaluates this response. Data extraction accuracy: 95%. 
Risk reasoning quality: 89%. Recommendation coherence: 83%. 
Overall score: 89 out of 100—excellent performance on a medium-difficulty 
scenario.

[Scenario 2 starts]

Scenario 2 tests hurricane response. A Category 3 hurricane is 
approaching the Gulf of Mexico. The agent must identify at-risk 
shipments and recommend immediate mitigation actions.

[Let it run]

And Scenario 3 synthesizes multiple concurrent risks across a 
$50 million portfolio, testing the agent's ability to prioritize 
under pressure.

[Final report appears]

Here's the final evaluation report. Aggregate performance: 87 out of 100. 
Strong data extraction, good risk reasoning, and coherent recommendations. 
The report breaks down performance across all three scenarios and 
identifies areas for improvement."
```

---

## 🔬 Part 3: Design Notes (40 seconds)

### Actions:
1. Open `agents/green_agent.py` in editor
2. Scroll to `evaluate_response()` function
3. Show data extraction scoring code
4. Show risk assessment evaluation
5. Show recommendation evaluation
6. Return to report or README

### Script:
```
"How does the Green Agent judge responses? Let me show you the 
evaluation logic.

[Show evaluate_response function]

For data extraction accuracy, it uses F1 scoring—comparing extracted 
facts against ground truth. For example, did the agent catch that 
the shipment is worth $3.9 million? Did it identify the 5-day delay?

[Scroll to risk section]

For risk reasoning, it checks if the agent identified the correct 
risk types—port congestion, financial exposure—and assigned 
appropriate severity levels.

[Scroll to recommendations section]

For recommendations, it measures alignment with optimal actions 
like rerouting or customer notification, and checks if each 
recommendation has clear rationale.

[Close or show report]

Why is this benchmark unique? It tests cross-modal reasoning—
combining unstructured emails with structured CSVs. It evaluates 
causal reasoning—linking a port delay to shipment impact to 
financial risk. And it simulates real operational constraints: 
incomplete data, time pressure, and high-stakes decisions.

[Final screen]

This approach creates fair, reproducible evaluation for agents 
in information-rich enterprise domains. CTAE-Green demonstrates 
how standardized benchmarks can assess not just coding or browsing, 
but complex real-world reasoning.

Thank you! CTAE-Green: evaluating multi-agent reasoning in 
commodity trade operations."
```

---

## ✅ Pre-Recording Checklist

Before you hit record:

- [ ] Terminal cleared: `clear`
- [ ] In correct directory: `pwd` shows `.../ctae-green`
- [ ] Virtual env active (if needed): `source ../venv/bin/activate`
- [ ] Old report deleted: `rm -f **/ctae_evaluation_report.txt`
- [ ] Files open in editor: emails, CSV, green_agent.py
- [ ] Font size readable (14-16pt recommended)
- [ ] Notifications OFF (Do Not Disturb mode)
- [ ] Recording software ready (QuickTime/OBS/Loom)
- [ ] Microphone tested (speak and listen back)
- [ ] Script practiced 2-3 times out loud

---

## 🎯 Key Points to Emphasize

### What makes CTAE-Green unique:
1. **Cross-modal evaluation**: Emails + CSVs + alerts
2. **Causal reasoning**: Port delay → shipment impact → financial risk
3. **Operational constraints**: Incomplete data, time pressure
4. **Reproducible metrics**: F1 scores, rubrics, LLM-as-judge

### Required elements for full credit:
- ✅ Task Introduction (environment, actions)
- ✅ Demonstration (Green evaluating White)
- ✅ Design Notes (test cases, reliability)
- ✅ Clear audio and visible screen
- ✅ Under 3 minutes

---

## 🚀 Quick Commands Reference

```bash
# Setup (do once)
cd /Users/mohamedhosny/cs194-agenticAI
python3 -m venv venv
source venv/bin/activate
pip install agentbeats

# Before recording
cd ctae-green
clear
rm -f **/ctae_evaluation_report.txt

# Run demo
./run_demo.sh

# View report
cat ctae_evaluation_report.txt

# Or run Python directly
cd agents
python3 green_agent.py
```

---

## 💡 Tips for Success

**Voice:**
- Speak clearly and at moderate pace
- Show enthusiasm but stay professional
- Pause briefly between sections

**Screen:**
- Keep cursor movements smooth
- Don't click/type too fast
- Let important info stay on screen 2-3 seconds

**Content:**
- Show, don't just tell (let demo run!)
- Highlight what makes it unique
- Connect to real-world value

**Technical:**
- Test recording 30 seconds first
- Check audio levels
- Verify screen is readable
- If you mess up, pause and re-record that part

---

## 🎬 You've Got This!

Remember: The reviewers want to see:
1. A working Green Agent
2. Clear evaluation process  
3. Thoughtful design choices

You don't need perfection—just clarity and completeness.

**Deep breath. Hit record. You're ready!**




