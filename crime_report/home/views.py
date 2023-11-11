from django.http import HttpResponse
from django.shortcuts import redirect, render
from home.models import *

from django.core.files.storage import FileSystemStorage
# Create your views here.
def index_page(request):
    if request.method == "POST":
        uname = request.POST['username']
        pwd = request.POST['password']
        print(uname,pwd)

        try:
            q = login.objects.get(username = uname,password=pwd)
            request.session['login_id']=q.pk

            if q.type == 'admin':
                return HttpResponse("<script>alert('Welcome admin');window.location='admin_user_home'</script>")
            if q.type == 'advocate':
                return HttpResponse("<script>alert('Welcome advocate');window.location='advocate_user_home'</script>")
            if q.type == 'police_stations':
                return HttpResponse("<script>alert('Welcome Police Station');window.location='police_station_home'</script>")
            if q.type == 'user':
                q1=users.objects.get(login_id=request.session['login_id'])
                request.session['user_id']=q1.pk

                return HttpResponse("<script>alert('Welcome Public Users');window.location='public_user_home'</script>")
        except:
            return HttpResponse("<script>alert('Failed to login');window.location='/'</script>")
    return render(request, 'index.html')

#   -----MODULES-----
def admin_user(request):
    return render(request,'admin_user_home.html')

def advocate_user(request):
    return render(request,'advocate_user_home.html')

def police_station_name(request):
    return render(request, 'police_station_home.html')

def public_user(request):
    return render(request,'public_user_home.html')


        

#for viewing
def advocate(request):
    q = advocates.objects.all()
    return render(request,'advocate.html',{'data':q})

def updates(request,id):

    login.objects.filter(login_id = id).update(type='advocate')
    advocates.objects.filter(login_id = id).update(status='accept')
    return HttpResponse("<script>alert('Approved');window.location='/admin_user'</script")
        

def delete(request,id):
    login.objects.get(login_id = id).delete()
    advocates.objects.get(login_id = id).delete()
    return HttpResponse("<script>alert('Deleted');window.location='advocate'</script>")


def user_register(request):
    q = users.objects.all()
    return render(request,'users.html',{'data':q})


def complaint(request):
    q = complaints.objects.all()
    return render(request,'complaints.html',{'data':q})


def criminal(request):
    q = criminals.objects.all()
    return render(request,'criminals.html',{'data':q})

def police_stations(request):
    q = stations.objects.all()
    return render(request,'police_station.html',{'data':q})

def crime_type_view(request):
    q = crime_types.objects.all()
    return render(request,'crime_types_view.html',{'data':q})

def found_reports(request):
    q = foundreport.objects.all()
    return render(request,'found_report.html',{'data':q})

def crime(request):
    q = crimes.objects.all()
    return render(request,'crimes.html',{'data':q})

def registered_user(request):
    r = users.objects.all()
    return render(request,'registered_users.html',{'data':r})

def case_type(request):
    q = case_types.objects.all()
    return render(request,'case_types.html',{'data':q})

def user_view(request):
    t = users.objects.all()
    return render(request, 'users_view.html', {'data':t})


def rating1(request):
    q = ratings.objects.all()
    return render(request,'rating.html',{'data':q})


def feedbacks(request):
    q = feedback.objects.all()
    return render(request, 'feedback.html',{'data':q})


def complaints_view(request):
    q = complaints.objects.all()
    return render(request,'complaints_view.html',{'data':q})



#admin module - crime_type manage started
def crime_type(request):
    if 'submit' in request.POST:
        crime_type=request.POST['crime_types']
        minimum_penalty=request.POST['minimum_penalty']
        q= crime_types(crime_type_name=crime_type,minimum_penalty=minimum_penalty)
        q.save()
    q = crime_types.objects.all()
    return render(request,'crime_types.html',{'data':q})

def update_crime_type(request,id):
    ab = crime_types.objects.get(crime_type_id=id)
    if 'update' in request.POST:
        crime_type=request.POST['crime_types']
        minimum_penalty=request.POST['minimum_penalties']

        ab.crime_type_name=crime_type
        ab.minimum_penalty=minimum_penalty
        ab.save()
        return HttpResponse("<script>alert('updated');window.location='/crime_types'</script>")
    
    return render(request,'crime_types.html',{'ab':ab})

