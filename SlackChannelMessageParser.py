import json, os
from pprint import pprint
from tuneship import application, db
from tuneship.models import TunesData

class SlackChannelMessageParser:
    rootdir = os.path.dirname(os.path.abspath(__file__))
    datadir = rootdir+'/data/tunes/'
    
    def __init__(self, filename):
        self.filename = filename
        self.datadir = SlackChannelMessageParser.datadir
        self.read_and_upload_json(self.datadir + self.filename)

    def read_and_upload_json(self,filename):
        MainDictionary = {}
        subdict = {}

        
        with open(filename, encoding='utf-8') as data_file:
            data = json.loads(data_file.read())
        for i, entry in enumerate(data):
            MainDictionary[i] = entry
            print("Processing: " + str(i))
            if "attachments" in MainDictionary[i]:
                print("ATTACHMENTS EXISTS")
                subdict[i] = MainDictionary[i]["attachments"][0]
                if "service_name" in subdict[i]:
                    if subdict[i]["service_name"] == "YouTube":
                        print(subdict[i]["title"])

                        if "video_html" in subdict[i]:
                            data_inserted = TunesData(title=subdict[i]['title'],thumb_url=subdict[i]['thumb_url'],iframe_string=subdict[i]['video_html'], media_url=subdict[i]['from_url'])
                        else:
                            data_inserted = TunesData(title=subdict[i]['title'],thumb_url=subdict[i]['thumb_url'], media_url=subdict[i]['from_url'])
                        try:
                            db.session.add(data_inserted)
                            db.session.commit()
                            db.session.close()
                        except:
                            db.session.rollback()
                    elif subdict[i]["service_name"] == "SoundCloud":
                        print(subdict[i]["title"])
                        if "audio_html" in subdict[i]:
                            data_inserted = TunesData(title=subdict[i]['title'], thumb_url=subdict[i]['thumb_url'],iframe_string=subdict[i]['audio_html'], media_url=subdict[i]['from_url'])
                        else:
                            data_inserted = TunesData(title=subdict[i]['title'], thumb_url=subdict[i]['thumb_url'], media_url=subdict[i]['from_url'])
                        try:
                            db.session.add(data_inserted)
                            db.session.commit()
                            db.session.close()
                        except:
                            db.session.rollback()
                else:
                    continue                
            else:
                print("NO ATTACHMENTS")
                continue
            
        
def main():
    for filename in os.listdir(SlackChannelMessageParser.datadir):
        print("Working on " + filename)
        SlackChannelMessageParser(filename)

if __name__ == "__main__":
    main()

