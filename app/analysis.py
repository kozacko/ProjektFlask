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

def generate_forecast_plot():
    plot_path = os.path.join(os.path.dirname(__file__), 'static', 'forecast.png')

    data = {
        'Rok': [2023, 2030, 2040, 2050, 2060],
        '0–17': [18, 17, 16, 15, 14],
        '18–64': [63, 60, 56, 53, 51],
        '65+': [19, 23, 28, 32, 35]
    }
    df = pd.DataFrame(data)

    plt.figure(figsize=(6, 4))
    plt.stackplot(df['Rok'], df['0–17'], df['18–64'], df['65+'],
                  labels=['0–17', '18–64', '65+'], colors=['#90caf9', '#a5d6a7', '#ffcc80'])
    plt.title('Prognoza struktury wiekowej ludności (2023–2060)')
    plt.xlabel('Rok')
    plt.ylabel('Udział procentowy (%)')
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.savefig(plot_path)
    plt.close()