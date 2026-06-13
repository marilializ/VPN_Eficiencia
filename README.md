<<<<<<< HEAD
﻿# Avaliação da Eficiência de VPNs na Redução da Exposição de Dados em Redes Wi-Fi Públicas

## Descrição
Experimento comparando a exposição de tráfego DNS em dois cenários: com e sem VPN, em rede Wi-Fi.

## Resultados
| Cenário | Média de queries DNS | Desvio padrão |
|---------|---------------------|---------------|
| Sem VPN | 339,60 | 11,30 |
| Com VPN | 0,13 | 0,35 |

- t = 164,42
- p-value = 4,04e-79
- IC 95%: [335,42 ; 343,51]
- Redução: 99,96%

## Ambiente
- Dispositivo: Notebook Snapdragon X Elite X1E78100, 16GB RAM
- SO: Windows 11 build 26200
- Navegador: Microsoft Edge 149.0.4022.52
- VPN: ProtonVPN 4.4.1 x64, WireGuard (UDP), servidor CA-FREE#16
- tshark: 4.6.6
- Npcap: 1.88
- Python: 3.12
- Selenium: 4.35.0

## Estrutura
- scripts/ — scripts de captura, navegação e extração
- data/ — CSVs com resultados
- analysis/ — script de análise estatística e gráfico
- capturas/ — arquivos .pcapng brutos

## Como reproduzir
1. Instalar Wireshark 4.6.6 e Npcap 1.88
2. Instalar Python 3.12 e dependências:
   pip install selenium webdriver-manager scipy pandas matplotlib
3. Instalar ProtonVPN
4. Desativar DNS seguro no navegador
5. Ajustar IP no scripts/capturar.py para o IP do dispositivo
6. Cenário A — sem VPN: python scripts/capturar.py
7. Cenário B — com VPN: ativar ProtonVPN e rodar python scripts/capturar.py
8. Análise: python analysis/analisar.py

## Hipóteses
- H0: VPN não reduz significativamente o número de queries DNS visíveis
- H1: VPN reduz significativamente o número de queries DNS visíveis
=======
# VPN_Eficiencia
Repositório destinado aos testes realizados no estudo de Henrique Antunes, Luís Antônio Godoy e Marília Liz Lima, com o intuito de avaliar a eficiência de VPNs na redução da exposição de dados em redes Wi-Fi públicas
>>>>>>> 99da279a4ac1fe43827736dd4b9402c51027a21e
