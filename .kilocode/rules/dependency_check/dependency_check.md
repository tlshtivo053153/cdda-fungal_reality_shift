# Dependency Check Guidelines

## Overview

This document provides guidelines for checking dependencies in MOD development.

## Circular Dependency Detection

- Avoid circular dependencies in recipes and item groups.
- Use tools to detect circular dependencies.
- Refactor code to eliminate circular dependencies.

## Existence Check

- Ensure that all referenced items and groups exist.
- Use a reference checker to validate references.
- Handle missing references gracefully.

## Dependency Graph Visualization

- Use tools to visualize dependency graphs.
- Identify and resolve complex dependency chains.
- Keep dependency graphs as simple as possible.

## Automated Dependency Check

- Implement automated dependency checks.
- Use continuous integration to run dependency checks.
- Include dependency checks in the pre-commit hook.

## Review and Approval

- Dependencies should be reviewed by at least one other developer.
- Reviews should focus on correctness and adherence to guidelines.
- Merge only after successful dependency check and review.