from django.shortcuts import render



def index(request):
    return render(request, 'LandingPage/index.html')


# def registerPage(request):
#     form = UserCreationForm()

# 	if request.method == "POST":
# 		form = UserCreationForm(request.POST)
# 		if form.is_valid():
# 			form.save()
#     context = {'form': form, }
#     return render(request, 'LandingPage/register.html', context)
