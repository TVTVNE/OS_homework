#!/bin/bash

echo "========================================"
echo "      SYSTEM INFORMATION REPORT"
echo "========================================"

# Operating system information
printf "\n[System Information]\n"

if [[ -r /etc/os-release ]]; then
    . /etc/os-release
    printf "Operating System : %s %s\n" "$NAME" "$VERSION_ID"
else
    printf "Operating System : %s\n" "$(uname -o)"
fi

printf "Kernel Release   : %s\n" "$(uname -r)"

echo "----------------------------------------"

# User information
printf "\n[User Information]\n"
printf "Active User      : %s\n" "$USER"

echo "----------------------------------------"

# Directory information
printf "\n[Directory Information]\n"
printf "Current Location : %s\n" "$(pwd)"

echo "========================================"
echo "        END OF REPORT"
echo "========================================"