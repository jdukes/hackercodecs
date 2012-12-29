Hacker Codecs
=============

This is a set of codecs for decoding and encoing things. Specifically
this was designed originally around the fact that decode('bin')
doesn't exist in the standard library and there are times (especially
in a CTF) where this is extremely convinient. 

Later 'morse' was added to easily encode and decode morse code without
needing to do it (as) manually. 

The 'ascii85' codec was added specifically for PDF parsing in
forensics challenges. This could be used, for example, with
python-magic to check if a string inside of a PDF is actually a file
of a specific type. 

The 'url' and 'entity' codecs were added as a quick way to encode and
decode data for web hacking. 

Other encodings like y-encode have been added, a full list is avaliable by reviewing the code. 

As I run across, or am told about other obscure encoding methods I
will continue to add to this library. 

