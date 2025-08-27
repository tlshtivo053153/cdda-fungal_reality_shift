# Task Completion Self-Evaluation Guidelines

## Overview

This document provides guidelines for conducting self-evaluations after completing tasks. The purpose is to improve the quality of work and identify areas for improvement.

## Task Completion Self-Evaluation

### When to Conduct Self-Evaluation
- Conduct a self-evaluation immediately after completing a task.
- Ensure that the task has been fully completed before starting the evaluation.

### Self-Evaluation Items
- **Goal Achievement**: Was the task's goal achieved?
- **Quality Standards**: Do the code or documentation meet the quality standards?
- **Time Management**: Was the time spent on the task appropriate?
- **Collaboration**: Was collaboration with other team members effective?

### How to Conduct Self-Evaluation
1. Review the task requirements and ensure all objectives have been met.
2. Evaluate the quality of the work produced.
3. Assess the time spent on the task and identify any inefficiencies.
4. Reflect on collaboration with team members and identify areas for improvement.

## Communication Clarity in Task Delegation

### Identifying Ambiguities
- When delegating tasks, clearly specify the expected outcome and the method of execution.
- If a task involves actions that Kilo Code cannot directly perform (e.g., executing git commands), explicitly state this and provide guidance on how the user should proceed.

### Improving Instructions
- Use precise language to avoid misinterpretation.
- When requesting a specific mode of operation, clearly indicate the desired mode (e.g., "Please provide the commands for the user to execute in `ask` mode").
- Provide examples or templates when necessary to illustrate the expected format or outcome.

### Example of Improved Task Delegation
- **Before**: "Create commits for the changes."
- **After**: "Provide the git commands to stage and commit the changes. The commands should follow the Conventional Commits format. Present these commands in `ask` mode so the user can copy and execute them."
## Improvement Based on Feedback

### Identifying Improvement Points
- Based on the self-evaluation results, identify specific areas for improvement.
- Document these improvement points clearly.

### Adding or Modifying Rules
- Add new rules to `.kilocode/rules/` based on the identified improvement points.
- Modify existing rules if necessary to reflect new insights or best practices.

## Adding or Modifying Rules

### Adding New Rules
- When adding new rules, follow the format of existing rule files.
- Ensure the new rule file is named appropriately using snake_case.

### Modifying Existing Rules
- When modifying existing rules, maintain the existing format.
- Clearly document the changes made and the reasons for them.

## Committing Documentation

### Commit Message Guidelines
- Write clear and concise commit messages.
- Follow the Conventional Commits format.
- Include a brief summary of the changes made.

### Example Commit Message
```sh
git add .
git commit -m "docs: add self-evaluation guidelines for task completion"