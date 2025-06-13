import os
import pandas as pd
import matplotlib
matplotlib.use('Agg')  
import matplotlib.pyplot as plt

def generate_analysis_plot():

    static_folder = os.path.join(os.path.dirname(__file__), 'static')
    os.makedirs(static_folder, exist_ok=True)
    plot_path = os.path.join(static_folder, 'plot.png')

    data = {
        'Rok': [2015, 2016, 2017, 2018, 2019, 2020],
        'Liczba ludności': [38400, 38500, 38450, 38300, 38200, 38100]
    }
    df = pd.DataFrame(data)

    # Tworzenie wykresu
    plt.figure(figsize=(6, 4))
    plt.plot(df['Rok'], df['Liczba ludności'], marker='o')
    plt.title('Liczba ludności w Polsce (2015–2020)')
    plt.xlabel('Rok')
    plt.ylabel('Liczba ludności (tys.)')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(plot_path)
    plt.close()
