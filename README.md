# dicom-gallery
Simple gallery to upload, parse, and display images in the [DICOM](https://en.wikipedia.org/wiki/DICOM) format

## Getting started

### Python Dependencies

- Python >= 3.5
- PyDicom (provides an interface to work with DICOM images)
- Pillow (to manage saving and resizing image data)
- Numpy
- Flask
- SqlAlchemy

In order to keep the environment and requirements consistent, this project includes an environment.yml file, which defines the version of Python to use, as well as all of the dependencies. I recommend using [Conda](https://conda.io/docs/index.html) to manage your environment.

To quickly install dependencies with conda, type the following at the command prompt in your terminal:

```
conda env create -f environment.yml
```
