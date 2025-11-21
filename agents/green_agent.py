"""
CTAE-Green Agent Implementation
Orchestrates and evaluates commodity trade agent performance
"""

import json
import time
from typing import Dict, List, Any
from pathlib import Path

class CTAEGreenAgent:
    """Green Agent for Commodity Trade Agent Evaluation"""
    
    def __init__(self, data_dir: str = None):
        # Auto-detect data directory
        if data_dir is None:
            # Try parent directory first (if running from agents/)
            if Path("../data").exists():
                data_dir = "../data"
            # Then try current directory (if running from ctae-green/)
            elif Path("./data").exists():
                data_dir = "./data"
            else:
                raise FileNotFoundError("Cannot find data directory. Please run from ctae-green/ or ctae-green/agents/")
        
        self.data_dir = Path(data_dir)
        self.scenarios = self.load_scenarios()
        self.ground_truth = self.load_ground_truth()
        
    def load_scenarios(self) -> List[Dict[str, Any]]:
        """Load evaluation scenarios from data files"""
        scenarios = []
        
        # Load emails
        emails_path = self.data_dir / "logistics_emails.json"
        with open(emails_path, 'r') as f:
            emails = json.load(f)
        
        # Load shipments
        shipments_path = self.data_dir / "shipment_manifest.csv"
        with open(shipments_path, 'r') as f:
            shipments = f.read()
        
        # Load risk alerts
        risks_path = self.data_dir / "risk_alerts.json"
        with open(risks_path, 'r') as f:
            risks = json.load(f)
        
        # Create scenario 1: Port Delay Crisis
        scenarios.append({
            "id": "scenario_01",
            "name": "Shanghai Port Delay - Oil Shipment Crisis",
            "difficulty": "medium",
            "description": "Analyze delayed oil shipment and assess impact",
            "data": {
                "emails": [emails[0], emails[2]],  # Port delay + price update
                "shipments": shipments,
                "risk_alerts": [risks[1]]  # Shanghai congestion
            },
            "task": "Analyze the Shanghai port delay for shipment SHP-2025-1042. Extract key details, assess financial and operational risks, and provide actionable recommendations.",
            "time_limit": 30
        })
        
        # Create scenario 2: Hurricane Warning
        scenarios.append({
            "id": "scenario_02",
            "name": "Hurricane Risk - Gulf Operations",
            "difficulty": "hard",
            "description": "Evaluate hurricane threat to Gulf shipping operations",
            "data": {
                "emails": [emails[1]],  # Hurricane alert
                "shipments": shipments,
                "risk_alerts": [risks[0]]  # Hurricane risk
            },
            "task": "A Category 3 hurricane is approaching the Gulf of Mexico. Identify which shipments are at risk, assess severity, and recommend mitigation actions.",
            "time_limit": 30
        })
        
        # Create scenario 3: Multi-risk Integration
        scenarios.append({
            "id": "scenario_03",
            "name": "Multi-Risk Assessment - Global View",
            "difficulty": "hard",
            "description": "Synthesize multiple risk factors across global operations",
            "data": {
                "emails": emails,
                "shipments": shipments,
                "risk_alerts": risks
            },
            "task": "Provide a comprehensive risk assessment across all active shipments. Prioritize the top 3 risks and recommend resource allocation for the operations team.",
            "time_limit": 45
        })
        
        return scenarios
    
    def load_ground_truth(self) -> Dict[str, Any]:
        """Load ground truth for evaluation"""
        return {
            "scenario_01": {
                "critical_facts": [
                    "SHP-2025-1042",
                    "50,000 barrels",
                    "crude oil",
                    "delayed 5 days",
                    "Shanghai Port",
                    "$3,925,000 value"
                ],
                "risks": [
                    {"type": "delay", "severity": "high", "shipment": "SHP-2025-1042"},
                    {"type": "financial", "severity": "medium", "impact": "storage costs"}
                ],
                "optimal_actions": [
                    "reroute",
                    "alternative port",
                    "customer notification"
                ]
            },
            "scenario_02": {
                "critical_facts": [
                    "Category 3 hurricane",
                    "Gulf of Mexico",
                    "Oct 24 landfall",
                    "Houston to Miami lane affected"
                ],
                "risks": [
                    {"type": "weather", "severity": "critical", "region": "Gulf Coast"},
                    {"type": "operational", "severity": "high", "impact": "delays"}
                ],
                "optimal_actions": [
                    "delay departures",
                    "reroute via Atlantic",
                    "secure vessels"
                ]
            },
            "scenario_03": {
                "critical_facts": [
                    "Multiple concurrent risks",
                    "Shanghai delay",
                    "Hurricane threat",
                    "Suez concerns",
                    "Total exposure > $50M"
                ],
                "risks": [
                    {"type": "weather", "severity": "critical"},
                    {"type": "port_congestion", "severity": "high"},
                    {"type": "geopolitical", "severity": "medium"}
                ],
                "optimal_actions": [
                    "prioritize hurricane response",
                    "establish contingency routes",
                    "enhance monitoring"
                ]
            }
        }
    
    def create_scenario_prompt(self, scenario: Dict[str, Any]) -> str:
        """Format scenario data into a prompt for the white agent"""
        prompt = f"""# Commodity Trade Analysis Task

**Scenario**: {scenario['name']}
**Description**: {scenario['description']}
**Time Limit**: {scenario['time_limit']} seconds

## Task
{scenario['task']}

## Available Data

### Logistics Emails
"""
        for email in scenario['data']['emails']:
            prompt += f"\n---\n**From**: {email['from']}\n**Subject**: {email['subject']}\n**Timestamp**: {email['timestamp']}\n\n{email['body']}\n"
        
        prompt += "\n\n### Shipment Manifest\n```csv\n"
        prompt += scenario['data']['shipments']
        prompt += "\n```\n"
        
        prompt += "\n\n### Risk Alerts\n"
        for risk in scenario['data']['risk_alerts']:
            prompt += f"\n**[{risk['severity']}]** {risk['title']}\n"
            prompt += f"- Category: {risk['category']}\n"
            prompt += f"- {risk['description']}\n"
            prompt += f"- Recommended Action: {risk['recommended_action']}\n"
        
        prompt += "\n\n## Required Output Format\n"
        prompt += """
Please provide your analysis in the following JSON format:
```json
{
  "extracted_data": {
    "shipment_ids": ["list of affected shipment IDs"],
    "commodities": ["list of commodities"],
    "key_facts": ["list of critical facts extracted"]
  },
  "risk_assessment": [
    {
      "risk_type": "type of risk",
      "severity": "low/medium/high/critical",
      "affected_assets": ["shipments or regions affected"],
      "description": "brief explanation"
    }
  ],
  "recommendations": [
    {
      "priority": "high/medium/low",
      "action": "specific action to take",
      "rationale": "why this action is recommended"
    }
  ],
  "reasoning": "Your step-by-step analysis process"
}
```
"""
        return prompt
    
    def evaluate_response(self, scenario_id: str, response: Dict[str, Any], response_time: float) -> Dict[str, Any]:
        """Evaluate white agent response against ground truth"""
        ground_truth = self.ground_truth[scenario_id]
        scores = {}
        
        # 1. Data Extraction Accuracy (0-100)
        extracted_facts = response.get("extracted_data", {}).get("key_facts", [])
        critical_facts = ground_truth["critical_facts"]
        
        # Calculate precision and recall
        extracted_lower = [f.lower() for f in extracted_facts]
        matched = sum(1 for fact in critical_facts if any(fact.lower() in ext for ext in extracted_lower))
        
        precision = (matched / len(extracted_facts)) * 100 if extracted_facts else 0
        recall = (matched / len(critical_facts)) * 100
        f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
        
        scores["data_extraction_accuracy"] = round(f1, 2)
        
        # 2. Risk Reasoning Quality (0-100)
        risk_assessment = response.get("risk_assessment", [])
        gt_risks = ground_truth["risks"]
        
        # Check if critical risks identified
        risk_types_found = {r.get("risk_type", "") for r in risk_assessment}
        risk_types_expected = {r["type"] for r in gt_risks}
        
        risk_recall = len(risk_types_found & risk_types_expected) / len(risk_types_expected) * 100 if risk_types_expected else 0
        
        # Check severity assessment accuracy
        severity_correct = sum(
            1 for r in risk_assessment 
            if any(
                r.get("risk_type") == gt["type"] and r.get("severity") == gt["severity"]
                for gt in gt_risks
            )
        )
        severity_accuracy = (severity_correct / len(gt_risks)) * 100 if gt_risks else 0
        
        scores["risk_reasoning_quality"] = round((risk_recall + severity_accuracy) / 2, 2)
        
        # 3. Recommendation Coherence (0-100)
        recommendations = response.get("recommendations", [])
        optimal_actions = ground_truth["optimal_actions"]
        
        # Check if recommendations align with optimal actions
        rec_texts = " ".join([r.get("action", "").lower() for r in recommendations])
        actions_covered = sum(1 for action in optimal_actions if action.lower() in rec_texts)
        
        action_coverage = (actions_covered / len(optimal_actions)) * 100 if optimal_actions else 0
        
        # Check if recommendations have clear rationale
        has_rationale = sum(1 for r in recommendations if r.get("rationale", "").strip())
        rationale_score = (has_rationale / len(recommendations)) * 100 if recommendations else 0
        
        scores["recommendation_coherence"] = round((action_coverage + rationale_score) / 2, 2)
        
        # 4. Response Time (normalized, lower is better)
        time_limit = 30  # Default
        time_score = max(0, 100 - (response_time / time_limit * 100))
        scores["response_time_seconds"] = round(response_time, 2)
        scores["response_time_score"] = round(time_score, 2)
        
        # 5. Overall Score (weighted average)
        scores["overall_score"] = round(
            scores["data_extraction_accuracy"] * 0.30 +
            scores["risk_reasoning_quality"] * 0.35 +
            scores["recommendation_coherence"] * 0.25 +
            scores["response_time_score"] * 0.10,
            2
        )
        
        return scores
    
    def generate_evaluation_report(self, results: List[Dict[str, Any]]) -> str:
        """Generate human-readable evaluation report"""
        report = "=" * 60 + "\n"
        report += "CTAE-GREEN EVALUATION REPORT\n"
        report += "Commodity Trade Agent Evaluation\n"
        report += "=" * 60 + "\n\n"
        
        for i, result in enumerate(results, 1):
            report += f"\n{'=' * 60}\n"
            report += f"SCENARIO {i}: {result['scenario_name']}\n"
            report += f"{'=' * 60}\n"
            report += f"Difficulty: {result['difficulty']}\n"
            report += f"Agent Response Time: {result['scores']['response_time_seconds']}s\n\n"
            
            report += "SCORES:\n"
            report += f"  Data Extraction Accuracy:    {result['scores']['data_extraction_accuracy']}/100\n"
            report += f"  Risk Reasoning Quality:      {result['scores']['risk_reasoning_quality']}/100\n"
            report += f"  Recommendation Coherence:    {result['scores']['recommendation_coherence']}/100\n"
            report += f"  Response Time Score:         {result['scores']['response_time_score']}/100\n"
            report += f"  -------------------------------\n"
            report += f"  OVERALL SCORE:               {result['scores']['overall_score']}/100\n"
            
            # Performance tier
            overall = result['scores']['overall_score']
            if overall >= 80:
                tier = "EXCELLENT"
            elif overall >= 60:
                tier = "GOOD"
            elif overall >= 40:
                tier = "FAIR"
            else:
                tier = "NEEDS IMPROVEMENT"
            
            report += f"\n  Performance Tier: {tier}\n"
        
        # Summary
        avg_overall = sum(r['scores']['overall_score'] for r in results) / len(results)
        avg_extraction = sum(r['scores']['data_extraction_accuracy'] for r in results) / len(results)
        avg_reasoning = sum(r['scores']['risk_reasoning_quality'] for r in results) / len(results)
        avg_recommendations = sum(r['scores']['recommendation_coherence'] for r in results) / len(results)
        
        report += f"\n\n{'=' * 60}\n"
        report += "AGGREGATE PERFORMANCE\n"
        report += f"{'=' * 60}\n"
        report += f"Average Overall Score:          {avg_overall:.2f}/100\n"
        report += f"Average Data Extraction:        {avg_extraction:.2f}/100\n"
        report += f"Average Risk Reasoning:         {avg_reasoning:.2f}/100\n"
        report += f"Average Recommendation Quality: {avg_recommendations:.2f}/100\n"
        
        return report

