def access_bit(data, num):
    base = int(num // 8)
    shift = int(num % 8)
    return (data[base] >> shift) & 0x1


def get_byte_from_bits(bins):
    return bytearray([sum([byte[b] << b for b in range(0, 8)]) for byte in zip(*(iter(bins),) * 8)])


def bitstring_to_bytes(s):
    v = int(s, 2)
    b = bytearray()
    while v:
        b.append(v & 0xff)
        v >>= 8
    return bytes(b[::-1])