def delete_crime_type(request,id):
    ef=crime_types.objects.get(crime_type_id=id)
    ef.delete()
    return HttpResponse("<script>alert('deleted');window.location='/crime_types'</script>")
#admin module - crime_type manage ended


# admin module - stations manage started
def station(request):
    if 'submit' in request.POST:
        names = request.POST['stationname']
        place = request.POST['place']
        district = request.POST['district']
        pincode = request.POST['pin']
        phoneno = request.POST['phone']
        mail = request.POST['email']
        fax_no = request.POST['fax']
        q = stations(station_name=names, place=place, district=district,pincode=pincode, phone=phoneno, email=mail, fax_no=fax_no)
        q.save()
    q = stations.objects.all()
    return render(request,'stations.html',{'data':q})

def update_stations(request, id):
    cd = stations.objects.get(station_id=id)
    if 'update' in request.POST:
        names = request.POST['stationname']
        place = request.POST['place']
        district = request.POST['district']
        pincode = request.POST['pin']
        phoneno = request.POST['phone']
        mail = request.POST['email']
        fax_no = request.POST['fax']

        cd.station_name=names
        cd.place=place
        cd.district=district
        cd.pincode=pincode
        cd.phone=phoneno
        cd.email=mail
        cd.fax_no=fax_no
        cd.save()
        return HttpResponse("<script>alert('updated');window.location='/stations'</script>")
    
    return render(request,'stations.html',{'cd':cd})

def delete_stations(request,id):
    ef=stations.objects.get(station_id=id)
    ef.delete()
    return HttpResponse("<script>alert('deleted');window.location='/stations'</script>")
# admin module - stations manage ended


#police module - crimes manage started
def crime_manage(request):
    qa=stations.objects.all()
    ab =crime_types.objects.all()
    if 'submit' in request.POST:
        t = request.POST['title']
        des = request.POST['description']
        occured = request.POST['occ_time']
        reported = request.POST['rep_time']
        stat = request.POST['status']
        c = request.POST['choose_crime']
        s = request.POST['station']
        p = request.POST['place']
        d = request.POST['district']
        image = request.FILES['img']
        
        q = crimes(crime_title=t, crime_description=des, date_time_occurred=occured, date_time_reported=reported, crime_status=stat,crime_type_id_id=c, station_id_id=s, place=p, district=d, image_pa=image)
        q.save()
        return HttpResponse("<script>alert('added');window.location='crimes_manage'</script>")
    qc = crimes.objects.all()
    return render(request,'crimes_manage.html',{'data':qc,'qa':qa, 'ab':ab})

def update_crime(request,id):
    qz=crimes.objects.get(crime_id=id)
    qa=stations.objects.all()
    ab =crime_types.objects.all()

    if 'update' in request.POST:
        t = request.POST['title']
        des = request.POST['description']
        occured = request.POST['occ_time']
        reported = request.POST['rep_time']
        stat = request.POST['status']
        c = request.POST['choose_crime']
        s = request.POST['station']
        p = request.POST['place']
        d = request.POST['district']
        image = request.FILES['img']

        qz.crime_title=t
        qz.crime_description=des
        qz.date_time_occurred=occured
        qz.date_time_reported=reported
        qz.crime_status=stat
        qz.crime_type_id_id=c
        qz.station_id_id=s
        qz.place=p
        qz.district=d
        qz.image_pa=image
        qz.save()
        return HttpResponse("<script>alert('updated');window.location='/crimes_manage'</script>")
    
    return render(request,'crimes_manage.html',{'qz':qz,'qa':qa,'ab':ab})

def delete_crime(request,id):
    ef=crimes.objects.get(crime_id=id)
    ef.delete()
    return HttpResponse("<script>alert('deleted');window.location='/crimes_manage'</script>")
#police module - crimes manage ended


