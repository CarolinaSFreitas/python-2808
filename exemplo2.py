import os, sys
from PIL import Image

size = (128, 128)

for infile in sys.argv[1:]:
    outfile = os.path.splitext(infile)[0] + ".thumbnail"
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                im.thumbnail(size)
                im.save(outfile, "JPEG")
                print(f"Ok! Thumbnail {outfile} gerado com sucesso :)")
        except OSError:
            print("cannot create thumbnail for", infile)