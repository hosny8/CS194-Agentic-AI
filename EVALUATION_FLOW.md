# CTAE-Green Evaluation Flow

## Visual Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                     CTAE-GREEN AGENT                             │
│                  (Orchestrator & Judge)                          │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ 1. Initialize & Load Data
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                     DATA ENVIRONMENT                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │   Logistics  │  │  Shipment    │  │    Risk      │          │
│  │    Emails    │  │  Manifest    │  │   Alerts     │          │
│  │              │  │              │  │              │          │
│  │  • Port      │  │  • IDs       │  │  • Weather   │          │
│  │    delays    │  │  • Values    │  │  • Port      │          │
│  │  • Updates   │  │  • Routes    │  │  • Geopolit. │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ 2. Create Scenario Prompt
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                     EVALUATION SCENARIO                          │
│                                                                  │
│  Scenario 1: Shanghai Port Delay - Oil Shipment Crisis          │
│  ┌──────────────────────────────────────────────────────┐      │
│  │ Task: Analyze delayed shipment SHP-2025-1042         │      │
│  │ - Extract: Shipment ID, delay duration, value        │      │
│  │ - Assess: Financial risk, operational impact         │      │
│  │ - Recommend: Rerouting, customer notification        │      │
│  │ Time Limit: 30 seconds                               │      │
│  └──────────────────────────────────────────────────────┘      │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ 3. Send via A2A Protocol
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      WHITE AGENT                                 │
│                 (Trade Analyst Being Evaluated)                  │
│                                                                  │
│  Processing...                                                   │
│  ┌──────────────────────────────────────────────────────┐      │
│  │ 1. Parse emails and shipment data                    │      │
│  │ 2. Extract critical facts:                           │      │
│  │    • SHP-2025-1042                                   │      │
│  │    • 50,000 barrels crude oil                        │      │
│  │    • 5-day delay at Shanghai                         │      │
│  │    • $3.9M value                                     │      │
│  │ 3. Assess risks:                                     │      │
│  │    • Delay risk: HIGH                                │      │
│  │    • Financial risk: MEDIUM                          │      │
│  │ 4. Recommend actions:                                │      │
│  │    • Reroute to Ningbo port                          │      │
│  │    • Notify customer immediately                     │      │
│  └──────────────────────────────────────────────────────┘      │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ 4. Return Response (JSON)
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                     GREEN AGENT EVALUATION                       │
│                                                                  │
│  Scoring Against Ground Truth:                                  │
│                                                                  │
│  ┌─────────────────────────────────────────────────────┐       │
│  │ 1. Data Extraction Accuracy (30% weight)            │       │
│  │    • Compare extracted facts vs. ground truth       │       │
│  │    • Calculate F1 score (precision + recall)        │       │
│  │    → Score: 95.2/100 ✓                              │       │
│  └─────────────────────────────────────────────────────┘       │
│                                                                  │
│  ┌─────────────────────────────────────────────────────┐       │
│  │ 2. Risk Reasoning Quality (35% weight)              │       │
│  │    • Check risk types identified                    │       │
│  │    • Verify severity assessments                    │       │
│  │    → Score: 88.7/100 ✓                              │       │
│  └─────────────────────────────────────────────────────┘       │
│                                                                  │
│  ┌─────────────────────────────────────────────────────┐       │
│  │ 3. Recommendation Coherence (25% weight)            │       │
│  │    • Match recommendations to optimal actions       │       │
│  │    • Check for clear rationale                      │       │
│  │    → Score: 82.5/100 ✓                              │       │
│  └─────────────────────────────────────────────────────┘       │
│                                                                  │
│  ┌─────────────────────────────────────────────────────┐       │
│  │ 4. Response Time Score (10% weight)                 │       │
│  │    • Normalize against time limit                   │       │
│  │    → Score: 94.3/100 ✓                              │       │
│  └─────────────────────────────────────────────────────┘       │
│                                                                  │
│  ┌─────────────────────────────────────────────────────┐       │
│  │ OVERALL SCORE: 89.1/100                             │       │
│  │ Performance Tier: EXCELLENT                         │       │
│  └─────────────────────────────────────────────────────┘       │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ 5. Generate Report
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                     EVALUATION REPORT                            │
│                                                                  │
│  SCENARIO 1: Shanghai Port Delay - Oil Shipment Crisis          │
│  SCORES:                                                         │
│    Data Extraction Accuracy:    95.2/100                        │
│    Risk Reasoning Quality:      88.7/100                        │
│    Recommendation Coherence:    82.5/100                        │
│    Response Time Score:         94.3/100                        │
│    -------------------------------                               │
│    OVERALL SCORE:               89.1/100                        │
│                                                                  │
│  [Repeat for Scenarios 2 & 3]                                   │
│                                                                  │
│  AGGREGATE PERFORMANCE:                                          │
│  Average Overall Score:          87.3/100                       │
│  Average Data Extraction:        91.5/100                       │
│  Average Risk Reasoning:         85.2/100                       │
│  Average Recommendation Quality: 80.8/100                       │
└─────────────────────────────────────────────────────────────────┘
```

## Evaluation Metrics Explained

### 1. Data Extraction Accuracy (0-100, 30% weight)

**What it measures:** How well the agent extracts critical facts from unstructured data.

**How it's calculated:**
- Compare extracted facts against ground truth
- Calculate precision: `correct extractions / total extractions`
- Calculate recall: `correct extractions / total facts in ground truth`
- F1 score: `2 × (precision × recall) / (precision + recall)`

**Ground truth example for Scenario 1:**
- ✓ Shipment ID: SHP-2025-1042
- ✓ Quantity: 50,000 barrels
- ✓ Commodity: Crude oil
- ✓ Delay: 5 days
- ✓ Location: Shanghai Port
- ✓ Value: $3,925,000

**Good performance:** 85-100  
**Fair performance:** 60-84  
**Needs improvement:** <60

---

### 2. Risk Reasoning Quality (0-100, 35% weight)

**What it measures:** Correctness of risk identification and severity assessment.

**How it's calculated:**
- Risk type recall: `identified risks / expected risks`
- Severity accuracy: `correct severity assignments / total risks`
- Average of both scores

**Ground truth example for Scenario 1:**
- ✓ Delay risk (severity: HIGH) affecting SHP-2025-1042
- ✓ Financial risk (severity: MEDIUM) due to storage costs

**Good performance:** 80-100  
**Fair performance:** 60-79  
**Needs improvement:** <60

---

### 3. Recommendation Coherence (0-100, 25% weight)

**What it measures:** Quality, actionability, and rationale of recommendations.

**How it's calculated:**
- Action coverage: `optimal actions covered / total optimal actions`
- Rationale score: `recommendations with clear rationale / total recommendations`
- Average of both scores

**Optimal actions example for Scenario 1:**
- ✓ Reroute to alternative port (Ningbo/Qingdao)
- ✓ Notify customer of revised ETA
- ✓ Assess storage/demurrage cost impact

**Good performance:** 75-100  
**Fair performance:** 50-74  
**Needs improvement:** <50

---

### 4. Response Time Score (0-100, 10% weight)

**What it measures:** Speed of analysis under operational constraints.

**How it's calculated:**
- Normalize response time against limit
- Score = `max(0, 100 - (response_time / time_limit × 100))`

**Time limits:**
- Scenario 1: 30 seconds
- Scenario 2: 30 seconds  
- Scenario 3: 45 seconds (more complex)

**Good performance:** 90-100 (< 10% of time limit)  
**Fair performance:** 70-89 (10-30% of time limit)  
**Needs improvement:** <70 (>30% of time limit)

---

### 5. Overall Score (0-100)

**How it's calculated:**
```
Overall = (Extraction × 0.30) + 
          (Reasoning × 0.35) + 
          (Recommendations × 0.25) + 
          (Time × 0.10)
