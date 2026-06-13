import subprocess
import time
import os

TSHARK = r"C:\Program Files\Wireshark\tshark.exe"
IP = "192.168.68.56"
PASTA = r"C:\experimento\capturas_com_vpn"
INICIO = 4
FIM = 33

for i in range(INICIO, FIM + 1):
    nome = f"cvpn_{i:02d}.pcapng"
    arquivo = os.path.join(PASTA, nome)
    print(f"=== Sessao {i} de {FIM} ===")
    print(f"Iniciando captura: {nome}")

    proc = subprocess.Popen([
        TSHARK,
        "-i", "4",
        "-f", f"udp port 53 and host {IP}",
        "-w", arquivo
    ])

    time.sleep(5)
    print("Iniciando navegacao...")
    os.system("python C:\\experimento\\sessao_unica.py")

    time.sleep(10)
    proc.terminate()
    print("Captura encerrada.")
    time.sleep(10)

print("Todas as sessoes concluidas.")
