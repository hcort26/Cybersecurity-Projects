#!/bin/bash

echo "Checking home directory permissions..."
echo

for dir in /Users/*; do
  [ -d "$dir" ] || continue
  perms=$(stat -f "%Sp" "$dir")  # macOS version of stat
  owner=$(stat -f "%Su" "$dir")

  echo "Directory: $dir"
  if [[ "$perms" != "drwx------" ]]; then
    echo "VULNERABILITY: $dir has insecure permissions: $perms"
  else
    echo "OK: $dir is secured"
  fi
  echo
done
