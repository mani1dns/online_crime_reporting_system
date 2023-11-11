from django.db import models

# Create your models here.
class login(models.Model):
    login_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    type = models.CharField(max_length=200)


class crime_types(models.Model):
    crime_type_id = models.AutoField(primary_key=True)
    crime_type_name = models.CharField(max_length=200)
    minimum_penalty = models.CharField(max_length=200)



class stations(models.Model):
    station_id = models.AutoField(primary_key=True)
    login_id = models.CharField(max_length=200)
    station_name = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    pincode = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    fax_no = models.CharField(max_length=200)



class crimes(models.Model):
    crime_id = models.AutoField(primary_key=True)
    crime_type_id = models.ForeignKey(crime_types, on_delete=models.CASCADE)
    crime_title = models.CharField(max_length=200)
    crime_description = models.CharField(max_length=200)
    date_time_occurred = models.CharField(max_length=200)
    date_time_reported = models.CharField(max_length=200)
    station_id = models.ForeignKey(stations,on_delete=models.CASCADE)
    crime_status = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    image_pa = models.ImageField(upload_to='static/uploads')


class criminals(models.Model):
    criminal_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    dob = models.CharField(max_length=200)
    photo_da = models.ImageField(upload_to='static/uploads')
    thumb_impression = models.ImageField(upload_to='static/uploads')
    identification_mark_1 = models.CharField(max_length=200)
    identification_mark_2 = models.CharField(max_length=200)
    house_name = models.CharField(max_length=200)
    father_name = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    district = models.CharField(max_length=200)


class users(models.Model):
    user_id = models.AutoField(primary_key=True)
    login_id = models.ForeignKey(login, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    house_name = models.CharField(max_length=200)
    place = models.CharField(max_length = 200)
    pincode = models.CharField(max_length = 200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)



class complaints(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(users, on_delete=models.CASCADE)
    station_id = models.ForeignKey(stations, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    date_time = models.CharField(max_length=200)
    status = models.CharField(max_length=200)


class evidences(models.Model):
    evidence_id = models.AutoField(primary_key=True)
    complaint_id = models.ForeignKey(complaints, on_delete=models.CASCADE)
    file_path = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date_time = models.CharField(max_length=200)


class message(models.Model):
    message_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(users, on_delete=models.CASCADE)
    message_description = models.CharField(max_length=200)
    reply = models.CharField(max_length=200)
    date_time = models.CharField(max_length=200)


class foundreport(models.Model):
    found_id = models.AutoField(primary_key=True)
    criminal_id = models.ForeignKey(criminals, on_delete=models.CASCADE)
    user_id = models.ForeignKey(users, on_delete=models.CASCADE)
    place = models.CharField(max_length=200)
    date_time = models.CharField(max_length=200)
    description = models.CharField(max_length=200)


class feedback(models.Model):
    feed_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(users,on_delete=models.CASCADE)
    feed_description = models.CharField(max_length=200)
    reply = models.CharField(max_length=200)
    date_time = models.CharField(max_length=200)


class advocates(models.Model):
    adv_id = models.AutoField(primary_key=True)
    login_id = models.ForeignKey(login, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    qualification = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    house_name = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    status = models.CharField(max_length=200)


class case_types(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)


class cases(models.Model):
    case_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(users, on_delete=models.CASCADE)
    type_id = models.ForeignKey(case_types,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    case_date = models.CharField(max_length=200)
    police_station = models.CharField(max_length=200)
    pincode = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    status = models.CharField(max_length=200)


class proposals(models.Model):
    proposal_id = models.AutoField(primary_key=True)
    case_id = models.ForeignKey(cases,on_delete=models.CASCADE)
    adv_id = models.ForeignKey(advocates, on_delete=models.CASCADE)
    fee = models.CharField(max_length=200)
    date_time = models.CharField(max_length=200)
    status = models.CharField(max_length=200)


class client_assigns(models.Model):
    assign_id = models.AutoField(primary_key=True)
    client_id = models.CharField(max_length=200)
    adv_id = models.ForeignKey(advocates, on_delete=models.CASCADE)
    case_id = models.ForeignKey(cases,on_delete=models.CASCADE)
    date_time = models.CharField(max_length=200)
    status = models.CharField(max_length=200)


class case_allocations(models.Model):
    allocation_id = models.AutoField(primary_key=True)
    proposal_id = models.ForeignKey(proposals, on_delete=models.CASCADE)
    date_time = models.CharField(max_length=200)


class law_details(models.Model):
    law_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    ipc_code = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    penalty = models.CharField(max_length=200)


class chats(models.Model):
    chat_id = models.AutoField(primary_key=True)
    sender_id = models.CharField(max_length=200)
    sender_type = models.CharField(max_length=200)
    receiver_id = models.CharField(max_length=200)
    receiver_type = models.CharField(max_length=200)
    message = models.CharField(max_length=200)
    date_time = models.CharField(max_length=200)


class case_files(models.Model):
    file_id = models.AutoField(primary_key=True)
    file_title = models.CharField(max_length=200)
    case_id = models.ForeignKey(cases,on_delete=models.CASCADE)
    file_path = models.CharField(max_length=200)


class case_notes(models.Model):
    note_id = models.AutoField(primary_key=True)
    case_id = models.ForeignKey(cases,on_delete=models.CASCADE)
    datetime = models.CharField(max_length=200)
    description = models.CharField(max_length=200)


class ratings(models.Model):
    rating_id = models.AutoField(primary_key=True)
    client_id = models.CharField(max_length=200)
    adv_id = models.ForeignKey(advocates, on_delete=models.CASCADE)
    rate = models.CharField(max_length=200)
    review = models.CharField(max_length=200)
    date_time = models.CharField(max_length=200)

    