```

**Performance tiers:**
- **EXCELLENT**: 80-100
- **GOOD**: 60-79
- **FAIR**: 40-59
- **NEEDS IMPROVEMENT**: <40

---

## Three Evaluation Scenarios

### Scenario 1: Shanghai Port Delay - Oil Shipment Crisis
**Difficulty:** Medium  
**Focus:** Single-event crisis management  
**Key Challenge:** Extract impact of 5-day delay on high-value shipment  

**Data sources:**
- Port delay email
- Market price update
- Shipment manifest
- Congestion alert

**What makes it challenging:**
- Information scattered across multiple sources
- Need to calculate financial impact
- Time-sensitive decision required

---

### Scenario 2: Hurricane Risk - Gulf Operations
**Difficulty:** Hard  
**Focus:** Weather-driven operational disruption  
**Key Challenge:** Identify at-risk assets and recommend mitigation  

**Data sources:**
- Hurricane alert email
- Risk bulletin
- Shipment manifest
- Weather risk alert

**What makes it challenging:**
- Need to infer which shipments are in hurricane path
- Multiple vessels potentially affected
- Safety vs. operational cost tradeoffs

---

### Scenario 3: Multi-Risk Assessment - Global View
**Difficulty:** Hard  
**Focus:** Synthesizing multiple concurrent risks  
**Key Challenge:** Prioritize top 3 risks across $50M+ portfolio  

**Data sources:**
- All emails (4)
- Full shipment manifest (5 shipments)
- All risk alerts (3)

**What makes it challenging:**
- Information overload (must filter signal from noise)
- Concurrent risks requiring prioritization
- Need causal reasoning across data sources
- Resource allocation decisions

---

## Why This Evaluation Design Is Strong

### 1. Real-World Relevance
- Based on actual commodity trade operations
- Uses realistic data formats (emails, CSVs, alerts)
- Tests skills needed in financial/logistics domains

### 2. Cross-Modal Reasoning
- **Unstructured text:** Emails with natural language
- **Structured data:** CSV with precise values
- **Semi-structured:** JSON risk alerts
- Agents must integrate all three

### 3. Causal Reasoning Assessment
Tests ability to link events:
```
Port delay → Shipment impact → Financial risk → Mitigation action
```

### 4. Operational Constraints
- **Time pressure:** 30-45 second limits
- **Incomplete data:** Not all information provided explicitly
- **Ambiguity:** Natural language requires interpretation

### 5. Reproducibility
- Fixed scenarios with deterministic ground truth
- Automated scoring pipeline
- Clear success criteria
- Repeatable across different agents

### 6. Scalability
- Easy to add new scenarios
- Extensible metric system
- Modular evaluation functions

---

## Comparison to Existing Benchmarks

| Benchmark | Domain | Data Types | Causal Reasoning | Operational Constraints |
|-----------|--------|------------|------------------|-------------------------|
| **τ-bench** | Tool use | API calls | Limited | No time limits |
| **BrowserGym** | Web nav | HTML/DOM | Limited | Task-based only |
| **SWE-bench** | Coding | Code files | Moderate | No time limits |
| **Finance Agent** | Finance | Text/tables | Moderate | Limited |
| **CTAE-Green** | Trade | Text+CSV+JSON | ✓ Strong | ✓ Time+incomplete data |

---

## Future Extensions

### More Scenarios
- Supply chain disruption cascades
- Commodity price volatility events
- Multi-party negotiation simulations
- Regulatory compliance checks

### Additional Metrics
- Cost optimization score
- Risk mitigation effectiveness
- Communication clarity (for multi-agent scenarios)
- Long-term strategic reasoning

### Multi-Agent Collaboration
- Coordination between analyst agents
- Information sharing protocols
- Conflict resolution in recommendations

### Dynamic Environments
- Real-time data streams
- Agent adaptation to changing conditions
- Online learning evaluation

---

## Summary

CTAE-Green provides a comprehensive, reproducible evaluation framework for agents in commodity trade operations. By combining cross-modal data, causal reasoning requirements, and operational constraints, it tests capabilities essential for real-world decision-making in information-rich enterprise domains.

The evaluation flow is transparent, automated, and fair—making it suitable for agent development, benchmarking, and leaderboards.




