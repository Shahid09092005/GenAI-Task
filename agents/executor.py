from tools.github_tool import search_github
from tools.weather_tool import get_weather

def execute_plan(plan):
    results = []

    for step in plan["steps"]:
        tool = step["tool"]
        data = step["input"]

        if tool == "github_search":
            results.append(search_github(**data))

        elif tool == "weather_fetch":
            results.append(get_weather(**data))

    return results
