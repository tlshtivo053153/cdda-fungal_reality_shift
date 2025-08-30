# Task Execution Improvement Guidelines

## Overview

This document provides guidelines for improving task execution quality and preventing mistakes. It covers transformation definition consistency checks, user intent confirmation processes, and code change verification processes.

## Transformation Definition Consistency Check

### Purpose
To ensure that terrain transformation definitions are consistent and function as intended.

### Process
1. **Review Existing Definitions**: Before creating new transformation definitions, review existing similar definitions in the base game and other MODs to ensure consistency.
2. **Validate Result Fields**: Ensure that the `result` field in `ter_furn_transform` definitions includes all appropriate terrain types that should be possible outcomes.
3. **Verify Valid Terrain**: Confirm that `valid_terrain` entries correctly specify which terrain types can be transformed.
4. **Test In-Game**: Use the debug menu to test terrain transformations in-game to verify correctness.

### Best Practices
- When modifying `ter_furn_transform` definitions, ensure that the transformation logic aligns with the intended gameplay mechanics.
- Check for potential typos or inconsistencies in terrain IDs.
- Document any complex transformation logic with comments.

## User Intent Confirmation Process

### Purpose
To ensure that the user's intent is clearly understood before proceeding with task execution.

### Process
1. **Initial Assessment**: Upon receiving a task, first try to understand the user's intent by analyzing the request and any provided context.
2. **Clarification**: If the intent is unclear or ambiguous, ask clarifying questions to the user with specific examples or suggestions.
3. **Confirmation**: Before implementing significant changes, confirm the approach with the user to ensure alignment with their expectations.
4. **Feedback Integration**: Incorporate user feedback promptly and adjust the implementation as needed.

### Best Practices
- Always prioritize understanding the user's intent over technical implementation details.
- Provide clear explanations of proposed solutions to ensure mutual understanding.
- Document any assumptions made during the task execution process.

## Code Change Verification Process

### Purpose
To ensure that code changes are correct, complete, and do not introduce unintended side effects.

### Process
1. **Self-Review**: Before submitting changes, conduct a self-review to check for syntax errors, logical issues, and adherence to style guidelines.
2. **Functionality Testing**: Test the changes in the game environment to verify they work as expected.
3. **Git Diff Confirmation**: Review the git diff to ensure that only intended changes are included and no unintended modifications were made.
4. **Peer Review**: Request a review from another developer to catch any issues that might have been missed.

### Best Practices
- Use VSCode or other tools to review git diffs for better visualization of changes.
- When testing, use the debug menu to spawn and test specific items or transformations.
- Document the testing process and results for future reference.
- Follow the established style guidelines for all code changes.