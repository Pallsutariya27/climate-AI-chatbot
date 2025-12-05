import customtkinter as ctk
from chatbot import climate_chatbot

# ------------------------------------------
# UI THEME
# ------------------------------------------
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.title("Climate Action AI Chatbot")
app.geometry("920x650")
app.configure(fg_color="#e3e7eb")  # Soft grey background

# ------------------------------------------
# SHADOW BELOW CARD (Fake blur)
# ------------------------------------------
shadow = ctk.CTkFrame(
    app,
    width=780,
    height=500,
    corner_radius=25,
    fg_color="#c9d0d6"   # soft grey (shadow)
)
shadow.place(relx=0.5, rely=0.455, anchor="center")

# ------------------------------------------
# MAIN CARD (Glass-Like)
# ------------------------------------------
card_frame = ctk.CTkFrame(
    app,
    width=780,
    height=500,
    corner_radius=25,
    fg_color="#f8f9fa"     # light white-grey (glass effect)
)
card_frame.place(relx=0.5, rely=0.45, anchor="center")

# ------------------------------------------
# TITLE
# ------------------------------------------
title = ctk.CTkLabel(
    app,
    text="🍃 Climate Action AI Chatbot",
    font=("Arial Rounded MT Bold", 30),
    text_color="#2e4d36"
)
title.pack(pady=25)

# ------------------------------------------
# CHAT BOX (Inside Card)
# ------------------------------------------
chat_box = ctk.CTkTextbox(
    card_frame,
    width=740,
    height=430,
    corner_radius=20,
    fg_color="#ffffff",      # pure white
    text_color="black",
    font=("Segoe UI", 14),
    wrap="word"
)
chat_box.place(relx=0.5, rely=0.5, anchor="center")

chat_box.insert("end", "🌱 Welcome! Ask anything about climate science.\n\n")
chat_box.configure(state="disabled")

# ------------------------------------------
# INPUT BAR (Fake glass)
# ------------------------------------------
input_container = ctk.CTkFrame(
    app,
    fg_color="#f7f7f7",   # soft white-grey (simulates matte glass)
    corner_radius=20,
)
input_container.place(relx=0.5, rely=0.87, anchor="center")

# Input Box
input_entry = ctk.CTkEntry(
    input_container,
    width=600,
    height=45,
    placeholder_text="Ask a climate-related question...",
    corner_radius=15,
    font=("Segoe UI", 14)
)
input_entry.grid(row=0, column=0, padx=10, pady=10)

# ------------------------------------------
# SEND MESSAGE
# ------------------------------------------
def send_message():
    user_text = input_entry.get().strip()
    if user_text == "":
        return

    chat_box.configure(state="normal")
    chat_box.insert("end", f"🧑‍💬 You: {user_text}\n\n")
    chat_box.configure(state="disabled")
    input_entry.delete(0, "end")
    chat_box.see("end")

    ai_answer = climate_chatbot(user_text)

    chat_box.configure(state="normal")
    chat_box.insert("end", f"🤖 AI: {ai_answer}\n\n")
    chat_box.configure(state="disabled")
    chat_box.see("end")

# Ask Button
ask_button = ctk.CTkButton(
    input_container,
    text="Ask",
    width=140,
    height=45,
    corner_radius=15,
    font=("Segoe UI", 15, "bold"),
    fg_color="#31c46d",
    hover_color="#28a65b",
    command=send_message
)
ask_button.grid(row=0, column=1, padx=10)

app.mainloop()
