print("--- Todo list ---")

with open("todo-list.txt", "r", encoding="utf-8") as f:
    todo_list = f.read().split("- ")
    todo_list = [todo for todo in todo_list if len(todo) > 0]
    todo_list = [todo.replace("\n", "") for todo in todo_list]

while True:
    for todo in todo_list:
        print(f"- {todo}")
    print('Write a new todo to add it to the list, or write "exit" to exit')
    user_input = input("> ")

    if user_input != "exit":
        todo_list.append(user_input)
    else:
        break

print("Saving and quitting...")

with open("todo-list.txt", "w", encoding="utf-8") as f:
    text = [f"- {todo}" for todo in todo_list]
    f.write("\n".join(text))
