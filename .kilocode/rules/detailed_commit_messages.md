# Detailed Commit Messages

## Overview
Commit messages should be as specific and detailed as possible to make it easier for other developers to understand the intent and content of the changes.

## Procedure
1.  **List Changes:** List the key files, features, or definitions that were changed, added, or removed in this commit.
2.  **Clarify Intent:** Briefly describe why the change was made and what problem it solves.
3.  **Describe Impact:** Describe what impact this change might have on other parts of the codebase, if any.
4.  **Follow Conventional Commits Format:** Adhere to the `<type>: <subject>` format.
    *   Use `type` such as `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`.
    *   `subject` should concisely explain the change.

## Example
```
// Better example
feat: change liquid terrain transformation to random single and refactor related files

- Refactor liquid terrain transformation logic to randomly select and transform only one terrain from supported terrains.
- Create separate JSON files for each liquid transformation target (e.g., t_lava, t_gasoline) under mods/fungal_reality_shift/effects_on_condition/terrain_transformation/liquid/individual/.
- Define individual `ter_furn_transform` for each `valid_terrain` in the new files.
- Remove the original mods/fungal_reality_shift/effects_on_condition/terrain_transformation/liquid/terrain_transformation_liquid.json.
- Update weighted_list_eocs in terrain_transformation.json to reference new EOCs.
```

## Why It's Necessary
*   To quickly understand the intent of changes from the commit history.
*   To make it easier to grasp the background of changes during troubleshooting or code reviews.

## Usage Situations
*   For all commits.