"""Build de-public.m3u from channels.tsv (name, tvg-id, group, url)."""
import csv

with open("channels.tsv", encoding="utf-8") as f, open("de-public.m3u", "w", encoding="utf-8") as out:
    out.write("#EXTM3U\n")
    for name, tvg, group, url in csv.reader(f, delimiter="\t"):
        out.write(f'#EXTINF:-1 tvg-id="{tvg}" tvg-name="{name}" group-title="{group}",{name}\n{url}\n')
