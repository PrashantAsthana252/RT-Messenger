from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpleFirstApp', '0003_productimages_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimages',
            name='product_img',
            field=models.FileField(max_length=255, upload_to=''),
        ),
    ]