# faq_gui.py
import tkinter as tk
from faq_file import get_response

# Function triggered on button click
def send_message():
    user_input = entry.get()
    if not user_input.strip():
        return
    response = get_response(user_input)

    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, f"You: {user_input}\n")
    chat_log.insert(tk.END, f"Bot: {response}\n\n")
    chat_log.config(state=tk.DISABLED)
    entry.delete(0, tk.END)

# Initialize main window
window = tk.Tk()
window.title("Handmade Goods FAQ Chatbot")

# Chat display
chat_log = tk.Text(window, height=20, width=60, state=tk.DISABLED, wrap=tk.WORD)
chat_log.pack(padx=10, pady=10)

# Input area
entry_frame = tk.Frame(window)
entry = tk.Entry(entry_frame, width=50)
entry.pack(side=tk.LEFT, padx=5)
send_button = tk.Button(entry_frame, text="Send", command=send_message)
send_button.pack(side=tk.LEFT)
entry_frame.pack(pady=10)

# Start GUI loop
window.mainloop()
