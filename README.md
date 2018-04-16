# Dicom Gallery
Simple gallery to upload, parse, and display images and data extracted from the [DICOM](https://en.wikipedia.org/wiki/DICOM) format

## Getting started

### Python Dependencies

- Python >= 3.5
- PyDicom (provides an interface to work with DICOM images)
- Pillow (to manage saving and resizing image data)
- Numpy
- Flask
- SqlAlchemy

In order to keep the environment and requirements consistent, this project includes an environment.yml file, which defines the version of Python to use, as well as the major dependencies. I recommend using [Conda](https://conda.io/docs/index.html) to manage your environment.

To quickly create the environment and install dependencies, type the following at the command prompt in your terminal:

```
conda env create -f environment.yml
```

To activate this environment, use:

```
source activate dicomenv
```

To start the server, type `python app.py` in the terminal and navigate to `0.0.0.0:5000` in your browser.
