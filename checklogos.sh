#!/bin/sh
# Test every logo URL in the *.tsv files (expects an image content type)
for f in tv.tsv radio.tsv intl.tsv; do
  while IFS="$(printf '\t')" read -r name _ _ _ logo; do
    r=$(curl -sL -m 15 -o /dev/null -w '%{http_code} %{content_type}' "$logo")
    case "$r" in "200 image/"*) ;; *) echo "$r $name $logo";; esac
    sleep "${LOGO_DELAY:-1}"
  done < "$f"
done
