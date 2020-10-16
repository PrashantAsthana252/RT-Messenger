from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simpleFirstApp', '0004_auto_20200814_1653'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductImages',
        ),
        migrations.DeleteModel(
            name='Products',
        ),
    ]