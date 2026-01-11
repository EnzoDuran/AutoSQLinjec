SQL Injection Vulnerability Checker

This project is a Python application designed to detect SQL injection vulnerabilities in a web application by sending concurrent HTTP requests. It automates security testing by running multiple SQL injection payloads in parallel to identify potential backend failures.

How It Works
Imports and Setup

The project uses the following libraries:

requests for sending HTTP requests

concurrent.futures for managing concurrency

time for controlling delays between requests

The target URL and default query parameters are defined at the beginning of the script.

SQL Injection Detection

The function check_sql_injection(test_case) sends an HTTP request to the web application using a specific query value for each test case. The response is analyzed for signs of SQL injection vulnerabilities, such as:

HTTP 500 status codes

Database or application error messages

Test Case Handling

The function read_test_cases(file_path) reads SQL injection payloads from a text file, where each line represents a unique test case used during testing.

Concurrent Execution

A ThreadPoolExecutor is used to execute multiple HTTP requests in parallel (50 threads by default). A small delay is added between requests to reduce server overload. The script waits for all threads to complete before exiting.

Test Cases File

The project expects a file named test_cases.txt containing SQL injection payloads. Each line in the file should contain a single test case.

Purpose

This tool was created for learning and testing purposes, focusing on automating basic SQL injection detection through parallel requests.
