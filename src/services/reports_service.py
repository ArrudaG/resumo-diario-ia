from datetime import datetime
from pathlib import Path

def salvar_report(conteudo):
    agora = datetime.now()
    ano = agora.strftime("%Y")
    mes = agora.strftime("%m")
    data = agora.strftime("%Y-%m-%d")

    pasta = Path("reports") / ano / mes
    pasta.mkdir(parents=True, exist_ok=True)

    arquivo = pasta / f"{data}.md"

    with open(arquivo, "w", encoding="utf-8") as f:
        f.write(f"# Relatório Semanal - {data}\n\n")
        f.write(conteudo)

    return arquivo
