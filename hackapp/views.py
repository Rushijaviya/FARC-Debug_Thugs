from sklearn.preprocessing import LabelEncoder, StandardScaler
from django.shortcuts import render
import pickle
# Create your views here.


def home(request):
    return render(request, 'index.html')

def blogg(request):
    return render(request,'blogg.html')

def post(request):
    return render(request,'post.html')

def post2(request):
    return render(request,'post2.html')

def post3(request):
    return render(request,'post3.html')
def post4(request):
    return render(request,'post4.html')
def frauddetection(request):

    if request.method == 'POST':

        amt = request.POST.get('amt')
        lat = request.POST.get('lat')
        longg = request.POST.get('long')
        zipp = request.POST.get('zipp')
        city_pop = request.POST.get('city_pop')
        unix_time = request.POST.get('unix_time')
        merch_lat = request.POST.get('merch_lat')
        merch_long = request.POST.get('merch_long')
        gender = request.POST.get('gender')

        lat = float(lat)
        longg = float(longg)
        amt = float(amt)
        city_pop = int(city_pop)
        zipp = int(zipp)
        unix_time = int(unix_time)
        merch_lat = float(merch_lat)
        merch_long = float(merch_long)
        gender_le = int(gender)

        a = [amt, zipp, lat, longg, city_pop, unix_time,
             merch_lat, merch_long, gender_le]

        model_v2 = pickle.load(open("model.pkl", 'rb'))

        ss = StandardScaler()
        xtest = ss.fit_transform([a])
        ypred = model_v2.predict(xtest)

        ypred = ypred[0]

        context = {
            'result': ypred
        }

        return render(request, 'result.html', context)

    return render(request, 'frauddetection.html')





def companies(request):

    companies_list = ['ASIANPAINT', 'ITC', 'TATAMOTORS', 'NESTLEIND', 'WIPRO', 'IOC', 'BAJFINANCE', 'SBIN', 'INDUSINDBK', 'ULTRACEMCO', 'TCS', 'CIPLA', 'BRITANNIA', 'VEDL', 'JSWSTEEL', 'MM', 'BAJAJ-AUTO',
                      'COALINDIA', 'ZEEL', 'AXISBANK', 'HEROMOTOCO', 'HDFCBANK', 'ADANIPORTS', 'RELIANCE', 'ICICIBANK', 'GAIL', 'HINDUNILVR', 'HDFC', 'DRREDDY', 'POWERGRID', 'KOTAKBANK', 'GRASIM', 'ONGC', 'MARUTI']

    context = {
        'companies_list': companies_list
    }

    if request.method == 'POST':
        company = request.POST.get('company')
        context = {
            'company': company
        }
        return render(request, 'company_details.html', context)

    return render(request, 'companies.html', context)
