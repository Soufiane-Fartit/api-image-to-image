def serve_pil_image(pil_img):
    """Serve a PIL image to be served in the API

    Args:
        pil_img ([PIL]): a PIL image

    Returns:
        [response]: Sends the contents of a file to the client
    """
    from io import BytesIO
    from flask import send_file

    img_io = BytesIO()
    pil_img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')

def toBytes(pil_img):
    """Convert a PIL image to a BytesIO object

    Args:
        pil_img ([type]): [description]

    Returns:
        [BytesIO]: A BytesIO object
    """
    from io import BytesIO
    img_io = BytesIO()
    pil_img.save(img_io, 'JPEG', quality=70)
    return img_io.getvalue()