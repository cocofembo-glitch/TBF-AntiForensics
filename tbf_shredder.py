import os
import sys
import time
import random
import string
import gc
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.prompt import Prompt, Confirm

console = Console()

def clear_screen():
    os.system("clear" if os.name != "nt" else "cls")

def animate_letter_t():
    clear_screen()
    t_frames = [
        """
  [bold cyan]███████████████████████[/bold cyan]
  [bold cyan]███████████████████████[/bold cyan]
           [bold cyan]█████[/bold cyan]          
           [bold cyan]█████[/bold cyan]          
           [bold cyan]█████[/bold cyan]          
           [bold cyan]█████[/bold cyan]          
           [bold cyan]█████[/bold cyan]          
        """,
        """
  [bold blue]███████████████████████[/bold blue]
  [bold blue]  ███████████████████  [/bold blue]
           [bold blue]█████[/bold blue]          
           [bold blue]█████[/bold blue]          
           [bold blue]█████[/bold blue]          
           [bold blue]█████[/bold blue]          
           [bold blue]█████[/bold blue]          
        """,
        """
  [bold magenta]███████████████████████[/bold magenta]
  [bold magenta]    ███████████████    [/bold magenta]
           [bold magenta]█████[/bold magenta]          
           [bold magenta]█████[/bold magenta]          
           [bold magenta]█████[/bold magenta]          
           [bold magenta]█████[/bold magenta]          
           [bold magenta]█████[/bold magenta]          
        """,
        """
  [bold red]███████████████████████[/bold red]
  [bold red]███████████████████████[/bold red]
           [bold red]█████[/bold red]          
           [bold red]█████[/bold red]          
           [bold red]█████[/bold red]          
           [bold red]█████[/bold red]          
           [bold red]█████[/bold red]          
        """
    ]

    for _ in range(2):
        for frame in t_frames:
            clear_screen()
            console.print("\n\n" + frame)
            console.print("[bold yellow]      INITIALIZING TBF CORE...[/bold yellow]", justify="left")
            time.sleep(0.12)
            
    clear_screen()

def show_legal_disclaimer():
    clear_screen()
    disclaimer = (
        "[bold red]LEGAL DISCLAIMER & WARNING / ЮРИДИЧНЕ ЗАСТЕРЕЖЕННЯ[/bold red]\n\n"
        "[bold white]1. Автор інструмента (TBF Brand / cocofembo-glitch) НЕ НЕСЕ ЖОДНОЇ ВІДПОВІДАЛЬНОСТІ "
        "за будь-які дії користувачів, втрату даних або протиправне використання.[/bold white]\n\n"
        "[bold white]2. Цей інструмент розроблено ВИКЛЮЧНО для навчальних цілей, системного адміністрування "
        "та безпечного видалення власних конфіденційних файлів.[/bold white]\n\n"
        "[bold white]3. Використовуючи софт, ви повністю приймаєте ризик незворотного знищення обраної інформації.[/bold white]"
    )
    console.print(Panel(disclaimer, title="[bold red]ATTENTION[/bold red]", border_style="bold red"))
    console.print("\n[bold green]Натисніть Enter, щоб підтвердити згоду та перейти далі...[/bold green]")
    input()

def authenticate_key():
    clear_screen()
    secret_key = "COCOF.TBF"
    
    key_panel = Panel(
        f"[bold yellow]КЛЮЧ ДОСТУПУ ДО ШРЕДЕРА:[/bold yellow] [bold cyan]{secret_key}[/bold cyan]\n\n"
        "[bold white]Введіть цей ключ нижче, щоб розблокувати TBF Anti-Forensics Suite.[/bold white]",
        title="[bold red]SECURITY AUTHENTICATION[/bold red]",
        border_style="yellow"
    )
    
    while True:
        clear_screen()
        console.print(key_panel)
        user_input = Prompt.ask("\n[bold green]Введіть ключ доступу[/bold green]")
        
        if user_input.strip() == secret_key:
            console.print("\n[bold green][✓] Ключ підтверджено! Доступ надано...[/bold green]")
            time.sleep(1)
            break
        else:
            console.print("\n[bold red][!] Невірний ключ доступу! Спробуйте ще раз.[/bold red]")
            time.sleep(1.5)

