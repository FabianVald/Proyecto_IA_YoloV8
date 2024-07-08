import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import Camara
import PIL.Image, PIL.ImageTk

def buscar_video():
    video_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi;*.mkv")])
    if video_path:
        print(f"Ruta del video seleccionado: {video_path}")

def ejecutar_codigo():
    # Aquí iría el código que quieres ejecutar al presionar el segundo botón
    print("Ejecutando código...")
    Camara.Capturer()

def inicializador():
    # Función para crear la interfaz gráfica
    
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Proyecto Final IA - Yolo")

    # Tamaño personalizado de la ventana
    window_width = 400
    window_height = 200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_position = int((screen_width - window_width) / 2)
    y_position = int((screen_height - window_height) / 2)
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Crear un estilo con bordes más redondeados para los botones
    style = ttk.Style()
    style.theme_use('clam')  # Usar un tema que soporte estilos personalizados
    style.configure('TButton', borderwidth=2, relief="groove", foreground='black', background='white', padding=10, font=('Helvetica', 12))

    # Función para crear botones con el estilo personalizado
    def rounded_button(parent, text, command):
        button = ttk.Button(parent, text=text, command=command, style='TButton')
        return button

    # Botón para buscar video
    buscar_button = rounded_button(root, "Buscar Video", buscar_video)
    buscar_button.pack(pady=20)

    # Botón para ejecutar código
    ejecutar_button = rounded_button(root, "Camara en Vivo", ejecutar_codigo)
    ejecutar_button.pack(pady=10)

    # Ejecutar el bucle principal de la ventana
    root.mainloop()