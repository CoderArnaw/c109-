import cv2
import dropbox
import time
import random
starttime=time.time()
def takesnapshot():
    number=random.randint(0,100)

    videocaptureobject=cv2.VideoCapture(0)
    result=True
    while(result):

        ret,frame=videocaptureobject.read()
        imagename='img'+str(number)+".png"
        starttime=time.time()

        cv2.imwrite(imagename,frame)
        result=False

    return imagename    
    videocaptureobject.release()
    cv2.destroyAllWindows()

def uplaod_file(imagename):
        access_token='sl.BFGiOU-paubW-tC3coH0nS_n3828xP2rUOH5Pa77wrHgKX_k5haPq24XJGzAHipZd_NHKF8PQOcuVIxQJX5e1tEEQrqKeI_Sdk2PCBKAUT3RW5g0mlmyFGvyXsSS3HSQH-hk1LQ'
        file_from=imagename
        file_to="/testfolder/"+imagename
        dbx=dropbox.Dropbox(self.access_token)


        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

while(True):
    if (time.time()-starttime>=5):
        name=takesnapshot()
        uplaod_file(name)            