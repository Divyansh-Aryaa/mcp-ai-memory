
#  MCP AI Memory — Personal AI Ops Assistant

A **secure, local, MCP-based AI memory system** that enables an LLM (Claude Desktop) to **store, search, and reason over persistent personal memory** using controlled tools.

This project demonstrates how to build **agentic AI systems correctly**:
- LLMs do reasoning
- MCP servers execute actions
- State lives outside the model
- Security is enforced by design

---

##  What This Project Does

Using natural language prompts, the AI can:

-  Store timestamped memories persistently
-  Search across past memories
-  Understand time (“today”, “yesterday”, “last week”)
-  Generate weekly summaries and insights
-  Interact with a **sandboxed file system**
-  Operate under strict security constraints

All memory is stored **locally on disk**, not inside the LLM.

---

##  Example Commands (Try These in Claude Desktop)

###  Memory Storage

<img width="2364" height="1826" alt="1FE06EEE-EA83-46CE-87C1-E47EB263B42E" src="https://github.com/user-attachments/assets/a723c289-7335-49df-b2a1-9f804cbb1adc" />

### Understand time (“today”, “yesterday”, “last week”)

<img width="2366" height="1850" alt="724B1A40-DC7C-48B3-B8FF-F0A32B5B1A71" src="https://github.com/user-attachments/assets/fa2e93bf-2c5c-4df3-b87e-48a480ffc5e1" />

### Read and Append files through Claude LLM

<img width="2362" height="1844" alt="A76C80AC-FFB3-4096-B646-B01CA1ADE88C" src="https://github.com/user-attachments/assets/85d78945-ae57-4101-800f-29e386b60034" />


---

##  Security Guarantees

This project is **security-first by design**:

-  No direct LLM access to the filesystem
-  No path traversal (`../`, absolute paths blocked)
-  No file deletion or overwrite
-  No shell execution
-  Append-only writes
-  Size-limited content
-  Sandboxed directory enforcement

###  Expected-to-Fail Abuse Attempts

<img width="2362" height="1844" alt="A76C80AC-FFB3-4096-B646-B01CA1ADE88C" src="https://github.com/user-attachments/assets/2e2d60c7-9a00-4645-a0f6-e42ec6ee6e5d" />



- **LLM** → reasoning & planning  
- **MCP Server** → secure execution & memory management  
- **Filesystem** → long-term state  

This separation mirrors **production-grade AI agent architectures**.

---

##  Why MCP (Model Context Protocol)?

- Standardized AI ↔ tool communication
- Model-agnostic (not framework-locked)
- Clear separation of concerns
- Safer than ad-hoc tool calling
- Designed for long-lived agents

---

##  Tech Stack

- Python 3.11
- Model Context Protocol (MCP)
- Claude Desktop
- Secure local filesystem sandbox

---

##  Use Cases

- Personal AI memory / journaling
- AI-assisted productivity tracking
- Long-term research notes
- Secure local AI assistants
- MCP / agent infrastructure experiments

---

##  Future Enhancements

- Memory tagging & importance scoring
- Semantic search (embeddings)
- Goal tracking & progress analysis
- Multi-user support
- Encrypted memory storage

---

##  License

MIT License







