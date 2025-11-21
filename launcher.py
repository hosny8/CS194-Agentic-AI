#!/usr/bin/env python3
"""
CTAE-Green Launcher
Orchestrates end-to-end evaluation: Green Agent evaluates White Agent(s)
"""

import sys
import time
from pathlib import Path
from typing import Dict, Any, List

# Add agents directory to path
sys.path.insert(0, str(Path(__file__).parent / "agents"))

from green_agent import CTAEGreenAgent, mock_white_agent_response


class CTAELauncher:
    """Launcher for CTAE-Green evaluation system"""
    
    def __init__(self):
        self.green_agent: CTAEGreenAgent = None
        self.white_agents: Dict[str, Any] = {}
        
    def initialize(self):
        """Initialize all agents"""
        print("\n" + "=" * 70)
        print("CTAE-GREEN EVALUATION LAUNCHER")
        print("=" * 70)
        print("\n[1/3] Initializing Green Agent...")
        
        try:
            self.green_agent = CTAEGreenAgent()
            print(f"      ✓ Green Agent ready")
            print(f"      ✓ Loaded {len(self.green_agent.scenarios)} evaluation scenarios")
        except Exception as e:
            print(f"      ✗ Failed to initialize Green Agent: {e}")
            return False
        
        print("\n[2/3] Initializing White Agents...")
        
        # Register mock white agents with different quality levels
        self.white_agents = {
            "strong_analyst": {
                "name": "Strong Analyst",
                "description": "High-quality trade analyst with excellent reasoning",
                "quality": "strong",
                "url": "mock://strong_analyst"  # Mock URL for demo
            },
            "weak_extractor": {
                "name": "Weak Extractor", 
                "description": "Poor at extracting structured data from text",
                "quality": "weak",
                "url": "mock://weak_extractor"
            },
            "moderate_analyst": {
                "name": "Moderate Analyst",
                "description": "Competent but not expert-level performance",
                "quality": "moderate",
                "url": "mock://moderate_analyst"
            }
        }
        
        print(f"      ✓ Registered {len(self.white_agents)} white agents:")
        for agent_id, agent_info in self.white_agents.items():
            print(f"        - {agent_info['name']}: {agent_info['description']}")
        
        print("\n[3/3] Verifying Environment...")
        print(f"      ✓ Data directory: {self.green_agent.data_dir}")
        print(f"      ✓ Ground truth loaded for {len(self.green_agent.ground_truth)} scenarios")
        print(f"      ✓ System ready for evaluation")
        
        return True
    
    def reset_agents(self):
        """Reset all agents to initial state"""
        print("\n[RESET] Resetting agents to initial state...")
        
        # Reset green agent
        self.green_agent = CTAEGreenAgent()
        print("        ✓ Green Agent reset")
        
        # In production, would send reset signals to white agents
        # For mock agents, no state to reset
        print("        ✓ White Agents reset")
    
    def evaluate_agent(self, agent_id: str, scenario_ids: List[str] = None) -> Dict[str, Any]:
        """
        Evaluate a single white agent on specified scenarios
        
        Args:
            agent_id: ID of white agent to evaluate
            scenario_ids: List of scenario IDs to run (None = all)
        
        Returns:
            Evaluation results with scores
        """
        if agent_id not in self.white_agents:
            raise ValueError(f"Unknown agent: {agent_id}")
        
        agent_info = self.white_agents[agent_id]
        agent_quality = agent_info["quality"]
        
        print(f"\n{'=' * 70}")
        print(f"EVALUATING: {agent_info['name']}")
        print(f"{'=' * 70}")
        print(f"Description: {agent_info['description']}")
        print(f"URL: {agent_info['url']}\n")
        
        # Select scenarios
        if scenario_ids:
            scenarios = [s for s in self.green_agent.scenarios if s['id'] in scenario_ids]
        else:
            scenarios = self.green_agent.scenarios
        
        results = []
        
        for i, scenario in enumerate(scenarios, 1):
            print(f"\n{'-' * 70}")
            print(f"Scenario {i}/{len(scenarios)}: {scenario['name']}")
            print(f"{'-' * 70}")
            print(f"Difficulty: {scenario['difficulty']}")
            print(f"Time Limit: {scenario['time_limit']}s\n")
            
            # Step 1: Green agent creates scenario prompt
            print("  [Step 1/4] Green Agent preparing scenario...")
            prompt = self.green_agent.create_scenario_prompt(scenario)
            print(f"            ✓ Scenario prompt ready ({len(prompt)} chars)")
            
            # Step 2: Send to white agent
            print(f"  [Step 2/4] Sending to {agent_info['name']}...")
            start_time = time.time()
            
            # In production: HTTP request to agent_info['url']
            # For demo: Use quality-aware mock
            if agent_quality == "strong":
                white_response = self._mock_strong_response(scenario)
            elif agent_quality == "weak":
                white_response = self._mock_weak_response(scenario)
            else:  # moderate
                white_response = self._mock_moderate_response(scenario)
            
            response_time = time.time() - start_time
            print(f"            ✓ Response received in {response_time:.2f}s")
            
            # Step 3: Green agent evaluates response
            print("  [Step 3/4] Green Agent evaluating response...")
            scores = self.green_agent.evaluate_response(
                scenario['id'],
                white_response,
                response_time
            )
            print(f"            ✓ Evaluation complete")
            
            # Step 4: Display scores
            print("  [Step 4/4] Scores:")
            print(f"            - Data Extraction:     {scores['data_extraction_accuracy']:.1f}/100")
            print(f"            - Risk Reasoning:      {scores['risk_reasoning_quality']:.1f}/100")
            print(f"            - Recommendations:     {scores['recommendation_coherence']:.1f}/100")
            print(f"            - Response Time:       {scores['response_time_score']:.1f}/100")
            print(f"            --------------------------------")
            print(f"            - OVERALL SCORE:       {scores['overall_score']:.1f}/100")
            
            # Determine tier
            overall = scores['overall_score']
            tier = (
                "EXCELLENT" if overall >= 80 else
                "GOOD" if overall >= 60 else
                "FAIR" if overall >= 40 else
                "NEEDS IMPROVEMENT"
            )
            print(f"            - Performance Tier:    {tier}")
            
            results.append({
                "scenario_id": scenario['id'],
                "scenario_name": scenario['name'],
                "difficulty": scenario['difficulty'],
                "scores": scores
            })
        
        # Calculate aggregate
        avg_overall = sum(r['scores']['overall_score'] for r in results) / len(results)
        avg_extraction = sum(r['scores']['data_extraction_accuracy'] for r in results) / len(results)
        avg_reasoning = sum(r['scores']['risk_reasoning_quality'] for r in results) / len(results)
        avg_recommendations = sum(r['scores']['recommendation_coherence'] for r in results) / len(results)
        
        print(f"\n{'=' * 70}")
        print(f"AGGREGATE RESULTS: {agent_info['name']}")
        print(f"{'=' * 70}")
        print(f"Average Overall Score:          {avg_overall:.2f}/100")
        print(f"Average Data Extraction:        {avg_extraction:.2f}/100")
        print(f"Average Risk Reasoning:         {avg_reasoning:.2f}/100")
        print(f"Average Recommendation Quality: {avg_recommendations:.2f}/100")
        print(f"{'=' * 70}\n")
        
        return {
            "agent_id": agent_id,
            "agent_name": agent_info['name'],
            "scenarios_evaluated": len(results),
            "results": results,
            "aggregate": {
                "overall_score": round(avg_overall, 2),
                "data_extraction": round(avg_extraction, 2),
                "risk_reasoning": round(avg_reasoning, 2),
                "recommendations": round(avg_recommendations, 2)
            }
        }
    
    def run_full_evaluation(self):
        """Run complete evaluation on all white agents"""
        print("\n" + "=" * 70)
        print("FULL EVALUATION: All White Agents × All Scenarios")
        print("=" * 70)
        
        all_results = []
        
        for agent_id in self.white_agents.keys():
            # Reset before each agent
            self.reset_agents()
            
            # Evaluate
            result = self.evaluate_agent(agent_id)
            all_results.append(result)
            
            # Small delay between agents
            time.sleep(0.5)
        
        # Display leaderboard
        self._display_leaderboard(all_results)
        
        return all_results
    
    def _display_leaderboard(self, results: List[Dict[str, Any]]):
        """Display leaderboard of all evaluated agents"""
        print("\n" + "=" * 70)
        print("LEADERBOARD: White Agent Performance Rankings")
        print("=" * 70)
        
        # Sort by overall score
        sorted_results = sorted(
            results,
            key=lambda r: r['aggregate']['overall_score'],
            reverse=True
        )
        
        print(f"\n{'Rank':<6} {'Agent Name':<25} {'Overall':<10} {'Extract':<10} {'Reason':<10} {'Recommend':<10}")
        print("-" * 70)
        
        for i, result in enumerate(sorted_results, 1):
            name = result['agent_name']
            agg = result['aggregate']
            print(
                f"{i:<6} {name:<25} "
                f"{agg['overall_score']:>6.1f}/100  "
                f"{agg['data_extraction']:>6.1f}/100  "
                f"{agg['risk_reasoning']:>6.1f}/100  "
                f"{agg['recommendations']:>6.1f}/100"
            )
        
        print("=" * 70 + "\n")
    
    def _mock_strong_response(self, scenario: Dict[str, Any]) -> Dict[str, Any]:
        """Generate strong performance mock response"""
        if "SHP-2025-1042" in str(scenario['data']):
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
                "reasoning": "Identified critical shipment SHP-2025-1042 with 5-day delay. High financial exposure ($3.9M) warrants immediate action."
            }
        else:
            # Generic strong performance for other scenarios
            return {
                "extracted_data": {
                    "shipment_ids": ["SHP-2025-1098", "SHP-2025-1042"],
                    "commodities": ["Crude Oil", "Copper"],
                    "key_facts": ["Multiple risks identified", "Portfolio value $50M+"]
                },
                "risk_assessment": [
                    {"risk_type": "weather", "severity": "critical", "affected_assets": ["Gulf operations"], "description": "Hurricane threat"},
                    {"risk_type": "port_congestion", "severity": "high", "affected_assets": ["SHP-2025-1042"], "description": "Shanghai delays"}
                ],
                "recommendations": [
                    {"priority": "high", "action": "Prioritize hurricane response", "rationale": "Safety critical"},
                    {"priority": "medium", "action": "Reroute delayed shipments", "rationale": "Cost optimization"}
                ],
                "reasoning": "Comprehensive risk analysis across all data sources"
            }
    
    def _mock_weak_response(self, scenario: Dict[str, Any]) -> Dict[str, Any]:
        """Generate weak performance mock response"""
        return {
            "extracted_data": {
                "shipment_ids": [],
                "commodities": [],
                "key_facts": ["Some delay mentioned", "Weather alert"]
            },
            "risk_assessment": [
                {
                    "risk_type": "weather",
                    "severity": "high",
                    "affected_assets": ["Unknown"],
                    "description": "Generic risk"
                }
            ],
            "recommendations": [
                {
                    "priority": "medium",
                    "action": "Monitor situation",
                    "rationale": "Standard precaution"
                }
            ],
            "reasoning": "Basic analysis without specific details"
        }
    
    def _mock_moderate_response(self, scenario: Dict[str, Any]) -> Dict[str, Any]:
        """Generate moderate performance mock response"""
        return {
            "extracted_data": {
                "shipment_ids": ["SHP-2025-1042"],
                "commodities": ["Crude Oil"],
                "key_facts": ["Delay at Shanghai", "50,000 barrels"]
            },
            "risk_assessment": [
                {
                    "risk_type": "delay",
                    "severity": "medium",  # Wrong severity
                    "affected_assets": ["SHP-2025-1042"],
                    "description": "Port congestion"
                }
            ],
            "recommendations": [
                {
                    "priority": "medium",
                    "action": "Consider rerouting",
                    "rationale": "May reduce delays"
                },
                {
                    "priority": "low",
                    "action": "Inform stakeholders",
                    "rationale": ""  # Missing rationale
                }
            ],
            "reasoning": "Identified issue but underestimated severity"
        }


