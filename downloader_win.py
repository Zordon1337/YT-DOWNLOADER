import pystyle
import subprocess
from pystyle import Colors, Colorate, Add, Center, Box, Write

print(Colorate.Horizontal(Colors.purple_to_red, "Enter video link", 1))
input1 = input("")
subprocess.Popen(["yt-dlp ", input1])

