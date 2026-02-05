from llm.client import call_llm

def verify_and_format(user_task, raw_results):
    prompt = f"""
User task: {user_task}

Raw results:
{raw_results}

Validate completeness.
Fix missing info if possible.
Return a clean structured JSON response.
"""

    return call_llm(prompt, system="You are a verifier agent.")
