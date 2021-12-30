import cleaner
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, LoggingEventHandler
from datetime import datetime, timedelta

class MyHandler(FileSystemEventHandler):
    def __init__(self):
        self.last_modified = datetime.now()
    def on_modified(self, event):
        if datetime.now() - self.last_modified < timedelta(seconds=1):
            return
        else:
            self.last_modified = datetime.now()
        
        print(f'Event type: {event.event_type}  path : {event.src_path}')
        print(event.is_directory) # This attribute is also available
        
        cleaner.orgArq('abr', 'cm', 'arquivo')
        cleaner.orgAud('mp3')
        cleaner.orgAdo('Adobe', 'psd')
        cleaner.orgImg('jpeg', 'jpg', 'png', 'gif', 'jfif', 'raw', 'bmp')
        cleaner.orgVid('mp4', 'mov', 'avi', 'flv')
        cleaner.orgRaR('winrar', 'zip', 'rar')
        cleaner.orgTor('torrent')
        cleaner.orgApp('exe', 'msi')
        cleaner.orgCod('py', 'cs', 'js', 'php', 'html', 'sql', 'css')
        cleaner.orgTxt('text')
        cleaner.orgPdf('pdf')
        cleaner.orgDoc('word' 'document')
        cleaner.orgSpr('spreadsheet')

if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    
    observer.schedule(event_handler, path= r'C:\Users\T-Gamer\Downloads', recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
        else:
            print ("got it")
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
