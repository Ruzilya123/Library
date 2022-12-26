# Generated by Django 4.1.4 on 2022-12-26 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LibraryApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('communication', models.CharField(max_length=50)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LibraryApp.book')),
            ],
        ),
    ]