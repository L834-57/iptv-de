#!/bin/sh
# Test every stream URL in channels.tsv (HTTP status only)
while IFS="$(printf '\t')" read -r name _ _ url; do
  code=$(curl -s -m 10 -o /dev/null -w '%{http_code}' "$url")
  echo "$code $name"
done < channels.tsv
