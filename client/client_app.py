import requests
import shutil
import zipfile
import os

url = 'http://localhost:5000/'
#url = 'http://api-image-to-image.herokuapp.com'

files = {
    'file1': ('input/6hxozv61s1j51.png', open('input/6hxozv61s1j51.png', 'rb')),
    'file2': ('input/fazfazfazfa.jpg', open('input/fazfazfazfa.jpg', 'rb')),
}

response = requests.post(url, files=files, stream=True)

print(response)

# READ THE RESPONSE AND GET THE ZIP FILE
if response.status_code == 200:
    with open("output/Outputfiles.zip", 'wb') as f:
        response.raw.decode_content = True
        shutil.copyfileobj(response.raw, f)

# EXTRACT IMAGES FROM THE ZIP FILE
try :
    print("Extracting images from the ZipFile")
    with zipfile.ZipFile("output/Outputfiles.zip", 'r') as zip_ref:
        zip_ref.extractall("output/")
except :
    print("ZipFile not found. Cannot extract images")

# DELETE THE ZIP FILE

try :
    print("Deleting the ZipFile")
    os.remove("output/Outputfiles.zip")
except :
    print("ZipFile not found. It cannot be deleted")