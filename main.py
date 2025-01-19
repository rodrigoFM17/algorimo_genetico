import math
import tkinter as tk
from tkinter import messagebox
from GeneticAlgorithm import GeneticAlgorithm
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def evaluation(x):
    return 0.1 * x * math.log(1 + abs(x)) * math.cos(x) * math.cos(x)

def save_video():
    return ""

# def show_grafic(a, b, geneticAlgorithm):
#     def func(x):
#         return 0.1 * x * np.log(1 + np.abs(x)) * np.cos(x) * np.cos(x)
    
#     x = np.linspace(a, b, 1000)
#     y = func(x)

#     i_min = np.argmin(y)
#     i_max = np.argmax(y)

#     x_min, y_min = x[i_min], y[i_min]
#     x_max, y_max = x[i_max], y[i_max]

#     figure, ax = plt.subplots()

#     ax.plot(x, y, label="grafica de la funcion", color="blue")


#     points = geneticAlgorithm.get_last_generation_points()
#     ax.scatter(points["general"]["x"], points["general"]["y"], color="black", label="individuos",zorder=5, s=50)

#     ax.scatter([points["best"]["x"]], [points["best"]["y"]], color="green", label="mejor", zorder=10, s=50)
#     ax.scatter([points["worst"]["x"]], [points["worst"]["y"]], color="red", label="peor", zorder=10, s=50)
    

#     ax.set_title("Grafica de la funcion")
#     ax.set_xlabel("x")
#     ax.set_ylabel("y")
#     ax.axvline(0, color="black", linewidth=0.5) 
#     ax.axhline(0, color="black", linewidth=0.5)  
#     ax.grid(color="gray", linestyle="--", linewidth=0.5)
#     ax.legend()

#     canvas = FigureCanvasTkAgg(figure, master=app) 
#     canvas.draw()

#     canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    # plt.plot(x, y, label=r"$0.1 \cdot x \cdot \ln(1 + |x|) \cdot \cos^2(x)$", color="blue")
    # plt.scatter([x_min, x_max], [y_min, y_max], color="red", label="Mín/Máx", zorder=5)

    # points = geneticAlgorithm.get_last_generation_points()
    # plt.scatter(points["general"]["x"], points["general"]["y"], color="black", label="individuos",zorder=5, s=50)

    # plt.scatter([points["best"]["x"]], [points["best"]["y"]], color="green", label="mejor", zorder=10, s=50)
    # plt.scatter([points["worst"]["x"]], [points["worst"]["y"]], color="red", label="peor", zorder=10, s=50)

    # plt.axhline(y=points["average_point"]["y"], color='blue', linestyle='--', linewidth=1)

    # plt.title("Gráfica de la función")
    # plt.xlabel("x")
    # plt.ylabel("y")
    # plt.axhline(0, color="black", linewidth=0.5)  
    # plt.axvline(0, color="black", linewidth=0.5)  
    # plt.grid(color="gray", linestyle="--", linewidth=0.5)
    # plt.legend()
    # plt.show()


def start_AG():
    continue_answer = True

    a = input_a.get()
    b = input_b.get()
    dx = input_dx.get()
    p_breed = input_p_breed.get()
    p_mutation = input_p_mutation.get()
    p_mutation_gen = input_p_mutation_gen.get()
    average_tolerancy = input_average_tolerancy.get()

    geneticAlgorithm = GeneticAlgorithm(
            a,
            b,
            dx,
            p_breed,
            p_mutation,
            p_mutation_gen,
            evaluation,
            average_tolerancy
        )
    
    while continue_answer:
        
        geneticAlgorithm.start()
        continue_answer = messagebox.askyesno(
            "Alerta",
            f"El mejor resultado obtenido es {geneticAlgorithm.best_subjects[len(geneticAlgorithm.best_subjects) - 1]}"
            )
    
    show_grafic(float(a), float(b), geneticAlgorithm)
    show_report(geneticAlgorithm)

app = tk.Tk()
app.title("Algoritmo Genetico")

inputs = tk.Frame(app, width=600, height=600)
inputs.grid(row=0, column=0, sticky="nsew", pady=30)

