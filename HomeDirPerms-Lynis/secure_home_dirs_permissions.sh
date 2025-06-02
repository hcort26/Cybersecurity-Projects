#!/bin/bash

echo "Scanning for vulnerable home directory permissions..."
echo

fix_list=()

for dir in /Users/*; do
  [ -d "$dir" ] || continue
  perms=$(stat -f "%Sp" "$dir")

  if [[ "$perms" != "drwx------" ]]; then
    echo "VULNERABILITY: $dir has $perms"
    fix_list+=("$dir")
  fi
done

if [[ ${#fix_list[@]} -eq 0 ]]; then
  echo "All home directories are secure."
  exit 0
fi

read -p "Fix insecure permissions? [Y/n] " choice
if [[ "$choice" =~ ^[Yy]$ ]]; then
  for dir in "${fix_list[@]}"; do
    chmod 700 "$dir"
    echo "FIXED: $dir permissions set to 700"
  done
else
  echo "No changes made."
fi
