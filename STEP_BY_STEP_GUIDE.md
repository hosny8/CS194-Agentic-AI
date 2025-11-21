# CTAE-Green Demo: Complete Step-by-Step Guide

This guide will walk you through **every single step** needed to create and record your 3-minute Green Agent demo video.

## Timeline Overview

- **Setup & Testing**: 30 minutes
- **Demo Recording**: 30 minutes  
- **Total**: ~1 hour

---

## Phase 1: Setup and Verification (20 minutes)

### Step 1: Verify Project Structure

Open Terminal and check that everything is in place:

```bash
cd /Users/mohamedhosny/cs194-agenticAI/ctae-green

# Check structure
ls -la
```

**Expected output:**
```
data/
agents/
README.md
run_demo.sh
requirements.txt
STEP_BY_STEP_GUIDE.md
```

### Step 2: Set Up Python Environment

```bash
# Go to parent directory
cd /Users/mohamedhosny/cs194-agenticAI

# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# Verify Python version (should be 3.11+)
python3 --version
```

### Step 3: Install Dependencies

```bash
# Install agentbeats
pip install agentbeats

# Verify installation
pip list | grep agentbeats
```

### Step 4: Test the Demo (Dry Run)

```bash
# Go back to ctae-green
cd ctae-green

# Make script executable
chmod +x run_demo.sh

# Run the demo
./run_demo.sh
```

**What you should see:**
1. Initialization messages
2. Three scenarios running sequentially
3. Scores for each scenario
4. Final aggregate report
5. "Report saved to ./ctae_evaluation_report.txt"

**If you get errors:**
- Check that you're in the right directory: `pwd` should show `.../ctae-green`
- Verify virtual environment is active: `which python3` should show path with `venv`
- Check data files exist: `ls data/`

### Step 5: Review the Output

```bash
# Open the generated report
cat ctae_evaluation_report.txt
```

**Expected report structure:**
- Header with benchmark name
- Three scenario sections with scores
- Aggregate performance summary
- Scores in range 70-95/100 (mock agent performs reasonably well)

---

## Phase 2: Prepare for Recording (10 minutes)

### Step 6: Clean Your Terminal

```bash
# Clear terminal
clear

# Reset demo environment
cd /Users/mohamedhosny/cs194-agenticAI/ctae-green
rm -f ctae_evaluation_report.txt  # Remove old report
rm -f agents/ctae_evaluation_report.txt  # Remove if created in agents/
```

### Step 7: Prepare Your Screen Layout

**Recommended setup:**

1. **Terminal**: Full screen or large window, easy-to-read font size (14-16pt)
2. **Code Editor** (VS Code/Cursor): Have these files open in tabs:
   - `README.md`
   - `data/logistics_emails.json`
   - `data/shipment_manifest.csv`
   - `agents/green_agent.py` (scroll to `evaluate_response` function)

3. **File Browser**: Optional, for showing project structure

### Step 8: Practice Your Script

Read through the **Demo Video Script** section below OUT LOUD 2-3 times. Time yourself—it should be ~2.5-3 minutes.

---

## Phase 3: Record Your Demo (30 minutes)

### Step 9: Choose Recording Method

**Option A: QuickTime (macOS - Simple)**

1. Open QuickTime Player
2. File → New Screen Recording
3. Select microphone for narration
4. Click red record button
5. Select screen area to record
6. Click "Start Recording"

**Option B: OBS Studio (All platforms - Advanced)**

1. Download OBS Studio (free)
2. Add "Display Capture" source
3. Add "Audio Input Capture" for your microphone
4. Click "Start Recording"

**Option C: Loom (Web-based - Easiest)**

1. Go to loom.com and sign up (free)
2. Install browser extension
3. Click Loom icon → "Record Screen"
4. Select "Screen + Camera" or "Screen Only"
5. Click "Start Recording"

### Step 10: Record the Demo

**Before you start recording:**
- Close unnecessary applications
- Turn off notifications (Do Not Disturb mode)
- Clear terminal: `clear`
- Position windows as planned
- Take a deep breath!

**Now record following this script:**

---

## Demo Video Script (3 minutes)

### **Part 1: Introduction (0:00-0:50, 50 seconds)**

**[Show: Project structure in file browser or `ls` output]**

> "Hello! I'm presenting CTAE-Green, a benchmark for evaluating AI agents in commodity trade operations."

**[Show: Open `data/logistics_emails.json` in editor]**

> "The task environment simulates real-world trade scenarios. Agents receive logistics emails with shipping updates..."

**[Scroll through the email file slowly]**

> "...like this urgent alert about a 5-day port delay affecting a $3.9 million oil shipment."

**[Show: Open `data/shipment_manifest.csv`]**

> "They also get structured shipment data with commodity types, quantities, origins, destinations, and financial values."

**[Show: Open `data/risk_alerts.json`]**

> "And real-time risk alerts for weather events like hurricanes, port congestion, and geopolitical disruptions."

**[Switch to README or just speak]**

