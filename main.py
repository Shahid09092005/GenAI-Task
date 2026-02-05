from dotenv import load_dotenv
load_dotenv()
from agents.planner import plan_task
from agents.executor import execute_plan
from agents.verifier import verify_and_format


def run():
    user_task = input("Enter your task: ")

    plan = plan_task(user_task)
    results = execute_plan(plan)
    final_output = verify_and_format(user_task, results)

    print("\nFinal Output:")
    print(final_output)

if __name__ == "__main__":
    run()
# Find top 3 Python AI repos and show current weather in Mumbai
# To find the top 3 Python AI repositories and show the current weather in Mumbai, you can use the following code: