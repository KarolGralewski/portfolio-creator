from flask import Flask, request, abort, send_file
import jinja2
from io import BytesIO
from zipfile import ZipFile, ZIP_DEFLATED
from os import listdir
from os.path import isfile, join, basename
import json
from types import SimpleNamespace

app = Flask(__name__)


@app.route('/generate_template', methods=['POST'])
def generateTemplate():
    if not request.form:
        abort(422)
    formData = request.form

    # if not {'first-name', 'last-name', 'email', 'number', 'github', 'linkedin', 'twitter', 'telegram', 'theme'}.issubset(formData.keys()):
    #     # here we can validate inputs if needed
    #     abort(422)

    # templatePath=f'./resume_templates/{formData["template_version"]}+{formData["language_choice"]}'

    templatePath=f'./resume_templates/{formData["template_version"]}{formData["language_choice"]}'
  
    templateLoader = jinja2.FileSystemLoader(searchpath=templatePath)
    templateEnv = jinja2.Environment(loader=templateLoader)

    # list file for the template
    templateFiles = [join(templatePath, f) for f in listdir(templatePath) if isfile(join(templatePath, f))]
    zipBuffer = BytesIO()
    with ZipFile(zipBuffer, "w", ZIP_DEFLATED, False) as zip_file:
        for file in templateFiles:
            if file.endswith('.jinja2'):
                # process jninja2 template files
                template = templateEnv.get_template(basename(file))
                outputText = template.render(data=formData)
                zip_file.writestr('template/'+basename(file).replace('.jinja2',''), outputText.encode())
            else:
                # process rest of the files
                with open(file, "rb") as notTemplatedFile:
                    zip_file.writestr('template/'+basename(file), notTemplatedFile.read())

    zipBuffer.seek(0) # before sending we need to got to first byte in buffer
    try:
        return send_file(zipBuffer, download_name='resume_template.zip')
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run()
