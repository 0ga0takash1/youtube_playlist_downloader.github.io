from io import BytesIO

from mutagen.id3 import ID3, APIC
from PIL import Image
import glob

def get_thumbnail_url(id):
    return "https://img.youtube.com/vi/"+id+"/maxresdefault.jpg"

def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))

def crop_max_square(pil_img):
    return crop_center(pil_img, min(pil_img.size), min(pil_img.size))

def crop_thumbnail(file):
    out_dir = os.path.dirname(file)
    tags = ID3(file)
    # print(tags)
    # return
    
    # カバーアート情報取得
    # apic = tags.get("APIC:")
    apic = tags.getall("APIC")[0].data
    # if apic is not None:
    cover_img = Image.open(BytesIO(apic))
    
    # artist, title = tags.get("TPE1"), tags.get("TIT2")
    # cover_img.save(f"{artist}_{title}.jpg")
    img_path = out_dir+"/test.jpg"
    # cover_img.save(img_path)

    cover_img_crop = crop_max_square(cover_img)
    # cover_img_crop.save(f"Reol/Sigma/test{i}.jpg")
    cover_img_crop.save(img_path)
    # cover_img_crop_byte = cover_img_crop.tobytes()

    tags.add(APIC(mime="image/jpeg", type=3, data=open(img_path, 'rb').read()))
    # tags.getall("APIC")[0].data = cover_img_crop
    tags.save()
    # os.remove(img_path)
    return


# files = glob.glob("Reol/Sigma/*mp3")
# files = glob.glob("ドンブラザーズ/ドンブラザーズ/*mp3")
# crop_thumbnail(files[0])
# for i, file in enumerate(files):
    # print(file)
    # crop_thumbnail(file)