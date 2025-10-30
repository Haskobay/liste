import os
import xml.etree.ElementTree as ET
from pytube import Playlist

# Playlist URL'sini oku
with open("playlist.txt", "r") as f:
    url = f.read().strip()

playlist = Playlist(url)

videos_elem = ET.Element("videos")

for video in playlist.video_urls:
    video_elem = ET.SubElement(videos_elem, "video")
    video_elem.set("type", "youtube")
    video_elem.set("src", video)

tree = ET.ElementTree(videos_elem)
os.makedirs("output", exist_ok=True)
tree.write("output/videos.xml", encoding="utf-8", xml_declaration=True)

print("XML oluşturuldu: output/videos.xml")
