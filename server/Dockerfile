FROM python
ADD wsgi_app.py /
ADD server_app.py /
ADD templates /templates
ADD static /static
ADD Storage /Storage
EXPOSE 33507
RUN pip install Pillow flask gevent
CMD ["python","./wsgi_app.py"]
