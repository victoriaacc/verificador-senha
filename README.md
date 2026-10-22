# Verificador de Segurança de Senhas (Password Strength Checker)

Uma ferramenta simples e eficiente desenvolvida em **Python** para analisar o nível de robustez e segurança de senhas, simulando validações essenciais de **Cybersecurity** contra ataques de força bruta e dicionário.

---

## O que este projeto faz?

O script avalia senhas inseridas pelo usuário com base em critérios fundamentais de segurança da informação:
- **Comprimento mínimo:** Verifica se a senha possui pelo menos 8 caracteres.
- **Complexidade de caracteres:** Checa a presença combinada de letras maiúsculas e minúsculas.
- **Dígitos numéricos:** Confere se inclui números.
- **Caracteres especiais:** Valida a utilização de símbolos (como `!`, `@`, `#`, `$`, etc.).

Ao final, o programa classifica a senha em **Forte 🟢**, **Média 🟡** ou **Fraca 🔴** e exibe um feedback detalhado com o que falta para torná-la segura.

---

## Tecnologias Utilizadas

- **Python 3** (Linguagem principal)
- **Módulo `re`** (Expressões regulares para validação de padrões)

---

## Como executar o projeto na sua máquina

Certifique-se de ter o [Python](https://www.python.org/) instalado no seu computador.

1. Clone este repositório:
   ```bash
   git clone https://github.com/victoriaacc/verificador-senha.git
