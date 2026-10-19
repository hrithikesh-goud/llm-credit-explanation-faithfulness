import urllib.request, zipfile, io, os

url = "https://archive.ics.uci.edu/static/public/522/south+german+credit.zip"
out_folder = r"C:\Users\manthuri hrithikesh\Desktop\ML Project- CA\data"

print("Downloading...")
data = urllib.request.urlopen(url).read()
print("Downloaded", len(data), "bytes")

os.makedirs(out_folder, exist_ok=True)
zipfile.ZipFile(io.BytesIO(data)).extractall(out_folder)
print("Done! Files:", os.listdir(out_folder))