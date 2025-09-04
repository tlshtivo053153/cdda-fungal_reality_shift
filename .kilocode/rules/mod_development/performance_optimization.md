# Performance Optimization Guidelines

## Overview

This document provides guidelines for considering performance in MOD development.

## Performance Optimization Principles

- Avoid unnecessary calculations and processing.
- Consider moving heavy processing inside loops to outside the loop.
- Cache data that can be cached to avoid recalculating.
- When handling large amounts of data, consider using iterators or generators.

## Performance Measurement

- Perform performance measurements in the actual game play environment.
- Use profiling tools to identify performance bottlenecks.

## Optimization Best Practices

- Optimization should be done after performance issues actually occur.
- Before optimizing, performance measurements to clearly identify problem points.
- After optimization, perform performance measurements again to confirm improvements.