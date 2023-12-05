# Generated by Django 3.2.20 on 2023-12-05 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('title', models.CharField(help_text='Лучший дизайнер для вас', max_length=255, verbose_name='Загаловок')),
                ('desc', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Личная информация',
                'verbose_name_plural': 'Личные информации',
            },
        ),
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='about_me/', verbose_name='Фото обо мне')),
                ('title', models.CharField(help_text='Я креативный дизайнер пользовательского интерфейса /UX', max_length=255, verbose_name='Загаловок')),
                ('suptitle', models.CharField(help_text='разработчик, базирующийся в Нью-Йорке.', max_length=255, verbose_name='Подзагаловок')),
                ('desc', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Обо мне',
                'verbose_name_plural': 'Обо мне',
            },
        ),
        migrations.CreateModel(
            name='AboutMeSkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название навыка')),
                ('number', models.IntegerField(help_text='В процентах!', verbose_name='Количество навыка')),
            ],
            options={
                'verbose_name': 'Моё умение',
                'verbose_name_plural': 'Мои умения',
            },
        ),
        migrations.AlterField(
            model_name='settings',
            name='logo',
            field=models.ImageField(help_text='Рекомендуемый размер 120x40px', upload_to='logo', verbose_name='Логотип сайта'),
        ),
    ]
