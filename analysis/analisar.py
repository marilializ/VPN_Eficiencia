import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np

# Carrega os dados
sem_vpn = pd.read_csv(r'C:\experimento\resultados\sem_vpn.csv')
com_vpn = pd.read_csv(r'C:\experimento\resultados\com_vpn.csv')

a = sem_vpn['Queries'].astype(float)
b = com_vpn['Queries'].astype(float)

# Estatísticas descritivas
print("=== Cenário A — sem VPN ===")
print(f"n: {len(a)}")
print(f"Média: {a.mean():.2f}")
print(f"Desvio padrão: {a.std():.2f}")
print(f"Min: {a.min()} | Max: {a.max()}")

print("\n=== Cenário B — com VPN ===")
print(f"n: {len(b)}")
print(f"Média: {b.mean():.2f}")
print(f"Desvio padrão: {b.std():.2f}")
print(f"Min: {b.min()} | Max: {b.max()}")

# Teste t de Student bicaudal
t_stat, p_value = stats.ttest_ind(a, b)
print(f"\n=== Teste t de Student bicaudal ===")
print(f"t: {t_stat:.4f}")
print(f"p-value: {p_value:.10f}")
if p_value < 0.05:
    print("Resultado: REJEITA H0 — diferenca estatisticamente significativa")
else:
    print("Resultado: NAO rejeita H0")

# Intervalo de confiança 95%
diff = a.mean() - b.mean()
se = np.sqrt(a.std()**2/len(a) + b.std()**2/len(b))
ic_low = diff - 1.96 * se
ic_high = diff + 1.96 * se
print(f"\n=== Intervalo de Confiança 95% ===")
print(f"Diferença entre médias: {diff:.2f}")
print(f"IC 95%: [{ic_low:.2f}, {ic_high:.2f}]")

# Gráfico boxplot
fig, ax = plt.subplots(figsize=(8, 6))
ax.boxplot([a, b], labels=['Sem VPN', 'Com VPN'], patch_artist=True,
           boxprops=dict(facecolor='lightblue'),
           medianprops=dict(color='red', linewidth=2))
ax.set_title('Queries DNS visíveis por sessão', fontsize=14)
ax.set_ylabel('Número de queries DNS', fontsize=12)
ax.set_xlabel('Cenário', fontsize=12)
ax.text(0.5, 0.95, f'p-value = {p_value:.2e}', transform=ax.transAxes,
        ha='center', va='top', fontsize=11,
        bbox=dict(boxstyle='round', facecolor='wheat'))
plt.tight_layout()
plt.savefig(r'C:\experimento\resultados\boxplot.png', dpi=150)
print("\nGráfico salvo em C:\\experimento\\resultados\\boxplot.png")