def show_banner():
    clear_screen()
    banner = """
 [bold red]████████╗██████╗ ██████╗     ███████╗██╗██╗  ██╗███████╗[/bold red]
 [bold red]╚══██╔══╝██╔══██╗██╔══.      ██╔════╝██║██║  ██║██╔════╝[/bold red]
 [bold yellow]   ██║   ██████╔╝██████.     ███████╗██║███████║█████╗  [/bold yellow]
 [bold yellow]   ██║   ██╔══██╗██╔═══╝     ╚════██║██║██╔══██║██╔══╝  [/bold yellow]
 [bold green]   ██║   ██████╔╝██║         ███████║██║██║  ██║███████╗[/bold green]
 [bold green]   ╚═╝   ╚═════╝ ╚═╝         ╚══════╝╚═╝╚═╝  ╚═╝╚══════╝[/bold green]
    """
    console.print(Panel(banner, title="[bold white]TBF Anti-Forensics v1.0 ULTIMATE[/bold white]", subtitle="[bold cyan]Secure Data Shredder & Memory Purge Suite[/bold cyan]", border_style="bold red"))

def generate_random_name(length=14):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def wipe_file(file_path, passes=1, algorithm_name="Zero Fill"):
    if not os.path.exists(file_path):
        console.print(f"[bold red][!] Файл не знайдено:[/bold red] {file_path}")
        return False

    file_size = os.path.getsize(file_path)
    console.print(f"\n[bold yellow][*] Ціль:[/bold yellow] {file_path} ([bold cyan]{file_size} bytes[/bold cyan])")
    console.print(f"[bold yellow][*] Алгоритм:[/bold yellow] {algorithm_name} ({passes} проходів)\n")

    try:
        with open(file_path, "ba+", buffering=0) as f:
            for current_pass in range(1, passes + 1):
                f.seek(0)
                
                if passes == 1:
                    pattern = b'\x00' * 1024
                elif current_pass == 1:
                    pattern = b'\x00' * 1024
                elif current_pass == 2:
                    pattern = b'\xFF' * 1024
                else:
                    pattern = os.urandom(1024)

                written = 0
                with Progress(
                    SpinnerColumn(),
                    TextColumn(f"[bold red]Прохід {current_pass}/{passes}[/bold red]"),
                    BarColumn(),
                    TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
                    console=console
                ) as progress:
                    task = progress.add_task("Wiping...", total=file_size)
                    
                    while written < file_size:
                        chunk_size = min(1024, file_size - written)
                        f.write(pattern[:chunk_size])
                        written += chunk_size
                        progress.update(task, completed=written)

        dir_name = os.path.dirname(file_path)
        random_name = generate_random_name() + ".tmp"
        new_path = os.path.join(dir_name, random_name)
        
        os.rename(file_path, new_path)
        time.sleep(0.2)

        os.remove(new_path)
        gc.collect()

        console.print(f"\n[bold green][✓] Файл знищено! Метадані затирті, RAM очищено.[/bold green]")
        return True

    except Exception as e:
        console.print(f"\n[bold red][!] Помилка під час знищення:[/bold red] {e}")
        return False

def render_menu():
    table = Table(title="[bold yellow]ОБЕРІТЬ РЕЖИМ ОЧИЩЕННЯ[/bold yellow]", expand=True, border_style="red")
    table.add_column("№", style="bold red", justify="center", width=4)
    table.add_column("Алгоритм", style="bold white", width=22)
    table.add_column("Опис та рівень надійності", style="dim cyan")

    table.add_row("1", "Quick Zero Fill (1 прохід)", "Швидке перезаписування нулями 0x00")
    table.add_row("2", "DoD 5220.22-M (3 проходи)", "Військовий стандарт (Нулі -> Одиниці -> Рандом)")
    table.add_row("3", "Gutmann Lite (7 проходів)", "Максимальний хаос байтів проти криміналістики")
    table.add_row("0", "Вихід", "Завершити роботу")

    console.print(table)

def main():
    animate_letter_t()
    show_legal_disclaimer()
    authenticate_key()

    while True:
        show_banner()
        render_menu()

        choice = Prompt.ask("\nОберіть алгоритм", choices=["0", "1", "2", "3"], default="1")

        if choice == "0":
            console.print("[bold red]Завершення роботи TBF Anti-Forensics...[/bold red]")
            sys.exit()

        file_path = Prompt.ask("\n[bold yellow]Введіть шлях до файла для знищення[/bold yellow]")

        if not os.path.isfile(file_path):
            console.print("[bold red][!] Помилка: Вказаний шлях не є файлом або він відсутній![/bold red]")
            time.sleep(2)
            continue

        if Confirm.ask(f"[bold red]ЗНИЩИТИ файл {file_path} без можливості відновлення?[/bold red]"):
            if choice == "1":
                wipe_file(file_path, passes=1, algorithm_name="Quick Zero Fill")
            elif choice == "2":
                wipe_file(file_path, passes=3, algorithm_name="DoD 5220.22-M")
            elif choice == "3":
                wipe_file(file_path, passes=7, algorithm_name="Gutmann Lite")

        console.print("\n[bold green]Натисніть Enter, щоб повернутися в головне меню...[/bold green]")
        input()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[bold red][!] Роботу перервано.[/bold red]")

