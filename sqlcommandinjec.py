import requests
import concurrent.futures
import time

# Define the application's URL and parameters
url = "http://testphp.vulnweb.com/"
params = {"query": ""}

# Função para verificar se há possível injeção SQL
def check_sql_injection(test_case):
    local_params = params.copy()  # Cria uma cópia dos parâmetros para evitar problemas de thread-safety
    local_params["query"] = test_case
    response = requests.get(url, params=local_params)
    # Verifique a resposta para sinais de injeção SQL
    if response.status_code == 500 or "Error" in response.text:
        print(f"Potential SQL injection detected: {test_case}")
# Função para ler casos de teste do arquivo
def read_test_cases(file_path):
    with open(file_path, 'r') as file:
        test_cases = file.readlines()
    return [test_case.strip() for test_case in test_cases]

# Caminho para o arquivo de casos de teste
file_path = 'test_cases.txt'

# Obtendo os casos de teste
test_cases = read_test_cases(file_path)
#threads 
num_threads = 50

# Cria um ThreadPoolExecutor para executar as requisições em paralelo
with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
    futures = []
    for test_case in test_cases:
        # Envia a tarefa para o executor e armazena o futuro
        futures.append(executor.submit(check_sql_injection, test_case))
        # Atraso entre o envio de cada tarefa
        time.sleep(0.01)

    # Espera todas as tarefas serem concluídas
    concurrent.futures.wait(futures)
