# Streamlit-LLM

Streamlit 範例程式，實作 ChatGPT 與 LangChain

## 功能介紹

目前有以下功能：

- **聊天** (與 ChatGPT 進行聊天)
- **翻譯** (整合 LangChain 將輸入內容翻譯成選擇的語言)

## 前置作業

### 虛擬環境

安裝所需套件 (使用 [Poetry](https://blog.kyomind.tw/python-poetry/)，建議把環境安裝在專案目錄)：

```sh
poetry install
```

進入環境：

```sh
poetry shell
```

---

### 環境變數

依照 `.env.example` 的內容設定環境變數，並將其改名為 `.env`

## 使用方法

### 開啟 Streamlit 介面

使用 [make](https://tehub.com/a/aCYp1uw0tG) 指令 (用第二種方法安裝)：

```sh
make streamlit
```

不想用 `make` 的話，請使用指令：

```sh
streamlit run _home.py
```

基本上會自動開啟網頁，如果沒有的話請開啟網址 (`port` 預設為 8501)：

> <http://localhost:8501>

如果想修改 `port` ，請將指令改為：

```sh
streamlit run _home.py --server.port {port_number}
```

---

### 運行靜態檢查與自動排版

輸入指令：

```sh
make lint
```

不想用 `make` 的話，請依序執行以下指令：

```sh
ruff check --select I --fix
ruff format
ruff check
mypy .
```

## 測試方法

輸入指令就會自動執行 `tests` 資料夾內的所有測試：

```sh
pytest
```

也可以用 VS Code 自帶的測試功能
