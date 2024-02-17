import base64
import zlib

# Replace the encoded string with your actual ASCII-85 encoded string
ascii85_string = "<~:eLln$31A4!!(&J:KTHB[lYo:!!!o;!!!9))usSe@:q37G]Zqb#lk'>A^+f5A^+e/GRFKP\"R#pf!!MKf!!!eD7d_XW#d7p1apA4PJejt[,I,F9/mp3eTh%7c\"e)0lAlRtL:eM$!1n(m8-3+#G)?9a;:eLfj*Wl`L#ljr*a'hbG1n(m8-3+#G)?9a;#QP\Az!<<*\"Uk&LG!!$VI@:q37G]Zqb\"TSX:A^+e/GRFKP\"R#pf!!MKf!!#hg\"U4r,!!!$\"!<>jp!!%6Dz~>"

# Remove ASCII-85 delimiters (<~ and ~>), if present
ascii85_string = ascii85_string[2:-2]

try:
    # Attempt to decode and decompress with zlib
    binary_data = base64.a85decode(ascii85_string)
    decompressed_data = zlib.decompress(binary_data)
except zlib.error:
    # If zlib decompression fails, assume the data is not zlib-compressed
    decompressed_data = base64.a85decode(ascii85_string)

# Save the decoded data to a file
with open('decoded_file.zip', 'wb') as f:
    f.write(decompressed_data)

print("Decoding complete. Check the 'decoded_file.zip'.")
