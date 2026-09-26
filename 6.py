def main():
    while True:
        print("=== ТВОЙ БЛОКНОТ ===")
        print("1. Показать дела")
        print("2. Добавить дело")
        print("0. Выход")
        
        button = input("Нажми кнопку: ")
        
        if button == '1':
            list_tasks()
        elif button == '2':
            add_task()
        elif button == '0':
            print("До встречи!")
            break
        else:
            print("Я не понял такую кнопку.\n")

if __name__ == "__main__":
    main()