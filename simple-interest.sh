#!/bin/bash

# Script to calculate simple interest

# Prompt user for principal, rate, and time
read -p "Enter Principal Amount: " principal
read -p "Enter Rate of Interest: " rate
read -p "Enter Time (in years): " time

# Calculate simple interest
si=$(echo "scale=2; $principal * $rate * $time / 100" | bc)

# Output the result
echo "Simple Interest = $si"
