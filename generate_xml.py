import yt_dlp
import xml.etree.ElementTree as ET
import os

# Playlist URL
playlist_url = "https://www.youtube.com/playlist?list=PLuBee2Uj-FU84qy9CB59nFZDSlH4UsR30"

# XML çıkışı için klasör
output_dir = os.path.join(os.getcwd(), "output")
os.makedirs(output_dir, exist_ok=True)
xml_path = os.path.join(output_dir, "videos.xml")

# yt-dlp ile playlist bilgisini çek
ydl_opts = {'quiet': False, 'extract_flat': True}  # False yaparak log görebiliriz
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(playlist_url, download=False)

# Playlist entries kontrolü
if 'entries' not in info or not info['entries']:
    print("Playlist boş veya veri alınamadı!")
    exit(1)

videos = info['entries']

# XML oluştur
root = ET.Element("videos")
for v in videos:
    video = ET.SubElement(root, "video")
    video.set("type", "youtube")
    video.set("src", f"https://www.youtube.com/watch?v={v['id']}")

tree = ET.ElementTree(root)
tree.write(xml_path, encoding="UTF-8", xml_declaration=True)

print(f"XML başarıyla oluşturuldu: {xml_path}")
