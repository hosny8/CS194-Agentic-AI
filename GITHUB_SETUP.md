# 🚀 Push to GitHub - Quick Guide

## Your Local Repo is Ready! ✅

I've initialized a git repository with all your files committed.

---

## Step 1: Create GitHub Repository

1. Go to [github.com](https://github.com) and login
2. Click the **"+" button** (top right) → "New repository"
3. Fill in:
   - **Repository name:** `ctae-green` (or `commodity-trade-agent-eval`)
   - **Description:** "CTAE-Green: Evaluating Multi-Agent Reasoning in Commodity Trade Operations"
   - **Visibility:** Public or Private (your choice)
   - **DON'T** check "Initialize with README" (you already have one!)
4. Click **"Create repository"**

---

## Step 2: Push Your Code

GitHub will show you commands. Use these:

```bash
cd /Users/mohamedhosny/cs194-agenticAI/ctae-green

# Add remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/ctae-green.git

# Push to GitHub
git branch -M main
git push -u origin main
```

**Example:** If your username is `mohamedhosny`:
```bash
git remote add origin https://github.com/mohamedhosny/ctae-green.git
git branch -M main
git push -u origin main
```

---

## Step 3: Clone in VS Code

### Option A: Clone in VS Code
1. Open VS Code
2. Press `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows)
3. Type "Git: Clone" and select it
4. Paste your repo URL: `https://github.com/YOUR_USERNAME/ctae-green.git`
5. Choose where to save it
6. Click "Open" when done

### Option B: Clone via Terminal
```bash
# Navigate to where you want the project
cd ~/Documents  # or wherever

# Clone the repo
git clone https://github.com/YOUR_USERNAME/ctae-green.git

# Open in VS Code
code ctae-green
```

---

## Step 4: Set Up in VS Code

Once opened:

```bash
# In VS Code terminal
cd ctae-green

# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate  # Mac/Linux
# OR
venv\Scripts\activate  # Windows

# Install dependencies
pip install agentbeats

# Test the demo
cd agents
python3 green_agent.py
```

---

## Quick Reference

### Push Future Changes
```bash
git add .
git commit -m "Your change description"
git push
```

### Pull Changes (if editing from multiple places)
```bash
git pull
```

### Check Status
```bash
git status
```

---

## Project Structure

```
ctae-green/
├── README.md              # Main documentation
├── START_HERE.md          # Quick start guide
├── QUICK_RECORDING_GUIDE.md  # For demo recording
├── data/                  # Evaluation data
│   ├── logistics_emails.json
│   ├── shipment_manifest.csv
│   └── risk_alerts.json
├── agents/                # Agent implementations
│   ├── green_agent.py
│   ├── green_agent_card.toml
│   └── white_agent_card.toml
└── requirements.txt       # Python dependencies
```

---

## Troubleshooting

### "Permission denied (publickey)"
If you get this error when pushing:
1. Use HTTPS URL instead: `https://github.com/YOUR_USERNAME/ctae-green.git`
2. Or set up SSH keys: [GitHub SSH Guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)

### "Updates were rejected"
If someone else pushed changes:
```bash
git pull --rebase
git push
```

### Need to change remote URL
```bash
git remote -v  # See current remote
git remote set-url origin NEW_URL  # Change it
```

---

## 🎯 You're Done!

Your code is now:
- ✅ Version controlled with Git
- ✅ Ready to push to GitHub
- ✅ Easy to clone into VS Code
- ✅ Shareable with teammates or instructors

Just follow **Step 1** to create the GitHub repo, then **Step 2** to push!




