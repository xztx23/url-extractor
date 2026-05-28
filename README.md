# url-extractor
从GitHub API返回的JSON数据（格式如 `{"output": [{"download_url": "https://..."}]}`）中提取所有 `download_url`，自动添加 `https://gh-proxy.com/` 代理前缀，并输出带序号的链接列表。适用于批量处理图片链接提取场景。
