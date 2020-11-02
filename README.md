Згідно свого варіанту мені треба було встановити Python 3.6 і Venv.
Встановлювавлось все на ОС Linux Ubuntu.

Встановлення **Pyenv**.
1) **apt update -y**    запустив з правами root для оновлення всіх системних компонент.

2)  **apt install -y make build-essential libssl-dev zlib1g-dev  \
     libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
     libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl \
     git**          встановлення залежностей pyenv

3) **git clone https://github.com/pyenv/pyenv.git ~/.pyenv** 
  клоную гіт репозиторій для встановлення  останньої версії pyenv
4)
**echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc \
  echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc \ 
  echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.bashrc**
   
   прописую стандартний шлях до pyenv

5) **pyenv install --list**
  з'явився список версій Python , серед якого обираю Python 3.6.0
  **pyenv install python 3.6.0**

6) pyenv global 3.6.0 #глобально змінюю версію Python




Встановлення   **venv**.
1) **sudo apt install -y python3-pip**       встановлення необхідних пакетів

2) **sudo apt install -y python3-venv**          встановлення самого venv

3)   **python3 -m venv test_env  
     **source test_env/bin/activate
     створення віртуального середовища і його активація 




Встановлення **Flask** i **Gunicorn**


1)   Можна встановити вручну:
    **pip install flask
    pip install gunicorn**

  або:
    Створити файл requirements.txt 
    і прописати наступне :

    Flask == 1.1.2
    gunicorn == 20.0.4

    Закрити файл і встановити за допомогою.

    pip freeze > requirements.txt 
    pip install -r requirements.txt





     
     

Створення самого API у **Pycharm**

1) створюю новий проект, обираю віртуальне середовище, яке я запустив раніше(з версією Python 3.6, яку і треба використовувати)

2) Код програми:

            from flask import Flask

            app = Flask(name)


            @app.route("/")
            def hello():
              return "hello"


            @app.route("/api/v1/hello-world-<int:post_id>")
            def hello_world(post_id):
              return "Hello World! %d" % post_id


            if name == "main":
              app.run()

  Запускати можна стандартно, а можна через команду 
  
   **gunicorn --bind 0.0.0.0:5000 main:app**

  Для перевірки чи є відгук на запит в терміналі можна використати 
  
   curl -v -XGET http://localhost:5000/api/v1/hello-world-3

   Якщо відповідь по запиту  200 , то сторінка існує, і може бути відкритою.


Закидую все у гітхаб.

     git init
     git add .
     git commit -m "first_lab_commit"
     git remote add origin https://github.com/no-code-no-life/PP
     git push -u origin master

