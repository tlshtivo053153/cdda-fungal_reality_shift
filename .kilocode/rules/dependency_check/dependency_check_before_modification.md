# Thorough Dependency Checking

## Overview
Before modifying or deleting a file, check if it is referenced from elsewhere and update dependencies appropriately.

## Procedure
1.  **Identify Targets for Modification/Deletion:** Identify the files or definitions (EOC, item, terrain, etc.) to be modified or deleted.
2.  **Search Entire Project:** Use `grep` or VSCode's search function to find where the file name or definition ID is referenced throughout the project.
3.  **Analyze Referencing Sources:** Analyze the context in which the found references are used (e.g. `run_eocs`, `weighted_list_eocs`, `copy-from`, etc.).
4.  **Update Dependencies:** Appropriately update the referencing source files or definitions due to the modification/deletion. If necessary, also change the referencing source ID.
5.  **Test:** After updating dependencies, verify that the related functions work correctly.

## Why It's Necessary
*   Performing modifications while leaving dependencies unchecked can cause runtime errors (e.g. `invalid effect_on_condition id`).
*   Checking dependencies is important to maintain code consistency and prevent unexpected bugs.

## Usage Situations
*   When deleting files or definitions.
*   When making significant changes to file structure.
*   When changing IDs.