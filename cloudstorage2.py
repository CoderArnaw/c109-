import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def uplaod_file(self, file_from, file_to):
        dbx=dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BFGiOU-paubW-tC3coH0nS_n3828xP2rUOH5Pa77wrHgKX_k5haPq24XJGzAHipZd_NHKF8PQOcuVIxQJX5e1tEEQrqKeI_Sdk2PCBKAUT3RW5g0mlmyFGvyXsSS3HSQH-hk1LQ'
    transferData =  TransferData(access_token)

    file_from = 'countingwords.py'
    file_to = '/test_dropbox/test.txt' 

    transferData.uplaod_file(file_from,file_to)

if __name__ == '__main__':
    main()


    
