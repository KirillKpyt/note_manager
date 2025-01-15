
note = {}
note["username"] = input("Введите имя пользователя: ")
note["content"] = input("Введите описание заметки: ")
note["status"] = input("Введите статус заметки (например, 'Активна', 'Выполнена'): ")
note["created_date"] = input("Введите дату создания заметки в формате 'день-месяц-год': ")
note["issue_date"] = input("Введите дату истечения заметки в формате 'день-месяц-год': ")


note["titles"] = []
for i in range(3):
    title = input(f"Введите заготовок заметки {i + 1}: ")
    note["titles"].append(title)


print("Собранная информация о заметке:")
print("Имя пользователя:", note["username"])
print("Заголовки заметки:", note["titles"])
print("Описание заметки:", note["content"])
print("Статус заметки:", note["status"])
print("Дата создания заметки:", note["created_date"][0:5])
print("Дата истечения заметки:", note["issue_date"][0:5])
