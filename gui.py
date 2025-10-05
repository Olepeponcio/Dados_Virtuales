    # gui.py
import tkinter as tk
import random


class DiceView:
    """Vista de un dado: lo dibuja en un Canvas."""
    def __init__(self, master, size=90):
        self.size = size
        self.canvas = tk.Canvas(master, width=size, height=size,
                                bg="#f5f5f5", highlightthickness=0)
        self.canvas.pack(padx=8, pady=8)
        self._draw_face(1)  # cara inicial

    def _draw_face(self, value: int):
        """Dibuja el cuadrado del dado y sus 'pips' (puntos) para la cara 'value'."""
        s = self.size
        c = self.canvas
        c.delete("all")

        # cuerpo del dado
        c.create_rectangle(3, 3, s-3, s-3, fill="white", outline="#222", width=2)

        # cálculo de posiciones en una malla 3x3 (esquinas, centros…)
        margen = s // 5
        cx = [margen, s // 2, s - margen]
        cy = [margen, s // 2, s - margen]
        posiciones = {
            1: [(1, 1)],
            2: [(0, 0), (2, 2)],
            3: [(0, 0), (1, 1), (2, 2)],
            4: [(0, 0), (2, 0), (0, 2), (2, 2)],
            5: [(0, 0), (2, 0), (1, 1), (0, 2), (2, 2)],
            6: [(0, 0), (2, 0), (0, 1), (2, 1), (0, 2), (2, 2)],
        }
        r = s // 12  # radio de cada punto
        for (ix, iy) in posiciones[value]:
            c.create_oval(cx[ix]-r, cy[iy]-r, cx[ix]+r, cy[iy]+r, fill="#111", outline="")


    def animate_to(self, target_value: int, frames: int = 14, interval_ms: int = 70):
        """Durante 'frames' alterna caras aleatorias y acaba en 'target_value'."""
        self._target = target_value
        self._frames_left = max(1, frames)
        self._interval = max(30, interval_ms)
        self._tick()


    def _tick(self):
        if self._frames_left > 0:
            rnd = random.randint(1, 6)
            self._draw_face(rnd)
            self._frames_left -= 1
            self.canvas.after(self._interval, self._tick)  # reprograma el siguiente frame
        else:
            self._draw_face(self._target)




def main():
    root = tk.Tk()
    root.title("Juego de Dados — GUI")
    root.geometry("400x250")  # tamaño provisional


    # escenario apra los dados
    top = tk.Frame(root, bg="#e9eef3")
    top.pack(padx=12, pady=12, fill="both", expand=True)

    dice_area = tk.Frame(top, bg="#e9eef3")
    dado_vista = DiceView(dice_area, size = 100)
    dice_area.pack()

    controls = tk.Frame(root, bg="#e9eef3")
    controls.pack(padx=12, pady=(0, 12), fill="x")

    # Boton que usa dado_vista para generar la cara con _draw_face
    btn = tk.Button(controls, text="Lanzar (demostracion animada)",
                    command=lambda: dado_vista.animate_to(6))
    btn.pack(side="left", padx=6)

    root.mainloop()



if __name__ == "__main__":
    main()
