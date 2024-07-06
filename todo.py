import flet as ft

class ToDoApp(ft.Column):
    def __init__(self):
        super().__init__()
        self.newTask = ft.TextField(hint_text="What's needs to be done?", expand=True)
        self.allTasks = ft.Column()
        self.width=600 
        self.controls=[
            ft.Row(
                controls=[
                    self.newTask, 
                    ft.FloatingActionButton(icon=ft.icons.ADD, on_click=self.add_clicked),
                ],
            ),
            self.allTasks,
        ]    

    def add_clicked(self, e):
        self.allTasks.controls.append(ft.Checkbox(label=self.newTask.value))
        self.newTask.value = ""
        self.view.update()  

def main(page: ft.Page):
    
    page.title = "To Do App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    todo = ToDoApp()

    page.add(todo)

if __name__ == "__main__":
    ft.app(target=main)
