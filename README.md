# 📬 Gmail AI Cleaner

An open-source CLI tool that uses a local LLM (via Ollama) to automatically clean up your Gmail inbox — without sending your data to any cloud service.

## ✨ Features

- 🤖 **AI-powered decisions** — Each email is analyzed individually by a local LLM
- 🔒 **100% local & private** — Your emails never leave your machine
- ⚡ **GPU accelerated** — Supports Vulkan backend for faster inference
- 📊 **Statistics report** — Summary of actions taken after each run
- 🔧 **Configurable** — Model and system prompt are fully customizable via `config.yaml`

## 🛠️ Requirements

- Python 3.10+
- [Ollama](https://ollama.com) installed and running
- A Google account with Gmail API access

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/dagsevenonur/gmail-ai-cleaner.git
cd gmail-ai-cleaner
```

### 2. Create a virtual environment and install dependencies

```bash
python -m venv .venv

# Windows
.\.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
```

### 3. Pull the model

```bash
ollama pull llama3.2
```

### 4. Set up Gmail API credentials

1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Create a new project
3. Enable the **Gmail API** under *APIs & Services*
4. Create **OAuth 2.0 credentials** (Desktop App)
5. Download `credentials.json` and place it in the project root

## 🚀 Usage

### Enable GPU acceleration (optional but recommended)

**Vulkan (recommended for Intel Arc, AMD):**
```bash
# Windows (PowerShell)
$env:OLLAMA_VULKAN="1"
ollama serve
```

### Run the tool

```bash
python main.py
```

On first run, a browser window will open for Gmail OAuth authentication. After that, a `token.json` file will be saved locally for future runs.

## ⚙️ Configuration

```yaml
# config.yaml
ollama:
  model: llama3.2
  system: |
    You are a Gmail cleanup assistant...
```

You can swap the model to any Ollama-supported model (e.g. `mistral`, `llama3.2:1b`, `gemma3:12b`).

## 📁 Project Structure

```
gmail-ai-cleaner/
├── main.py           # Entry point
├── client.py         # Gmail API client
├── auth.py           # OAuth authentication
├── model.py          # Ollama LLM integration
├── config.yaml       # Your local config (git-ignored)
├── requirements.txt
└── README.md
```

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or pull requests.

## 📄 License

Apache 2.0