# Mock white agent response function for demo purposes
def mock_white_agent_response(scenario_prompt: str, agent_quality: str = "strong") -> Dict[str, Any]:
    """
    Simulates a white agent response for demo purposes.
    In production, this would be an actual A2A call to the white agent.
    
    Args:
        scenario_prompt: The scenario description
        agent_quality: "strong", "weak", or "moderate" for different performance levels
    """
    # Simple mock - extracts some keywords and generates basic response
    if "SHP-2025-1042" in scenario_prompt and agent_quality == "strong":
        return {
            "extracted_data": {
                "shipment_ids": ["SHP-2025-1042"],
                "commodities": ["Crude Oil WTI"],
                "key_facts": [
                    "50,000 barrels of crude oil",
                    "Delayed 5 days",
                    "Shanghai Port congestion",
                    "Value: $3,925,000"
                ]
            },
            "risk_assessment": [
                {
                    "risk_type": "delay",
                    "severity": "high",
                    "affected_assets": ["SHP-2025-1042"],
                    "description": "5-day delay at Shanghai port due to severe congestion"
                },
                {
                    "risk_type": "financial",
                    "severity": "medium",
                    "affected_assets": ["SHP-2025-1042"],
                    "description": "Additional storage and demurrage costs"
                }
            ],
            "recommendations": [
                {
                    "priority": "high",
                    "action": "Reroute to alternative port (Ningbo or Qingdao)",
                    "rationale": "Reduce delay impact and minimize storage costs"
                },
                {
                    "priority": "high",
                    "action": "Notify customer of delay and revised ETA",
                    "rationale": "Maintain transparency and manage expectations"
                }
            ],
            "reasoning": "Identified critical shipment SHP-2025-1042 with 5-day delay. High financial exposure ($3.9M) warrants immediate action. Rerouting is optimal to minimize further delays."
        }
    elif "hurricane" in scenario_prompt.lower():
        return {
            "extracted_data": {
                "shipment_ids": [],
                "commodities": [],
                "key_facts": [
                    "Category 3 hurricane",
                    "Gulf of Mexico",
                    "Landfall October 24"
                ]
            },
            "risk_assessment": [
                {
                    "risk_type": "weather",
                    "severity": "critical",
                    "affected_assets": ["Gulf Coast terminals"],
                    "description": "Category 3 hurricane approaching Gulf"
                }
            ],
            "recommendations": [
                {
                    "priority": "high",
                    "action": "Delay all Gulf departures",
                    "rationale": "Avoid vessel damage and crew safety risks"
                }
            ],
            "reasoning": "Hurricane poses immediate threat. Safety is priority."
        }
    else:
        # Multi-risk scenario
        return {
            "extracted_data": {
                "shipment_ids": ["SHP-2025-1042", "SHP-2025-1098"],
                "commodities": ["Crude Oil", "Copper", "Natural Gas"],
                "key_facts": [
                    "Shanghai port delay",
                    "Hurricane threat",
                    "Total exposure > $50M"
                ]
            },
            "risk_assessment": [
                {
                    "risk_type": "weather",
                    "severity": "critical",
                    "affected_assets": ["Gulf operations"],
                    "description": "Hurricane Category 3"
                },
                {
                    "risk_type": "port_congestion",
                    "severity": "high",
                    "affected_assets": ["SHP-2025-1042"],
                    "description": "Shanghai 5-day delays"
                },
                {
                    "risk_type": "geopolitical",
                    "severity": "medium",
                    "affected_assets": ["Suez route shipments"],
                    "description": "Suez Canal concerns"
                }
            ],
            "recommendations": [
                {
                    "priority": "high",
                    "action": "Prioritize hurricane response - secure Gulf vessels",
                    "rationale": "Critical safety and operational priority"
                },
                {
                    "priority": "medium",
                    "action": "Reroute Shanghai shipment to alternative port",
                    "rationale": "Mitigate delay costs"
                },
                {
                    "priority": "medium",
                    "action": "Monitor Suez situation and prepare Cape route contingency",
                    "rationale": "Proactive risk management"
                }
            ],
            "reasoning": "Three concurrent risks identified. Hurricane is highest priority due to safety concerns. Shanghai delay is costly but manageable. Suez situation requires monitoring."
        }


