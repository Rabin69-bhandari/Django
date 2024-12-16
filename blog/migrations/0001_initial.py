# Generated by Django 5.1.3 on 2024-12-14 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('head0', models.CharField(max_length=500)),
                ('head1', models.CharField(max_length=500)),
                ('head2', models.CharField(max_length=500)),
                ('thumbnail', models.ImageField(upload_to='blog/images')),
            ],
        ),
    ]