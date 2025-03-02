# Generated by Django 5.1.4 on 2025-01-15 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Painting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('dimensions', models.CharField(max_length=100)),
                ('canvas_size', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='paintings/')),
                ('category', models.CharField(choices=[('Bookmark', 'Bookmark'), ('Landscape', 'Landscape'), ('Portrait', 'Portrait')], default='Bookmark', max_length=10)),
                ('faces', models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3')], null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('released_date', models.DateField()),
            ],
        ),
    ]