#police module - criminals manage started
def criminal_manage(request):
    if 'submit' in request.POST:
        f = request.POST['first']
        l = request.POST['last']
        g = request.POST['gender']
        date = request.POST['dob']
        i = request.FILES['photo']
        t = request.FILES['thumb']
        iden1 = request.POST['id1']
        iden2 = request.POST['id2']
        h = request.POST['house']
        father = request.POST['father_name']
        p = request.POST['place']
        d = request.POST['district']
        w = criminals(first_name=f, last_name=l, gender=g, dob=date, photo_da=i, thumb_impression=t, identification_mark_1=iden1, identification_mark_2=iden2, house_name=h, father_name=father, place=p, district=d)
        w.save()

        return HttpResponse("<script>alert('added');window.location='criminals_manage'</script>")
    w = criminals.objects.all()
    return render(request,'criminals_manage.html',{'data':w})

def update_criminal(request,id):
    ab=criminals.objects.get(criminal_id=id)

    if 'update' in request.POST:
        f = request.POST['first']
        l = request.POST['last']
        g = request.POST['gender']
        date = request.POST['dob']
        i = request.FILES['photo']
        t = request.FILES['thumb']
        iden1 = request.POST['id1']
        iden2 = request.POST['id2']
        h = request.POST['house']
        father = request.POST['father_name']
        p = request.POST['place']
        d = request.POST['district']

        ab.first_name=f
        ab.last_name=l
        ab.gender=g
        ab.dob=date
        ab.photo_da=i
        ab.thumb_impression=t
        ab.identification_mark_1=iden1
        ab.identification_mark_2=iden2
        ab.house_name=h
        ab.father_name=father
        ab.place=p
        ab.district=d
        ab.save()
        return HttpResponse("<script>alert('updated');window.location='/criminals_manage'</script>")
    return render(request,'criminals_manage.html',{'ab':ab})

def delete_criminal(request,id):
    ma=criminals.objects.get(criminal_id=id)
    ma.delete()
    return HttpResponse("<script>alert('deleted');window.location='/crimes_manage'</script>")


#admin module - case_type manage started
def case_type_manage(request):
    if 'submit' in request.POST:
        type = request.POST['typename']
        des = request.POST['description']
        q = case_types(type_name=type, description=des)
        q.save()
    q = case_types.objects.all()
    return render(request, 'case_types_manage.html',{'data':q})

def update_case_type_manage(request,id):
    ab = case_types.objects.get(type_id=id)

    if 'update' in request.POST:
        type = request.POST['typename']
        des = request.POST['description']

        ab.type_name = type
        ab.description = des
        ab.save()
        return HttpResponse("<script>alert('updated');window.location='/case_types_manage'</script>")
    
    return render(request,'case_types_manage.html',{'ab':ab})

def delete_case_type_manage(request,id):
    ab=case_types.objects.get(type_id=id)
    ab.delete()
    return HttpResponse("<script>alert('Deleted');window.location='/case_types_manage'</script>")

#admin module - case_type manage ended

#admin module - law_details manage started
def law_detail_manage(request):
    if 'submit' in request.POST:
        titles = request.POST['title']
        ipc = request.POST['code']
        description = request.POST['des']
        penalty = request.POST['penalties']
        q = law_details(title=titles, ipc_code=ipc, description=description, penalty=penalty)
        q.save()
    q = law_details.objects.all()
    return render(request,'law_details_manage.html', {'data':q})

def update_law_detail_manage(request,id):
    cd = law_details.objects.get(law_id=id)

    if 'update' in request.POST:
        titles = request.POST['title']
        ipc = request.POST['code']
        description = request.POST['des']
        penalty = request.POST['penalties']

        cd.title = titles
        cd.ipc_code = ipc
        cd.description = description
        cd.penalty = penalty
        cd.save()
        return HttpResponse("<script>alert('updated');window.location='/law_details_manage'</script>")
    
    return render(request,'law_details_manage.html',{'cd':cd})


def delete_law_detail_manage(request,id):
    ef=law_details.objects.get(law_id=id)
    ef.delete()
    return HttpResponse("<script>alert('deleted');window.location='/law_details_manage'</script>")
#admin module - law_details manage ended

def law_detail(request):
    q = law_details.objects.all()
    return render(request,'law_details.html',{'data':q})

