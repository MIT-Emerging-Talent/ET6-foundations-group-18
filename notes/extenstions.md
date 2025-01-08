# 🚀 Guide: Installing and Running Ruff, Black, Pylint, and MarkdownLint in VS Code

This guide will help you set up and use Ruff, Black, Pylint, and MarkdownLint in
Visual Studio Code (VS Code) to maintain clean and consistent code and Markdown
files and pass all the CI checks.

---

## 🛠️ Prerequisites

Before starting, ensure the following are installed on your system:

- [Python](https://www.python.org/)
- [VS Code](https://code.visualstudio.com/)
- [Node.js](https://nodejs.org/) (for MarkdownLint)

---

## 🔧 Install Extensions in VS Code

1. Open VS Code.
2. Go to the Extensions Marketplace (`Ctrl+Shift+X` or `Cmd+Shift+X` on Mac).
3. Install the following extensions:
   - **Python** (by Microsoft)
   - **MarkdownLint** (by David Anson)

---

## ⚙️ Setting Up Ruff, Black, and Pylint

### 1️⃣ Install Ruff

Ruff is a fast Python linter and formatter.

```bash
pip install ruff
```

To integrate Ruff with VS Code:

1. Open the VS Code settings (`Ctrl+,` or `Cmd+,` on Mac).
2. Search for `Python › Linting: Enabled` and ensure it is checked.

### 2️⃣ Install Black

Black is a Python code formatter.

```bash
pip install black
```

To use Black in VS Code:

1. Go to the VS Code settings.
2. Search for `Python › Formatting: Provider` and set it to `black`.

### 3️⃣ Install Pylint

Pylint is a Python linter that checks for errors and enforces a coding standard.

```bash
pip install pylint
```

Enable Pylint in VS Code:

1. Open the VS Code settings.
2. Search for `Python › Linting: Pylint Enabled` and ensure it is checked.

---

## 📜 Setting Up MarkdownLint

MarkdownLint checks for style and consistency issues in Markdown files.

### Install MarkdownLint

1. Use npm to install MarkdownLint globally:

   ```bash
   npm install -g markdownlint-cli
   ```

### Run MarkdownLint

- **From the command line**:

  ```bash
  markdownlint yourfile.md
  ```

- **In VS Code**:
  MarkdownLint will automatically highlight issues in your `.md` files as you
edit them.

---

## ▶️ Running the Tools

### Run Ruff, Black, and Pylint for Python Files

1. **Ruff**:

   ```bash
   ruff path/to/your/code
   ```

2. **Black**:

   ```bash
   black path/to/your/code
   ```

3. **Pylint**:

   ```bash
   pylint path/to/your/code
   ```

### Run MarkdownLint for Markdown Files

1. **MarkdownLint**:

   ```bash
   markdownlint path/to/your/file.md
   ```

---

## 🎉 You're All Set

You are now ready to use Ruff, Black, Pylint, and MarkdownLint in VS Code to
ensure your code and documentation are clean, consistent, and professional.
Happy coding! 🚀
