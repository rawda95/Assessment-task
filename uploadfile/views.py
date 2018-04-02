from django.shortcuts import render ,redirect
from .forms import FileForm




def model_form_upload(request):
    if request.method == 'POST':
        form =FileForm (request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'file_upload.html', {
                'form': form,
                'message': 'file upload successfully'
            })
    form = FileForm()
    return render(request, 'file_upload.html', {
        'form': form
    })