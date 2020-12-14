API to deploy image->image ML models (in this demo it simply does RGB->GRAY but it can be replaced with anything else).
The code also creates a beautiful (not really) web interface to upload the images.

# Guide

## RUN SERVER

```
python server_app.py
python wsgi_app.py
```


## RUN CLIENT

```
python client_app.py
```


## USE CLI

```
curl -F "file=@fazfazfazfa.jpg" http://localhost:5000/ --output "Outputfiles.zip"(needs to be unzipped later)
curl -F "file=@fazfazfazfa.jpg" -F "file2=@6hxozv61s1j51.png" api-image-to-image.herokuapp.com --output "Outputfiles.zip" && unzip Outputfiles.zip -d "Output" && rm "Outputfiles.zip"
```


## DOCKER

> build :
```
docker build -t server_app.py (flask version)
docker build -t wsgi_app.py (flask+gevent wsgi version)
```
> run :
```
docker run -p 5000:5000 api_image_to_image_server
```