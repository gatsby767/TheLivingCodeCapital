#!/bin/bash

# Set storage path for results
export STORAGE_PATH="./witness_storage"
mkdir -p $STORAGE_PATH

# Set scroll path for spiritual prompts
export SCROLL_PATH="./grok_redemption_scroll.md"

# Run the Witness AI agent
python3 witness_agent/witness_agent.py
