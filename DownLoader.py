import os

class YouTube_Downloader:

    def __init__(self, url, idx=":") -> None:
        self.url = "\""+url+"\""
        self.index = idx
        self.ffmpeg_path = "\"C:\\Users\\XXX\\ffmpeg_dl\\bin\""

    def DL(self):
        # コマンド用の文字列を生成
        cmd = "yt-dlp --ignore-errors -x --audio-format mp3 --audio-quality 0 -o \"%%(playlist)s/%%(playlist_index)s %%(title)s.%%(ext)s\" --embed-metadata --add-metadata --embed-thumbnail --ppa \"EmbedThumbnail+ffmpeg_o:-c:v mjpeg -vf crop=\\\"'if(gt(ih,iw),iw,ih)':'if(gt(iw,ih),ih,iw)'\\\"\" --exec ffprobe --ffmpeg-location "
        cmd += self.ffmpeg_path
        cmd += " -I "
        cmd += self.index
        cmd += " "
        cmd += self.url
        
        # cmdファイルを生成
        cmd_path = "Downloader.cmd"
        with open(cmd_path, mode="w") as f:
            f.write("@echo off\n")
            f.write("cd \\Users\\takashi_ritsDE\\Music\\\n")
            f.write(cmd)
        
        # cmdファイルの実行
        os.system(cmd_path)
        return

URLs = {
    "ヒプ": "https://music.youtube.com/playlist?list=PL_tZf_DVhK5Y8wSPBkZYoeHTGvLcQoXAr",
    "カリ": "https://music.youtube.com/playlist?list=PL_tZf_DVhK5Y4tOuNe2WbplDB6ES9BbbX",
    "va": "https://music.youtube.com/playlist?list=PL_tZf_DVhK5bPfb14CynNfEKI4yIlpQTi",
    "なつ":"https://music.youtube.com/playlist?list=PL_tZf_DVhK5YooDq_uw4dqKjykVznyvG4",
    "mj_the":"https://music.youtube.com/playlist?list=OLAK5uy_mOjLBgz48J7NUYO6bDipwHKHpTYjDACR8",
    "mj_his":"https://music.youtube.com/playlist?list=OLAK5uy_kUDpgk4yWnyIVfpftIeU0icvhlKAROmx0",
    "mj_dan":"https://music.youtube.com/playlist?list=OLAK5uy_nsZm9AscLdmJf4wE2Af8D3JvFzfPCKdEs",
    "SO":"https://music.youtube.com/playlist?list=PL_tZf_DVhK5bOrCyrvOf-OSeBh6w7q7Mm",
    "D":"https://music.youtube.com/playlist?list=PL_tZf_DVhK5a5SCBAV7XmBpPQbIh5dmiX",
    "DX":"https://music.youtube.com/playlist?list=OLAK5uy_mjfUh_HnYR9yjAZI0NUtrOuKtpKqtrdBU",
    "Creepy":"https://music.youtube.com/playlist?list=PL_tZf_DVhK5Zo9hnLRiD_7ffYecl6y90k",
    "para": "https://music.youtube.com/browse/VLPL_tZf_DVhK5aEgIMZIjgCM9TAumChl2-Q",
    "juju":"https://music.youtube.com/playlist?list=PL_tZf_DVhK5YSJiSbHoiOp03CBAMmVhAY",
    "AGE": "https://music.youtube.com/playlist?list=PL_tZf_DVhK5YcjX3D2UrritboZddEqszD",
    "Topic": "https://music.youtube.com/playlist?list=PL_tZf_DVhK5afpgoiUGpunru8640JegSF"
}

if __name__ == '__main__':
    URL = str( input("URLを入力:") )
    if URL in URLs:
        URL = URLs[URL]
    index = str( input("インデックス:") )

    YTD = YouTube_Downloader(URL, index)
    YTD.DL()
