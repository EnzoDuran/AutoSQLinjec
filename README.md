Este projeto implementa uma aplicação em Python para verificar vulnerabilidades de injeção SQL em uma aplicação web, utilizando requisições HTTP concorrentes. O objetivo é automatizar a detecção de possíveis falhas de segurança relacionadas à injeção de SQL, realizando testes em paralelo com múltiplos casos de teste.

Funcionamento
Importações e Definições Iniciais:

As bibliotecas requests, concurrent.futures, e time são importadas para realizar requisições HTTP, gerenciar a concorrência e controlar o tempo entre as requisições, respectivamente.
A URL da aplicação a ser testada é definida, juntamente com os parâmetros de consulta padrão.
Verificação de Injeção SQL:

A função check_sql_injection(test_case) envia uma requisição HTTP à aplicação web com um parâmetro de consulta específico para cada caso de teste.
A resposta da aplicação é analisada em busca de sinais de falha, como código de status 500 ou mensagens de erro, que podem indicar uma vulnerabilidade de injeção SQL.
Leitura de Casos de Teste:

A função read_test_cases(file_path) lê um arquivo de texto contendo os casos de teste (um por linha) e retorna uma lista desses casos para ser utilizada na verificação.
Execução Concorrente:

Um ThreadPoolExecutor é criado para enviar múltiplas requisições em paralelo, utilizando um número especificado de threads (neste caso, 50).
Um pequeno atraso é introduzido entre o envio de cada requisição para evitar sobrecarga no servidor.
O script aguarda a conclusão de todas as requisições antes de finalizar.
Arquivo de Casos de Teste
O projeto espera que o arquivo test_cases.txt contenha os casos de teste que serão utilizados para verificar a presença de injeção SQL. Cada linha do arquivo deve representar um caso de teste único.
