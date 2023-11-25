import zipfile
from urllib.request import urlopen

with zipfile.ZipFile(urlopen("https://vgmrips.net/files/Arcade/Capcom/Ghouls%27n_Ghosts_%28CP_System%29.zip").read()) as myzip:
    ziplist = myzip.namelist()
    for item in ziplist:
    	print(item)
