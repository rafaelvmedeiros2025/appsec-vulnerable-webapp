# AppSec Vulnerable Web App

A deliberately vulnerable web application created to demonstrate common web security vulnerabilities.

## Tech Stack

- Python
- Flask
- SQLite

---

# Vulnerability: SQL Injection

SQL Injection happens when user input is inserted directly into a SQL query without proper validation or parameterization.

In this application the query is built like this:

```python
query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
```

Because the input is concatenated directly into the query, an attacker can manipulate the SQL statement.

---

# Exploit

Authentication can be bypassed using the following payload:

```
http://localhost:5000/login?username=admin'--&password=x
```

The `--` comments out the rest of the SQL query, allowing login without knowing the password.

---

# Result

![SQL Injection Login Bypass](resources/logged.png)

The attacker successfully bypasses authentication.

---

# Solution

SQL Injection can be prevented by using **parameterized queries**.

Example:

```python
query = "SELECT * FROM users WHERE username=? AND password=?"
cursor.execute(query, (username, password))
```

Parameterized queries ensure that user input is treated as data instead of executable SQL.

---

# Disclaimer

This project is intentionally vulnerable and created for educational purposes only.
Do not deploy this application in production.