import tkinter as tk

class ReportDetailWindow(tk.Toplevel):
    def __init__(self, master, report_id, report_title, report_body):
        super().__init__(master)
        self.title(f"{report_title}")  # Устанавливаем заголовок окна как название отчета
        self.geometry("800x600")  # Увеличим размер окна

        self.create_widgets(report_title, report_body)

    def create_widgets(self, report_title, report_body):
        tk.Label(self, text=report_title, font=("Arial", 20)).pack(pady=20)
        tk.Label(self, text=report_body, font=("Arial", 14), wraplength=750).pack(pady=20)

        tk.Button(self, text="Back", font=("Arial", 14), command=self.destroy).pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = ReportDetailWindow(master=root, report_id=1, report_title="Sample Title", report_body="Sample Body")
    app.mainloop()
