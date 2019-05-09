from PIL import Image
import piexif
img = input("Enter the image filename/path: ")
exif_dict = piexif.load(img)
if exif_dict == {'0th': {}, 'Exif': {}, 'GPS': {}, 'Interop': {}, '1st': {}, 'thumbnail': None}:
    print("\n No Exif data Avaliable")
else:
    for ifd in ("0th", "Exif", "GPS", "1st"):
        for tag in exif_dict[ifd]:
            print(piexif.TAGS[ifd][tag]["name"], exif_dict[ifd][tag])
