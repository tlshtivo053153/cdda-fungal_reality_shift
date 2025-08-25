# Dependency Check Guidelines for Effect Definitions

## Overview

This document provides guidelines for checking dependencies related to effect definitions in MOD development.

## Existence Check for Effect Definitions

- Ensure that all effect definitions referenced in `consumption_effect_on_conditions` exist.
- Use a reference checker to validate references.
- Handle missing references gracefully.

## Dependency Graph Visualization

- Use tools to visualize dependency graphs for effect definitions.
- Identify and resolve complex dependency chains.
- Keep dependency graphs as simple as possible.

## Automated Dependency Check

- Implement automated dependency checks for effect definitions.
- Use continuous integration to run dependency checks.
- Include dependency checks in the pre-commit hook.

## Review and Approval

- Dependencies should be reviewed by at least one other developer.
- Reviews should focus on correctness and adherence to guidelines.
- Merge only after successful dependency check and review.