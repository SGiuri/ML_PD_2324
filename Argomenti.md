# 7.1 Elementi di data science:
    - Cos’è la data science e di cosa si occupa il data scientist,
    -Cosa sono i Big Data,
    - Cosa sono le reti neurali e il deep learning,
    - Applicazioni di machine learning,
    - Cos’è il data mining,
    - Struttura di un progetto di data science.
# 7.2 Data science con Python:
    - Obiettivi di analisi: comprensione del problema di business e dei requisiti aziendali,
    - Approccio analitico per la soluzione del problema di business,
    - Data requirements: identificazione del contenuto, del formato e delle fonti di dati
necessari per la raccolta dei dati,
    - Data collection: strumenti per la raccolta dei dati dalle fonti individuate,
    - Data understanding: controllo del tipo e degli attributi dei dati raccolti,
    - Data preparation: preparazione dei dati per la modellazione, normalizzazione, pulizia,
    - Implementazione del modello di machine learning,
    - Valutazione del modello: tecniche di hold-out e cross-validation,
    - Deployment del modello e feedback.
        


## 1. Setup di un ambiente di sviluppo
- Cenni sui **markdown**, i file .md
- Creazione e Clonazione di un repository
    - Git - Github 
        - Commit, Push
    - [Scientific Python per VSCode](https://code.visualstudio.com/docs/datascience/data-science-tutorial):
        - Ambienti Virtuali:
            - Virtualenv 
            - Conda, [Anaconda](https://www.anaconda.com/download) e [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/)

            ```bash
            (base) C:\Windows\..\> conda create -n myenv python=3.10 pandas jupyter seaborn scikit-learn keras tensorflow 
            ```
        - Jupyter Notebook