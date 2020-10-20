from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Upload, batata,file_content
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.files.uploadedfile import UploadedFile
import csv
from django.conf import settings
from threading import Thread
import time,sys,os,signal

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

is_paused = False
stopped = False
pid= os.getpid()
def show(request):
    content =  {}
    if request.method =='POST':
        uploaded_file = request.FILES['file']
        uploaded_file_chunks = UploadedFile.chunks(uploaded_file,chunk_size=100)
        print(uploaded_file.name)
        print(uploaded_file.size)
        fs = FileSystemStorage()
        fs.save(uploaded_file.name,uploaded_file)
        global upload 
        upload = Upload()
        upload.title = uploaded_file.name
        upload.file = uploaded_file
        upload.save()
        global filecontent 
        filecontent = file_content()
        path = os.path.join(BASE_DIR, 'media/')+uploaded_file.name
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader)
            for row in csv_reader:
                if not is_paused:
                    filecontent.seq = row[0]
                    filecontent.First_name =row[1] 
                    filecontent.Last_name = row[2]
                    filecontent.age = row[3]
                    filecontent.street = row[4]
                    filecontent.city = row[5]
                    filecontent.state = row[6]
                    filecontent.zipcode = row[7]
                    filecontent.dollar = row[8]
                    filecontent.color = row[9]
                    filecontent.date = row[10]
                    filecontent.CSV_ID=upload.pk
                    filecontent.save()
                    time.sleep(1)
                    if stopped:
                        break
                while is_paused:
                    time.sleep(1)
                    print("paused")
    return render(request,'upload/upload.html', content)


def pause_upload(request):
    global is_paused
    if not is_paused:
        is_paused = True
    return render(request, 'upload/upload.html')

def resume(request):
    global is_paused
    if is_paused:
        is_paused = False 
    print('thread continued')
    return render(request,'upload/upload.html')    


def stop(request):
    global stopped
    if not stopped:
        stopped = True
    return HttpResponse('stopped')