"""Build the M3U playlists from the *.tsv files (name, tvg-id, group, url, logo).

Jellyfin has no radio marker in M3U files, so each playlist gets its own channel
number range (tvg-chno) and radio stations get a name prefix.
"""
import csv

# source file -> (target file, first channel number, name prefix)
PLAYLISTS = {
    "tv.tsv": ("de-public.m3u", 1, ""),
    "intl.tsv": ("intl.m3u", 500, ""),
    "radio.tsv": ("de-radio.m3u", 1000, "\U0001F4FB "),
}

for src, (dst, first, prefix) in PLAYLISTS.items():
    with open(src, encoding="utf-8") as f, open(dst, "w", encoding="utf-8") as out:
        out.write("#EXTM3U\n")
        for no, (name, tvg, group, url, logo) in enumerate(csv.reader(f, delimiter="\t"), first):
            label = prefix + name
            out.write(
                f'#EXTINF:-1 tvg-id="{tvg}" tvg-chno="{no}" tvg-name="{label}" '
                f'tvg-logo="{logo}" group-title="{group}",{label}\n{url}\n'
            )
