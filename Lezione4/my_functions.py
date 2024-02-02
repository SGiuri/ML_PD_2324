from math import ceil
import matplotlib.pyplot as plt
from numpy import unravel_index

from math import ceil
import matplotlib.pyplot as plt
from numpy import unravel_index


def show_multiple_img(images, targets):
    """
    Visualizza una griglia di immagini con i relativi titoli.
    
    Questa funzione prende in input due liste: una di immagini e una di etichette corrispondenti (targets) e 
    le visualizza in una griglia. Il numero massimo di colonne è fissato a 6; il numero di righe è calcolato 
    in base al numero totale di immagini. Le dimensioni della figura sono adattate in base al numero di colonne e righe.
    
    :param images: Lista di immagini da visualizzare. Ogni elemento della lista è un'immagine che può essere visualizzata con plt.imshow.
    :param targets: Lista di etichette corrispondenti alle immagini. Ogni etichetta è visualizzata come titolo della rispettiva immagine.
    :return: None
    """

    # Determina il numero di colonne (limitato a un massimo di 6) e calcola il numero di righe necessarie.
    if len(images) < 6:
        my_cols = len(images)
    else:
        my_cols = 6
    my_rows = ceil(len(images) / my_cols)  # Calcola il numero di righe necessario.

    # Calcola le dimensioni della figura in base al numero di righe e colonne.
    fig_width = my_cols * 10 / 6  # Adatta la larghezza della figura.
    fig_height = my_rows * 10 / 4  # Adatta l'altezza della figura.

    # Crea la figura con le dimensioni calcolate.
    fig = plt.figure(figsize=(fig_width, fig_height))
    gs = fig.add_gridspec(my_rows, my_cols)  # Crea una griglia per le sottofigure.

    axes = []  # Lista per memorizzare gli assi delle sottofigure.
    matrix_dimension = (my_rows, my_cols)  # Dimensione della matrice per posizionare le sottofigure.
    for n, image in enumerate(images):
        subplot_position = unravel_index(n, matrix_dimension)  # Calcola la posizione della sottofigura.
        axes.append(fig.add_subplot(gs[subplot_position]))  # Aggiunge la sottofigura alla griglia.

    # Nasconde gli assi per tutte le sottofigure.
    for ax in axes:
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

    # Imposta i titoli e mostra le immagini nelle rispettive sottofigure.
    for ax, image, target in zip(axes, images, targets):
        ax.set_title(target)  # Imposta il titolo con l'etichetta corrispondente.
        ax.imshow(image, cmap=plt.cm.gray_r)  # Mostra l'immagine con colormap grigio invertito.
    
    plt.tight_layout()  # Ottimizza la disposizione delle sottofigure.
    plt.show()  # Visualizza la figura.
