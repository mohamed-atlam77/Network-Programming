import tkinter as tk
import socket

class GuessGame:
    def __init__(self, master):
        self.master = master
        self.server_address = ('localhost', 8000)

        self.create_widgets()

    def create_widgets(self):
        self.message_label = tk.Label(self.master, text="Choose apple, banana, or grape:")
        self.message_label.pack()

        self.choice_frame = tk.Frame(self.master)
        self.choice_frame.pack()

        self.grape_button = tk.Button(self.choice_frame, text="Grape", command=lambda: self.send_choice("grape"))
        self.grape_button.pack(side=tk.LEFT)

        self.banana_button = tk.Button(self.choice_frame, text="Banana", command=lambda: self.send_choice("banana"))
        self.banana_button.pack(side=tk.LEFT)

        self.apple_button = tk.Button(self.choice_frame, text="Apple", command=lambda: self.send_choice("apple"))
        self.apple_button.pack(side=tk.LEFT)

        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack()

    def send_choice(self,choice):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect(self.server_address)
            sock.sendall(choice.encode())
            data = sock.recv(1024).decode()

        self.result_label.configure(text=data)

    def reset_game(self):
        self.result_label.configure(text="")


root = tk.Tk()
root.title("Guess Game")
root.geometry('300x200')
game = GuessGame(root)
root.mainloop()