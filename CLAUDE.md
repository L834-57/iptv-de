# iptv-de

- **Zweck:** M3U-Playlist der öffentlich-rechtlichen deutschen Sender für Jellyfin (Live TV). Nur Links auf offizielle Sender-Streams.
- **Stack:** Reine Textdateien. `tv.tsv`, `radio.tsv`, `intl.tsv` (Spalten: Name, tvg-id, Gruppe, Stream-URL, Logo-URL) sind die Quellen, `build.py` erzeugt `de-public.m3u` (TV), `de-radio.m3u`, `intl.m3u` (kein Server, kein Hot Reload nötig).
- **Start-Befehl:** `python3 build.py`
- **Test-Befehl:** `./check.sh` (Streams, alles 200/206) und `LOGO_DELAY=8 ./checklogos.sh` (Logos, keine Ausgabe = alles ok; Wikimedia drosselt bei zu schnellen Anfragen)
- **URL/Port:** kein Port. Playlist-URL: https://raw.githubusercontent.com/L834-57/iptv-de/main/de-public.m3u
- Neue Sender: Zeile in `die passende .tsv` ergänzen (Tabs!), `build.py` und `check.sh` laufen lassen, committen.
- Keine Streams von Drittanbietern/Weiterverteilern aufnehmen, nur offizielle Sender-CDNs.
- Logos liegen als Dateien in `logos/` (selbst gehostet, weil Wikimedia/imgur bei vielen parallelen Abrufen drosseln). Neues Logo: Datei nach `logos/` legen und die Raw-URL in die 5. Spalte der .tsv eintragen.
