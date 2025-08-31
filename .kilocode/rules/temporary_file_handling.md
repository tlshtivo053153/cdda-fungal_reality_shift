# Clarification of Temporary File Handling

## Overview
When creating temporary files (test plans, notes, etc.) during task execution, clarify the necessity and future handling (whether to delete or not) in advance.

## Procedure
1.  **Judging the Necessity of File Creation:** Determine how creating the file will help in performing the task. If it is merely a work record, consider whether it can be replaced by other methods (TODO list, comments).
2.  **Clarifying the Purpose and Lifespan of the File:** If you create a file, clarify its purpose (e.g., test plan, design note) and lifespan (e.g., delete after task completion).
3.  **Confirmation with User:** If you plan to delete the file, confirm this with the user. If the user finds the file useful, leave it or consider an alternative way to save it.
4.  **Commenting on Temporary Files:** Add a comment at the beginning of the file indicating that it is a temporary file (e.g., `<!-- This is a temporary test plan file. It will be deleted after the task is completed. -->`).

## Why It's Necessary
*   Prevent unnecessary files from remaining in the repository and maintain codebase organization.
*   Prevent discrepancies between the user's intentions and the worker's intentions.

## Usage Situations
*   When creating temporary documents or plan files during task execution.
*   When handling files that will become unnecessary after task completion.