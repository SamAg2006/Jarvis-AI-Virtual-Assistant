import tkinter as tk
from commands import processcommand
import speech_recognition as sr
recognizer = sr.Recognizer()


def listen():
    try:
        with sr.Microphone() as source:
            chat.insert(tk.END, "Jarvis: Listening...\n")

            recognizer.adjust_for_ambient_noise(source, duration=1)

            audio = recognizer.listen(source)

            command = recognizer.recognize_google(audio)

            # show what user said
            entry.delete(0, tk.END)
            entry.insert(0, command)

            # automatically send
            send()

    except sr.UnknownValueError:
        chat.insert(tk.END, "Jarvis: Could not understand audio\n")

    except Exception as e:
        chat.insert(tk.END, f"Error: {e}\n")




def send():
    user_input = entry.get()

    if user_input.strip() == "":
        return

    chat.insert(tk.END, "You: " + user_input + "\n")

    response = processcommand(user_input, speak_output=False)

    chat.insert(tk.END, "Jarvis: " + response + "\n\n")

    entry.delete(0, tk.END)

    # auto scroll
    chat.see(tk.END)

root = tk.Tk()
root.title("Jarvis AI Assistant")
root.geometry("500x600")

chat = tk.Text(root, wrap=tk.WORD, font=("Arial", 12))
chat.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(padx=10, pady=5, fill=tk.X)

send_btn = tk.Button(root, text="Send", command=send)
send_btn.pack(pady=5)

mic_btn = tk.Button(root, text="🎤 Speak", command=listen)
mic_btn.pack(pady=5)

root.mainloop()

















