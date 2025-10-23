# 🎥 QUICK RECORDING GUIDE - Read This While Recording!

## Pre-Recording Checklist ✅
- [ ] Terminal in `ctae-green/agents` directory
- [ ] Terminal cleared (`clear`)
- [ ] Old report deleted (`rm -f ctae_evaluation_report.txt`)
- [ ] Files open in editor: emails.json, manifest.csv, green_agent.py
- [ ] Font size readable (14-16pt)
- [ ] Recording software ready (QuickTime/Loom)
- [ ] Do Not Disturb mode ON (no notifications!)
- [ ] Microphone tested

---

## 🎬 RECORDING FLOW (3 minutes)

### Part 1: Introduction (50 seconds)

**SHOW:** Open data files in editor

**SAY:**
> "This is CTAE-Green, a benchmark for commodity trade agents. 
> 
> The environment provides logistics emails with shipping updates, 
> like this port delay affecting a $3.9 million oil shipment.
> 
> Agents also receive structured shipment data and real-time risk alerts 
> for hurricanes, port congestion, and geopolitical events.
> 
> They must extract facts, assess risks, and recommend actions. 
> The Green Agent evaluates them on data extraction, risk reasoning, 
> recommendations, and response time."

---

### Part 2: Run Demo (90 seconds)

**SHOW:** Terminal

**TYPE & RUN:**
```bash
python3 green_agent.py
```

**SAY (as it runs):**
> "The Green Agent loads three evaluation scenarios. 
> 
> Scenario 1 tests the delayed oil shipment. The White Agent extracts 
> the shipment ID, delay duration, and value. It assesses high delay risk 
> and recommends rerouting.
> 
> [PAUSE as scores appear]
> 
> The Green Agent scores this: 80% data extraction, 100% risk reasoning, 
> 83% recommendations. Overall: 89 out of 100—excellent performance.
> 
> [Let Scenario 2 run]
> 
> Scenario 2 tests hurricane response. The agent identifies the threat 
> and suggests mitigation.
> 
> Scenario 3 synthesizes multiple risks across the portfolio.
> 
> [Final report appears]
> 
> The final report shows aggregate performance with detailed metrics 
> across all scenarios."

---

### Part 3: Explain Design (40 seconds)

**SHOW:** Open `green_agent.py`, scroll to `evaluate_response` function

**SAY:**
> "How does evaluation work? The Green Agent uses F1 scoring for 
> data extraction—did the agent catch the $3.9M value and 5-day delay?
> 
> For risk reasoning, it checks if correct risk types and severity 
> levels were identified.
> 
> For recommendations, it measures alignment with optimal actions 
> and checks for clear rationale.
> 
> This benchmark tests cross-modal reasoning—combining emails and CSVs—
> causal reasoning linking events across data sources, and real 
> operational constraints like time pressure and incomplete data.
> 
> CTAE-Green provides fair, reproducible evaluation for agents in 
> complex, information-rich domains. Thank you!"

---

## ⚡ Quick Commands

**Before recording:**
```bash
cd /Users/mohamedhosny/cs194-agenticAI/ctae-green/agents
clear
rm -f ctae_evaluation_report.txt
```

**During recording:**
```bash
python3 green_agent.py
```

**View report:**
```bash
cat ctae_evaluation_report.txt
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
2. **Check timing** - Under 3 minutes?
3. **Verify content** - Task intro + demo + design notes all covered?
4. **Export/save** - Name it clearly: `CTAE_Green_Demo_Mohamed.mp4`

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

---

## 🎯 You've Got This!

Remember what you're showing:
1. ✅ A working Green Agent that orchestrates evaluation
2. ✅ Real evaluation scenarios with actual scoring
3. ✅ Thoughtful design (cross-modal, causal reasoning, operational constraints)

Just run the demo and explain what's happening. It's that simple!

**NOW GO RECORD! 🎬**

