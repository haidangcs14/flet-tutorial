import flet as ft

class Task(ft.Column):
    def __init__(self, taskName, taskDelete):
        super().__init__()
        self.taskName = taskName
        self.taskDelete = taskDelete
        self.displayTask = ft.Checkbox(value=False, label=self.taskName)
        self.editName = ft.TextField(expand=1)

        self.displayView = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER, 
            controls=[
                self.displayTask,
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.CREATE_OUTLINED,
                            tooltip="Edit",
                            on_click=self.edit_clicked,
                        ),
                        
                        ft.IconButton(
                            icon=ft.icons.DELETE,
                            tooltip="Delete",
                            on_click=self.delete_clicked,
                        ),
                    ],
                )
            ],
        )

        self.editView = ft.Row(
            visible=False,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.editName,
                ft.IconButton(
                    icon=ft.icons.DONE_OUTLINE_OUTLINED,
                    icon_color = ft.colors.GREEN,
                    tooltip="Update",
                    on_click=self.update_clicked,
                ),
            ],
        )

        self.controls = [self.displayView, self.editView]
    
    def edit_clicked(self, e):
        self.editName.value = self.displayTask.label
        self.displayView.visible = False
        self.editView.visible = True
        self.update()

    def update_clicked(self, e):
        self.displayTask.label = self.editName.value
        self.displayView.visible = True
        self.editView.visible = False
        self.update()

    def delete_clicked(self, e):
        self.taskDelete(self)

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
        task = Task(self.newTask.value, self.task_delete)
        self.allTasks.controls.append(task)
        self.newTask.value = ""
        self.update()

    def task_delete(self, task):
        self.allTasks.controls.remove(task)
        self.update()

def main(page: ft.Page):
    
    page.title = "To Do App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    todo = ToDoApp()

    page.add(todo)

if __name__ == "__main__":
    ft.app(target=main)
