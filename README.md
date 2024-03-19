# Проект QR Code Generator

## Описание
Этот проект - это генератор QR-кодов, написанный на Python с использованием библиотек PySide6 и qrcode.

## Установка и настройка

Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:AnatoliiBessmertnyi/qrcode_generator.git
```
```
cd qrcode_generator

```
#### Создать и активировать виртуальное окружение

На Linux
```
python3 -m venv venv
```
```
source venv/bin/activate
```
На Windows:
```
python -m venv venv
```
```
source venv/Scripts/activate
```
#### Установить зависимости:
```
pip install -r requirements.txt
```
#### Для компиляции qrcode_window.py из qrcode_window.ui используйте:
```
pyside6-uic qrcode_window.ui -o qrcode_window.py
```


## Использование

Запустите окно:
```
py main.py
```

Введите текст, который вы хотите преобразовать в QR-код. 
Вы можете изменить цвет фона QR-кода, размер или сохранить файл у себя.


## Используемые технологии

- **Python**: Язык программирования, используемый для написания основного кода приложения.
- **PySide6**: Библиотека Python для создания графического пользовательского интерфейса с использованием Qt Widgets.
- **qrcode**: Библиотека Python для генерации изображений QR-кода.
- **ООП (Объектно-ориентированное программирование)**: Парадигма программирования, используемая для структурирования кода приложения.
- **Qt Designer**: Графический редактор интерфейса для создания файлов .ui, которые затем преобразуются в код Python.

## Автор

[Anatolii Bessmertnyi](https://github.com/AnatoliiBessmertnyi)






