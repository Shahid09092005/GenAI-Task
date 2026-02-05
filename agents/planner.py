import json
from llm.client import call_llm

def plan_task(user_input):
    prompt = f"""
Convert the following task into a JSON plan.

Task: {user_input}

Schema:
{{
  "steps": [
    {{
      "tool": "github_search | weather_fetch",
      "input": {{}}
    }}
  ]
}}
Only return valid JSON.
"""
    plan = call_llm(prompt, system="You are a planner agent.")
    return json.loads(plan)
