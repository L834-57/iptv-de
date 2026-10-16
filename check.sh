#!/bin/sh
# Test every stream URL in the *.tsv files (HTTP status only, follows redirects)
for f in tv.tsv radio.tsv intl.tsv; do
  while IFS="$(printf '\t')" read -r name _ _ url; do
    code=$(curl -sL -m 10 -r 0-2000 -o /dev/null -w '%{http_code}' "$url")
    echo "$code $f $name"
  done < "$f"
done
