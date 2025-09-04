# Explicit Reference Updates

## Overview

This rule emphasizes the importance of explicitly managing and updating references when files are moved or deleted to prevent broken links and maintain code integrity.

## Purpose

- To ensure that all references are updated when files are moved or deleted.
- To prevent broken links and maintain code integrity.
- To reduce the risk of runtime errors due to missing references.

## Process

1.  **Identify References**: Before moving or deleting a file, identify all references to that file in the codebase.
2.  **List References**: Create a list of all files and lines that reference the file to be moved or deleted.
3.  **Update References**: Update all references to point to the new location or remove them if the file is deleted.
4.  **Verify Updates**: After updating references, verify that all links are working correctly and that there are no broken references.
5.  **Test**: Test the affected functionality to ensure that it works as expected after the changes.

## Benefits

- Ensures that all references are updated when files are moved or deleted.
- Prevents broken links and maintains code integrity.
- Reduces the risk of runtime errors due to missing references.
- Improves overall code quality and maintainability.