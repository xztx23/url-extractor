# URL Extractor

从 GitHub API 返回的 JSON 数据（格式如 `{"output": [{"download_url": "..."}]}`）中提取所有图片下载链接，并自动添加 `https://gh-proxy.com/` 代理前缀，输出带序号的文本。

## 使用方法

### 1. 将 JSON 保存为文件（例如 `input.json`）
文件内容就是你从 Coze 上游节点复制出来的 JSON（完整对象）。

### 2. 运行脚本

```bash
python extract_urls.py input.json
