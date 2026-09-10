import sys
import json
from client import LeastToMostPlanner

planner = LeastToMostPlanner()

def handle_call(name, arguments):
    if name == "decompose":
        goal = arguments["goal"]
        subtasks = arguments["subtasks"]
        planner.decompose(goal, subtasks)
        return {"subtask_count": len(planner.subtasks)}
    elif name == "run":
        res = planner.execute_sequentially(lambda sub, ctx: f"Solved: {sub}")
        return {"results": res}
    return {"error": f"Unknown tool: {name}"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_call(req.get("name"), req.get("arguments", {}))
            print(json.dumps({"id": req.get("id"), "result": res}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()

if __name__ == "__main__":
    main()
