import math
import numpy as np
from utilities.image_work import normalize_channel


def cut_image_on_blocks(image, block_widths, block_heights, chunk=None):
    step = 0
    block = None

    for blockX in range(chunk[0], len(block_widths)):
        for blockY in range(chunk[1], len(block_heights[blockX])):
            if chunk[2] is not None and step >= chunk[2]:
                return block

            left = sum([block_widths[i] for i in range(blockX)])
            upper = sum([block_heights[blockX][i] for i in range(blockY)])
            grid = np.ix_(range(left, left + block_widths[blockX]), range(upper, upper + block_heights[blockX][blockY]))

            block = image[grid]

            step += 1
    return block


def merge_blocks_to_image(image, blocks, block_widths, block_heights, chunk=None):
    step = 0

    for blockX in range(chunk[0], len(block_widths)):
        for blockY in range(chunk[1], len(block_heights[blockX])):
            if chunk[2] is not None and step >= chunk[2]:
                return image

            left = sum([block_widths[i] for i in range(blockX)])
            upper = sum([block_heights[blockX][i] for i in range(blockY)])
            grid = np.ix_(range(left, left + block_widths[blockX]), range(upper, upper + block_heights[blockX][blockY]))

            block = blocks[step]

            image[grid] = block
            step += 1
    return image


def cut_image_on_blocks_and_trans(image, block_width, block_height, trans_forward, transform_params, chunk=None):
    width = image.shape[0]
    height = image.shape[1]

    num_blocks_w = int(width / block_width)
    num_blocks_h = int(height / block_height)

    blocks = np.zeros((num_blocks_w, num_blocks_h, block_width, block_height), dtype=float)

    for blockX in range(chunk[0], num_blocks_w):
        for blockY in range(chunk[1], num_blocks_h):
            if chunk[2] is not None and (blockX - chunk[0]) * num_blocks_h + (blockY - chunk[1]) >= chunk[2]:
                return blocks

            left = blockX * block_width
            upper = blockY * block_height
            grid = np.ix_(range(left, left + block_width), range(upper, upper + block_height))

            block = trans_forward(image[grid], transform_params)

            blocks[blockX, blockY] = block
    return blocks


def merge_trans_blocks_to_image(image, blocks, trans_inverse, transform_params, span, chunk=None):
    num_blocks_w = blocks.shape[0]
    num_blocks_h = blocks.shape[1]
    block_width = blocks.shape[2]
    block_height = blocks.shape[3]

    if image is None:
        image = np.zeros((num_blocks_w * block_width, num_blocks_h * block_height), dtype=int)

    for blockX in range(chunk[0], num_blocks_w):
        for blockY in range(chunk[1], num_blocks_h):
            if chunk[2] is not None and (blockX - chunk[0]) * num_blocks_h + (blockY - chunk[1]) >= chunk[2]:
                return image

            left = blockX * block_width
            upper = blockY * block_height
            grid = np.ix_(range(left, left + block_width), range(upper, upper + block_height))

            block = trans_inverse(blocks[blockX, blockY], transform_params)
            block = np.round(block)
            block = normalize_channel(block, span)

            image[grid] = block
    return image


def check_block_frequency(block, block_size):
    high_freq = [[], [], [], [], [], [], [], []]
    mid_freq = [[], [], [], [], [], [], [], []]
    low_freq = [[], [], [], [], [], [], [], []]
    for n in range(len(block_size)):
        h = block_size[n][0]
        w = block_size[n][1]
        k = h / w * -1
        b = h - 1
        for i in range(h):
            for j in range(w):
                p = k * j + b
                md = math.ceil(p)
                mdd = math.ceil(p - k)
                if i == md or i == mdd or i - 1 == p:
                    mid_freq[n].append([i, j])
                elif i < md:
                    low_freq[n].append([i, j])
                else:
                    high_freq[n].append([i, j])
    LF = 0
    HF = 0
    for p in low_freq[block_size]:
        LF += abs(block[p[0], p[1]])

    for p in high_freq[block_size]:
        HF += abs(block[p[0], p[1]])

    return HF, LF