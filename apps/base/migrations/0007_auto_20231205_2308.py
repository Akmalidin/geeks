# Generated by Django 3.2.20 on 2023-12-05 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20231205_2250'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(verbose_name='Отзыв')),
                ('image', models.ImageField(upload_to='reviews/', verbose_name='Фото автора')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('work', models.CharField(max_length=255, verbose_name='Профессия')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='category',
            field=models.CharField(choices=[('branding', 'Брендинг'), ('design', 'Дизайн'), ('wordpress', 'WordPress'), ('marketing', 'Маркетинг')], help_text='Выберите категорию', max_length=255, verbose_name='Выберите категорию'),
        ),
    ]
