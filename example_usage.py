from client import LeastToMostPlanner

def main():
    print("=== Testing Least-to-Most Subgoal Planner ===")
    planner = LeastToMostPlanner()
    planner.decompose(
        complex_goal="Calculate compound interest",
        subtasks_list=[
            "Extract principal P and rate r",
            "Calculate annual factor (1 + r)",
            "Raise factor to exponent t",
            "Multiply by principal P"
        ]
    )
    print(f"Decomposed into {len(planner.subtasks)} sequential subtasks.")

    def mock_solver(subtask, context):
        return f"Completed: {subtask} [ctx_size={len(context)}]"

    results = planner.execute_sequentially(mock_solver)
    for k, v in results.items():
        print(f"  {k} -> {v}")

    assert len(results) == 4
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
