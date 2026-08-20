# AI Finance Agent

An AI-powered personal finance assistant designed to ingest bank statements, normalize and validate financial transactions, store them in a database, and eventually use an AI agent to analyze spending and provide actionable insights.

> 🚧 This project is currently under development.

---

## Overview

Bank statements can come in different formats depending on the financial institution.

For example, one bank may provide:

```text
Date
Name / Description
Debit
Credit
Account Number
IBAN
```

while another may provide:

```text
Date
Name / Description
Debit/Credit
Amount (EUR)
Transaction Type
Notifications
```

The goal of this project is to build a robust data pipeline that converts these different formats into a standardized internal schema:
date
description
transaction_type
amount

Sensitive information that is not required for financial analysis, such as:

Bank account numbers
IBANs
Source/destination account information
Other unnecessary sensitive fields

is intentionally excluded from the standardized dataset.

Project Architecture

```text
The planned architecture is:
Bank Statement
      │
      ▼
┌─────────────┐
│  Ingestion  │
└──────┬──────┘
       ▼
┌────────────────┐
│ Transformation │
└──────┬─────────┘
       ▼
┌──────────────┐
│  Validation  │
└──────┬───────┘
       ▼
┌────────────┐
│  Database  │
└──────┬─────┘
       ▼
┌────────────┐
│ AI Agent   │
└──────┬─────┘
       ▼
┌───────────────────────┐
│ Analysis / Tools / AI │
└───────────────────────┘
```

The project is being developed incrementally, with a focus on clear separation of responsibilities between each layer.

Planned approaches:

Rule-based merchant categorization
LLM-assisted categorization
Evaluation of classification accuracy
AI Agent

The long-term goal is to build an agent capable of receiving natural-language requests and deciding which tools are required.

Example:

"Analyze my expenses this month, identify where I am spending the most, and suggest ways to save money."

The agent may eventually have access to tools such as:

Database queries
Python-based financial analysis
Document search
Chart generation
Report generation

AI Agent Architecture

The planned agent workflow is:
User Request
     │
     ▼
    LLM
     │
     ▼
Determine required tools
     │
     ├──────────────┐
     ▼              ▼
Database         Python
Query            Analysis
     │              │
     └───────┬──────┘
             ▼
        Tool Results
             │
             ▼
            LLM
             │
             ▼
      Final Response


This project is intended to explore concepts such as:

Tool calling
Agent loops
Planning
Structured outputs
Guardrails
Error handling
Observability
LLM evaluation
LLM

The project is planned to support a locally running open-source LLM through Ollama.

Using a local model allows development and experimentation without requiring a paid API for every interaction.

The LLM will not initially be responsible for every part of the system.

Instead, deterministic software components will handle tasks such as:

File ingestion
Data normalization
Validation
Database operations
Numerical calculations

The LLM will primarily be used where natural-language understanding or reasoning provides value.

Privacy

Financial data is sensitive.

The project follows a principle of data minimization: only information required for the application's functionality should be retained.

For example, the standardized transaction schema does not contain:

Account Number
IBAN
Source Account
Destination Account

The application is also being designed with local development and local LLM execution in mind.

Sample data used during development is synthetic and does not represent real banking information.

Technology Stack

Current / planned technologies:

Python
pandas
SQLite / PostgreSQL
Ollama
Open-source LLM
Docker
Git / GitHub

Additional libraries will be introduced as the project evolves.

Project Structure

Current structure:

ai-finance/
│
├── data/
│   └── sample.csv
│
├── src/
│   ├── main.py
│   ├── ingestion.py
│   ├── transformation.py
│   └── validation.py
│
├── .gitignore
├── README.md
└── .venv/

The virtual environment is intentionally excluded from version control.

Running the Project
1. Clone the repository
git clone <repository-url>
cd ai-finance
2. Create a virtual environment
python3 -m venv .venv
3. Activate the virtual environment

macOS / Linux:

source .venv/bin/activate
4. Install dependencies
pip install -r requirements.txt
5. Run the application
python src/main.py
Development Goals

The project is being developed with two goals in mind:

Engineering

Build a reliable financial data pipeline capable of handling inconsistent real-world input formats.

AI Engineering

Build an AI agent that combines an LLM with deterministic tools and structured financial data.

The key design principle is:

Use traditional software where deterministic logic is sufficient, and use AI where reasoning or natural-language understanding provides additional value.

Roadmap
Phase 1 — Data Pipeline
Ingestion
   ↓
Transformation
   ↓
Validation
Phase 2 — Database
Validated Transactions
          ↓
       Database
Phase 3 — Categorization
Transaction
     ↓
Merchant / Rules
     ↓
Category
Phase 4 — Local LLM
Transactions
     ↓
Ollama
     ↓
LLM-assisted analysis
Phase 5 — AI Agent
User
 ↓
Agent
 ↓
Tools
 ├── Database
 ├── Python
 ├── Charts
 └── Reports
Phase 6 — Production-oriented Improvements
Docker
Observability
Guardrails
Automated tests
Evaluation framework
Improved error handling
Better security and privacy controls
Why This Project?

This project is an opportunity to explore the intersection of:

Data engineering
Software engineering
Machine learning
LLMs
AI agents

Rather than treating an LLM as the entire application, the project focuses on building an AI system where the model operates as one component within a larger, structured software architecture.
