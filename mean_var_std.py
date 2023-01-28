import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    teste = np.array(list).reshape(3,3)

    calculations = {
        "mean": [np.mean(teste, axis=0).tolist(), np.mean(teste, axis=1).tolist(), np.mean(teste).tolist()],
        "variance": [np.var(teste, axis=0).tolist(), np.var(teste, axis=1).tolist(), np.var(teste).tolist()],
        "standard deviation": [np.std(teste, axis=0).tolist(), np.std(teste, axis=1).tolist(), np.std(teste).tolist()],
        "max": [np.max(teste, axis=0).tolist(), np.max(teste, axis=1).tolist(), np.max(teste).tolist()],
        "min": [np.min(teste, axis=0).tolist(), np.min(teste, axis=1).tolist(), np.min(teste).tolist()],
        "sum": [np.sum(teste, axis=0).tolist(), np.sum(teste, axis=1).tolist(), np.sum(teste).tolist()]

    }

    return calculations