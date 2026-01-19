
from mcp.server.fastmcp import FastMCP
from datetime import datetime, date, timedelta 
import os
from pathlib import Path

# Creates MCP server instance

mcp = FastMCP("my_mcp_server")

BASE_DIR = Path(__file__).parent
SANDBOX_DIR = BASE_DIR / "sandbox"
MAX_WRITE_SIZE = 5_000 #5000 CHARACTERS
ALLOWED_EXTENSIONS = {".txt", ".md", ".log"}
MEMORY_DIR = SANDBOX_DIR / "memory"
MEMORY_DIR.mkdir(exist_ok=True)

#------------Tools---------------#

@mcp.tool()

def add_numbers(a:int,b:int)->int:
    """Adds two numbers and returns the result."""
    return print(a + b)

@mcp.tool()
def reverse_string(text:str)->str:
    """Reverses the input string and returns it. """
    return text[::-1]


#------------Resource---------------#

@mcp.tool()
def server_info()->dict:
    """Basic information about the server."""
    return {
        "server_name": "Divyansh's MCP Server",
        "version": "1.0.0-beta",
        "language": "Python",
        "purpose": "Demonstration of MCP server capabilities"
    }

@mcp.tool()
def current_time()->dict:
    """Returns the current server time."""
    return {
        "current_time": datetime.now().isoformat(),
    }

@mcp.tool()
def list_files()->list[str]:
    """Lists Files present in the sandbox directory"""
    if not SANDBOX_DIR.exists():
        return []
    return[
        file.name
        for file in SANDBOX_DIR.iterdir()
        if file.is_file()
    ]
@mcp.tool()
def read_file(filename: str) -> str:
    """
    Securely read a file from the sandbox directory.
    Prevents directory traversal attacks.
    """
    try:
        # Resolve real absolute path
        file_path = (SANDBOX_DIR / filename).resolve()

        # Ensure file is inside sandbox
        if not str(file_path).startswith(str(SANDBOX_DIR.resolve())):
            return "Error: Access denied."

        if not file_path.exists():
            return "Error: File does not exist."

        if not file_path.is_file():
            return "Error: Not a file."

        return file_path.read_text(encoding="utf-8")

    except Exception as e:
        return f"Error: {str(e)}"
    
def is_safe_filename(filename: str) -> bool:
    return (
        filename
        and "/" not in filename
        and "\\" not in filename
        and Path(filename).suffix in ALLOWED_EXTENSIONS
    )

def create_file(filename:str,content:str)->str:
    """
    Securely create a file in the sandbox directory.
    """
    if not is_safe_filename(filename):
        return "Error: Invalid filename."
    if len(content) > MAX_WRITE_SIZE:
        return "Error: Content exceeds maximum allowed size."    
    file_path = (SANDBOX_DIR / filename).resolve()

    if not str(file_path).startswith(str(SANDBOX_DIR.resolve())):
        return "Error: Access denied."
    if file_path.exists():
        return "Error: File already exists."
    file_path.write_text(content, encoding="utf-8")
    return "File created successfully."
@mcp.tool()
def append_file(filename:str, content:str)->str:
    """
    Appends contents to an existing file in the sandbox directory.
    """
    if not is_safe_filename(filename):
        return "Error: Invalid filename."
    if len(content) > MAX_WRITE_SIZE:
        return "Error: Content is too large."
    file_path = (SANDBOX_DIR / filename).resolve()
    if not str(file_path).startswith(str(SANDBOX_DIR.resolve())):
        return "Error: Access denied"
    if not file_path.exists():
        return "Error: File does not exist."
    
    with open(file_path, "a", encoding="utf-8") as f:
        f.write("\n" + content)
        return "Content appended successfully."
    
@mcp.tool()
def store_memory(text: str) -> str:
    """
    Store a memory/note for today with a timestamp.
    Use this to save thoughts, tasks, ideas, or logs.
    """    
    if len(text) > 2000:
        return "Error: Memory too long."
    
    today = date.today().isoformat()
    file_path = (MEMORY_DIR / f"{today}.md").resolve()

    if not str(file_path).startswith(str(MEMORY_DIR.resolve())):
        return "Error: Access denied."
    
    timestamp = datetime.now().strftime("%H:%M:%S")
    entry = f" - [{timestamp}] {text}\n"

    with open(file_path, "a", encoding="utf-8") as f:
        f.write(entry)
        return "Memory stored successfully."
    
@mcp.tool()
def read_today_memory() -> str:
    """
    Read all memories stored today.
    """
    today = date.today().isoformat()
    file_path = MEMORY_DIR / f"{today}.md"

    if not file_path.exists():
        return "No memories stored today."
    
    return file_path.read_text(encoding="utf-8")

@mcp.tool()
def list_memory_days() -> list[str]:
    """
    List days for which memory exists.
    """

    return sorted(
        f.stem for f in MEMORY_DIR.iterdir() if f.is_file()
    )
@mcp.tool()
def search_memory(keyword: str) -> str:
    """
    Search all stored memories for a keyword.
    Returns matching entries with dates
    """
    keyword = keyword.lower()
    results = []

    for file in MEMORY_DIR.iterdir():
        if not file.is_file():
            continue

        date_label = file.stem
        lines = file.read_text(encoding="utf-8").splitlines()

        for line in lines:
            if keyword in line.lower():
                results.append(f"{date_label} {line}")

    if not results:
        return "No matching memories found."
    return "\n".join(results)            

@mcp.tool()
def read_memory_for_day(date_str: str) -> str:

    """
    Read memories for a specific date (YYYY-MM-DD).
    """

    file_path = MEMORY_DIR / f"{date_str}.md"

    if not file_path.exists():
        return f"No memories found for {date_str}."
    
    return file_path.read_text(encoding="utf-8")


@mcp.tool()
def read_yesterday_memory() -> str:
    """
    Read memories stored yesterday.
    """
    yesterday = date.today() - timedelta(days=1)
    file_path = MEMORY_DIR / f"{yesterday.isoformat()}.md"

    if not file_path.exists():
        return "No memories stores yesterday."
    
    return file_path.read_text(encoding="utf-8")

@mcp.tool()
def get_memory_last_n_days(days: int) -> str:
    """
    Retrieve memory entries from the last N days.
    """
    if days <= 0 or days >30:
        return "Error: days must be between 1 and 30."
    
    today = date.today()
    entries = []

    for i in range(days):
        day = today - timedelta(days=i)
        file_path = MEMORY_DIR / f"{day.isoformat()}.md"

        if file_path.exists():
            content = file_path.read_text(encoding="utf-8")
            entries.append(f"## {day.isoformat()}\n{content}")

        if not entries:
            return "No memories entries found."

        return "\n".join(entries)    
    
@mcp.tool()
def get_last_week_memory() -> str:
    """
    Retrieve memory entries from the last 7 days.
    """
    return get_memory_last_n_days(7)
    

if __name__ == "__main__":
    print("🚀 MCP File System Server running (read-only)")
    mcp.run()

