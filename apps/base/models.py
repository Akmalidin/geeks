from django.db import models

# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    desc = models.TextField(
        verbose_name='Описание сайта'
    )
    logo = models.ImageField(
        upload_to='logo',
        verbose_name='Логотип сайта',
        help_text='Рекомендуемый размер 120x40px'
    )
    email = models.EmailField(
        verbose_name='Email: ',
        blank=True
    )
    phone = models.CharField(
        max_length=13,
        verbose_name='Телефон: ',
        blank=True
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'

class About(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Имя'
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Загаловок',
        help_text='Лучший дизайнер для вас'
    )
    desc = models.TextField(
        verbose_name='Описание'
    )
    def __str__(self):
        return f'{self.name} - {self.title}'
    class Meta:
        verbose_name='Личная информация'
        verbose_name_plural='Личные информации'

class AboutMe(models.Model):
    image = models.ImageField(
        upload_to='about_me/',
        verbose_name='Фото обо мне',
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Загаловок',
        help_text='Я креативный дизайнер пользовательского интерфейса /UX'
    )
    suptitle = models.CharField(
        max_length=255,
        verbose_name='Подзагаловок',
        help_text='разработчик, базирующийся в Нью-Йорке.'
    )
    desc = models.TextField(
        verbose_name='Описание'
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Обо мне'
        verbose_name_plural='Обо мне'
class AboutMeSkills(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название навыка'
    )
    number = models.IntegerField(
        verbose_name='Количество навыка',
        help_text='В процентах!'
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Моё умение'
        verbose_name_plural='Мои умения'

class Services(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название услуги'
    )
    suptitle = models.CharField(
        max_length=60,
        verbose_name='Описание',
        help_text='Желательно 55 символов.'
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Услуга'
        verbose_name_plural='Услуги'
class Happy_Clients(models.Model):
    number = models.IntegerField(
        verbose_name='Количество успехов',
        help_text='В цифрах!'
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Название успеха',
        help_text='Успешные Проекты'
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Успех'
        verbose_name_plural='Успехи'
class Portfolio(models.Model):
    image = models.ImageField(
        upload_to='portfolio/',
        verbose_name='Фото портфолио',
    )
    CATEGORIES = (
        ('branding', 'Брендинг'),
        ('design', 'Дизайн'),
        ('wordpress', 'WordPress'),
        ('marketing', 'Маркетинг')
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Название портфолио'
    )
    category = models.CharField(
        max_length=255,
        choices=CATEGORIES,
        help_text='Выберите категорию',
        verbose_name='Выберите категорию'
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Портфолио'
        verbose_name_plural='Портфолио'
class Reviews(models.Model):
    review = models.TextField(
        verbose_name='Отзыв'
    )
    image = models.ImageField(
        upload_to='reviews/',
        verbose_name='Фото автора'
    )
    name = models.CharField(
        max_length=255,
        verbose_name='Имя'
    )
    work = models.CharField(
        max_length=255,
        verbose_name='Профессия'
    )
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Отзыв'
        verbose_name_plural='Отзывы'

class Contact(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name = 'Имя'
    )
    email = models.EmailField(
        verbose_name='Почта'
    )
    message = models.TextField(verbose_name = 'Сообщение')
    def __str__(self):
        return f"{self.name} -- {self.email}"
    class Meta:
        verbose_name = 'Обратная связь',
        verbose_name_plural = 'Обратная связь'