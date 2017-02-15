from enum import Enum
import bits_mod

""""
would use 'pyserial' and bits_mod (or more useful rewrite)

This allows us to store the packet inside a long. perhaps the most dense data structure for this problem
"""


class EndBit(Enum):
    """This ENUM defines what the most significant bit should be. The first byte should end with 1 else 0"""
    FIRST_BYTE = 1
    OTHER_BYTE = 0


class PacketByte:
    """This class allows easy manipulation, conversion and handling of our packet bytes"""

    def __init__(self, data_bytes, endbit):
        if endbit in EndBit:
            self._endbit = endbit

        self.data_bytes = int(data_bytes, 2)  # this will through ValueError back if it fails


packet = bits_mod.Bits(104)


def packet_range(start, stop):
    """Range wrapper that auto works in reverse"""
    if start <= stop:
        return list(range(start, stop))
    else:
        return list(range(start, stop, -1))


#how map coule be represented
packet_map = {
    'left_encoder': packet_range(0, 7),
    'right_encoder': packet_range(8, 15),
    'well_made_function': [2, 44, 45] + packet_range(90, 104),
}

for i in packet_map['left_encoder']:
    if i % 2 != 0:
        packet.mark(i)


def get_bits(array_of_indexes):
    bits = b''
    for i in array_of_indexes:
        if packet.is_true(i):
            bits += b'1'
        else:
            bits += b'0'
    return bits


print(get_bits(packet_map['left_encoder'])) #get related bytes


def test_mapping_ranges(packet_map):
    expected_range = set(range(0, 104))
    actual_range = set()
    for i in packet_map.values():
        if actual_range.intersection() is None: # see if there are overlapping mapings
            actual_range.add(i)
        else:
            pass #fail out as there are overlapping maps
    if set(range(0, 104)).difference(actual_range) is not None:
        pass # fail as there are missing mappings
