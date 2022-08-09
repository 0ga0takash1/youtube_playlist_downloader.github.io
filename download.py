import youtube_dl, os
from mutagen.easyid3 import EasyID3

import get_URL_list


def set_mp3_track_number(file_path, num):
    tags = EasyID3(file_path)
    tags['tracknumber'] = str(num)
    tags.save()

def get_exist_mp3s_in_out_dir(out_dir):
    res = []
    files = glob.glob(out_dir)

    for file in files:
        tags = EasyID3(file)
        # print(tags['tracknumber'][0], tags['album'][0])
        # print(tags)
    # return

        # res.append([
        #     int(tags['tracknumber'][0]), 
        #     [
        #         file, tags['album'][0]
        #     ]
        # ])
        List = [0, os.path.basename(file)[:-4], "no album infomation"]
        for key, value in tags.items():
            if key == 'tracknumber': List[0] = int(value[0])
            if key == 'album': List[2] = value[0]
        res.append(List)
    res.sort()
    return res

def is_downloaded(mp3_file_path, exsist_file_path):
    now_tags = EasyID3(mp3_file_path)
    ex_tags = EasyID3(exsist_file_path)

    if os.path.exists(mp3_file_path):
        pass

    return (now_tags['tracknumber'] == ex_tags['tracknumber'] and now_tags['album'] == ex_tags['album'])

table = str.maketrans({
    '/' : '',
    '\n': ' ',
    ':' : '#',
    '?' : '#',
    '\"': "#",
})

def DL_1video(item, out_dir):
    title = item[0].translate(table)
    file_name = out_dir+'/'+title
    mp3_path = file_name+'.mp3'

    if os.path.exists(mp3_path): return mp3_path
    
    url = item[1]
    ydl_opts = {
        # 'writethumbnail': True,
        'format': 'bestaudio/best',
        'outtmpl': file_name+'.%(ext)s',
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            },
            {'key': 'FFmpegMetadata'},
            # {'key': 'EmbedThumbnail'},
        ],
    }

    try:
        ydl = youtube_dl.YoutubeDL(ydl_opts)
        info_dict = ydl.extract_info(url, download=True)
    except:
        pass
    return mp3_path

def DL(playlist_url, out_dir):
    items = get_URL_list.main(playlist_url)
    items.reverse()

    exists_files = ["no one"]
    if os.path.exists(out_dir):
        path = "./"+out_dir+"/*.mp3" 
        exists_files = get_exist_mp3s_in_out_dir(path)
    
    for i in range(len(items)):
        # print(items[i][0], exists_files[i][1])
        # print(items[i][0] == exists_files[i][1])
        if exists_files != ["no one"] and i < len(exists_files):
            if items[i][0] == exists_files[i][1] and i+1 == exists_files[i][0]:
                print(items[i][0], "is already downloaded.")
                continue

        set_mp3_track_number(DL_1video(items[i], out_dir), i+1)

def DL1(playlist_url, item_num, out_dir):
    items = get_URL_list.main(playlist_url)
    items.reverse()

    exists_files = ["no one"]
    if os.path.exists(out_dir):
        path = "./"+out_dir+"/*.mp3" 
        exists_files = get_exist_mp3s_in_out_dir(path)

    set_mp3_track_number(DL_1video(items[item_num], out_dir), item_num+1)

def main(key):
    DL(key, "downloads")