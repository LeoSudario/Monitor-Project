# Monitoramento de Página Web com Python e Relatório por E-mail

## Web Page Monitoring with Python and Email Reporting

---

> **Aviso:** Este projeto está em desenvolvimento e foi criado para fins de prática e aprendizado. Novas funcionalidades, melhorias e correções podem ser adicionadas futuramente. Sinta-se à vontade para contribuir ou adaptar para seus estudos!
>
> **Notice:** This project is under development and was created for practice and learning purposes. New features, improvements, and bug fixes may be added in the future. Feel free to contribute or adapt it for your studies!

---

## 🇧🇷 Documentação em Português

### Descrição

Este projeto tem como objetivo monitorar o tempo de atividade de uma página web utilizando Python.  
A aplicação registra o horário de início e término do monitoramento e envia essas informações por e-mail automaticamente.  
A ideia é evoluir o projeto para incluir inteligência artificial, análise de padrões de uso e geração automática de relatórios.

---

### Funcionalidades

- Abrir uma página web através do navegador controlado pelo Python (Selenium).
- Registrar o horário exato de início e término do monitoramento.
- Calcular o tempo total de atividade da página.
- Enviar as informações de monitoramento por e-mail automaticamente.
- Armazenar os dados para futuras análises.

---

### Como executar

#### 1. Instale as dependências

```bash
pip install selenium yagmail
```

Baixe o ChromeDriver e coloque-o no diretório do projeto ou no PATH.

#### 2. Configure o e-mail

No arquivo principal, preencha seus dados:

```python
EMAIL = "seuemail@gmail.com"
SENHA = "sua_senha_de_app"
DESTINATARIO = "destinatario@gmail.com"
```

> Recomenda-se usar senha de aplicativo do Gmail para maior segurança.

#### 3. Execute o monitoramento

```bash
python monitor_email.py
```

O script irá abrir a página, registrar os horários e enviar o relatório por e-mail ao encerrar.

---

### Melhorias Futuras

- Armazenar os dados em arquivos ou banco de dados para análise histórica.
- Criar gráficos e relatórios automáticos com pandas/matplotlib.
- Implementar modelos de IA para prever padrões de uso e detectar anomalias.
- Desenvolver uma interface web com Flask ou Streamlit.
- Automatizar o processo de monitoramento e envio em intervalos programados.
- Permitir monitoramento de múltiplas páginas simultâneas.

---

### Histórico de versões

- **v0.1**: Versão inicial, monitoramento simples e envio de relatório por e-mail.

---

### Licença

Este projeto é livre para uso acadêmico e pessoal.

---

## 🇬🇧 Documentation in English

### Description

This project aims to monitor the uptime of a web page using Python.  
The application records the exact start and end times of the monitoring and automatically sends this information by email.  
The idea is to evolve the project to include artificial intelligence, usage pattern analysis, and automatic report generation.

---

### Features

- Open a web page using a browser controlled by Python (Selenium).
- Record the exact start and end times of the monitoring.
- Calculate the total active time of the page.
- Send the monitoring information by email automatically.
- Store data for future analysis.

---

### How to run

#### 1. Install dependencies

```bash
pip install selenium yagmail
```

Download ChromeDriver and place it in the project directory or in your PATH.

#### 2. Configure your email

In the main script, fill in your data:

```python
EMAIL = "youremail@gmail.com"
PASSWORD = "your_app_password"
RECIPIENT = "recipient@gmail.com"
```

> It is recommended to use an app-specific password for Gmail for better security.

#### 3. Run the monitoring

```bash
python monitor_email.py
```

The script will open the web page, record the times, and send the report by email when finished.

---

### Future improvements

- Store data in files or databases for historical analysis.
- Create automatic graphs and reports with pandas/matplotlib.
- Implement AI models to predict usage patterns and detect anomalies.
- Develop a web interface using Flask or Streamlit.
- Automate the monitoring and email sending process at scheduled intervals.
- Allow monitoring of multiple pages simultaneously.

---

### Version history

- **v0.1**: Initial version, simple monitoring and email reporting.

---

### License

This project is free for academic and personal use.
