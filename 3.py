def save_tasks(tasks):
    with open(FILE_NAME, 'w', encoding='') as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

def add_task():
    title = input("Напиши задачу: ")
    tasks = load_tasks()
    task_id = len(tasks) + 1
    tasks.append({"id": task_id, "title": title})
    save_tasks(tasks)
    print("Записал!")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("Список пуст.")
        return