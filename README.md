# Bot de Cotação do Dólar (USD/BRL)

Este projeto é um bot em Python que automatiza a pesquisa da cotação do dólar em relação ao real (USD/BRL) e atualiza os dados em um arquivo Excel. O objetivo é monitorar a variação da cotação de forma simples e eficiente, mantendo um histórico organizado.

## Funcionalidades

- Obtém a cotação do dólar usando a API da [AwesomeAPI](https://docs.awesomeapi.com.br/).
- Atualiza as informações (data, hora, e cotação) em um arquivo Excel.
- Possui funcionalidade de agendamento para executar automaticamente em intervalos regulares (por padrão, a cada 1 hora).

## Tecnologias Utilizadas

- **Python 3.8 ou superior**
- Bibliotecas:
  - `requests`: Para realizar chamadas à API.
  - `openpyxl`: Para manipulação do arquivo Excel.
  - `schedule`: Para agendamento de tarefas.

## Pré-requisitos

1. Certifique-se de ter o Python 3.8 ou superior instalado.
2. Instale as bibliotecas necessárias com o seguinte comando:
   ```bash
   pip install requests openpyxl schedule
   ```

## Como Usar

### 1. Executar o Script Manualmente

- Clone este repositório:
  ```bash
  git clone https://github.com/cai0duque/cambio_dolar.git
  ```
- Navegue até o diretório do projeto:
  ```bash
  cd cambio_dolar
  ```
- Execute o script:
  ```bash
  python cotacao_dolar.py
  ```
- O arquivo Excel (`cotacao_dolar.xlsx`) será atualizado com as novas informações.

### 2. Rodar Como Serviço ou Programa Sempre Ativo

#### Windows
- Configure o script no **Agendador de Tarefas** para rodar em intervalos regulares ou ao iniciar o sistema.

#### Linux
- Crie um serviço usando `systemd` para manter o bot ativo em segundo plano. Veja instruções detalhadas no código.

#### MacOS
- Use `launchd` para configurar o script como um daemon sempre ativo.

### 3. Personalização
- Você pode alterar o intervalo de atualização modificando o agendamento na função `agendar_atualizacoes`:
  ```python
  schedule.every(1).hour.do(atualizar_excel)  # Atualizar a cada 1 hora
  ```

## Estrutura do Projeto

```plaintext
├── cotacao_dolar.py         # Script principal do projeto
├── cotacao_dolar.xlsx       # Arquivo Excel gerado automaticamente (após a execução do script)
├── README.md                # Documentação do projeto
└── requirements.txt         # Dependências do projeto
```

## Exemplo de Arquivo Excel

| Data       | Hora     | Cotação (USD/BRL) |
|------------|----------|-------------------|
| 07/01/2025 | 10:00:00 | 5.32              |
| 07/01/2025 | 11:00:00 | 5.34              |

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma [issue](https://github.com/cai0duque/cambio_dolar/issues) ou enviar um pull request.

## Autor

[Caio Duque](https://github.com/cai0duque)

---

