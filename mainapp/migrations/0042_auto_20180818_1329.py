# Generated by Django 2.1 on 2018-08-18 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0041_auto_20180818_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='rescuecamp',
            name='total_females',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of Females'),
        ),
        migrations.AddField(
            model_name='rescuecamp',
            name='total_infants',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of Infants (<2y)'),
        ),
        migrations.AddField(
            model_name='rescuecamp',
            name='total_males',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of Males'),
        ),
        migrations.AlterField(
            model_name='contributor',
            name='address',
            field=models.TextField(verbose_name='Address - വിലാസം'),
        ),
        migrations.AlterField(
            model_name='contributor',
            name='district',
            field=models.CharField(choices=[('alp', 'Alappuzha - ആലപ്പുഴ'), ('ekm', 'Ernakulam - എറണാകുളം'), ('idk', 'Idukki - ഇടുക്കി'), ('knr', 'Kannur - കണ്ണൂർ'), ('ksr', 'Kasaragod - കാസർഗോഡ്'), ('kol', 'Kollam - കൊല്ലം'), ('ktm', 'Kottayam - കോട്ടയം'), ('koz', 'Kozhikode - കോഴിക്കോട്'), ('mpm', 'Malappuram - മലപ്പുറം'), ('pkd', 'Palakkad - പാലക്കാട്'), ('ptm', 'Pathanamthitta - പത്തനംതിട്ട'), ('tvm', 'Thiruvananthapuram - തിരുവനന്തപുരം'), ('tcr', 'Thrissur - തൃശ്ശൂർ'), ('wnd', 'Wayanad - വയനാട്')], max_length=15, verbose_name='District - ജില്ല'),
        ),
        migrations.AlterField(
            model_name='contributor',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name - പേര്'),
        ),
        migrations.AlterField(
            model_name='contributor',
            name='phone',
            field=models.CharField(max_length=10, verbose_name='Phone - ഫോണ്\u200d നമ്പര്\u200d'),
        ),
        migrations.AlterField(
            model_name='districtmanager',
            name='district',
            field=models.CharField(choices=[('alp', 'Alappuzha - ആലപ്പുഴ'), ('ekm', 'Ernakulam - എറണാകുളം'), ('idk', 'Idukki - ഇടുക്കി'), ('knr', 'Kannur - കണ്ണൂർ'), ('ksr', 'Kasaragod - കാസർഗോഡ്'), ('kol', 'Kollam - കൊല്ലം'), ('ktm', 'Kottayam - കോട്ടയം'), ('koz', 'Kozhikode - കോഴിക്കോട്'), ('mpm', 'Malappuram - മലപ്പുറം'), ('pkd', 'Palakkad - പാലക്കാട്'), ('ptm', 'Pathanamthitta - പത്തനംതിട്ട'), ('tvm', 'Thiruvananthapuram - തിരുവനന്തപുരം'), ('tcr', 'Thrissur - തൃശ്ശൂർ'), ('wnd', 'Wayanad - വയനാട്')], max_length=15, verbose_name='District - ജില്ല'),
        ),
        migrations.AlterField(
            model_name='districtmanager',
            name='email',
            field=models.CharField(max_length=100, verbose_name='Email - ഇമെയിൽ'),
        ),
        migrations.AlterField(
            model_name='districtmanager',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name - പേര്'),
        ),
        migrations.AlterField(
            model_name='districtmanager',
            name='phone',
            field=models.CharField(max_length=11, verbose_name='Phone - ഫോണ്\u200d നമ്പര്\u200d'),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='address',
            field=models.TextField(verbose_name='Address - വിലാസം'),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='area',
            field=models.CharField(choices=[('dcr', 'Doctor'), ('hsv', 'Health Services'), ('elw', 'Electrical Works'), ('mew', 'Mechanical Work'), ('cvw', 'Civil Work'), ('plw', 'Plumbing work'), ('vls', 'Vehicle Support'), ('ckg', 'Cooking'), ('rlo', 'Relief operation'), ('cln', 'Cleaning'), ('bot', 'Boat Service'), ('rck', 'Rock Climbing'), ('oth', 'Other')], max_length=15, verbose_name='Area of volunteering - സന്നദ്ധസേവനം'),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='district',
            field=models.CharField(choices=[('alp', 'Alappuzha - ആലപ്പുഴ'), ('ekm', 'Ernakulam - എറണാകുളം'), ('idk', 'Idukki - ഇടുക്കി'), ('knr', 'Kannur - കണ്ണൂർ'), ('ksr', 'Kasaragod - കാസർഗോഡ്'), ('kol', 'Kollam - കൊല്ലം'), ('ktm', 'Kottayam - കോട്ടയം'), ('koz', 'Kozhikode - കോഴിക്കോട്'), ('mpm', 'Malappuram - മലപ്പുറം'), ('pkd', 'Palakkad - പാലക്കാട്'), ('ptm', 'Pathanamthitta - പത്തനംതിട്ട'), ('tvm', 'Thiruvananthapuram - തിരുവനന്തപുരം'), ('tcr', 'Thrissur - തൃശ്ശൂർ'), ('wnd', 'Wayanad - വയനാട്')], max_length=15, verbose_name='District - ജില്ല'),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name - പേര്'),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='phone',
            field=models.CharField(max_length=10, verbose_name='Phone - ഫോണ്\u200d നമ്പര്\u200d'),
        ),
    ]