> "Agents must extract critical facts, assess risks, and recommend actions—like rerouting cargo or hedging positions. The Green Agent evaluates them on four metrics: data extraction accuracy, risk reasoning quality, recommendation coherence, and response time."

### **Part 2: Demonstration (0:50-2:20, 90 seconds)**

**[Show: Terminal, in the ctae-green directory]**

> "Let's see it in action. I'll run the Green Agent demo."

**[Type and execute:]**
```bash
./run_demo.sh
```

**[As the demo runs, narrate over it:]**

> "The Green Agent initializes and loads three evaluation scenarios. Here's Scenario 1: Shanghai Port Delay—a crisis involving the delayed oil shipment we just saw."

**[Let it run, show the scenario loading]**

> "It sends this scenario to a White Agent—the agent being evaluated. The White Agent has 30 seconds to analyze the situation."

**[Show the "White Agent responded" message]**

> "The White Agent extracts key facts: shipment ID SHP-2025-1042, 50,000 barrels of crude oil, delayed 5 days, value $3.9 million. It assesses the delay as high-risk and recommends rerouting to an alternative port."

**[Show the scores appearing]**

> "The Green Agent evaluates this response. Data extraction accuracy: 95%. Risk reasoning quality: 89%. Recommendation coherence: 83%. Overall score: 89 out of 100—excellent performance on a medium-difficulty scenario."

**[Let Scenario 2 start]**

> "Scenario 2 tests hurricane response. A Category 3 hurricane is approaching the Gulf of Mexico. The agent must identify at-risk shipments and recommend immediate mitigation actions."

**[Let it finish quickly]**

> "And Scenario 3 synthesizes multiple concurrent risks across a $50 million portfolio, testing the agent's ability to prioritize under pressure."

**[Show the final aggregate report appearing]**

> "Here's the final evaluation report. Aggregate performance: 87 out of 100. Strong data extraction, good risk reasoning, and coherent recommendations. The report breaks down performance across all three scenarios and identifies areas for improvement."

### **Part 3: Design Notes (2:20-3:00, 40 seconds)**

**[Show: Open `agents/green_agent.py` and scroll to the `evaluate_response` function]**

> "How does the Green Agent judge responses? Let me show you the evaluation logic."

**[Show the scoring code briefly]**

> "For data extraction accuracy, it uses F1 scoring—comparing extracted facts against ground truth. For example, did the agent catch that the shipment is worth $3.9 million? Did it identify the 5-day delay?"

**[Scroll to risk assessment evaluation]**

> "For risk reasoning, it checks if the agent identified the correct risk types—port congestion, financial exposure—and assigned appropriate severity levels."

**[Scroll to recommendation evaluation]**

> "For recommendations, it measures alignment with optimal actions like rerouting or customer notification, and checks if each recommendation has clear rationale."

**[Close the file or show the report again]**

> "Why is this benchmark unique? It tests cross-modal reasoning—combining unstructured emails with structured CSVs. It evaluates causal reasoning—linking a port delay to shipment impact to financial risk. And it simulates real operational constraints: incomplete data, time pressure, and high-stakes decisions."

**[Show final report or README]**

> "This approach creates fair, reproducible evaluation for agents in information-rich enterprise domains. CTAE-Green demonstrates how standardized benchmarks can assess not just coding or browsing, but complex real-world reasoning."

**[End screen: Show the aggregate score or project structure]**

> "Thank you! CTAE-Green: evaluating multi-agent reasoning in commodity trade operations."

**[Stop recording]**

---

### Step 11: Review Your Recording

Watch your recording:

✅ **Check for:**
- Clear audio (no background noise, no echo)
- Screen content is visible (fonts large enough)
- Demo runs smoothly without errors
- Time is under 3 minutes
- All required elements covered:
  - ✅ Task introduction (what/environment/actions)
  - ✅ Demonstration (Green Agent evaluating White Agent)
  - ✅ Design notes (test case generation, reliability testing)

