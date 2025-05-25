import tkinter as tk
from tkinter import scrolledtext
import socket 
import threading
import random

PORT = 7878
HOST = 'localhost'
COLORS = [
    "#fb4934",  # red
    "#fe8019",  # orange
    "#fabd2f",  # yellow
    "#b8bb26",  # green
    "#8ec07c",  # aqua
    "#83a598",  # blue
    "#d3869b",  # purple
]

GRUVBOX = {
    "bg": "#282828",       
    "fg": "#ebdbb2",     
    "gray": "#928374",    
    "red": "#fb4934",
    "green": "#b8bb26",
    "yellow": "#fabd2f",
    "blue": "#83a598",
    "purple": "#d3869b",
    "aqua": "#8ec07c",
    "orange": "#fe8019",
    "dark_gray": "#3c3836"
}


FONT_SIZE = 12
user_colors = {}

class GUI:
    def __init__(self, root, port, host):
        self.port = port
        self.host = host
        self.color = ""
        self.root = root
        self.root.title("TCP Chat Server") 
        self.root.configure(bg=GRUVBOX['bg'])
        self.root.resizable(False, False);

        self.chat_area = scrolledtext.ScrolledText(
            root, wrap=tk.WORD, state='disabled',
            width=70, height=20,
            bg=GRUVBOX["dark_gray"], fg=GRUVBOX["fg"], insertbackground=GRUVBOX["fg"],
            font=("Consolas", 10),  # or "Fira Code"
            borderwidth=0
        )

        self.chat_area.pack(padx=10, pady=5)

        # Chat's config
        self.chat_area.tag_config("chat", foreground=GRUVBOX['fg'], font=("Fira Code", FONT_SIZE))
        self.chat_area.tag_config("alert", foreground=GRUVBOX['gray'], font=("Fira Code", FONT_SIZE))
        # End

        self.entry = tk.Entry(
            root, width=40,
            bg=GRUVBOX["bg"], fg=GRUVBOX["fg"], insertbackground=GRUVBOX["fg"],
            highlightthickness=1, highlightbackground=GRUVBOX["gray"]
        )
        self.entry.pack(side=tk.LEFT, padx=(10, 0), pady=5)
        # self.entry.bind('<Return>', self.send_message)

        self.send_button = tk.Button(
            root, text="Send",
            command=self.send_message,
            bg=GRUVBOX["blue"], fg=GRUVBOX["bg"],
            activebackground=GRUVBOX["aqua"], activeforeground=GRUVBOX["bg"],
            relief=tk.FLAT, padx=10, pady=2
        )
        self.send_button.pack(side=tk.LEFT, padx=5, pady=5)


        # Connect to socket
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))
        
        message = self.client.recv(1024).decode('ascii')
        # if message.startswith("Color:"):
        #     self.color = message.split(' ')[1]
        #     print("color " + self.color)


        threading.Thread(target=self.receive_message, daemon=True).start();

    def send_message(self):
        message = self.entry.get()

        self.client.send(message.encode('ascii'))

    def receive_message(self):
        while True:
            message = self.client.recv(1024).decode('ascii')
            print(message)

            if "> " in message:
                ip_port, content = message.split(">", 1)
            else:
                ip_port = ""
                content = message

            if ip_port not in user_colors:
                color = random.choice(COLORS)
                user_colors[ip_port] = color
                self.chat_area.tag_config(ip_port, foreground=color, font=("Fira Code", FONT_SIZE, "bold"))

            self.chat_area.configure(state='normal')

            if ip_port == "":
                self.chat_area.insert(tk.END, f"{content}\n", "alert")
            else:
                self.chat_area.insert(tk.END, f"{ip_port}", ip_port)
                self.chat_area.insert(tk.END, f"{content}\n", "chat")
                
            self.chat_area.configure(state='disabled')
            self.chat_area.see(tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    gui = GUI(root, PORT, HOST)
    root.mainloop()