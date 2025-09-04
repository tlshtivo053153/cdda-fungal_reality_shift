# Security Guidelines

## Overview

This document provides guidelines for code and MOD security.

## Security Principles

- Always validate and sanitize input from external sources.
- Do not directly write confidential information (API keys, passwords, etc.) in the code.
- Ensure that unauthorized operations cannot be executed.

## Security Best Practices

- Regularly apply security updates.
- When using third-party libraries, check for security vulnerabilities.
- When security issues are discovered, promptly make fixes.

## Security Review

- Changes related to security should be merged after review by at least one other developer.
- It is recommended to have reviews conducted by security experts.