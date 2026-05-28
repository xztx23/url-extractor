#!/usr/bin/env python3
"""
从 GitHub API 返回的 JSON 数据中提取所有 download_url，
并添加 gh-proxy.com 前缀，输出带序号的文本。
"""

import json
import sys
import os

def extract_urls_with_proxy(data, proxy_prefix="https://gh-proxy.com/"):
    """
    从 data 中提取 download_url，并添加代理前缀。
    data 格式可以是:
        - 直接是数组: [{"download_url": "https://..."}, ...]
        - 或者包含 "output" 键: {"output": [{"download_url": "..."}, ...]}
    """
    # 如果是字典且包含 "output" 键，取 output 的值
    if isinstance(data, dict) and "output" in data:
        items = data["output"]
    else:
        items = data

    if not isinstance(items, list):
        raise ValueError("输入数据必须包含数组（直接或放在 output 键下）")

    urls = []
    for idx, item in enumerate(items, start=1):
        if isinstance(item, dict) and "download_url" in item:
            raw_url = item["download_url"]
            # 拼接代理前缀
            proxied_url = proxy_prefix + raw_url
            urls.append(f"{idx}.{proxied_url}")
    return "\n".join(urls)

def main():
    # 支持三种输入方式：
    # 1. 命令行参数指定 JSON 文件路径
    # 2. 从标准输入读取 JSON（管道或重定向）
    # 3. 直接作为参数传递 JSON 字符串（简单场景）
    if len(sys.argv) > 1:
        # 参数是文件路径
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        # 从标准输入读取
        input_str = sys.stdin.read()
        if not input_str:
            print("错误：未提供任何输入。请使用管道传入 JSON 或指定文件路径。", file=sys.stderr)
            sys.exit(1)
        data = json.loads(input_str)

    result = extract_urls_with_proxy(data)
    print(result)

if __name__ == "__main__":
    main()
