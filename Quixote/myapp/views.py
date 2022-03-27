from ast import mod
from tkinter.messagebox import NO
from django.shortcuts import render
from .models import Image_Model
from PIL import Image
from PIL.ExifTags import TAGS
import boto3
from django.conf import settings
import cloudinary.uploader

# Create your views here.
def img(request):
    obj=None
    if request.method=='POST':
        imagename = request.FILES.get('textfield')
        print(imagename)  
        try:
            print('hello')
            upload_data = cloudinary.uploader.upload(imagename,folder="uploads")
            print(upload_data)
            if upload_data:
                image = Image.open(imagename)
                info_dict = {
                    "Filename": imagename,
                    "Image Size": image.size,
                    "Image Height": image.height,
                    "Image Width": image.width,
                    "Image Format": image.format,
                    "Image Mode": image.mode,
                    "Image is Animated": getattr(image, "is_animated", False),
                    "Frames in Image": getattr(image, "n_frames", 1)
                }
              
                modelobj = Image_Model(size=str(image.size),resolution=str(image.width*image.height),timestamp=str(upload_data['created_at']),filename=imagename,file_extension=upload_data.get('format'),image_id=upload_data.get('public_id').split('uploads/')[1])
                modelobj.save()
            
            # for label,value in info_dict.items():
            #     print(f"{label:25}: {value}")

            id_data =  upload_data.get('public_id')
            obj=Image_Model.objects.all()
            error=None
        except Exception as e:
            print(e)
            error = "Something went wrong! Please select image"
    else:
        obj=Image_Model.objects.all()
        error = None
    context={'items':obj, 'success' :True,'error':error}
    return render(request, 'myapp/home.html',context)
    
def show_data(request,image_id):
    model_obj = Image_Model.objects.get(image_id=image_id)
    # link = model_obj.get(image_id=image_id)
    # print(link)
    link= f'http://res.cloudinary.com/dsnwtu0ir/image/upload/v1648291012/uploads/{ image_id }.png'
    context={'items':model_obj, 'link' :link}
    return render(request , 'myapp/show.html',context)