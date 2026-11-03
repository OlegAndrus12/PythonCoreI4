from rich import print
from rich.table import Table

def print_table():
    table = Table(title="Top Libraries")
    
    table.add_column("Library", style="cyan", no_wrap=True)
    table.add_column("Purpose", style="magenta")
    
    table.add_row("Rich", "Beautiful terminal formatting")
    table.add_row("Typer", "CLI app made easy")
    table.add_row("Pydantic", "Data validation using type hints")
    print(table)


if __name__ == "__main__":
    print_table()