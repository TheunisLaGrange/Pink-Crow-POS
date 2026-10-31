# 🐦 Pink Crow Café — Proprietary Franchise POS Terminal

A modular, lightweight, single-page POS terminal client framework designed for easy franchise deployment. This application utilizes a decoupled Python/Flask back-end routing engine to write daily transactional logs directly into data caches, mapped dynamically alongside an interactive, cartoon-style visual menu.

## 🚀 Single-Click Installation Guide

### Prerequisites
Before running the node application for the first time, ensure the host system has **Python 3.10 or newer** installed:
* **Windows:** Download via the Microsoft Store or from [python.org](https://python.org). Ensure you check **"Add Python to PATH"** during setup.

### 🏁 Launching the POS Terminal
1. Download and extract this project folder to your local folder directory workspace.
2. Double-click the file named **`run.bat`**.

*That's it!* The automated batch process will instantly:
* Compile a secure, isolated localized environment sandbox (`.venv`).
* Satisfy software packaging dependencies securely via `pip`.
* Launch your default web browser automatically directly to the checkout grid portal (`http://127.0.0.1:5000`).

---

## 📂 Structural Architecture Components
* **`server.py`:** Core backend traffic router engine routing transactional checkouts.
* **`static/menu.csv`:** Flat-file configuration menu item database database.
* **`templates/terminal.html`:** Tab-navigated client interface structure viewport framework.
* **`static/css/styles.css`:** Customized cartoon layout theme elements featuring signature pink accent bounding boxes.
* **`data_cache/`:** Automatically generated folder directory where active transaction rows are saved into daily CSV files.
