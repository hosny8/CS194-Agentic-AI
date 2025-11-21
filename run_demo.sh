#!/bin/bash

echo "=========================================="
echo "CTAE-GREEN DEMO RUNNER"
echo "Commodity Trade Agent Evaluation"
echo "=========================================="
echo ""

# Check if we're in the right directory
if [ ! -d "data" ] || [ ! -d "agents" ]; then
    echo "Error: Please run this script from the ctae-green directory"
    exit 1
fi

# Check Python version
python_version=$(python3 --version 2>&1 | awk '{print $2}' | cut -d. -f1,2)
echo "✓ Python version: $python_version"

# Check if virtual environment is activated
if [ -z "$VIRTUAL_ENV" ]; then
    echo ""
    echo "Warning: No virtual environment detected."
    echo "It's recommended to run this in a virtual environment."
    echo ""
    read -p "Continue anyway? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

echo ""
echo "Running CTAE-Green Agent Demo..."
echo ""

cd agents
python3 green_agent.py

echo ""
echo "=========================================="
echo "Demo Complete!"
echo "=========================================="




