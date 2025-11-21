# 🎥 QUICK RECORDING GUIDE - Read This While Recording!

## Pre-Recording Checklist ✅
- [ ] Terminal in `ctae-green/` directory (NOT agents/)
- [ ] Terminal cleared (`clear`)
- [ ] Files open in editor: emails.json, manifest.csv, launcher.py
- [ ] Font size readable (14-16pt)
- [ ] Recording software ready (QuickTime/Loom)
- [ ] Do Not Disturb mode ON (no notifications!)
- [ ] Microphone tested

---

## 🎬 RECORDING FLOW (5 minutes max)

### Part 1: Task Introduction (60 seconds)

**SHOW:** Open data files in editor (emails.json, manifest.csv)

**SAY:**
> "This is CTAE-Green, a green agent for the AgentBeats platform that evaluates 
> commodity trade agents. 
> 
> [SHOW emails.json]
> The environment provides logistics emails with shipping updates, like this 
> port delay affecting a $3.9 million oil shipment.
> 
> [SHOW manifest.csv]
> Agents receive structured shipment data tracking $50 million in commodities.
> 
> [Back to terminal]
> They also get real-time risk alerts for hurricanes, port congestion, and 
> geopolitical events. Agents must extract facts, link causal event chains, 
> assess risks, and recommend actions under time pressure.
> 
> The Green Agent evaluates them on four metrics: data extraction accuracy, 
> risk reasoning quality, recommendation coherence, and response time."

---

### Part 2: Demonstration (180 seconds)

**SHOW:** Terminal

**[Command 1] List Available Agents and Scenarios (30 seconds)**

**TYPE & RUN:**
```bash
python3 launcher.py list
```

**SAY:**
> "Let's see what we have. The launcher shows three white agents registered for 
> evaluation: Strong Analyst, Weak Extractor, and Moderate Analyst. These 
> demonstrate different performance levels.
> 
> We have three scenarios: Shanghai Port Delay, Hurricane Risk, and Multi-Risk 
> Assessment, ranging from medium to hard difficulty."

---

**[Command 2] Single Agent Evaluation (90 seconds)**

**TYPE & RUN:**
```bash
python3 launcher.py evaluate --agent strong_analyst --scenarios scenario_01
```

**SAY (as it runs):**
> "Now let's evaluate the Strong Analyst on Scenario 1—the Shanghai port delay. 
> 
> [Step 1 appears]
> The Green Agent prepares the scenario with emails, shipment data, and risk alerts.
> 
> [Step 2 appears]
> It sends this to the Strong Analyst white agent...
> 
> [Step 3 appears]
> The white agent responds with extracted facts: shipment ID SHP-2025-1042, 
> 50,000 barrels delayed 5 days, value $3.9 million.
> 
> [Step 4 - scores appear]
> The Green Agent evaluates: Data extraction 80 out of 100—caught the key facts. 
> Risk reasoning 100 out of 100—perfectly identified delay and financial risks 
> with correct severity levels. Recommendations 83—provided actionable steps 
> like rerouting to alternative ports.
> 
> Overall score: 89.8 out of 100. EXCELLENT performance tier."

---

**[Command 3] Full Leaderboard (60 seconds)**

**TYPE & RUN:**
```bash
python3 launcher.py launch
```

