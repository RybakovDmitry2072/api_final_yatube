### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```shell
git clone https://github.com/KurmaevAmir/api_final_yatube.git
```

```shell
cd api_final_yatube_broke
```

Создать и активировать виртуальное окружение:

```shell
python3 -m venv venv
```

```shell
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:
```shell
pip install --upgrade pip
```

```shell
pip install -r requirements.txt
```

Выполнить миграции:
```shell
cd yatube_api
```

```shell
python3 manage.py migrate
```

Запустить проект
```shell
python3 manage.py runserver
```