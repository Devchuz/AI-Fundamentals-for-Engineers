import numpy as np

# Generación de datos
n_samples = 15
X = np.random.rand(n_samples, 1)
for _ in range(2, 11):
    X = np.hstack((X, (10**_) * np.random.rand(n_samples, 1)))

def pca(X: np.array, k: int, standardize: bool = True) -> np.array:
    """Encuentra pca. Puede seleccionar si estandarizar los datos o no.

    Args:
        X (np.array): Datos de entrada.
        k (int): Número de componentes principales a retener.
        standardize (bool, optional): Bandera para elegir si estandarizar. Por defecto es True.

    Returns:
        np.array: datos proyectados
    """
    mean = X.mean(axis=0)
    if standardize:
        X = X - mean
    covariance_matrix = np.dot(X.T, X) / X.shape[0]
    eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)
    eigenvectors = eigenvectors[:, np.argsort(eigenvalues)[::-1]]
    if standardize:
        return np.dot(X, eigenvectors[:, :k]) / np.sqrt(eigenvalues[:k])
    else:
        return np.dot(X, eigenvectors[:, :k])

# Aplicando PCA
k = 2  # Número de dimensiones a las que queremos reducir nuestros datos
X_pca = pca(X, k)

# Imprimir los datos proyectados
print("Datos proyectados mediante PCA:")
print(X_pca)

# Opcional: Visualización de los datos proyectados
# Si estás ejecutando esto en un entorno que soporta gráficos, como un Jupyter Notebook, puedes visualizar los datos proyectados.
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c='blue', marker='o', edgecolor='k', s=50)
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.title('Visualización de PCA')
plt.grid(True)
plt.show()
