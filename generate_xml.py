import yt_dlp
import xml.etree.ElementTree as ET
import os

# Playlist URL
playlist_url = "https://www.youtube.com/playlist?list=PLbxwMdSNkTatJqrlpHhw4mu9as2CQurn7"

# XML çıkışı için klasör
os.makedirs("output", exist_ok=True)

# yt-dlp ile playlist bilgisini çek
ydl_opts = {'quiet': True, 'extract_flat': True}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(playlist_url, download=False)

videos = info['entries']

# XML oluştur
root = ET.Element("videos")
for v in videos:
    video = ET.SubElement(root, "video")
    video.set("type", "youtube")
    video.set("src", f"https://www.youtube.com/watch?v={v['id']}")

tree = ET.ElementTree(root)
tree.write("output/videos.xml", encoding="UTF-8", xml_declaration=True)

print(f"XML başarıyla oluşturuldu: output/videos.xml")
