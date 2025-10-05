import tkinter as tk
from game_manager import GameManager
from gui  import DiceView

def main():
    root = tk.Tk()
    root.title("Juego de Dados — GUI")
    root.geometry("400x250")  # tamaño provisional


    # escenario apra los dados
    top = tk.Frame(root, bg="#e9eef3")
    top.pack(padx=12, pady=12, fill="both", expand=True)

    dice_area = tk.Frame(top, bg="#e9eef3")

    # dado_vista = DiceView(dice_area, size = 100) # genera una imagen de prueba
    dice_area.pack()

    controls = tk.Frame(root, bg="#e9eef3")
    controls.pack(padx=12, pady=(0, 12), fill="x")

    # Boton que usa dado_vista para generar la cara con _draw_face
    # btn = tk.Button(controls, text="Lanzar (demostracion animada)",
    #                 command=lambda: dado_vista.animate_to(6))
    # btn.pack(side="left", padx=6)
    #


    # Modelo
    game = GameManager()
    game.numero_dados(2, 6)  # por ejemplo, 2 dados de 6 caras

    # Vistas (una por cada dado lógico)
    dice_views = []
    for _ in range(len(game.dados)):
        dice_views.append(DiceView(dice_area, size=100))

    def lanzar_desde_modelo():
        """Pide al modelo la ronda y anima cada vista a su cara real."""
        resultado = game.ronda_de_lanzamiento()  # dict: {"Dado 1": n1, "Dado 2": n2, ...}
        total = 0
        for i, view in enumerate(dice_views, start=1):
            # obtenemos la clave y valor
            value = resultado.get(f"Dado {i}", 1)
            total += value
            # Pequeño escalonado visual opcional
            root.after((i - 1) * 80, lambda v=view, val=value: v.animate_to(val))
        lbl_total.config(text=f"Total: {total}")

    # Controles reales
    btn = tk.Button(controls, text="Lanzar", command=lanzar_desde_modelo, width=12)
    btn.pack(side="left", padx=6)

    lbl_total = tk.Label(controls, text="Total: –", bg="#e9eef3",
                         font=("Segoe UI", 12, "bold"))
    lbl_total.pack(side="right")

    root.mainloop()



main()

