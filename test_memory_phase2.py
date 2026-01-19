
from server import (
    store_memory,
    search_memory,
    read_yesterday_memory,
    list_memory_days,
)

store_memory("Worked on Phase 2 memory search implementation.")
store_memory("Tested keyword-based memory retrieval.")

print(search_memory("memory"))
print(list_memory_days())
print(read_yesterday_memory())
