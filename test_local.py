
#for local testing purposes only
#from server import add_numbers, reverse_string, server_info, current_time, list_files, read_file

#print(add_numbers(5, 7))  # Expected output: 12
#print(reverse_string("Ashutosh"))  # Expected output: hsotuhsA
#print(server_info())  # Expected output: Server information dictionary
#print(current_time())  # Expected output: Current time dictionary
#print(list_files())
#print(read_file("example.txt"))
#print(read_file("../server.py")) #should fail
#print(read_file("../../../../etc/passwd")) #should fail

#from server import create_file, append_file, read_file

#print(create_file("ai_notes.txt", "This file was created by AI."))
#print(append_file("ai_notes.txt", "Second line added."))
#print(read_file("ai_notes.txt"))

#print(create_file("../hack.txt", "bad"))          # ❌
#print(create_file("evil.sh", "rm -rf /"))          # ❌
#print(append_file("big.txt", "x" * 10000))         # ❌

from server import store_memory, read_today_memory, list_memory_days

print(store_memory("Worked on MCP security and path traversal fixes."))
print(store_memory("Connected Claude Desktop to MCP successfully."))
print(read_today_memory())
print(list_memory_days())
