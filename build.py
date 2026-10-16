"""Build the M3U playlists from the *.tsv files (name, tvg-id, group, url, logo)."""
import csv

PLAYLISTS = {"tv.tsv": "de-public.m3u", "radio.tsv": "de-radio.m3u", "intl.tsv": "intl.m3u"}

for src, dst in PLAYLISTS.items():
    with open(src, encoding="utf-8") as f, open(dst, "w", encoding="utf-8") as out:
        out.write("#EXTM3U\n")
        for name, tvg, group, url, logo in csv.reader(f, delimiter="\t"):
            out.write(f'#EXTINF:-1 tvg-id="{tvg}" tvg-name="{name}" tvg-logo="{logo}" group-title="{group}",{name}\n{url}\n')
