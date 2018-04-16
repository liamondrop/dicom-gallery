import errno
import os
import pydicom
import numpy as np
from PIL import Image

upload_dir = os.path.join('static', 'uploads')
thumbnail_size = 256, 256

def mkdir_p(path):
    """ Creates a directory or directories if they do not exist (mkdir -p)
    """
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

def normalize_and_scale(image):
    """ Normalizes and scales the pixel values to fit within standard
        0-255 value range
    Args:
        image (numpy.array): Input image.
    Returns:
        2D image scaled to uint8 (numpy.array)
    """
    minimum = image.min()
    maximum = image.max()
    intensity_range = float(maximum - minimum)

    # account for special case of zero
    # difference in max and min intensities
    if intensity_range == 0:
        return np.zeros_like(image)

    # normalize image values to 0. - 1. scale
    norm_image = (image - minimum) / intensity_range

    # return image scaled to 0 - 255
    return (255. * norm_image).astype(np.uint8)

def read_dicom_file(dicom_file):
    """ Reads a dicom file
    Args:
        dicom_file (FileStorage (application/dicom))
    Returns:
        PyDicom dataset (pydicom.dataset.FileDataset)
    """
    return pydicom.read_file(dicom_file)

def crop_square_image(pixel_data):
    """ Crops a image to a square the size of the smallest of the image
        height or width
    Args:
        pixel_data: numpy.array
    Returns:
        cropped pixel data (numpy.array)
    """
    height, width = pixel_data.shape[:2]
    smallest_dimension = min(height, width)
    start_y = int(height / 2 - smallest_dimension / 2)
    end_y = start_y + smallest_dimension
    start_x = int(width / 2 - smallest_dimension / 2)
    end_x = start_x + smallest_dimension
    return pixel_data[start_y:end_y, start_x:end_x]

def write_image_and_thumbnail(dataset, filename):
    """ Extracts pixel data from dicom file and writes an image and
        thumbnail to disk
    Args:
        dataset (pydicom.dataset.FileDataset)
        filename (string)
    Returns:
        image name (string)
    """
    pixel_data = normalize_and_scale(dataset.pixel_array)

    # prepare and save full size image
    image = Image.fromarray(pixel_data)
    image_rgb = image.convert('RGB')
    image_name = '{}.jpg'.format(filename)
    image_path = os.path.join(upload_dir, 'images', image_name)
    image_rgb.save(image_path, 'JPEG')

    # crop and save thumbnail image
    cropped_data = crop_square_image(pixel_data)
    thumbnail_image = Image.fromarray(cropped_data)
    thumbnail_image_rgb = thumbnail_image.convert('RGB')
    thumbnail_image_rgb.thumbnail(thumbnail_size, Image.ANTIALIAS)
    thumbnail_path = os.path.join(upload_dir, 'thumbnails', image_name)
    thumbnail_image_rgb.save(thumbnail_path, "JPEG")
    return image_name
