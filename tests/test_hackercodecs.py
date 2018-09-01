import unittest
from hypothesis import given, assume, strategies as st
from sys import path
path.append('../')
from hackercodecs import *

class TestHelperFunctions(unittest.TestCase):

    @given(st.tuples(st.text(), st.integers(max_value=2**32)))
    def test_blocks(self, s):
        data, size = s
        assume(size > 0) # we don't need to check divide by zero
        if not ((len(data) % size) == 0):
            # make sure we assert here
            try:
                blocks(data, size)
            except AssertionError, e:
                assert e.message == (
                    "Cannot divide into blocks of size %s" % size)
        else:
            results = blocks(data, size)
            try:
                first = next(results)
                assert all(len(r) == len(first)
                           for r in results)
            except StopIteration:
                pass

    @given(st.lists(st.booleans()))
    def test_parity(self, s):
        if sum(s) % 2 == 0:
           assert parity(s) == 0
           assert parity(s, odd=True) == 1
        else:
           assert parity(s) == 1
           assert parity(s, odd=True) == 0

    @given(st.tuples(st.text(),
                     st.integers(min_value=0, max_value=26)))
    def test_rotx(self, s):
        data, rot = s
        encoded = rotx(data, rot)
        decoded = rotx(encoded, -rot)
        assert data == decoded

    def test_rotx_codec_generator(self):
        # we proved rotx above
        codec = rotx_codec_generator(10)
        self.assertEqual(codec.name, 'rot10')


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
        assert s.encode('bin') == decoded.encode('bin'), (
            "{} != {}".format(s, decoded))

    @given(st.text())
    def test_ascii85(self, s):
        assume(all(ord(c) <= 255 for c in s))
        assume(not s.endswith('\0')) # we know we can't encode this
        encoded, encoded_len = ascii85_encode(s)
        decoded, decoded_len = ascii85_decode(encoded)
        assert s.encode('bin') == decoded.encode('bin'), (
            "{} != {}".format(repr(s), repr(decoded)))

    @given(st.text())
    def test_y(self, s):
        assume(all(ord(c) <= 255 for c in s))
        encoded, encoded_len = y_encode(s)
        decoded, decoded_len = y_decode(encoded)
        assert s.encode('bin') == decoded.encode('bin')

    # these need a lot of fixing
    @given(st.text())
    def test_aba_track_2(self, s):
        encoded, encoded_len = aba_track_2_encode(s)
        decoded, decoded_len = aba_track_2_decode(encoded)
        assert s.encode('bin') == decoded.encode('bin')


if __name__ == '__main__':
    unittest.main()
