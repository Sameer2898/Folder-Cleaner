import os

def createIfNotExist(folder):
        if not os.path.exists(folder):
            os.makedirs(folder)

def move(foldername,files):
        for file in files:
            os.replace(file,f'{foldername}/{file}')
        
if __name__ == "__main__":

    files = os.listdir()
    files.remove('main.py')
    # print(files)

    createIfNotExist('Images')
    createIfNotExist('Docs')
    createIfNotExist('Audio')
    createIfNotExist('Video')
    createIfNotExist('Others')

    img_extension = ['.png','.jpg','.jpeg','.ico']
    images = [file for file in files if os.path.splitext(file)[1].lower() in img_extension]
    # print(images)

    docs_extension = ['.doc','.docx','.txt','.pdf','.xls']
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docs_extension]
    # print(docs)

    audio_extension = ['.aif','.cda','.mid','.midi','.mp3','.mpa','.ogg','.wav','.wma','.wpl' ]
    audios = [file for file in files if os.path.splitext(file)[1].lower() in audio_extension]
    # print(audios)

    video_extension = ['.3g2','.3gp','.avi','.flv','.h264','.m4v','.mkv','.mov','.mp4','.mpg','.mpeg']
    videos= [file for file in files if os.path.splitext(file)[1].lower() in video_extension]
    # print(videos)

    others = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in img_extension) and (ext not in docs_extension) and (ext not in audio_extension) and (ext not in video_extension) and os.path.isfile(file):
            others.append(file)
    # print(others)

    #Moving files in to their corresponding folders
    move('Images',images)
    move('Docs',docs)
    move('Audios',audios)
    move('Videos',videos)
    move('Others',others)
