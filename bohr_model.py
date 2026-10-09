import math
import tkinter as tk

# Electron capacities per principal energy level (n = 1, 2, 3, 4, ...)
SHELL_CAPACITIES = [2, 8, 18, 32, 50, 72]


def calculate_electron_distribution(total_electrons):
    """Distribute electrons across shells according to capacity rules."""
    shells = []
    remaining = total_electrons

    for cap in SHELL_CAPACITIES:
        if remaining <= 0:
            break
        count = min(remaining, cap)
        shells.append(count)
        remaining -= count

    return shells


def draw_bohr_model(protons, neutrons, electrons):
    """Create a window and render the Bohr model for the given particle counts."""
    # Window setup
    root = tk.Tk()
    root.title(f"Bohr Model — Protons: {protons}, Neutrons: {neutrons}, Electrons: {electrons}")

    canvas_size = 700
    center = canvas_size // 2
    canvas = tk.Canvas(root, width=canvas_size, height=canvas_size, bg="#1e1e2e")
    canvas.pack(fill=tk.BOTH, expand=True)

    # Calculate electron shells
    electron_shells = calculate_electron_distribution(electrons)

    # ---------------------------------------------------------
    # 1. DRAW NUCLEUS
    # ---------------------------------------------------------
    nucleus_radius = 45
    canvas.create_oval(
        center - nucleus_radius,
        center - nucleus_radius,
        center + nucleus_radius,
        center + nucleus_radius,
        fill="#313244",
        outline="#cdd6f4",
        width=2,
    )

    # Text inside nucleus
    canvas.create_text(
        center,
        center - 12,
        text=f"{protons} p⁺",
        fill="#f38ba8",
        font=("Helvetica", 14, "bold"),
    )
    canvas.create_text(
        center,
        center + 12,
        text=f"{neutrons} n⁰",
        fill="#89dceb",
        font=("Helvetica", 14, "bold"),
    )

    # ---------------------------------------------------------
    # 2. DRAW ELECTRON SHELLS & ELECTRONS
    # ---------------------------------------------------------
    shell_spacing = 40
    electron_radius = 6

    for shell_index, count in enumerate(electron_shells):
        orbit_radius = nucleus_radius + (shell_index + 1) * shell_spacing

        # Draw orbit ring
        canvas.create_oval(
            center - orbit_radius,
            center - orbit_radius,
            center + orbit_radius,
            center + orbit_radius,
            outline="#585b70",
            dash=(4, 4),
            width=1.5,
        )

        # Place electrons along the orbit
        for e_index in range(count):
            # Angle in radians, distributed evenly across 360 degrees
            angle = (2 * math.pi / count) * e_index - (math.pi / 2)

            e_x = center + orbit_radius * math.cos(angle)
            e_y = center + orbit_radius * math.sin(angle)

            # Draw electron
            canvas.create_oval(
                e_x - electron_radius,
                e_y - electron_radius,
                e_x + electron_radius,
                e_y + electron_radius,
                fill="#89b4fa",
                outline="#b4befe",
                width=1,
            )

    # ---------------------------------------------------------
    # 3. DRAW LEGEND / INFORMATION
    # ---------------------------------------------------------
    legend_text = (
        f"Protons (p⁺): {protons}\n"
        f"Neutrons (n⁰): {neutrons}\n"
        f"Electrons (e⁻): {electrons}\n"
        f"Shell Distribution: {electron_shells}"
    )
    canvas.create_text(
        15,
        20,
        text=legend_text,
        anchor="nw",
        fill="#cdd6f4",
        font=("Courier", 11, "bold"),
    )

    root.mainloop()


if __name__ == "__main__":
    # Example: Carbon-12 (6 Protons, 6 Neutrons, 6 Electrons)
    # Change these values to generate any element!
    P = 6
    N = 6
    E = 6

    draw_bohr_model(protons=P, neutrons=N, electrons=E)
