from fileinput import filename
from django.shortcuts import render,  redirect
from django.views.generic import CreateView, TemplateView
from .models import Image
from tensorflow import keras
from keras.preprocessing import image
import tensorflow as tf
import numpy as np
from django.conf import settings
import random, string

labels = {
    '0':'Changunarayan',
    '1': 'maya devi',
    '2': 'shiva',
    '3': 'Swyambhu'
}

# Create your views here.
class HomeView(CreateView):
    model = Image
    template_name = 'home.html'
    fields = ['image']

    def form_valid(self, form):
        randomstr = ''.join(random.choices(string.ascii_letters+string.digits,k=5))
        form.instance.image_name = randomstr
        form.instance.image = form.cleaned_data['image']
        form.save()
        return redirect('redirect')




def image_recognition(request):

    list1 = Image.objects.all()


    print(f"\n\n\n\n{list1}\n\n\n\n")
    print(f"\n\n\n\n{list1[len(list1)-1]}\n\n\n\n")
    image_ = list1[len(list1)-1].image.url
    print(f"\n\n\n\n\n\n\{image_}\n\n\n\n\n")

    model = keras.models.load_model('Heritage1.h5')
    img=tf.keras.utils.load_img(image_[1:], target_size=(200, 200))
    x=tf.keras.utils.img_to_array (img)
    x /= 255
    x=np.expand_dims(x, axis=0)
    images = np.vstack([x])

    print(model.predict(images))

    classes = model.predict(images)
    classes = classes.tolist()
    print(classes)
    max_value = max(classes[0])
    print(max_value)
    label_value = classes[0].index(max_value)
    print(label_value)
    # if classes >0.5:
    #     print(" is a Swayambhu")
    #     return redirect('Swoyambhu')
    # else:
    #     return redirect('Changunarayan')

    if label_value == 0:
        return redirect('Changunarayan')
    elif label_value == 1:
        return redirect('mayadevi')
    elif label_value == 2:
        return redirect('shiva')
    elif label_value == 3:
        return redirect('Swoyambhu')
    else:
        pass


class SwoyambhuView(TemplateView):
    template_name = 'swoyambhu.html'

class ChangunarayanView(TemplateView):
    template_name = 'changunarayan.html'

class MayaDevi(TemplateView):
    template_name = 'mayadevi.html'

class Shiva(TemplateView):
    template_name = 'shiva.html'