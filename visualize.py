import numpy as np
import matplotlib.pyplot as plt

# Dati noti
mean = -0.006012731697410345     # Sostituisci con la tua media
varianza = 0.00020424691319931298  # Sostituisci con la tua varianza
min_value = -0.01785433292388916   # Sostituisci con il tuo minimo
max_value = 0.017719922587275505   # Sostituisci con il tuo massimo

# Genera una distribuzione normale basata su mean e varianza
std_dev = np.sqrt(varianza)
synthetic_data = np.random.normal(mean, std_dev, 1000)

# Clamp dei valori tra il minimo e il massimo
synthetic_data = np.clip(synthetic_data, min_value, max_value)

# Visualizza l'istogramma
plt.hist(synthetic_data, bins=30, edgecolor='black')
plt.title('Distribuzione approssimata basata su mean e varianza')
plt.xlabel('Valore')
plt.ylabel('Frequenza')
plt.show()