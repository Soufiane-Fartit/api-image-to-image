"""
Can send images using the command :

curl -F "file=@fazfazfazfa.jpg" http://localhost:5000/ --output "Outputfiles.zip"
curl -F "file=@fazfazfazfa.jpg" -F "file2=@6hxozv61s1j51.png" api-image-to-image.herokuapp.com --output "Outputfiles.zip" && unzip Outputfiles.zip -d "Output" && rm "Outputfiles.zip"

filename : fazfazfazfa.jpg

"""

from PIL import Image
from flask import Flask, request, Response, send_file, after_this_request, render_template, redirect, url_for
import zipfile
import os
from utils import toBytes

import logging
logging.basicConfig(level=logging.DEBUG)


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def home():
    cli_mode = 0
    
    # GET LIST OF UPLOADED FILES
    files_list = request.files.getlist('file')
    print(f'request : {request.data}')
    print(f'files_list : {files_list}')
    files_names = [f.filename for f in files_list]
    if len(files_list)==0 :
        cli_mode = 1
        cli_files_list = request.files.to_dict()
        if len(cli_files_list)==0 :
            #return "oups no files"
            return redirect(url_for('index'))
    
    # ITERATE OVER THE LIST OF FILES AND PROCESS THEM INDIVIDUALLY
    output_list = []
    if cli_mode==0 :
        for file in request.files.getlist('file'):

            # READ AND PROCESS THE IMAGE
            img = Image.open(file)
            gray = img.convert('LA').convert('RGB')

            # SAVE THE IMAGE IN THE SERVER SIDE
            #img.save('Storage/'+file.filename)
            #gray.save('Storage/gray_'+file.filename)

            output_list.append(toBytes(gray))
    else:
        for file_name in cli_files_list:

            file = request.files[file_name]
            #file_extension = file.filename.split('.')[1]

            # READ AND PROCESS THE IMAGE
            img = Image.open(file)
            gray = img.convert('LA').convert('RGB')

            # SAVE THE IMAGE IN THE SERVER SIDE
            #img.save('Storage/img_file.'+'jpg')
            #gray.save('Storage/gray_img_file.'+'jpg')

            output_list.append(toBytes(gray))
    
    # COMPRESS THE OUTPUT IMAGES IN A ZIP FILE TO BE SENT
    zipf = zipfile.ZipFile('Storage/'+'Outputfiles.zip','w', zipfile.ZIP_DEFLATED)
    if cli_mode==0 :
        for file_name,file in zip(files_names, output_list):
            zipf.writestr(file_name, file)
    else :
        for file_name,file in zip(cli_files_list, output_list):
            zipf.writestr(file_name+'.jpg', file)
    zipf.close()

    # PROGRAM THE DELETION OF THE ZIP FILE AFTER IT IS SENT
    
    @after_this_request
    def remove_file(response):
        """Deletes the file 'Outputfiles.zip' after sending the response

        Args:
            response ([Response]): [Response]

        Returns:
            [Response]: [Response]
        """
        try :
            os.remove('Storage/'+'Outputfiles.zip')
        except :
            pass
        return response
    
    # SEND THE ZIPFILE
    return send_file('Storage/'+'Outputfiles.zip', mimetype = 'zip', attachment_filename= 'Outputfiles.zip', as_attachment = True)



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)