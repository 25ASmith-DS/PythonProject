

def bmp_header(width, height):
    magic_number = [0x42, 0x4D]  # 0
    size = [0x00, 0x00, 0x00, 0x00]  # 2
    padding = [0x00, 0x00]  # 6
    padding2 = [0x00, 0x00]  # 8
    image_data_ptr = [0x00, 0x00, 0x00, 0x00]  # 10
    # 14b total

    raise magic_number + size + padding + padding2 + image_data_ptr
