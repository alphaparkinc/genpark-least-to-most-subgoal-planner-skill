class LeastToMostPlanner:
    """
    Least-to-Most Prompting (Zhou et al.).
    Decomposes complex question into ordered subproblems and sequentially solves them,
    passing accumulated answers as context to subsequent subproblems.
    """
    def __init__(self):
        self.subtasks = []

    def decompose(self, complex_goal, subtasks_list):
        self.subtasks = list(subtasks_list)

    def execute_sequentially(self, solver_fn):
        context = {}
        for idx, sub in enumerate(self.subtasks):
            res = solver_fn(sub, context)
            context[f"subtask_{idx}"] = res
        return context
