# JSON Validation Guidelines

## Overview

This document provides guidelines for validating JSON files in MOD development.

## JSON Syntax Validation

- All JSON files must be syntactically correct.
- Use a JSON validator to check the syntax of JSON files.
- Ensure that all fields are properly closed with commas and braces.

## Field Name Validation

- Verify that all field names are correct and match the expected schema.
- Use the game's JSON documentation to confirm field names.
- Pay special attention to fields that are case-sensitive.

## Dependency Validation

- Check for circular dependencies in recipes and item groups.
- Ensure that all referenced items and groups exist.
- Use tools to visualize and validate dependency graphs.

## Automated Testing

- Implement automated tests to validate JSON files.
- Use continuous integration to run JSON validation tests.
- Include JSON validation in the pre-commit hook.

## Review and Approval

- JSON files should be reviewed by at least one other developer.
- Reviews should focus on correctness and adherence to guidelines.
- Merge only after successful validation and review.