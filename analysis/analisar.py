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

# Gráfico de barras com barra de erro
fig, ax = plt.subplots(figsize=(8, 6))

cenarios = ['Sem VPN', 'Com VPN']
medias = [a.mean(), b.mean()]
desvios = [a.std(), b.std()]
cores = ['#e74c3c', '#2ecc71']

bars = ax.bar(cenarios, medias, yerr=desvios, capsize=8,
              color=cores, edgecolor='black', linewidth=0.8,
              error_kw=dict(elinewidth=1.5, ecolor='black'))

# Valores em cima das barras
for bar, media, desvio in zip(bars, medias, desvios):
    ax.text(bar.get_x() + bar.get_width()/2,
            bar.get_height() + desvio + 5,
            f'{media:.1f} ± {desvio:.1f}',
            ha='center', va='bottom', fontsize=11, fontweight='bold')

ax.set_title('Queries DNS visíveis por sessão\n(média ± desvio padrão)', fontsize=14)
ax.set_ylabel('Número de queries DNS', fontsize=12)
ax.set_xlabel('Cenário', fontsize=12)
ax.set_ylim(0, 420)

ax.text(0.5, 0.92,
        f'p-value = {p_value:.2e}  |  IC 95%: [{ic_low:.1f}, {ic_high:.1f}]',
        transform=ax.transAxes, ha='center', va='top', fontsize=10,
        bbox=dict(boxstyle='round', facecolor='lightyellow', edgecolor='gray'))

plt.tight_layout()
plt.savefig(r'C:\experimento\resultados\grafico.png', dpi=150)
print("\nGráfico salvo em C:\\experimento\\resultados\\grafico.png")
