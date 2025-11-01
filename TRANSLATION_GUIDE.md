# Translation Guide - Automated with GitHub Copilot Agent

## ⚡ TL;DR - 1 Day Translation Plan

**Use GitHub Copilot Agent mode** to translate everything automatically in 6-8 hours.

**Only 3 things to check manually:**
1. 🔴 Agent prompts still route correctly
2. 🔴 Korean keywords are bilingual (keep Korean + add English)
3. 🔴 Test agent behavior before/after

---

## 🤖 GitHub Copilot Agent - Automated Translation

### Setup (5 minutes)

1. Install **GitHub Copilot** extension in VS Code
2. Open Copilot Chat panel (`Cmd+I` on Mac, `Ctrl+I` on Windows)
3. Make sure you're in **Agent mode** (not Edit mode)
4. Agent will automatically handle multi-file operations

### Step 1: Translate All Documentation (2 hours)

**Copilot Agent Prompt:**

```
Translate all Korean text to English in these files:
- README.md
- CONFIGURATION.md
- PREREQUISITES.md
- OBSERVABILITY.md
- DEVCONTAINER.md
- MODEL_CHANGE_GUIDE.md

Rules:
- Keep emoji and formatting
- Keep technical terms (Agent, Container Apps, Azure, etc.)
- Keep environment variable names unchanged
- Translate headings from "한글 (English)" to just "English"
- Keep URLs and file paths unchanged
```

**Agent will translate files one by one automatically** → Review and accept changes!

---

### Step 2: Translate All Notebooks (2 hours)

**Copilot Agent Prompt:**

```
Translate all Korean markdown cells to English in notebooks:
- 01_deploy_azure_resources.ipynb
- 02_setup_ai_search_rag.ipynb
- 03_deploy_foundry_agent.ipynb
- 04_deploy_foundry_agent_with_maf.ipynb
- 05_maf_workflow_patterns.ipynb
- 06_maf_dev_ui.ipynb
- 07_evaluate_agents.ipynb

Rules:
- Translate markdown cells to English
- Translate Korean text in print() statements in code cells
- Translate code comments in code cells to English
- Keep Python code logic unchanged
- Keep variable names and values unchanged
- Keep environment variable names unchanged
```

**Agent will process notebooks systematically** → Review and accept changes!

---

### Step 3: Translate Python Code - SAFE Parts (1 hour)

**Copilot Agent Prompt:**

```
Translate Korean comments and docstrings to English in:
- src/foundry_agent/api_server.py
- src/agent_framework/api_server.py
- src/mcp/server.py
- show_eval_results.py

Rules:
- Translate docstrings and comments only
- Keep function names unchanged
- Keep variable names unchanged
- Translate print statements
```

**Agent will handle code translations carefully** → Review changes!

---

### Step 4: Translate Python Code - CRITICAL Parts (2 hours + testing)

**⚠️ This step requires manual review!**

**Copilot Agent Prompt:**

```
Translate all agent prompts, instructions, and comments to English in:
- src/foundry_agent/main_agent.py
- src/foundry_agent/tool_agent.py
- src/foundry_agent/research_agent.py
- src/agent_framework/main_agent_workflow.py

CRITICAL RULES:
1. Translate ALL Korean text to English (comments, docstrings, instructions, examples)
2. Update keyword lists to English in main_agent_workflow.py:
   - tool_keywords: Use English keywords (weather, temperature, temp, forecast, climate, etc.)
   - research_keywords: Use English keywords (travel, trip, destination, tour, tourism, etc.)
3. Translate agent instruction examples to English
4. Translate Q&A examples to English
5. Keep city names as proper nouns (Seoul, Busan, Jeju)

WHAT TO TRANSLATE:
- All Korean comments and docstrings
- All Korean text in instruction strings
- All Korean keywords in keyword lists
- All Korean example queries
- All error messages

WHAT NOT TO TRANSLATE:
- Variable names, function names
- Environment variable names
- City proper nouns (Seoul, Busan, Jeju - already English)
```

**Agent will propose changes - carefully review before accepting!**

---

### Step 5: Translate Data, Evaluation, and DevContainer Files (1 hour)

**Copilot Agent Prompt:**

```
Translate all Korean text to English in:
- data/knowledge-base.json (title, content, category, section, subsection)
- evals/eval-queries.json (query, ground-truth)
- evals/eval-input.jsonl (Korean queries and responses)
- .devcontainer/devcontainer.json (comments only)
- .devcontainer/setup.sh (comments only)

RULES:
1. Translate all Korean text to English
2. Keep JSON structure, metadata, tags unchanged
3. Keep place names as proper nouns (Seoul, Busan, Jeju)
4. Keep configuration values and file paths unchanged
```

**Agent will handle JSON and config files carefully** → Review changes!