**SAY (let it run, then show leaderboard):**
> "Now let's run the full evaluation across all agents and scenarios.
> 
> [Let first agent run quickly, don't narrate details]
> 
> The launcher evaluates all three white agents on all three scenarios—
> that's nine total evaluations.
> 
> [Leaderboard appears]
> 
> Here's the leaderboard. Strong Analyst ranks first with 45 out of 100. 
> Weak Extractor second at 27. Moderate Analyst third at 22.
> 
> This demonstrates the Green Agent can differentiate performance levels—
> from excellent extraction and reasoning to poor quality responses. The 
> quantitative scores provide clear, reproducible feedback for agent developers."

---

### Part 3: Validation & Design (60 seconds)

**SHOW:** Open `launcher.py` or `agents/green_agent.py` in editor

**SAY:**
> "How does validation work? Let me show you the evaluation logic.
> 
> [Scroll to evaluation code, around line 150-200 in green_agent.py]
> 
> For data extraction, we use F1 scoring—comparing extracted facts against 
> ground truth. Did the agent catch 'SHP-2025-1042', '50,000 barrels', '$3.9M'?
> 
> For risk reasoning, we check if correct risk types were identified—delay, 
> financial—and if severity levels match: HIGH for 5-day delay, MEDIUM for 
> storage costs.
> 
> For recommendations, we measure alignment with optimal actions like rerouting 
> and customer notification, plus whether clear rationale was provided.
> 
> [Show ground truth section or test case]
> 
> Each scenario has pre-defined ground truth. This makes evaluation reproducible—
> same input, same score every time. Running the same agent twice gives identical 
> results, verified by our test cases.
> 
> What makes this unique? It tests cross-modal reasoning—combining unstructured 
> emails with structured CSVs. It requires causal reasoning—linking port delay 
> to shipment impact to financial exposure. And it simulates real operational 
> constraints: time pressure, incomplete data, high-stakes decisions.
> 
> CTAE-Green provides standardized, reproducible evaluation for agents in 
> complex, information-rich enterprise domains. Thank you!"

---

## ⚡ Quick Commands

**Before recording:**
```bash
cd /Users/mohamedhosny/cs194-agenticAI/ctae-green
clear
```

**During recording (in order):**
```bash
# 1. List agents and scenarios
python3 launcher.py list

# 2. Single agent evaluation
python3 launcher.py evaluate --agent strong_analyst --scenarios scenario_01

# 3. Full evaluation with leaderboard
python3 launcher.py launch
```

---

## 💡 Recording Tips

### Audio
- Speak clearly, moderate pace
- Don't rush through the scores
- Show enthusiasm but stay professional

### Screen
- Let important info stay visible for 2-3 seconds
- Don't click too fast
- Keep cursor movements smooth

### If You Make a Mistake
- **Small mistake**: Keep going, viewers won't notice
- **Big mistake**: Pause recording, take a breath, start that section again
- **Major issue**: Just re-record from the beginning (it's only 3 minutes!)

---

## ✅ After Recording

1. **Watch your video** - Is audio clear? Screen readable?
2. **Check timing** - Under 5 minutes?
3. **Verify content** - Task intro + demonstration + validation all covered?
4. **Check requirements** - Shows Green Agent evaluating White Agents with test cases?
5. **Export/save** - Name it clearly: `CTAE_Green_Demo_Mohamed.mp4`

---

## 🚨 Common Issues

**Terminal text too small:**
- Cmd + Plus to increase font size

**Forgot to clear terminal:**
- Run `clear` before starting

**Recording software freezes:**
- Use Loom web app instead (simpler, more reliable)

**Too nervous:**
- Remember: This is a demo, not a Hollywood production!
- Your reviewers care about: working system, clear explanation, completeness
- You don't need perfection!

**Video too long:**
- Target: 4-5 minutes (5 min max)
- If over: Skip detailed narration of Scenarios 2-3 in the full launch
- Focus on: Strong Analyst evaluation + final leaderboard

---

## 🎯 You've Got This!

Remember what you're showing:
1. ✅ A working Green Agent that orchestrates evaluation of multiple White Agents
2. ✅ Real evaluation with differentiation (Strong: 89/100, Weak: 27/100, Moderate: 22/100)
3. ✅ Leaderboard showing comparative performance
4. ✅ Reproducible scoring with ground truth validation
5. ✅ Thoughtful design (cross-modal, causal reasoning, operational constraints)

The launcher makes your demo look professional and shows the full system in action!

**NOW GO RECORD! 🎬**

