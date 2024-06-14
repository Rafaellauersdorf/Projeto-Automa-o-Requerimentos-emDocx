import docx
import re
import os

def normalizar_texto(texto):
    """Remove pontuação e converte para minúsculas."""
    texto = re.sub(r'[.,!?;:]', '', texto)  # Remove apenas pontuação básica
    return texto.lower()

def substituir_frases_word(arquivo_entrada, arquivo_saida_base):
    """Substitui frases em um arquivo Word, mantendo a formatação original."""

    doc = docx.Document(arquivo_entrada)
    contador = 1

    while True:
        arquivo_saida = f"{arquivo_saida_base}_{contador}.docx"
        if not os.path.exists(arquivo_saida):
            break
        contador += 1

    while True:
        frase_antiga = input("Digite a frase a ser substituída (ou 'sair' para encerrar): ")
        if frase_antiga.lower() == 'sair':
            break

        frase_antiga_normalizada = normalizar_texto(frase_antiga)

        frase_nova = input("Digite a nova frase: ")

        for paragrafo in doc.paragraphs:
            texto_paragrafo = paragrafo.text
            texto_paragrafo_normalizado = normalizar_texto(texto_paragrafo)

            if frase_antiga_normalizada in texto_paragrafo_normalizado:
                for run in paragrafo.runs:
                    if frase_antiga_normalizada in normalizar_texto(run.text):
                        run.text = run.text.replace(frase_antiga, frase_nova)

    doc.save(arquivo_saida)
    print(f"Arquivo salvo como '{arquivo_saida}'")

if __name__ == "__main__":
    while True:
        arquivo_entrada = input("Digite o nome do arquivo Word de entrada (com extensão .docx): ")
        if os.path.exists(arquivo_entrada):
            break
        else:
            print("Arquivo não encontrado. Tente novamente.")

    arquivo_saida_base = input("Digite o nome base para o arquivo de saída (sem extensão): ")
    substituir_frases_word(arquivo_entrada, arquivo_saida_base)
