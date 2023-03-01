import threading
import zipfile


class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        read_data = ''
        with open(self.infile, encoding="utf-8") as ftext:
            read_data = ftext.read()
        ftext.close()

        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.writestr(self.infile.split('/')[-1], read_data)
        f.close()
        print('Finished background zip of:', self.infile)


background = AsyncZip('../../resource/readFile.txt', '../../resource/readFile.zip')
background.start()
print('The main program continues to run in foreground.')

background.join()    # Wait for the background task to finish
print('Main program waited until background was done.')



