# Generated by Django 3.2.22 on 2023-10-27 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='advocates',
            fields=[
                ('adv_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('qualification', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('house_name', models.CharField(max_length=200)),
                ('place', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='case_types',
            fields=[
                ('type_id', models.AutoField(primary_key=True, serialize=False)),
                ('type_name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='cases',
            fields=[
                ('case_id', models.AutoField(primary_key=True, serialize=False)),
                ('client_id', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('case_date', models.CharField(max_length=200)),
                ('police_station', models.CharField(max_length=200)),
                ('pincode', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.case_types')),
            ],
        ),
        migrations.CreateModel(
            name='chats',
            fields=[
                ('chat_id', models.AutoField(primary_key=True, serialize=False)),
                ('sender_id', models.CharField(max_length=200)),
                ('sender_type', models.CharField(max_length=200)),
                ('receiver_id', models.CharField(max_length=200)),
                ('receiver_type', models.CharField(max_length=200)),
                ('message', models.CharField(max_length=200)),
                ('date_time', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='complaints',
            fields=[
                ('complaint_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=200)),
                ('date_time', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='crime_types',
            fields=[
                ('crime_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('crime_type_name', models.CharField(max_length=200)),
                ('minimum_penalty', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='criminals',
            fields=[
                ('criminal_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('dob', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='criminals')),
                ('thumb_impression', models.CharField(max_length=200)),
                ('identification_mark_1', models.CharField(max_length=200)),
                ('identification_mark_2', models.CharField(max_length=200)),
                ('house_name', models.CharField(max_length=200)),
                ('father_name', models.CharField(max_length=200)),
                ('place', models.CharField(max_length=200)),
                ('district', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='law_details',
            fields=[
                ('law_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('ipc_code', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('penalty', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('login_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='stations',
            fields=[
                ('station_id', models.AutoField(primary_key=True, serialize=False)),
                ('login_id', models.CharField(max_length=200)),
                ('station_name', models.CharField(max_length=200)),
                ('place', models.CharField(max_length=200)),
                ('district', models.CharField(max_length=200)),
                ('pincode', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('fax_no', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('house_name', models.CharField(max_length=200)),
                ('place', models.CharField(max_length=200)),
                ('pincode', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('login_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.login')),
            ],
        ),
        migrations.CreateModel(
            name='ratings',
            fields=[
                ('rating_id', models.AutoField(primary_key=True, serialize=False)),
                ('client_id', models.CharField(max_length=200)),
                ('rate', models.CharField(max_length=200)),
                ('review', models.CharField(max_length=200)),
                ('date_time', models.CharField(max_length=200)),
                ('adv_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.advocates')),
            ],
        ),
        migrations.CreateModel(
            name='proposals',
            fields=[
                ('proposal_id', models.AutoField(primary_key=True, serialize=False)),
                ('fee', models.CharField(max_length=200)),
                ('date_time', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('adv_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.advocates')),
                ('case_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.cases')),
            ],
        ),
        migrations.CreateModel(
            name='message',
            fields=[
                ('message_id', models.AutoField(primary_key=True, serialize=False)),
                ('message_description', models.CharField(max_length=200)),
                ('reply', models.CharField(max_length=200)),
                ('date_time', models.CharField(max_length=200)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.users')),
            ],
        ),
        migrations.CreateModel(
            name='foundreport',
            fields=[
                ('found_id', models.AutoField(primary_key=True, serialize=False)),
                ('place', models.CharField(max_length=200)),
                ('date_time', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('criminal_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.criminals')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.users')),
            ],
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('feed_id', models.AutoField(primary_key=True, serialize=False)),
                ('feed_description', models.CharField(max_length=200)),
                ('reply', models.CharField(max_length=200)),
                ('date_time', models.CharField(max_length=200)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.users')),
            ],
        ),
        migrations.CreateModel(
            name='evidences',
            fields=[
                ('evidence_id', models.AutoField(primary_key=True, serialize=False)),
                ('file_path', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('date_time', models.CharField(max_length=200)),
                ('complaint_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.complaints')),
            ],
        ),
        migrations.CreateModel(
            name='crimes',
            fields=[
                ('crime_id', models.AutoField(primary_key=True, serialize=False)),
                ('crime_title', models.CharField(max_length=200)),
                ('crime_description', models.CharField(max_length=200)),
                ('date_time_occurred', models.CharField(max_length=200)),
                ('date_time_reported', models.CharField(max_length=200)),
                ('station_id', models.CharField(max_length=200)),
                ('crime_status', models.CharField(max_length=200)),
                ('place', models.CharField(max_length=200)),
                ('district', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=200)),
                ('crime_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.crime_types')),
            ],
        ),
        migrations.AddField(
            model_name='complaints',
            name='station_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.stations'),
        ),
        migrations.AddField(
            model_name='complaints',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.users'),
        ),
        migrations.CreateModel(
            name='client_assigns',
            fields=[
                ('assign_id', models.AutoField(primary_key=True, serialize=False)),
                ('client_id', models.CharField(max_length=200)),
                ('date_time', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('adv_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.advocates')),
                ('case_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.cases')),
            ],
        ),
        migrations.CreateModel(
            name='case_notes',
            fields=[
                ('note_id', models.AutoField(primary_key=True, serialize=False)),
                ('datetime', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('case_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.cases')),
            ],
        ),
        migrations.CreateModel(
            name='case_files',
            fields=[
                ('file_id', models.AutoField(primary_key=True, serialize=False)),
                ('file_title', models.CharField(max_length=200)),
                ('file_path', models.CharField(max_length=200)),
                ('case_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.cases')),
            ],
        ),
        migrations.CreateModel(
            name='case_allocations',
            fields=[
                ('allocation_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_time', models.CharField(max_length=200)),
                ('proposal_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.proposals')),
            ],
        ),
        migrations.AddField(
            model_name='advocates',
            name='login_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.login'),
        ),
    ]
