# JSON Flag Definition Validation Guidelines

## Overview

This document provides guidelines for validating JSON flag definitions in MOD development to prevent errors during MOD loading.

## JSON Flag Definition Validation

### Field Name Validation

- When defining a new `json_flag`, ensure that only valid field names are used.
- Common valid fields for `json_flag` include:
  - `id`: The unique identifier for the flag.
  - `name`: The display name of the flag.
- Avoid using invalid or unsupported fields such as `description` or `info_text` in `json_flag` definitions, as these may cause errors during MOD loading.

### Reference to Existing Definitions

- Before adding a new `json_flag`, check existing flag definitions in the base game or other MODs to ensure consistency and avoid redefining existing flags.
- Use the game's JSON documentation to confirm the correct structure and supported fields for `json_flag`.

### Automated Validation

- Implement automated validation checks for `json_flag` definitions.
- Use continuous integration to run validation checks.
- Include validation checks in the pre-commit hook.

## Review and Approval

- JSON flag definitions should be reviewed by at least one other developer.
- Reviews should focus on correctness and adherence to guidelines.
- Merge only after successful validation and review.