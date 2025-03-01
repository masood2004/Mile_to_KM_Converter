from tkinter import *
from tkinter import font


def miles_to_km():
    try:
        miles = float(miles_input.get())
        km = miles * 1.609
        kilometer_result_label.config(text=f"{km:.2f}", fg="#2E86C1")
    except ValueError:
        kilometer_result_label.config(text="Invalid input!", fg="#E74C3C")


# Window setup
window = Tk()
window.title("Mile to KM Converter")
window.config(padx=25, pady=25, bg="#F8F9F9")
window.geometry("400x200")

# Custom font setup
title_font = font.Font(family="Helvetica", size=12, weight="bold")
label_font = font.Font(family="Helvetica", size=10)
button_font = font.Font(family="Helvetica", size=10, weight="bold")

# Create main container frame
container = Frame(window, bg="#F8F9F9")
container.pack(expand=True, fill="both")

# Input Section
input_frame = Frame(container, bg="#F8F9F9")
input_frame.grid(row=0, column=0, pady=10, sticky="ew")

miles_input = Entry(input_frame, width=10, font=label_font, bd=2, relief="flat",
                    highlightthickness=1, highlightcolor="#3498DB", justify=CENTER)
miles_input.grid(row=0, column=0, padx=5, sticky="ew")

miles_label = Label(input_frame, text="Miles",
                    font=label_font, bg="#F8F9F9", fg="#2C3E50")
miles_label.grid(row=0, column=1, padx=5, sticky="w")

# Result Section
result_frame = Frame(container, bg="#F8F9F9")
result_frame.grid(row=1, column=0, pady=10, sticky="ew")

is_equal_label = Label(result_frame, text="is equal to",
                       font=label_font, bg="#F8F9F9", fg="#2C3E50")
is_equal_label.grid(row=0, column=0, padx=5, sticky="e")

kilometer_result_label = Label(
    result_frame, text="", font=label_font, bg="#F8F9F9", fg="#2E86C1")
kilometer_result_label.grid(row=0, column=1, padx=5)

kilometer_label = Label(result_frame, text="KM",
                        font=label_font, bg="#F8F9F9", fg="#2C3E50")
kilometer_label.grid(row=0, column=2, padx=5, sticky="w")

# Button Section
button_frame = Frame(container, bg="#F8F9F9")
button_frame.grid(row=2, column=0, pady=15, sticky="ew")

calculate_button = Button(button_frame, text="Calculate Conversion", command=miles_to_km,
                          font=button_font, bg="#3498DB", fg="white", activebackground="#2980B9",
                          relief="flat", padx=15, pady=5)
calculate_button.pack()

# Configure grid weights for responsive scaling
container.columnconfigure(0, weight=1)
input_frame.columnconfigure(0, weight=1)
result_frame.columnconfigure(0, weight=1)
result_frame.columnconfigure(1, weight=0)
result_frame.columnconfigure(2, weight=0)

# Add subtle watermark
watermark = Label(window, text="Converter App", font=("Helvetica", 8),
                  bg="#F8F9F9", fg="#BDC3C7")
watermark.place(relx=1.0, rely=1.0, anchor="se")

window.mainloop()
