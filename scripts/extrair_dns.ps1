# Script de extracao de queries DNS
# Uso: .\extrair_dns.ps1 -pasta capturas_sem_vpn -saida resultados\sem_vpn.csv

param(
    [string]$pasta,
    [string]$saida
)

$tshark = "C:\Program Files\Wireshark\tshark.exe"
$resultados = @()

$arquivos = Get-ChildItem "C:\experimento\$pasta\*.pcap*" | Sort-Object Name

foreach ($arquivo in $arquivos) {
    $queries = & $tshark -r $arquivo.FullName -Y "dns.flags.response == 0" -T fields -e dns.qry.name 2>$null | Where-Object { $_ -ne "" } | Sort-Object -Unique
    $contagem = ($queries | Measure-Object).Count
    $resultados += [PSCustomObject]@{
        Sessao  = $arquivo.Name
        Queries = $contagem
    }
    Write-Host "Processado: $($arquivo.Name) -> $contagem queries"
}

$resultados | Export-Csv -Path "C:\experimento\$saida" -NoTypeInformation -Encoding UTF8
Write-Host "Salvo em C:\experimento\$saida"
