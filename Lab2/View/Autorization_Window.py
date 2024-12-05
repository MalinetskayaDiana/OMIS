# Autorization_Window.py
import tkinter as tk
from tkinter import messagebox

class AuthorizationWindow(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Authorization")
        self.geometry("500x300")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # Обработчик закрытия окна

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="AUTORIZATION", font=("Arial", 20)).pack(pady=20)

        self.info_frame = tk.Frame(self)
        self.info_frame.pack(pady=10)

        tk.Label(self.info_frame, text="Login:", font=("Arial", 14)).grid(row=0, column=0, pady=5)
        self.login_entry = tk.Entry(self.info_frame, font=("Arial", 14), width=25)
        self.login_entry.grid(row=0, column=1, pady=5)

        tk.Label(self.info_frame, text="Password:", font=("Arial", 14)).grid(row=1, column=0, pady=5)
        self.password_entry = tk.Entry(self.info_frame, show="*", font=("Arial", 14), width=25)
        self.password_entry.grid(row=1, column=1, pady=5)

        tk.Button(self.info_frame, text="Log In", bg="green", font=("Arial", 14), command=self.login).grid(row=2, columnspan=2, pady=20)

    def login(self):
        login = self.login_entry.get()
        password = self.password_entry.get()
        self.controller.login(login, password)

    def on_closing(self):
        self.controller.on_closing()

if __name__ == "__main__":
    root = tk.Tk()
    app = AuthorizationWindow(master=root, controller=None)
    app.mainloop()
