import tkinter as tk
import random

# Define the rarities and their properties
rarities = [
    {"name": "Common", "probability": 0.5, "color": "#808080"},
    {"name": "Uncommon", "probability": 0.3, "color": "#008000"},
    {"name": "Rare", "probability": 0.15, "color": "#0000FF"},
    {"name": "Epic", "probability": 0.04, "color": "#800080"},
    {"name": "Legendary", "probability": 0.01, "color": "#FFD700"}
]

def roll_rarity():
    roll = random.random()
    cumulative_probability = 0.0
    for rarity in rarities:
        cumulative_probability += rarity["probability"]
        if roll < cumulative_probability:
            return rarity

def smooth_color_transition(start_color, end_color, steps=20, delay=50):
    start_color = window.winfo_rgb(start_color)
    end_color = window.winfo_rgb(end_color)
    
    r_diff = (end_color[0] - start_color[0]) // steps
    g_diff = (end_color[1] - start_color[1]) // steps
    b_diff = (end_color[2] - start_color[2]) // steps

    def transition_step(step=0):
        if step <= steps:
            r = start_color[0] + (r_diff * step)
            g = start_color[1] + (g_diff * step)
            b = start_color[2] + (b_diff * step)
            new_color = f"#{r//256:02x}{g//256:02x}{b//256:02x}"
            window.config(bg=new_color)
            window.after(delay, transition_step, step + 1)
        else:
            roll_button.config(state=tk.NORMAL)

    transition_step()

def roll_animation():
    roll_button.config(state=tk.DISABLED)
    color_sequence = [random.choice(rarities)["color"] for _ in range(20)]

    def animate(index=0):
        if index < len(color_sequence):
            next_color = color_sequence[index]
            smooth_color_transition(window.cget("bg"), next_color, steps=5, delay=25)
            window.after(150, animate, index + 1)
        else:
            final_rarity = roll_rarity()
            smooth_color_transition(window.cget("bg"), final_rarity["color"], steps=10, delay=50)
            result_label.config(text=f"You rolled: {final_rarity['name']}", bg=final_rarity["color"])

    animate()

# Setup the GUI
window = tk.Tk()
window.title("Rarity Roller")
window.geometry("500x300")
window.config(bg="#FFFFFF")

result_label = tk.Label(window, text="", font=("Helvetica", 18, "bold"), pady=10, bg="#FFFFFF")
result_label.pack(pady=20)

roll_button = tk.Button(window, text="Roll", command=roll_animation, font=("Helvetica", 16, "bold"), bg="#FFFFFF", fg="#000000", bd=5, relief="raised")
roll_button.pack(pady=20)

# Display the rarities table
rarities_frame = tk.Frame(window, bg="#FFFFFF", bd=2, relief="solid")
rarities_frame.pack(pady=10)

tk.Label(rarities_frame, text="Rarity Table", font=("Helvetica", 14, "bold"), pady=5, bg="#FFFFFF").pack()
for rarity in rarities:
    tk.Label(rarities_frame, text=f"{rarity['name']}: {rarity['probability']*100}%", fg=rarity["color"], font=("Helvetica", 12), bg="#FFFFFF").pack()

window.mainloop()