❌ **If any issues:**
- Re-record that section only (if your tool allows)
- Or do a full re-take (it's just 3 minutes!)

### Step 12: Export and Save

**For QuickTime:**
- File → Save
- Choose a clear filename: `CTAE_Green_Demo_Mohamed_Matheus.mov`
- Save to Desktop or Downloads

**For OBS Studio:**
- Recordings are auto-saved to Videos folder
- Find the file and rename it

**For Loom:**
- Video auto-uploads to your Loom library
- Download MP4 or share link directly

---

## Phase 4: Prepare Short Report (15 minutes)

### Step 13: Create Short Report Document

You already have most of the content from your original query! Create a document (Google Docs, Word, or Markdown) with these sections:

```markdown
# CTAE-Green: Evaluating Multi-Agent Reasoning in Commodity Trade

## Team
- Mohamed Hosny
- Matheus [Last Name]

## Abstract
The Commodity Trade Agent Evaluation Green Agent (CTAE-Green) is a benchmarking 
and evaluation agent designed to assess multi-agent performance in complex, 
data-driven decision environments such as commodity trade logistics and risk 
management...

[Copy your Q3 response]

## Task Description
The CTAE-Green Agent tests how well "white agents" handle reasoning in simulated 
commodity trade operations...

[Copy your Q5 response]

## Related Work
Existing evaluation benchmarks like τ-bench, BrowserGym, and SWE-bench assess 
reasoning and task automation but lack real-world data interdependencies...

[Copy your Q6 response]

## Evaluation Design
### Inputs
- Streams of textual emails, CSV shipment data, and simulated news headlines
- API endpoints for live data queries (simulated market/risk feeds)

### Outputs
- Structured reports summarizing current exposure, risk events, and operational 
  recommendations

### Success Criteria
- Data extraction accuracy (precision/recall)
- Correct risk-event linkage to shipments
- Timely and coherent reasoning output (≤30s per scenario)
- Quality of written summaries (LLM-as-judge + rubric-based scoring)

[Continue with Q7 content]

## Implementation
[Describe what you built]

We implemented CTAE-Green as a Python-based orchestration system with:
- 3 evaluation scenarios of varying difficulty
- Ground truth datasets for logistics emails, shipment manifests, and risk alerts
- Automated scoring across 4 metrics: data extraction, risk reasoning, 
  recommendations, and response time
- Mock white agent for demonstration purposes
- Detailed evaluation reports with aggregate performance

## Demo
[Link or describe your video]

Our 3-minute demo video demonstrates:
1. The task environment with logistics emails, shipment data, and risk alerts
2. The Green Agent orchestrating evaluation across three scenarios
3. Scoring of white agent responses with detailed metrics
4. Evaluation methodology using F1 scoring, rubric-based assessment, and 
   LLM-as-judge techniques

## Division of Labor
- Mohamed: Green Agent architecture, orchestration logic, and evaluation metrics
- Matheus: Data generation, environment setup, and demo preparation

## Repository
[Link to GitHub repo if you create one]

## References
- AgentBeats Platform: https://github.com/agentbeats/agentbeats
- [Any other references]
```

### Step 14: Polish and Format

- Ensure consistent formatting
- Add page numbers if required
- Proofread for typos
- Export as PDF

---

## Phase 5: Submission (5 minutes)

### Step 15: Prepare Submission Package

Create a folder with:
- ✅ Demo video file (MP4 or MOV, <100MB ideally)
- ✅ Short report (PDF)
- ✅ (Optional) Link to GitHub repo with code

### Step 16: Upload and Submit

Follow your course's submission instructions:
- Upload to Canvas/Gradescope/etc.
- Or share Loom link + PDF report
- Or email if instructed

---

## Troubleshooting

### "Permission denied" when running run_demo.sh
```bash
chmod +x run_demo.sh
```

### Python not found or wrong version
```bash
python3 --version  # Should be 3.11+

# If wrong version, specify:
python3.11 -m venv venv
```

### Module not found: agentbeats
```bash
source venv/bin/activate  # Make sure venv is active
pip install agentbeats
```

### Demo runs but no report generated
```bash
# Check if it was created in agents/ subdirectory
ls agents/*.txt

# Or run the Python script directly
cd agents
python3 green_agent.py
cd ..
```

### Recording software not working
- **Mac**: Use built-in QuickTime (already installed)
- **Windows**: Use Xbox Game Bar (Win+G)
- **Any platform**: Use Loom web app (no install needed)

### Video is too long (>3 minutes)
- Speed up narration
- Cut the introduction shorter
- Skip showing some code details
- Focus on the demo run itself

### Video is too large to upload
```bash
# Compress with ffmpeg (if installed)
ffmpeg -i input.mov -vcodec h264 -acodec aac -b:v 2M output.mp4

# Or use online compressor: https://www.freeconvert.com/video-compressor
# Or upload to YouTube as unlisted and share link
```

---

## Quick Checklist

Before submitting, verify:

### Code & Demo
- [ ] All data files exist in `data/`
- [ ] Demo runs without errors
- [ ] Evaluation report is generated
- [ ] Scores are reasonable (70-95 range)

### Video
- [ ] Under 3 minutes
- [ ] Audio is clear
- [ ] Screen content is readable
- [ ] Covers: task intro, demonstration, design notes
- [ ] Shows Green Agent evaluating White Agent

### Report
- [ ] All sections complete (abstract, task, evaluation, etc.)
- [ ] Team member names included
- [ ] Division of labor specified
- [ ] Formatted and proofread

### Submission
- [ ] Video file exported and named properly
- [ ] Report exported as PDF
- [ ] Files uploaded to submission platform
- [ ] Confirmation received

---

## You're Done! 🎉

**Timeline Recap:**
- ✅ Setup & verify: 20 minutes
- ✅ Practice script: 10 minutes  
- ✅ Record demo: 20 minutes
- ✅ Create report: 15 minutes
- ✅ Submit: 5 minutes

**Total: ~70 minutes**

If you encounter any issues, refer to the Troubleshooting section above or check the main README.md for additional details.

Good luck with your submission!




