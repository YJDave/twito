
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import (
    TwitterApp,
    LocationSearch,
)

from .forms import (
    TwitterApp_Form,
    SearchLocation_Form,
)

from tweepy import(
    OAuthHandler,
	API,
	Cursor,
)


login_url = '/'


def index(request):
    return render(request, 'index.html')


@login_required(login_url=login_url)
def dashboard(request):

    if request.method == 'POST':

        form = TwitterApp_Form(request.POST)

        # log form details here

        if form.is_valid():

            _consumerKey = request.POST['ConsumerKey'].strip()
            _consumerToken = request.POST['ConsumerToken'].strip()
            _access_token = request.POST['access_token'].strip()
            _access_key = request.POST['access_key'].strip()

            try:
                auth = OAuthHandler(_consumerKey, _consumerToken)
                auth.get_authorization_url()

                auth.set_access_token(_access_token,_access_key)

                api = API(auth)
                twitterName = (api.me()).name

                # if consumer token and Access Tokens are valid then only would go further

                app = form.save(commit=False)
                app.user = request.user
                app.save()

                return redirect('/dashboard/')

            except Exception as e:
                # log exception
                print(str(e))

                messages.warning(
                    request,
                    '''Error in Consumer Key/Toekn!
                    Please try again with correct Twitter App Credentials!''')

                return redirect('/dashboard/')
        else:
            print(form.errors)
            return redirect('/dashboard/')

    else:

        form = TwitterApp_Form()

        apps = TwitterApp.objects.filter(
            user=request.user).order_by('-created_at')

        return render(request, 'dashboard.html', {'apps': apps, 'form': form})


@login_required(login_url=login_url)
def appPage(request, app_id):


    if request.method == 'POST':

        form = SearchLocation_Form(request.POST)


        if form.is_valid():

            _latitude = request.POST['latitude']
            _longitude = request.POST['longitude']
            _radius = request.POST['radius']
            _radiusUnit = request.POST['radiusUnit']

            try:

                TwitoApp = get_object_or_404(TwitterApp, id=app_id, user=request.user)

                app = form.save(commit=False)
                app.user = request.user
                app.AppName = TwitoApp
                app.save()



                auth = OAuthHandler(TwitoApp.ConsumerKey, TwitoApp.ConsumerToken)
                auth.get_authorization_url()

                auth.set_access_token(TwitoApp.access_token, TwitoApp.access_key)

                api = API(auth)

                StatusObjects = api.search(geocode=str(_latitude) + "," +
                                                   str(_longitude) + "," +
                                                   (str(_radius) + _radiusUnit)
                                           )


                return render(request, 'searchlocation.html', {'status': StatusObjects})
#                return redirect('/dashboard/'+app_id+'/'+'search/')

            except Exception as e:

                print(e)
                return redirect('/dashboard/'+app_id+'/')
        else:
            print(form.errors)
            return redirect('/dashboard/'+app_id+'/')

    else:

        app = get_object_or_404(TwitterApp, id=app_id, user=request.user)

        users = TwitterApp.objects.filter(AppName=app)

        return render(request, 'app.html', {'app': app, 'users': users})



@login_required(login_url=login_url)
def searchLocationwise(request, app_id):

    try:

        app = get_object_or_404(TwitterApp, id=app_id, user=request.user)
        queryobj = LocationSearch.objects.get(AppName=app, user=request.user)

        auth = OAuthHandler(app.ConsumerKey, app.ConsumerToken)
        auth.get_authorization_url()

        auth.set_access_token(app.access_token, app.access_key)

        api = API(auth)

        StatusObjects = api.search(geocode=str(queryobj.latitude) + "," +
                                           str(queryobj.longitude) + "," +
                                           (str(queryobj.radius)+queryobj.radiusUnit)
                                   )

        return render(request, 'searchlocation.html', {'status': StatusObjects})

    except Exception as e:

        print(e)
        return redirect('/dashboard/'+app_id+'/')



@login_required(login_url=login_url)
def deleteTwitterApp(request, app_id):

    get_object_or_404(TwitterApp, id=app_id, user=request.user).delete()

    return redirect('/dashboard/')



#####################MAKE USER AWARE OF ERROR SHOW ERROR MESSAGE BY POP UP MENU ####################