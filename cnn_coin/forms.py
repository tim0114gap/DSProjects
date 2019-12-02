from django import forms
from .models import ImageModel

class ImageForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ImageForm, self).__init__(*args, **kwargs)
        self.fields['image'].widget.attrs = {
            "class":"choose_button",
            "value":"select",
        }
    
    class Meta:
        model = ImageModel
        fields = ('image',)

    # image = forms.ImageField(label='画像ファイル', widget=forms.FileInput(attrs={"class":"file-upload-input","type":"file"}))