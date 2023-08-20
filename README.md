# Pythom-Project
## Описание проекта **Консольный блокнот на Python**

0. При разработке использован модуль argparse, который  позволяет разбирать аргументы, передаваемые скрипту при его запуске из командной строки, и даёт возможность пользоваться этими аргументами в скрипте _(что значительно упрощает задачу и добавляет удобства в написании кода)_.

1. Класс Note содержит все необходимые поля (идентификатор, заголовок, тело заметки и дату/время создания или последнего изменения заметки).

2. Класс NotesManager содержит список заметок и методы для работы с ними (сохранение, чтение списка заметок и самих заметок, добавление, редактирование и удаление заметок).

3. Заметки сохраняются в файле в формате json (использована библиотека json).

4. Реализован пользовательский интерфейс консольного приложения, которое предлагает пользователю выбрать одну из команд (создать новую заметку, просмотреть список заметок, редактировать заметку и т.д.) и запрашивает необходимые данные для выполнения команды.

5. При выполнении команды программа вызывает соответствующий метод NotesManager для выполнения необходимых операций с заметками.

6. В конце работы программы все изменения сохраняются в файл в формате json.

7. Пример использования:

<code>

python3 ConsoleNote.py create --title="Test note" --body="Text test note"

python3 ConsoleNote.py list

python3 ConsoleNote.py read --id=4

</code>