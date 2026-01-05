# Google Gemini screen capture with voiceover of the main text

Инструмент для автоматического захвата экрана, распознавания текста с помощью Google Gemini API и озвучивания текста (Text-to-Speech) для игры "Космические рейнджеры 2".

## Описание

Данное приложение помогает читать текстовые квесты:
*   Захватывает экран по горячей клавише (**Ctrl + L**).
*   Извлекает текст квеста через Gemini AI (игнорируя интерфейс).
*   Читает текст вслух с ускорением (x1.5).

## Установка и запуск

### Вариант 1: Запуск скрипта (Python)

1.  Установите Python 3.8+.
2.  Установите зависимости: `pip install -r requirements.txt`.
3.  Запустите: `python main.py`.
4.  Введите ваш API ключ Gemini при запуске.

### Вариант 2: Запуск .exe

1.  Скачайте или скомпилируйте `SR2_Reader.exe`.
2.  Запустите файл.
3.  Введите API ключ в консоли.

## Компиляция (для разработчиков)

Для создания `.exe` файла используйте PyInstaller:

```bash
pyinstaller --onefile --version-file=version.txt --icon=i64.ico --name "SR2_Reader" --add-data "capture.py;." --add-data "ai_service.py;." --add-data "tts_service.py;." main.py
```

## Управление

*   **Ctrl + L**: Прочитать текст с экрана.
*   **Ctrl + Shift + Q**: Выход.
