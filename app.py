from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

root_dir = ""

@app.route('/')
def index():
    files = os.listdir(root_dir)
    isdir = gen_isdir_list(root_dir)
    return render_template('files_list.html', files=files, isdir=isdir)

@app.route('/<path:sub_dir>')
def sub_dir(sub_dir):
    files = os.listdir(f"{root_dir}/{sub_dir}")
    isdir = gen_isdir_list(f"{root_dir}/{sub_dir}")
    return render_template('files_list.html', files=files, isdir=isdir, path=sub_dir)

@app.route('/<path:sub_dir>/<filename>')
def download(sub_dir, filename):
    print(sub_dir)
    infile_1 = open(f"{root_dir}/{sub_dir}/{filename}", "r")
    st_1 = infile_1.read()
    infile_1.close()

    return st_1.replace('\n','<br>',-1)
    #return send_from_directory(f"{root_dir}/{sub_dir}", filename, as_attachment=False)

def gen_isdir_list(dir_name):
    files = os.listdir(dir_name)
    isdir_list = []
    for f in files:
        if os.path.isdir(f"{dir_name}/{f}"):
            isdir_list.append(True)
        else:
            isdir_list.append(False)
    return isdir_list

app.run(debug=True, host = "0.0.0.0")
