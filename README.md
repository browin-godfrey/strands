# strands agent
This project integrates Agentic AI (using Strands Agents) into our workflow to automatically perform security reviews and threat modelling.


agentic-ai-security-review/
│
├── README.md
├── requirements.txt
├── security_review.py      # Main Strands script
├── arch.png                # Sample architecture diagram
├── output/                 # Folder for storing generated reports
│   └── sample_report.txt
└── diagrams/
    └── architecture_flow.png


# Agentic AI for Automated Security Review using Strands

This project demonstrates how **Agentic AI** can be used in **Cybersecurity** to automate security reviews and threat analysis of architecture diagrams using the **Strands open-source AI agent SDK**.

Instead of manually performing reviews, this project uses AI agents to:
- Analyze architecture diagrams
- Identify vulnerabilities & threats (STRIDE framework)
- Generate structured security review reports
- Post summaries directly into ticketing systems

---

## 🚀 Features
- **Multi-Agent Workflow** using Strands' Swarm capability
- **Security Reviewer Agent** for deep-dive analysis
- **STRIDE Reporter Agent** for structured documentation
- **Image + Text Input** for contextual analysis
- **Customizable Prompts** for different review styles
- **Automated Report Generation**

---

## 📂 Project Structure
- `security_review.py` → Main script
- `arch.png` → Sample architecture diagram input
- `output/sample_report.txt` → Generated output report
- `diagrams/architecture_flow.png` → High-level workflow diagram

---

## 🛠️ Installation

1. **Clone the Repository**
```bash
git clone https://github.com/<your-username>/agentic-ai-security-review.git
cd agentic-ai-security-review
