import tkinter as tk

# -----------------------------
# Configuración general
# -----------------------------
CELL = 12      # Tamaño de cada celda en píxeles
ROWS = 40      # Número de filas del tablero
COLS = 60      # Número de columnas del tablero
DELAY = 60     # Tiempo entre generaciones en milisegundos

# Desplazamientos relativos a las 8 celdas vecinas
NEIGHBORS = [
    (dr, dc)
    for dr in (-1, 0, 1)
    for dc in (-1, 0, 1)
    if (dr, dc) != (0, 0)
]


def next_generation(alive):
    """
    Calcula la siguiente generación del Juego de la Vida.

    Parámetro:
        alive (set[tuple[int, int]]):
            Conjunto de posiciones (fila, columna) de las células vivas.

    Retorna:
        set[tuple[int, int]]:
            Nuevo conjunto de células vivas después de aplicar las reglas.

    Idea del algoritmo:
    1. Para cada célula viva, se recorren sus 8 vecinos.
    2. Se cuenta cuántas veces aparece cada posición como vecina viva.
    3. Luego se aplican las reglas de Conway:
       - Una célula nace si tiene exactamente 3 vecinos vivos.
       - Una célula sobrevive si ya estaba viva y tiene exactamente 2 vecinos vivos.
    """

    # Diccionario para contar vecinos vivos:
    # clave   -> posición (fila, columna)
    # valor   -> cantidad de vecinos vivos que tiene esa posición
    counts = {}

    # Recorremos cada célula viva actual
    for r, c in alive:
        # Revisamos sus 8 vecinos
        for dr, dc in NEIGHBORS:
            nr, nc = r + dr, c + dc

            # Solo contamos posiciones que estén dentro del tablero
            if 0 <= nr < ROWS and 0 <= nc < COLS:
                pos = (nr, nc)
                counts[pos] = counts.get(pos, 0) + 1

    # Construimos el nuevo conjunto de células vivas
    new_alive = {
        pos
        for pos, n in counts.items()
        if n == 3 or (n == 2 and pos in alive)
    }

    return new_alive


class LifeApp:
    """
    Aplicación gráfica del Juego de la Vida usando Tkinter.

    Atributos principales:
        root      : ventana principal de Tkinter
        alive     : conjunto de células vivas
        running   : indica si la simulación está corriendo
        canvas    : área donde se dibuja el tablero
    """

    def __init__(self, root):
        """
        Inicializa la aplicación, crea la interfaz gráfica
        y prepara el tablero vacío.
        """
        self.root = root
        self.root.title("Juego de la Vida")

        # Estado inicial del sistema
        self.alive = set()
        self.running = False

        # Canvas donde se dibuja la rejilla y las células
        self.canvas = tk.Canvas(
            root,
            width=COLS * CELL,
            height=ROWS * CELL,
            bg="white"
        )
        self.canvas.pack()

        # Marco para los botones de control
        controls = tk.Frame(root)
        controls.pack(pady=6)

        # Botones de la interfaz
        tk.Button(
            controls,
            text="Start / Stop",
            command=self.toggle_run,
            width=12
        ).pack(side="left", padx=4)

        tk.Button(
            controls,
            text="Step",
            command=self.step,
            width=10
        ).pack(side="left", padx=4)

        tk.Button(
            controls,
            text="Clear",
            command=self.clear,
            width=10
        ).pack(side="left", padx=4)

        # Al hacer clic sobre el tablero, se cambia el estado de una célula
        self.canvas.bind("<Button-1>", self.toggle_cell)

        # Dibujo inicial
        self.draw()

    def toggle_cell(self, event):
        """
        Cambia el estado de la célula sobre la que hizo clic el usuario.

        Si la célula estaba viva, la mata.
        Si la célula estaba muerta, la revive.

        Parámetro:
            event: evento de Tkinter que contiene la posición del clic.
        """
        row = event.y // CELL
        col = event.x // CELL
        pos = (row, col)

        if pos in self.alive:
            self.alive.remove(pos)
        else:
            self.alive.add(pos)

        self.draw()

    def toggle_run(self):
        """
        Inicia o detiene la simulación.

        - Si estaba detenida, la pone a correr.
        - Si estaba corriendo, la detiene.
        """
        self.running = not self.running
        if self.running:
            self.animate()

    def animate(self):
        """
        Ejecuta la animación automática.

        Esta función:
        1. Avanza una generación.
        2. Programa su propia llamada futura con root.after(...).

        Se repite mientras 'running' sea True.
        """
        if self.running:
            self.step()
            self.root.after(DELAY, self.animate)

    def step(self):
        """
        Avanza exactamente una generación del Juego de la Vida
        y redibuja el tablero.
        """
        self.alive = next_generation(self.alive)
        self.draw()

    def clear(self):
        """
        Limpia el tablero:
        - Detiene la simulación.
        - Borra todas las células vivas.
        - Redibuja el tablero vacío.
        """
        self.running = False
        self.alive.clear()
        self.draw()

    def draw(self):
        """
        Dibuja el estado actual del tablero en el canvas.

        Hace dos cosas:
        1. Dibuja la rejilla.
        2. Dibuja las células vivas como rectángulos negros.
        """
        self.canvas.delete("all")

        # Dibujar líneas horizontales de la rejilla
        for y in range(0, ROWS * CELL, CELL):
            self.canvas.create_line(0, y, COLS * CELL, y, fill="#e8e8e8")

        # Dibujar líneas verticales de la rejilla
        for x in range(0, COLS * CELL, CELL):
            self.canvas.create_line(x, 0, x, ROWS * CELL, fill="#e8e8e8")

        # Dibujar células vivas
        for r, c in self.alive:
            x0, y0 = c * CELL, r * CELL
            x1, y1 = x0 + CELL, y0 + CELL
            self.canvas.create_rectangle(
                x0, y0, x1, y1,
                fill="black",
                outline="black"
            )


if __name__ == "__main__":
    """
    Punto de entrada del programa.

    Aquí se:
    1. Crea la ventana principal.
    2. Crea la aplicación LifeApp.
    3. Inicia el bucle principal de Tkinter.
    """
    root = tk.Tk()
    app = LifeApp(root)
    root.mainloop()
