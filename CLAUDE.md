# iptv-de

- **Zweck:** M3U-Playlist der öffentlich-rechtlichen deutschen Sender für Jellyfin (Live TV). Nur Links auf offizielle Sender-Streams.
- **Stack:** Reine Textdateien. `channels.tsv` ist die Quelle, `build.py` erzeugt `de-public.m3u` (kein Server, kein Hot Reload nötig).
- **Start-Befehl:** `python3 build.py`
- **Test-Befehl:** `./check.sh` (zeigt HTTP-Status jedes Streams, alles sollte 200 sein)
- **URL/Port:** kein Port. Playlist-URL: https://raw.githubusercontent.com/L834-57/iptv-de/main/de-public.m3u
- Neue Sender: Zeile in `channels.tsv` ergänzen (Tabs!), `build.py` und `check.sh` laufen lassen, committen.
- Keine Streams von Drittanbietern/Weiterverteilern aufnehmen, nur offizielle Sender-CDNs.