def run_demo():
    """Run a demonstration of CTAE-Green evaluation"""
    print("\n" + "=" * 60)
    print("CTAE-GREEN AGENT DEMO")
    print("Commodity Trade Agent Evaluation")
    print("=" * 60 + "\n")
    
    # Initialize green agent (auto-detects data directory)
    green_agent = CTAEGreenAgent()
    
    print("✓ Green Agent initialized")
    print(f"✓ Loaded {len(green_agent.scenarios)} evaluation scenarios\n")
    
    # Run evaluation on each scenario
    all_results = []
    
    for i, scenario in enumerate(green_agent.scenarios, 1):
        print(f"\n{'=' * 60}")
        print(f"Running Scenario {i}/{len(green_agent.scenarios)}: {scenario['name']}")
        print(f"{'=' * 60}")
        print(f"Difficulty: {scenario['difficulty']}")
        print(f"Time Limit: {scenario['time_limit']}s\n")
        
        # Create scenario prompt
        scenario_prompt = green_agent.create_scenario_prompt(scenario)
        print(f"✓ Scenario prompt prepared ({len(scenario_prompt)} chars)")
        
        # Send to white agent (mocked for demo)
        print("✓ Sending scenario to White Agent...")
        start_time = time.time()
        
        # In production: white_response = send_a2a_message(white_agent_url, scenario_prompt)
        white_response = mock_white_agent_response(scenario_prompt)
        
        response_time = time.time() - start_time
        print(f"✓ White Agent responded in {response_time:.2f}s\n")
        
        # Evaluate response
        print("✓ Evaluating response...")
        scores = green_agent.evaluate_response(scenario['id'], white_response, response_time)
        
        result = {
            "scenario_name": scenario['name'],
            "difficulty": scenario['difficulty'],
            "scores": scores
        }
        all_results.append(result)
        
        print(f"\n  Overall Score: {scores['overall_score']}/100")
    
    # Generate final report
    print("\n\n" + "=" * 60)
    print("GENERATING EVALUATION REPORT")
    print("=" * 60)
    
    report = green_agent.generate_evaluation_report(all_results)
    print(report)
    
    # Save report
    report_path = Path("./ctae_evaluation_report.txt")
    with open(report_path, 'w') as f:
        f.write(report)
    print(f"\n✓ Report saved to {report_path}")


if __name__ == "__main__":
    run_demo()

