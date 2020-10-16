from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('simpleFirstApp', '0005_auto_20200814_1747'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.FileField(max_length=255, upload_to='')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simpleFirstApp.Products')),
            ],
        ),
    ]