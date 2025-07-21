
## 🛠️ Base do Projeto

Este projeto foi baseado em um tutorial do canal **TreinaWeb**, com diversas adaptações e melhorias pessoais, como:

- Implementação de botão checkbox com data de finalização
- Contadores dinâmicos de tarefas pendentes e concluídas
- Melhorias na experiência visual usando Bootstrap

---

## 🎯 Objetivo

Criar uma aplicação web para gerir tarefas do dia a dia com um CRUD completo.

---
## ⚙️ Funcionalidades

- ✅ Criar uma nova tarefa
- 📄 Listar todas as tarefas
- ✏️ Atualizar tarefas existentes
- ❌ Deletar tarefas
- ✔️ Marcar tarefas como concluídas (com data de finalização)
- 🔁 Contador de tarefas totais, concluídas e pendentes
- 🧠 Feedback visual com Bootstrap

---

## 🚀 Tecnologias Utilizadas

- Python 3.13
- Django 5.2.4
- HTML5
- Bootstrap 5
- SQLite
- VSCode (com alguns plugins de produtividade)

### 🔌 Plugins recomendados do VSCode

- MySQL (Database Client)
- Django (Baptiste Darthenay)
- Database Client JDBC (Database Client)
- Python, Python Debugger, Pylance (Microsoft)
- SQLite Viewer (Florian Klampfer)
---

## ▶️ Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/Wefrit/CRUD
   ```

2. Crie e ative o ambiente virtual:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # No Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Rode as migrações:
   ```bash
   python manage.py migrate
   ```

5. Execute o servidor:
   ```bash
   python manage.py runserver
   ```

6. Acesse no navegador:
   ```
   http://localhost:8000
   ```

---

## 🗂️ Estrutura de Pastas

```
TWTODOS/
│
├── .venv/
├── .vscode/
│
├── setup/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── todos/
│   ├── models.py
│   ├── views.py
│   ├── migrations/
│   └── templates/todos/
│       ├── todo_list.html
│       ├── todo_form.html
│       └── todo_update.html
│
├── db.sqlite3
└── manage.py
```


---

Criado por Nathan Lopes
