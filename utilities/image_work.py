import PIL.Image as Image
import numpy as np


def get_image_channel(image, channel):
    return image[::, ::, channel:channel + 1].reshape(image.shape[0], image.shape[1])


def build_image_from_channels(channels):
    width = channels[0].shape[0]
    height = channels[0].shape[1]
    image = np.empty((width, height, len(channels)), dtype=int)

    for i in range(len(channels)):
        grid = np.ix_(range(width), range(height), range(i, i + 1))
        image[grid] = channels[i].reshape(width, height, 1)

    return image


def normalize_image(image, isYCbCr):
    channels = np.empty((image.shape[2], image.shape[0], image.shape[1]), dtype=int)
    # span = [[16, 235], [16, 240], [16, 240]] if isYCbCr else [[0, 255], [0, 255], [0, 255]]
    span = [[16, 235], [16, 240], [16, 240]] if isYCbCr else [[0, 255], [0, 255], [0, 255]]
    for i in range(image.shape[2]):
        channels[i] = normalize_channel(get_image_channel(image, i), span[i])
    return build_image_from_channels(channels)


def normalize_channels(channels, isYCbCr):
    # span = [[16, 235], [16, 240], [16, 240]] if isYCbCr else [[0, 255], [0, 255], [0, 255]]
    span = [[0, 255], [0, 255], [0, 255]] if isYCbCr else [[0, 255], [0, 255], [0, 255]]
    for i in range(len(channels)):
        channels[i] = normalize_channel(channels[i], span[i])
    return channels


def normalize_channel(channel, span=None):
    if span is None:
        span = [0, 255]
    min_channel = np.min(channel)
    max_channel = np.max(channel)

    if min_channel < span[0] and max_channel > span[1]:
        channel = normalize_matrix(channel, span[0], span[1], min_channel, max_channel)
    elif min_channel < span[0]:
        channel = normalize_matrix(channel, span[0], max_channel, min_channel, max_channel)
    elif max_channel > span[1]:
        channel = normalize_matrix(channel, min_channel, span[1], min_channel, max_channel)
    return channel


def normalize_matrix(matrix, t_min, t_max, min_matrix, max_matrix):
    norm_arr = np.zeros((matrix.shape[0], matrix.shape[1]), dtype=int)
    diff = t_max - t_min
    diff_arr = max_matrix - min_matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            norm_arr[i, j] = (((matrix[i, j] - min_matrix) * diff) / diff_arr) + t_min
    return norm_arr


def RGBtoYCbCr(image):
    im = Image.fromarray(image, 'RGB')
    im = im.convert('YCbCr')
    imageInYCbCr = np.array(im).astype(np.uint8)

    # imageInYCbCr = colour.RGB_to_YCbCr(image, in_int=True, out_int=True, in_range=(0, 255), out_range=(16, 235, 16, 240))
    return imageInYCbCr


def YCbCrtoRGB(image):
    im = Image.fromarray(image.astype(np.uint8), 'YCbCr')
    im = im.convert('RGB')
    imageInRGB = np.array(im)

    # imageInRGB = colour.YCbCr_to_RGB(image, in_int=True, out_int=True, in_range=(16, 235, 16, 240), out_range=(0, 255))
    return imageInRGB


def resize_image_to_divisible_for(image, dividerW, dividerH):
    width = int(image.shape[0] / dividerW) * dividerW
    height = int(image.shape[1] / dividerH) * dividerH

    grid = np.ix_(range(width), range(height))
    newImage = image[grid]

    return newImage
