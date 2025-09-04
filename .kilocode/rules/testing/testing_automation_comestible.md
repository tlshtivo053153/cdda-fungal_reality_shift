# Testing Automation Guidelines for Comestible Items

## Overview

This document provides guidelines for automating tests related to comestible items in MOD development.

## Automated Testing for Comestible Item Usage

- Implement automated tests to verify that comestible items can be consumed without errors.
- Use the debug menu to spawn and consume comestible items during testing.
- Validate that `consumption_effect_on_conditions` effects are properly triggered.

## Test Coverage

- Test all comestible items with `consumption_effect_on_conditions` to ensure they function correctly.
- Include tests for items that reference effect definitions to verify the effects are properly applied.
- Test edge cases such as items with multiple effects or complex effect conditions.

## Continuous Integration

- Use continuous integration to run automated tests for comestible items.
- Configure CI to run tests on pull requests.
- Block merging if tests fail.

## Pre-commit Hooks

- Use pre-commit hooks to run automated tests for comestible items.
- Prevent commits if tests fail.
- Provide clear feedback on test failures.

## Review and Approval

- Automated test results should be reviewed by developers.
- Address test failures before merging.
- Merge only after successful automated tests.