# 🐳 Docker Service Library

一套模組化的 Docker Compose 集合工具包，提供常見基礎設施與開發工具的快速啟動能力。

 🧾 設計目標：**可擴展 / 低維護 / 自動發現 / 即開即用**


## 1️⃣ 專案結構

```
docker-library/
├── database/
├── dev_tools/
├── identity/
├── reverse_proxy/
└── README.md
```



## 2️⃣ 模組設計

採用「分類資料夾 + 子服務」設計：

```
<category>/<service>/docker-compose.yml
```

### 📁 範例

```
database/mysql/docker-compose.yml
database/redis/docker-compose.yml
dev_tools/grafana/docker-compose.yml
```

**任何新服務只需新增資料夾即可，不需要修改 README**



## 3️⃣ 查看服務

### 方法 1：直接列出目錄

```bash
find . -name "docker-compose.yml"
```

或：

```bash
tree -L 2
```



### 方法 2：分類瀏覽

```bash
ls database
ls dev_tools
ls identity
ls reverse_proxy
```



## 4️⃣ 使用方式

### ① 進入服務

```bash
cd <category>/<service>
```

例如：

```bash
cd database/mysql
```



### ② 啟動服務

```bash
docker-compose up -d --build
```



### ③ 停止服務

```bash
docker-compose down
```


### ④ 查看狀態

```bash
docker-compose ps
```


## 5️⃣ 通用配置規範

所有服務遵循統一設計：

### ① 環境變數

使用 `.env`：

```
.env
docker-compose.yml
```


### ② 資料持久化

```yaml
volumes:
  - ./data:/data
```

### ③ Port 

避免衝突：

* DB：30000+
* Dev Tools：31000+
* Proxy：80 / 443
（...）



## 6️⃣ 可觀測性

本專案採用「可插拔式監控架構」，可依需求自由組合既有服務。




### 🧪 Type1 : 本地開發

```text
grafana + 任一 database
```

範例：

```bash
dev_tools/grafana
database/mysql
```

👉 用途：

* 快速查看資料或建立簡單 dashboard
* 搭配 `docker logs` 進行除錯



### 🧪 Type2 : 基礎監控

```text
grafana + redis + database
```

範例：

```bash
dev_tools/grafana
database/postgres
database/redis
```

👉 用途：

* 觀察 DB / cache 使用情況
* 建立基本系統監控（connections / memory 等）



### 🧪 Type3 : DevOps/系統監控

```text
grafana + portainer + database
```

範例：

```bash
dev_tools/grafana
dev_tools/portainer
database/mongodb
```

👉 用途：

* Grafana：指標與視覺化
* Portainer：容器狀態 / 資源監控
* DB：實際 workload



### 🧪 Type4 : 微服務觀測

```text
grafana + nginx + redis + database
```

範例：

```bash
dev_tools/grafana
reverse_proxy/nginx
database/redis
database/postgres
```

👉 用途：

* Nginx：流量入口
* Redis：快取層
* DB：資料層
* Grafana：統一觀察



### 🧪 Type5 : 含身份驗證的系統

```text
grafana + keycloak + database
```

範例：

```bash
dev_tools/grafana
identity/keycloak
database/postgres
```

👉 用途：

* Keycloak：Auth / SSO
* DB：儲存使用者資料
* Grafana：觀察登入 / 使用情況


## 7️⃣ 設計原則

* **📦 Plug & Play**：每個服務獨立
* **🧩 可擴展**：新增服務零修改 README
* **🔌 低耦合**：服務可自由組合
* **🛠 統一操作**：所有服務操作一致


---
![License](https://img.shields.io/badge/license-MIT-green)
![Docker](https://img.shields.io/badge/Docker-ready-brightgreen)



