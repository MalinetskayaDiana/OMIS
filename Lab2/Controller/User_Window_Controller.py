class UserWindowController:
    def __init__(self, user_window):
        self.user_window = user_window

    def record_arrival(self):
        self.user_window.record_arrival()

    def record_departure(self):
        self.user_window.record_departure()

    def start_break(self):
        self.user_window.start_break()

    def end_break(self):
        self.user_window.end_break()

    def logout(self):
        self.user_window.logout()

    def on_closing(self):
        self.user_window.on_closing()