results = tk.Frame(app, width=600, height=600)
results.grid(row=0, column=1, sticky="nsew")

def show_grafic(a, b, geneticAlgorithm):
    def func(x):
        return 0.1 * x * np.log(1 + np.abs(x)) * np.cos(x) * np.cos(x)
    
    x = np.linspace(a, b, 1000)
    y = func(x)

    i_min = np.argmin(y)
    i_max = np.argmax(y)

    x_min, y_min = x[i_min], y[i_min]
    x_max, y_max = x[i_max], y[i_max]

    figure, ax = plt.subplots()

    ax.plot(x, y, label="grafica de la funcion", color="blue")


    points = geneticAlgorithm.get_last_generation_points()
    ax.scatter(points["general"]["x"], points["general"]["y"], color="black", label="individuos",zorder=5, s=50)

    ax.scatter([points["best"]["x"]], [points["best"]["y"]], color="green", label="mejor", zorder=10, s=50)
    ax.scatter([points["worst"]["x"]], [points["worst"]["y"]], color="red", label="peor", zorder=10, s=50)
    ax.axhline(y=points["average_point"]["y"], color='blue', linestyle='--', linewidth=1)

    

    # Detalles del gráfico
    ax.set_title("Grafica de la funcion")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.axvline(0, color="black", linewidth=0.5) 
    ax.axhline(0, color="black", linewidth=0.5)  
    ax.grid(color="gray", linestyle="--", linewidth=0.5)
    ax.legend()

    canvas = FigureCanvasTkAgg(figure, master=results) 
    canvas.draw()

    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=2)

label = tk.Label(inputs, text="Ingrese los parametros")
label.pack()

input_a_label = tk.Label(inputs, text="a: ")                                        
input_a = tk.Entry(inputs)                   
input_b_label = tk.Label(inputs, text="b: ")
input_b = tk.Entry(inputs)                                                          
input_dx_label = tk.Label(inputs, text="dx: ") 
input_dx = tk.Entry(inputs)                                                          
input_p_breed_label = tk.Label(inputs, text="probabilidad de cruza: ")                                                           
input_p_breed = tk.Entry(inputs)
input_p_mutation_label = tk.Label(inputs, text="probabilidad de mutacion del sujeto: ")                                                           
input_p_mutation = tk.Entry(inputs)
input_p_mutation_gen_label = tk.Label(inputs, text="probabilidad de mutacion del gen del sujeto: ")                                                           
input_p_mutation_gen = tk.Entry(inputs)
input_average_tolerancy_label = tk.Label(inputs, text="tolerancia para el promedio: ")                                                           
input_average_tolerancy = tk.Entry(inputs)

input_a_label.pack()
input_a.pack()
input_b_label.pack()
input_b.pack()
input_dx_label.pack()
input_dx.pack()
input_p_breed_label.pack()
input_p_breed.pack()
input_p_mutation_label.pack()
input_p_mutation.pack()
input_p_mutation_gen_label.pack()
input_p_mutation_gen.pack()
input_average_tolerancy_label.pack()
input_average_tolerancy.pack()

start_button = tk.Button(inputs, text="Iniciar", command=start_AG)
start_button.pack()

video_button = tk.Button(inputs, text="Guardar video", command=save_video)


def show_report(geneticAlgorithm):
    result_label = tk.Label(inputs, text="Reporte del mejor caso")
    best_case = geneticAlgorithm.get_best_subject()
    genome_label = tk.Label(inputs, text=f"cadena de bits: {best_case.get_string_genome(geneticAlgorithm.n_bits)}")
    decimal_label = tk.Label(inputs, text=f"valor decimal: {best_case.int_genome}")
    x_label = tk.Label(inputs, text=f"x*: {best_case.get_x()}")
    phenotype_label = tk.Label(inputs, text=f"f(x*): {best_case.get_y()}")
    delta_label = tk.Label(inputs, text=f"d*x: {geneticAlgorithm.dx}")

    result_label.pack()
    genome_label.pack()
    decimal_label.pack()
    x_label.pack()
    phenotype_label.pack()
    delta_label.pack()
    video_button.pack()




app.geometry("1200x600")

app.mainloop()

