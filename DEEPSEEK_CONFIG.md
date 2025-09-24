# DeepSeek API 配置说明

## 手动创建 .env 文件

请在项目根目录下创建一个名为 `.env` 的文件，并添加以下内容：

```env
# DeepSeek API 配置
OPENAI_API_KEY=sk-34a3d5f1cfb94199b78c991ae41eee46
OPENAI_BASE_URL=https://api.deepseek.com

# 邮件发送配置（发送旅行计划邮件用，可选）
# 注意：如果不需要邮件功能，可以不配置这些
SENDGRID_API_KEY=your_sendgrid_api_key_here
FROM_EMAIL=your_verified_sender@example.com  # 必须是在SendGrid中验证过的发送者邮箱
TO_EMAIL=your_to_email@example.com
EMAIL_SUBJECT=你的旅行计划

# 搜索API配置（搜索航班和酒店用，可选）
SERPAPI_API_KEY=your_serpapi_api_key_here

# LangChain 可观测性配置（可选）
LANGCHAIN_API_KEY=your_langchain_api_key_here
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=ai_travel_agent
```

## 配置说明

1. **必需配置**：
   - `OPENAI_API_KEY`: 你的DeepSeek API密钥
   - `OPENAI_BASE_URL`: DeepSeek API端点

2. **可选配置**：
   - `SERPAPI_API_KEY`: 用于搜索航班和酒店信息
   - `SENDGRID_API_KEY`: 用于发送邮件功能
   - 邮件相关配置: `FROM_EMAIL`, `TO_EMAIL`, `EMAIL_SUBJECT`

## 代码修改

我已经修改了 `agents/agent.py` 文件，将模型从 OpenAI GPT-4o 更改为 DeepSeek Chat：

- 模型名称: `deepseek-chat`
- API端点: `https://api.deepseek.com`
- 支持通过环境变量配置

## 运行应用

配置完成后，使用以下命令运行应用：

```bash
conda activate ai-travel-agent
streamlit run app.py
```

应用将在 http://localhost:8501 启动。
