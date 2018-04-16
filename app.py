import os
from flask import Flask, flash, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from models import db_session, Image as ImageModel
from dicom import read_dicom_file, write_image_and_thumbnail

ALLOWED_EXTENSIONS = ['dcm']

app = Flask(__name__)

session = db_session()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def image_gallery():
    all_images = session.query(ImageModel).all()
    return render_template('image-gallery.html', images=all_images)

@app.route('/images/<int:image_id>/detail')
def image_detail(image_id):
    image = session.query(ImageModel).filter_by(id=image_id).one()
    return render_template('image-detail.html', image=image)

@app.route('/images/new', methods=['POST'])
def new_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(url_for('image_gallery'))

    dicom_file = request.files['file']
    if dicom_file.filename == '':
        flash('No selected file')

    elif not allowed_file(dicom_file.filename):
        flash('File type not allowed')

    else:
        filename = secure_filename(dicom_file.filename)
        dataset = read_dicom_file(dicom_file)
        image_filename = write_image_and_thumbnail(dataset, filename)
        new_image = ImageModel(filename=image_filename,
                               dicom_data=str(dataset))
        session.add(new_image)
        session.commit()
        flash('Image saved ({})'.format(image_filename))
    return redirect(url_for('image_gallery'))

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.debug = True
    app.secret_key = 'secret key'
    app.run(host='0.0.0.0', port=5000)
