__author__ = 'vincent'
import json
from urllib import urlencode
from urllib2 import Request, urlopen
import ShooterUtil as shooter


class SubtitleDownloader:
    def __init__(self, filepath, language='Chn'):  # Eng or Chn
        self.__filename = filepath.split('/')[-1]
        self.__path = filepath
        self.__hash = shooter.get_shooter_hash(filepath)
        self.__url = shooter.get_API_URL()
        self.__lang = language
        values = dict(filehash=self.__hash, pathinfo=self.__path, format="json", lang=self.__lang)
        self.__params = urlencode(values).encode('utf-8', 'replace')

    def download(self):
        rsp = urlopen(Request(self.__url, self.__params))
        content = rsp.read().decode('utf-8', 'replace')
        if content == 0xff:
            print "No subtitle in Shooter!"
        else:
            subtitle_json = json.loads(content)
            i = 0
            for subinfo in subtitle_json:
                if subinfo["Delay"] != 0:
                    pass
                else:
                    for fileinfo in subinfo["Files"]:
                        link = fileinfo["Link"]
                        ext = fileinfo["Ext"]
                        out_filename = self.__path + "." + self.__lang + '.' + str(i) + "." + ext
                        with open(out_filename, 'wb') as output:
                            print "downloading"
                            output.write(urlopen(link).read())
                    i += 1


if __name__ == '__main__':
    print "Welcome to PyShooterSubDownloader"
    filepath = "/Users/vincent/Movies/game.of.thrones.s04e08.720p.hdtv.x264-killers.mkv"
    downloader = SubtitleDownloader(filepath)
    print "Start download Subtitle"
    downloader.download()
    print "finished, Please check the file"


