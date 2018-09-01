import unittest
from hypothesis import given, assume, strategies as st
from sys import path
path.append('../')
from hackercodecs import *

class TestBlocks(unittest.TestCase):
    def test_blocks(self):
        # should always yield equal size blocks
        # self.assertEqual(expected, blocks(data, size))
        assert False # TODO: implement your test here

class TestParity(unittest.TestCase):
    def test_parity(self):
        # self.assertEqual(expected, parity(bit_array, odd))
        assert False # TODO: implement your test here

class TestRotx(unittest.TestCase):
    def test_rotx(self):
        # self.assertEqual(expected, rotx(data, rotval))
        assert False # TODO: implement your test here

class TestRotxCodecGenerator(unittest.TestCase):
    def test_rotx_codec_generator(self):
        # self.assertEqual(expected, rotx_codec_generator(rotval))
        assert False # TODO: implement your test here

class TestGetCodecsList(unittest.TestCase):
    def test_get_codecs_list(self):
        # self.assertEqual(expected, get_codecs_list())
        assert False # TODO: implement your test here

    def test_get_codecs_not_in_list(self):
        # self.assertEqual(expected, get_codecs_list())
        assert False # TODO: implement your test here

class TestCodecs(unittest.TestCase):
    @given(st.text(alphabet=''.join(i[0] for i in MORSE)))
    def test_morse(self, s):
        encoded,encoded_len = morse_encode(s)
        decoded, decoded_len = morse_decode(encoded)
        assert s.upper() == decoded

    @given(st.text())
    def test_bin(self, s):
        assume(all(ord(c) <= 255 for c in s))
        encoded, encoded_len = bin_encode(s)
        decoded, decoded_len = bin_decode(encoded)
        assert s.encode('bin') == decoded.encode('bin')

    @given(st.text())
    def test_url(self, s):
        # s=u'\u0100'
        assume(all(ord(c) <= 255 for c in s))
        encoded, encoded_len = bin_encode(s)
        decoded, decoded_len = bin_decode(encoded)
        assert s.encode('bin') == decoded.encode('bin')

    @given(st.text())
    def test_entity(self, s):
        assume(all(ord(c) <= 255 for c in s))
        encoded, encoded_len = entity_encode(s)
        decoded, decoded_len = entity_decode(encoded)
        assert s.encode('bin') == decoded.encode('bin')

    @given(st.text())
    def test_entity_hex(self, s):
        assume(all(ord(c) <= 255 for c in s))
        encoded, encoded_len = entity_encode_hex(s)
        decoded, decoded_len = entity_decode_hex(encoded)
        assert s.encode('bin') == decoded.encode('bin')

    # @given(st.text())
    # def test_ascii85(self, s):
    #     # u'\x80'
    #     assume(all(ord(c) <= 255 for c in s))
    #     encoded, encoded_len = ascii85_encode(s)
    #     decoded, decoded_len = ascii85_decode(encoded)
    #     assert s.encode('bin') == decoded.encode('bin')

    @given(st.text())
    def test_y(self, s):
        # s=u'\x80'
        assume(all(ord(c) <= 255 for c in s))
        encoded, encoded_len = y_encode(s)
        decoded, decoded_len = y_decode(encoded)
        assert s.encode('bin') == decoded.encode('bin')

    ## these need a lot of fixing
    # @given(st.text())
    # def test_aba_track_2(self, s):
    #     encoded, encoded_len = aba_track_2_encode(s)
    #     decoded, decoded_len = aba_track_2_decode(encoded)
    #     assert s == decoded


if __name__ == '__main__':
    unittest.main()
