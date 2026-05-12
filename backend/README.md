# Flower Shop Backend

花店小程序后端API服务

## 技术栈

- FastAPI - Web框架
- SQLAlchemy - ORM
- MySQL - 数据库
- Docker - 容器化

## 快速启动

### 方式一：Docker (推荐)

```bash
docker-compose up -d
```

### 方式二：本地运行

```bash
pip install -r requirements.txt
cp .env.example .env  # 编辑 .env 配置数据库
python scripts/init_data.py
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## API 文档

启动后访问 http://localhost:8000/docs 查看交互式API文档

## 环境变量

| 变量 | 说明 | 默认值 |
|------|------|--------|
| DATABASE_URL | 数据库连接URL | mysql+pymysql://... |
| APP_NAME | 应用名称 | Flower Shop API |
| DEBUG | 调试模式 | true |
