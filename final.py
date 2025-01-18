

username = input("Введите имя пользователя: ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки (например, 'Активна', 'Выполнена'): ")
created_date = input("Введите дату создания заметки в формате 'день-месяц-год': ")
issue_date = input("Введите дату истечения заметки в формате 'день-месяц-год': ")


title = input("Введите первый заголовок заметки: ")
title2 = input("Введите второй заголовок заметки: ")
title3 = input("Введите третий заголовок заметки: ")
titles = [title, title2, title3]

note = [
    username,
    titles,
    content,
    status,
    created_date[0:5],
    issue_date[0:5]
    ]
print(note)