#public module - cases_manage started
def cases_manage(request):
    if 'submit' in request.POST:
        t = request.POST['title']
        des = request.POST['description']
        casedate = request.POST['date']
        p = request.POST['police']
        pin = request.POST['pincode']
        ph = request.POST['phone']
        stat = request.POST['status']
        case1 = request.POST['case']
        q = cases(client_id=id, title=t, description=des, case_date=casedate, police_station=p, pincode=pin, phone=ph, status=stat, type_id=case1)
        q.save()
    q = cases.objects.all()
    c = case_types.objects.all()
    return render(request,'case_manage.html',{'data':q,'data':c})


#public module - cases_manage ended


#registration starts from here
def advocate_register(request):
    if 'submit' in request.POST:    
        first = request.POST['firstname']
        last = request.POST['lastname']
        qualify = request.POST['qualification']
        genders = request.POST['gender']
        phones = request.POST['phone']
        emails = request.POST['email']
        pwd = request.POST['password']
        house = request.POST['house_name']
        places = request.POST['place']
        

        obj = login(username=first,password=pwd,type='pending')
        obj.save()  
        print(obj.pk)   
        q=advocates(first_name=first,last_name=last,qualification=qualify,gender=genders,phone=phones,email=emails,house_name=house,place=places,status='pending',login_id_id=obj.pk)
        q.save()

        return redirect('/')
    return render(request,'advocates_register.html')


def public_registers(request):
    if 'submit' in request.POST:
        f = request.POST['firstname']
        l = request.POST['lastname']
        h = request.POST['house_name']
        p = request.POST['place']
        pin = request.POST['pincode']
        phone = request.POST['phone']
        email = request.POST['email']
        pwd = request.POST['password']

        obj = login(username=f,password=pwd,type='public')
        obj.save()
        print(obj.pk)
        q = users(first_name=f,last_name=l,house_name=h,place=p,pincode=pin,phone=phone,email=email,login_id_id=obj.pk)
        q.save()

        return redirect('/')
    return render(request, 'public_register.html')  
#Registration ends here


def public_make_complaints(request):
    qa=complaints.objects.all()
    if 'submit' in request.POST:
        des = request.POST['description']
        da_ti = request.POST['dat_time']
        stat = request.POST['status']

        
        q = complaints(description=des, date_time=da_ti, status=stat)
        q.save()
        return HttpResponse("<script>alert('added');window.location='public_make_complaint'</script>")
    qa = complaints.objects.all()
    return render(request,'public_make_complaint.html',{'qa':qa})

#foundreport inserting in ###################   user module
def found_report_insert(request):
    q1=criminals.objects.all()
    if 'submit' in request.POST:
        p = request.POST['place']
        d = request.POST['date']
        des = request.POST['description']
        cri=request.POST['criminal']
        q = foundreport(place=p, date_time=d, description=des,criminal_id_id=cri,user_id_id=request.session['user_id'])
        q.save()
    q = foundreport.objects.all()

    return render(request,'found_report_insert.html',{'data':q,'q1':q1})

# viewing criminal found reporting in ################    police module
def criminal_found_report(request):
    q = foundreport.objects.all()
    return render(request,'criminal_found_report.html',{'data':q})


def user_make_complaint(request):
    qz = stations.objects.all()
    ab = users.objects.all()
    if 'submit' in request.POST:
        stat = request.POST['station']
        des = request.POST['description']
        date = request.POST['date_time']
        q = complaints(station_id_id=stat, description=des, date_time=date,status='pending',user_id_id=request.session['user_id'])
        q.save()
        return HttpResponse("<script>alert('Complaint made');window.location='/user_make_complaint'</script>")
    q = complaints.objects.all()

    return render(request,'user_make_complaint.html',{'data':q, 'qz':qz, 'ab':ab})


def upload_evidence(request):
    qp = complaints.objects.all()
    if 'submit' in request.POST:
        img = request.POST['image']
        q = evidences(file_path=img)
        q.save()
        return HttpResponse("<script>alert('Evidence Uploaded Successfully');window.location='/user_make_complaint'</script>")
    return render(request,'upload_evidence.html',{'data':qp})

def user_cases_view(request,id):
    r= cases.objects.get(user_id_id=id)
    return render(request,'user_cases_view.html',{'data':r})