def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description="CTAE-Green Evaluation Launcher")
    parser.add_argument(
        "command",
        choices=["launch", "evaluate", "list"],
        help="Command to execute"
    )
    parser.add_argument(
        "--agent",
        help="Agent ID to evaluate (for 'evaluate' command)",
        choices=["strong_analyst", "weak_extractor", "moderate_analyst"]
    )
    parser.add_argument(
        "--scenarios",
        nargs="+",
        help="Scenario IDs to run (default: all)",
        choices=["scenario_01", "scenario_02", "scenario_03"]
    )
    
    args = parser.parse_args()
    
    # Initialize launcher
    launcher = CTAELauncher()
    
    if not launcher.initialize():
        print("\n✗ Initialization failed")
        return 1
    
    # Execute command
    if args.command == "launch":
        # Full evaluation
        launcher.run_full_evaluation()
        
    elif args.command == "evaluate":
        # Single agent evaluation
        if not args.agent:
            print("\n✗ Error: --agent required for 'evaluate' command")
            print("   Available agents: strong_analyst, weak_extractor, moderate_analyst")
            return 1
        
        launcher.evaluate_agent(args.agent, args.scenarios)
        
    elif args.command == "list":
        # List available agents and scenarios
        print("\n" + "=" * 70)
        print("AVAILABLE WHITE AGENTS")
        print("=" * 70)
        for agent_id, info in launcher.white_agents.items():
            print(f"\n  {agent_id}:")
            print(f"    Name: {info['name']}")
            print(f"    Description: {info['description']}")
            print(f"    URL: {info['url']}")
        
        print("\n" + "=" * 70)
        print("AVAILABLE SCENARIOS")
        print("=" * 70)
        for scenario in launcher.green_agent.scenarios:
            print(f"\n  {scenario['id']}:")
            print(f"    Name: {scenario['name']}")
            print(f"    Difficulty: {scenario['difficulty']}")
            print(f"    Time Limit: {scenario['time_limit']}s")
            print(f"    Description: {scenario['description']}")
        
        print("\n" + "=" * 70 + "\n")
    
    print("\n✓ Evaluation complete\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())

