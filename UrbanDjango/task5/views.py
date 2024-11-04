from django.shortcuts import render
from  .forms import UserRegister

users = (
    'Иван',
    'Андрей',
    'Алевтина'
)


# Create your views here.
def sign_up_by_html(request):
    info = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        age = request.POST.get('age')

        # Преобразуем возраст в целое число
        try:
            age = int(age)
        except ValueError:
            info['error'] = f'Возраст должен быть числом'
            return render(request, 'fifth_task/registration_page.html', info)

        if username in users:
            info['error'] = f'Пользователь уже существует'
        elif password != password1:
            info['error'] = f'Пароли не совпадают'
        elif age < 18:
            info['error'] = f'Вы должны быть старше 18'
        else:
            info['success'] = f'Регистрация прошла успешно! Добро пожаловать, {username}!'
            return render(request, 'fifth_task/registration_page.html', info)
    print(f'info', info)
    return render(request, 'fifth_task/registration_page.html', info)


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password1 = form.cleaned_data['password1']
            age = form.cleaned_data['age']
            if username in users:
                info['error'] = f'Пользователь уже существует'
            elif password != password1:
                info['error'] = f'Пароли не совпадают'
            elif age < 18:
                info['error'] = f'Вы должны быть старше 18'
            else:
                info['success'] = f'Регистрация прошла успешно! Добро пожаловать, {username}!'

        else:
            form = UserRegister()
    print(f'info', info)

    return render(request, 'fifth_task/registration_page.html', info)
    
        