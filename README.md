# DICOM Gallery
Simple gallery to upload, parse, and display images and data extracted from the [DICOM](https://en.wikipedia.org/wiki/DICOM) format.

## About
This project provides a very simple server that allows a user to select a file in the `application/dcm` format, a DICOM file, to be uploaded, saved and its relevant data extracted. The pixel data stored in the DICOM file is minimally processed and normalized to ensure that the pixel intensity values fall within the 0-255 range supported by standard unisigned 8-bit integer datatypes used by normal images. Both color and grayscale images are supported.

Additionally, the accompanying data is displayed on a detail page, along with the full-sized image in the following format:

```
(0008, 0005) Specific Character Set              CS: 'ISO_IR 100'
(0008, 0008) Image Type                          CS: ['ORIGINAL', 'PRIMARY']
(0008, 0016) SOP Class UID                       UI: Ophthalmic Photography 8 Bit Image Storage
(0008, 0018) SOP Instance UID                    UI: 1.2.840.113654.2007.3.101
(0008, 0020) Study Date                          DA: '20070727'
(0008, 0023) Content Date                        DA: '20070727'
(0008, 002a) Acquisition DateTime                DT: '20070727120000'
(0008, 0030) Study Time                          TM: '120000'
...
```

## Getting started

The project has the following dependencies:

- Python >= 3.5
- PyDicom (provides an interface to work with DICOM images)
- Pillow (to manage saving and resizing image data)
- Numpy (to normalize the image values and crop the thumbnail)
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

This project was developed in part with the help of the data made available at the [Visible Human Project](https://mri.radiology.uiowa.edu/visible_human_datasets.html).
