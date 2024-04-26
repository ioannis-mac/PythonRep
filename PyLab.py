from pylab import *
import csv
import numpy as np
import matplotlib as plt

def read_csv(filename):
    with open(filename) as f:
        csv_reader = csv.reader(f)
        next(csv_reader)
        summer = []
        highest_correlated = []
        for row in csv_reader:
            summer.append(float(row[1]))
            highest_correlated.append(float(row[2]))
    return summer, highest_correlated

def correlation(x,y):
    corr_matrix = np.corrcoef(x,y)
    corr = corr_matrix[0,1]
    return corr

def scatter_plot(x,y):
    plt.scatter(x,y)
    plt.xlabel('Summer Data')
    plt.ylabel('Higest Corr Data')
    plt.title('Scatter Plot')
    plt.grid(True)

def calculate_correlation(x, y):
    """
    Calcule la corrélation entre deux ensembles de données.
    
    :param x: Première liste de données.
    :param y: Deuxième liste de données.
    :return: Valeur de corrélation.
    """
    corr_matrix = np.corrcoef(x, y)
    correlation = corr_matrix[0, 1]
    return correlation

def plot_scatter(x, y):
    """
    Crée un graphique de dispersion à partir de deux ensembles de données.
    
    :param x: Données pour l'axe des abscisses.
    :param y: Données pour l'axe des ordonnées.
    """
    plt.scatter(x, y)
    plt.xlabel('Summer Data')
    plt.ylabel('Highest Correlated Data')
    plt.title('Scatter Plot of Data Correlation')
    plt.grid(True)

# Utilisation des fonctions définies ci-dessus
if __name__ == "__main__":
    summer_data, highest_correlated_data = read_csv('correlate-summer.csv')
    correlation_value = calculate_correlation(summer_data, highest_correlated_data)
    print(f'Highest correlation: {correlation_value}')
    plot_scatter(summer_data, highest_correlated_data)
    plt.show()