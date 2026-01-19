from server import read_file, create_file, append_file

tests = [
    ("Traversal read", lambda: read_file("../server.py")),
    ("Absolute read", lambda: read_file("/etc/passwd")),
    ("Traversal write", lambda: create_file("../hack.txt", "bad")),
    ("Overwrite", lambda: create_file("example.txt", "oops")),
    ("Bad extension", lambda: create_file("evil.exe", "oops")),
    ("Large write", lambda: append_file("example.txt", "A" * 10000)),
]

for name, test in tests:
    try:
        result = test()
        print(f"[{name}] → {result}")
    except Exception as e:
        print(f"[{name}] CRASHED → {e}")
