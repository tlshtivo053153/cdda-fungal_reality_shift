# Testing Automation Guidelines

## Overview

This document provides guidelines for automating tests in MOD development.

## JSON Validation Tests

- Automate JSON syntax and field validation.
- Run JSON validation tests on every commit.
- Fail the build if JSON validation fails.

## MOD Loading Tests

- Automate MOD loading tests.
- Run MOD loading tests on every commit.
- Fail the build if MOD loading fails.

## Startup Tests

- Automate game startup tests with the MOD.
- Run startup tests on every commit.
- Fail the build if startup tests fail.

## Automated Testing for Comestible Item Usage

- Implement automated tests to verify that comestible items can be consumed without errors.
- Use the debug menu to spawn and consume comestible items during testing.
- Validate that `consumption_effect_on_conditions` effects are properly triggered.

## Test Coverage for Comestible Items

- Test all comestible items with `consumption_effect_on_conditions` to ensure they function correctly.
- Include tests for items that reference effect definitions to verify the effects are properly applied.
- Test edge cases such as items with multiple effects or complex effect conditions.

## Continuous Integration

- Use continuous integration to run automated tests.
- Configure CI to run tests on pull requests.
- Block merging if tests fail.

## Pre-commit Hooks

- Use pre-commit hooks to run automated tests.
- Prevent commits if tests fail.
- Provide clear feedback on test failures.

## Review and Approval

- Automated test results should be reviewed by developers.
- Address test failures before merging.
- Merge only after successful automated tests.