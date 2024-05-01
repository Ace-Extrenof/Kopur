from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel

console = Console()

tasks = ['1) hello', '2) monke']
for task in tasks:
    renderable = Columns(task, equal=True,)
    new_renderable = Panel(renderable)
    console.print(new_renderable)
