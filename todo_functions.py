import csv

def add_todo(file_name):
    print("Add todo")
    # Ask the title of the todo
    todo_name = input("Enter a todo: ")
    # Open file - list.csv
    with open(file_name, "a") as f:
        writer = csv.writer(f)
        # Insert values - title = user entered
                      # - completed = False
        writer.writerow([todo_name, "False"])

def remove_todo(file_name):
    print("Remove todo")
    todo_name = input("Enter a todo you want to remove: ")
    # Copy all the contents of the csv into a new csv
    # While doing this, we constantly check for the condition
    # When we encounter the todo to be removed, we don't copy that one
    # The final new todo will be written into a new csv file
    todo_lists = []
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if (todo_name != row[0]):
                todo_lists.append(row)
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(todo_lists)
    

def mark_todo(file_name):
    print("Mark todo")
    todo_name = input("Enter the todo name that you want to mark as complete: ")
    todo_lists = []
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if (todo_name != row[0]):
                todo_lists.append(row)
            else:
                todo_lists.append([row[0], "True"])
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(todo_lists)

def view_todo(file_name):
    print("View todo")
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        reader.__next__()
        for row in reader:
            # row = ["Todo 1", "False"]
            if (row[1] == "True"):
                print(f"Todo {row[0]} is complete")
            else:
                print(f"Todo {row[0]} is not complete")