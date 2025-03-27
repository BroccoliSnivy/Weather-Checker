import ttkbootstrap as tb
from tkinter import StringVar, messagebox
import threading
import random

class WeatherCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Checker")
        self.root.geometry("400x200")
        self.root.resizable(False, False)

        self.root.iconbitmap("resources/app_icon.ico")

        self.location_var = StringVar()
        
        tb.Label(root, text="Enter your location:", font=("Arial", 12)).pack(pady=10)
        self.entry = tb.Entry(root, textvariable=self.location_var, width=30)
        self.entry.pack(pady=5)
        
        self.check_button = tb.Button(root, text="Check Weather", command=self.check_weather, bootstyle="info")
        self.check_button.pack(pady=10)
        
        self.status_label = tb.Label(root, text="", font=("Arial", 10))
        self.progress = tb.Progressbar(root, mode='determinate', length=250, bootstyle='danger')
        
        self.fake_statuses = [
            "Fetching data...",
            "Reaching the location server...",
            "Calibrating satellite sensors...",
            "Decrypting meteorological data...",
            "Consulting the weather gods...",
            "Verifying atmospheric pressure..."
        ]
        
        self.troll_messages = [
            "Lmao just look outside bro.",
            "I dunno man, just look outside or something.",
            "Google it, I ain't got time for this.",
            "Probably sunny, probably not. Who knows?", 
            "Just step outside and feel the vibes, dude.",
            "I'm not your weather app, use your eyes.",
            "Might be raining, might be snowing, might be neither. Figure it out.",
            "Bruh, it's called looking. Use your vision." 
        ]
        
    def check_weather(self):
        location = self.location_var.get().strip()
        if not location:
            messagebox.showerror("Error", "Bro, at least type something.")
            return
        
        self.check_button.config(state='disabled', text="Checking...")
        self.status_label.pack(pady=5)
        self.progress.pack(pady=10)
        self.progress['value'] = 0
        
        threading.Thread(target=self.fake_loading, daemon=True).start()
        
    def fake_loading(self):
        for i in range(1, 11):
            self.root.after(i * 400, lambda val=i * 10: self.update_progress(val))
        
        self.root.after(4500, self.show_result)
        
    def update_progress(self, value):
        self.progress['value'] = value
        self.status_label.config(text=random.choice(self.fake_statuses))
        
    def show_result(self):
        self.progress.pack_forget()
        self.status_label.pack_forget()
        self.show_custom_message()
        self.check_button.config(state='normal', text="Check Weather")
    
    def show_custom_message(self):
        top = tb.Toplevel(self.root)
        top.title("Weather Report")
        top.iconbitmap("resources/app_icon.ico")  # Set custom icon
        top.geometry("350x150")
        top.resizable(False, False)

        tb.Label(top, text=random.choice(self.troll_messages), font=("Arial", 12), wraplength=250, justify="center").pack(pady=20)
        tb.Button(top, text="OK", command=top.destroy, bootstyle="primary").pack(pady=10)

        top.transient(self.root)  # Keep it on top of the main window
        top.grab_set()  # Make it modal
        self.root.wait_window(top)  # Pause main window until closed


if __name__ == "__main__":
    root = tb.Window(themename="cyborg")  # Cyberpunk theme
    app = WeatherCheckerApp(root)
    root.mainloop()
