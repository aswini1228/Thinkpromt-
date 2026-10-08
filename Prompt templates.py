def build_prompt(technique, task):

    if technique == "Zero-shot":
        return f"""
Answer the following task directly without using any examples.

Task:
{task}

Provide a clear, accurate, and concise answer.
"""

    elif technique == "One-shot":
        return f"""
Use the following example as a guide.

Example:
Task: What is Artificial Intelligence?
Answer: Artificial Intelligence is the ability of machines
to perform tasks that normally require human intelligence.

Now answer the following task:

Task:
{task}

Follow the style and structure of the example.
"""

    elif technique == "Few-shot":
        return f"""
Use the following examples to understand the expected
answering pattern.

Example 1:
Task: What is Python?
Answer: Python is a high-level programming language.

Example 2:
Task: What is Machine Learning?
Answer: Machine Learning enables computers to learn from data.

Example 3:
Task: What is Deep Learning?
Answer: Deep Learning is a subset of Machine Learning
that uses neural networks.

Now answer this task:

Task:
{task}

Follow the pattern shown in the examples.
"""

    elif technique == "CoT":
        return f"""
Solve the following task using a structured step-by-step
reasoning approach.

Task:
{task}

Break the problem into logical steps and provide a concise
reasoning summary followed by the final answer.
"""

    elif technique == "Manual CoT":
        return f"""
Solve the following task using these predefined steps:

Step 1: Understand the task.
Step 2: Identify the important information.
Step 3: Break the task into smaller parts.
Step 4: Analyze each part logically.
Step 5: Combine the results.
Step 6: Provide the final answer.

Task:
{task}

Give a clear and well-structured answer.
"""

    elif technique == "ToT":
        return f"""
Solve the following task using a Tree-of-Thoughts approach.

Task:
{task}

Consider multiple possible approaches.

Approach 1:
Develop one possible solution.

Approach 2:
Develop an alternative solution.

Approach 3:
Develop another suitable solution.

Compare the approaches and select the most suitable one.

Finally, provide the best answer clearly.
"""

    else:
        raise ValueError("Invalid prompting technique selected.")
