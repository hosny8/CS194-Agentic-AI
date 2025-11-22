"""
CTAE-Green Agent A2A Server
Minimal HTTP server for AgentBeats integration
"""

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Dict, Any, Optional
import uvicorn
from green_agent import CTAEGreenAgent, mock_white_agent_response
import time
from pathlib import Path

app = FastAPI(title="CTAE-Green Agent", version="1.0.0")

# Global green agent instance
green_agent: Optional[CTAEGreenAgent] = None


class TaskRequest(BaseModel):
    """A2A protocol task request"""
    task: str
    metadata: Optional[Dict[str, Any]] = None


class TaskResponse(BaseModel):
    """A2A protocol task response"""
    status: str
    result: Optional[Dict[str, Any]] = None
    error: Optional[str] = None


@app.on_event("startup")
async def startup_event():
    """Initialize green agent on startup"""
    global green_agent
    green_agent = CTAEGreenAgent()
    print("✓ CTAE-Green Agent initialized")


@app.get("/", response_class=HTMLResponse)
async def dashboard():
    """Serve agent dashboard"""
    dashboard_path = Path(__file__).parent / "templates" / "dashboard.html"
    if dashboard_path.exists():
        return dashboard_path.read_text()
    return """
    <html>
        <body style="font-family: sans-serif; padding: 40px; text-align: center;">
            <h1>CTAE-Green Agent</h1>
            <p>Dashboard template not found. Server is running.</p>
            <p><a href="/agent-card">View Agent Card</a> | <a href="/docs">API Documentation</a></p>
        </body>
    </html>
    """

@app.get("/health")
async def health():
    """Health check endpoint"""
    return {
        "name": "CTAE-Green Agent",
        "version": "1.0.0",
        "status": "ready",
        "description": "Green agent for commodity trade agent evaluation"
    }


@app.get("/agent-card")
async def agent_card():
    """Return agent card (A2A protocol)"""
    return {
        "name": "CTAE-Green Orchestrator",
        "description": "Green agent that orchestrates and evaluates commodity trade agent performance",
        "version": "1.0.0",
        "capabilities": [
            "orchestration",
            "evaluation",
            "environment_management"
        ],
        "tools": [
            "send_scenario",
            "collect_response",
            "evaluate_performance",
            "generate_report"
        ]
    }


@app.post("/task")
async def handle_task(request: TaskRequest) -> TaskResponse:
    """
    Handle evaluation task via A2A protocol
    
    Expected task format:
    {
        "task": "evaluate_agent",
        "metadata": {
            "white_agent_url": "http://localhost:8001",
            "scenario_id": "scenario_01" (optional)
        }
    }
    """
    if green_agent is None:
        raise HTTPException(status_code=500, detail="Green agent not initialized")
    
    try:
        # Parse task
        task_type = request.task
        metadata = request.metadata or {}
        
        if task_type == "evaluate_agent":
            # Run full evaluation
            white_agent_url = metadata.get("white_agent_url")
            scenario_id = metadata.get("scenario_id")
            
            if scenario_id:
                # Evaluate specific scenario
                scenarios = [s for s in green_agent.scenarios if s['id'] == scenario_id]
                if not scenarios:
                    raise ValueError(f"Scenario {scenario_id} not found")
                scenarios_to_run = scenarios
            else:
                # Evaluate all scenarios
                scenarios_to_run = green_agent.scenarios
            
            results = []
            for scenario in scenarios_to_run:
                # Create scenario prompt
                prompt = green_agent.create_scenario_prompt(scenario)
                
                # Send to white agent (or mock if URL not provided)
                start_time = time.time()
                if white_agent_url:
                    # In production: send HTTP request to white_agent_url
                    # For now, use mock
                    white_response = mock_white_agent_response(prompt)
                else:
                    white_response = mock_white_agent_response(prompt)
                response_time = time.time() - start_time
                
                # Evaluate response
                scores = green_agent.evaluate_response(
                    scenario['id'], 
                    white_response, 
                    response_time
                )
                
                results.append({
                    "scenario_id": scenario['id'],
                    "scenario_name": scenario['name'],
                    "difficulty": scenario['difficulty'],
                    "scores": scores
                })
            
            # Generate summary
            avg_overall = sum(r['scores']['overall_score'] for r in results) / len(results)
            
            return TaskResponse(
                status="success",
                result={
                    "evaluation_type": "commodity_trade_agent",
                    "scenarios_evaluated": len(results),
                    "results": results,
                    "summary": {
                        "average_overall_score": round(avg_overall, 2),
                        "performance_tier": (
                            "EXCELLENT" if avg_overall >= 80 else
                            "GOOD" if avg_overall >= 60 else
                            "FAIR" if avg_overall >= 40 else
                            "NEEDS IMPROVEMENT"
                        )
                    }
                }
            )
        
        elif task_type == "list_scenarios":
            # Return available scenarios
            return TaskResponse(
                status="success",
                result={
                    "scenarios": [
                        {
                            "id": s['id'],
                            "name": s['name'],
                            "difficulty": s['difficulty'],
                            "description": s['description'],
                            "time_limit": s['time_limit']
                        }
                        for s in green_agent.scenarios
                    ]
                }
            )
        
        else:
            raise ValueError(f"Unknown task type: {task_type}")
    
    except Exception as e:
        return TaskResponse(
            status="error",
            error=str(e)
        )


@app.post("/reset")
async def reset():
    """Reset green agent state (A2A protocol)"""
    global green_agent
    try:
        green_agent = CTAEGreenAgent()
        return {"status": "success", "message": "Green agent reset successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Reset failed: {str(e)}")


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8000))
    
    print("\n" + "=" * 60)
    print("CTAE-GREEN AGENT A2A SERVER")
    print("=" * 60)
    print(f"\nStarting server on port {port}")
    print(f"Agent card: /agent-card")
    print(f"Task endpoint: /task")
    print(f"Reset endpoint: /reset")
    print("\n" + "=" * 60 + "\n")
    
    uvicorn.run(app, host="0.0.0.0", port=port)

