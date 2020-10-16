from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpleFirstApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultiStepFormModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=255)),
                ('lname', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('twitter', models.CharField(max_length=255)),
                ('facebook', models.CharField(max_length=255)),
                ('gplus', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
    ]