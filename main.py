import re

def verificar_forca_senha(senha):
    pontuacao = 0
    criterios = []

    # Critério 1: Comprimento mínimo (8 caracteres)
    if len(senha) >= 8:
        pontuacao += 1
    else:
        criterios.append("❌ A senha deve ter pelo menos 8 caracteres.")

    # Critério 2: Letras maiúsculas e minúsculas
    if re.search(r"[a-z]", senha) and re.search(r"[A-Z]", senha):
        pontuacao += 1
    else:
        criterios.append("❌ A senha deve conter letras maiúsculas e minúsculas.")

    # Critério 3: Números
    if re.search(r"\d", senha):
        pontuacao += 1
    else:
        criterios.append("❌ A senha deve conter pelo menos um número.")

    # Critério 4: Caracteres especiais
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha):
        pontuacao += 1
    else:
        criterios.append("❌ A senha deve conter pelo menos um caractere especial (!@#$%^&*).")

    # Avaliação final
    print("\n--- Resultado da Análise ---")
    if pontuacao == 4:
        print("🟢 Senha FORTE! Parabéns, sua senha é segura.")
    elif pontuacao >= 2:
        print("🟡 Senha MÉDIA. Pode melhorar adicionando mais complexidade.")
    else:
        print("🔴 Senha FRACA. Vulnerável a ataques de força bruta/dicionário.")

    if criterios:
        print("\nO que falta ajustar:")
        for erro in criterios:
            print(erro)

if __name__ == "__main__":
    print("=== Verificador de Segurança de Senhas ===")
    senha_usuario = input("Digite a senha que deseja testar: ")
    verificar_forca_senha(senha_usuario)