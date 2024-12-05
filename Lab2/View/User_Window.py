# User_Window.py
import tkinter as tk
from tkinter import messagebox, ttk
import datetime


class UserWindow(tk.Toplevel):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.title("User Dashboard")
        self.geometry("700x800")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # Обработчик закрытия окна

        self.create_widgets()

        self.arrival_time = None
        self.departure_time = None
        self.break_times = []
        self.work_start_time = None
        self.work_timer_running = False
        self.break_start_time = None

    def create_widgets(self):
        tk.Label(self, text="User Dashboard", font=("Arial", 20)).pack(pady=20)

        self.info_frame = tk.Frame(self)
        self.info_frame.pack(pady=10)

        tk.Label(self.info_frame, text="ID:", font=("Arial", 14)).grid(row=0, column=0, sticky='e')
        self.id_label = tk.Label(self.info_frame, text="123456", font=("Arial", 14))
        self.id_label.grid(row=0, column=1, sticky='w')

        tk.Label(self.info_frame, text="Arrival Time:", font=("Arial", 14)).grid(row=1, column=0, sticky='e')
        self.arrival_time_label = tk.Label(self.info_frame, text="Not Recorded", font=("Arial", 14))
        self.arrival_time_label.grid(row=1, column=1, sticky='w')

        tk.Label(self.info_frame, text="Departure Time:", font=("Arial", 14)).grid(row=2, column=0, sticky='e')
        self.departure_time_label = tk.Label(self.info_frame, text="Not Recorded", font=("Arial", 14))
        self.departure_time_label.grid(row=2, column=1, sticky='w')

        tk.Label(self.info_frame, text="Total Time Worked:", font=("Arial", 14)).grid(row=3, column=0, sticky='e')
        self.total_worked_time_label = tk.Label(self.info_frame, text="00:00:00", font=("Arial", 14))
        self.total_worked_time_label.grid(row=3, column=1, sticky='w')

        self.break_frame = tk.Frame(self)
        self.break_frame.pack(pady=10)

        self.break_table = ttk.Treeview(self.break_frame, columns=("start", "end"), show='headings')
        self.break_table.heading("start", text="Break Start")
        self.break_table.heading("end", text="Break End")
        self.break_table.pack()

        tk.Button(self, text="Record Arrival", font=("Arial", 14), command=self.record_arrival).pack(pady=10)
        tk.Button(self, text="Record Departure", font=("Arial", 14), command=self.record_departure).pack(pady=10)
        tk.Button(self, text="Start Break", font=("Arial", 14), command=self.start_break).pack(pady=10)
        tk.Button(self, text="End Break", font=("Arial", 14), command=self.end_break).pack(pady=10)
        tk.Button(self, text="Logout", font=("Arial", 14), bg="red", command=self.logout).pack(pady=20)

    def record_arrival(self):
        if self.arrival_time is None:
            self.arrival_time = datetime.datetime.now()
            self.arrival_time_label.config(text=self.arrival_time.strftime("%H:%M:%S"))
            self.work_start_time = self.arrival_time
            self.start_work_timer()
            messagebox.showinfo("Arrival", "Arrival time recorded successfully.")
        else:
            messagebox.showwarning("Warning", "Arrival time has already been recorded.")

    def record_departure(self):
        if self.arrival_time is None:
            messagebox.showerror("Error", "Arrival time is not recorded.")
        elif self.departure_time is None:
            self.departure_time = datetime.datetime.now()
            self.departure_time_label.config(text=self.departure_time.strftime("%H:%M:%S"))
            self.stop_work_timer()
            messagebox.showinfo("Departure", "Departure time recorded successfully.")
        else:
            messagebox.showwarning("Warning", "Departure time has already been recorded.")

    def start_work_timer(self):
        if not self.work_timer_running:
            self.work_timer_running = True
            self.update_work_timer()

    def stop_work_timer(self):
        self.work_timer_running = False

    def update_work_timer(self):
        if self.work_timer_running:
            now = datetime.datetime.now()
            worked_seconds = (now - self.work_start_time).total_seconds()
            for break_time in self.break_times:
                if "end" in break_time:
                    worked_seconds -= (break_time["end"] - break_time["start"]).total_seconds()
            hours, remainder = divmod(worked_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            self.total_worked_time_label.config(text=f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}")
            self.after(1000, self.update_work_timer)

    def start_break(self):
        if self.work_timer_running:
            self.break_start_time = datetime.datetime.now()
            self.work_timer_running = False
            self.break_times.append({"start": self.break_start_time})
            messagebox.showinfo("Break", "Break started successfully.")
        else:
            messagebox.showwarning("Warning", "Cannot start break without starting work timer.")

    def end_break(self):
        if not self.work_timer_running and self.break_start_time:
            break_end_time = datetime.datetime.now()
            self.break_times[-1]["end"] = break_end_time
            self.break_table.insert('', 'end', values=(
            self.break_start_time.strftime("%H:%M:%S"), break_end_time.strftime("%H:%M:%S")))
            self.work_start_time += (break_end_time - self.break_start_time)
            self.break_start_time = None
            self.start_work_timer()
            messagebox.showinfo("Break", "Break ended successfully.")
        else:
            messagebox.showwarning("Warning", "No break in progress to end.")

    def logout(self):
        self.controller.logout()

    def on_closing(self):
        self.controller.on_closing()


if __name__ == "__main__":
    root = tk.Tk()
    app = UserWindow(master=root, controller=None)
    app.mainloop()
