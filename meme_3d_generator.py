import tkinter as tk
from tkinter import ttk, messagebox
from solid import *
from solid.utils import *
from solid import scad_render_to_file

# A simple dictionary mapping meme names to the text that will be extruded
MEME_DICT = {
    "All Your Base": "All Your Base Are Belong To Us",
    "Rickroll": "Never Gonna Give You Up",
    "Nyan Cat": "Nyan Cat",
    "Doge": "Such Meme, Much Wow"
}

def generate_meme_model(meme_text, extrude_height=10, text_size=10):
    """
    Generates a 3D model by extruding text.
    
    :param meme_text: The text to convert into 3D.
    :param extrude_height: How deep the text is extruded.
    :param text_size: The size of the text.
    :return: A SolidPython model.
    """
    # The text() function creates 2D text, and linear_extrude makes it 3D.
    model = linear_extrude(height=extrude_height)(
        text(meme_text, size=text_size, font="Arial")
    )
    return model

def generate_file():
    selected_meme = meme_var.get()
    if selected_meme not in MEME_DICT:
        messagebox.showerror("Error", "Please select a valid meme.")
        return

    meme_text = MEME_DICT[selected_meme]
    model = generate_meme_model(meme_text)
    
    # Generate a filename by replacing spaces with underscores
    filename = f"{selected_meme.replace(' ', '_')}_meme.scad"
    scad_render_to_file(model, filename)
    messagebox.showinfo("Success", f"3D model file generated:\n{filename}")

# Create the main Tkinter window
root = tk.Tk()
root.title("2000s Meme 3D Generator")

# Set up a frame for padding and layout
frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Dropdown (combobox) to select a meme
meme_var = tk.StringVar()
ttk.Label(frame, text="Select a Meme:").grid(row=0, column=0, sticky=tk.W)
meme_combo = ttk.Combobox(frame, textvariable=meme_var, state="readonly")
meme_combo['values'] = list(MEME_DICT.keys())
meme_combo.grid(row=1, column=0, sticky=(tk.W, tk.E))
meme_combo.current(0)  # default to the first meme

# Button to trigger the 3D model generation
generate_button = ttk.Button(frame, text="Generate 3D Model", command=generate_file)
generate_button.grid(row=2, column=0, pady=10)

# Start the GUI event loop
root.mainloop()
