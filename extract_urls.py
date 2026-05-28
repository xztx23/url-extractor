#!/usr/bin/env python3
"""
从 JSON 文件中读取数据，提取所有 download_url，添加 gh-proxy.com 前缀，
输出带序号的列表，并保存到 Text/<student_id>.txt。
使用方法: python extract_urls.py <input.json> <student_id>
"""

import json
import sys
import os

def extract_urls_with_proxy(data, proxy_prefix="https://gh-proxy.com/"):
    # 兼容 {"output": [...]} 或直接 [...]
    if isinstance(data, dict) and "output" in data:
        items = data["output"]
    else:
        items = data

    if not isinstance(items, list):
        raise ValueError("输入数据必须包含数组（直接或放在 output 键下）")

    result_lines = []
    for idx, item in enumerate(items, start=1):
        if isinstance(item, dict) and "download_url" in item:
            raw_url = item["download_url"]
            proxied_url = proxy_prefix + raw_url
            result_lines.append(f"{idx}.{proxied_url}")
    return "\n".join(result_lines)

def main():
    if len(sys.argv) < 3:
        print("用法: python extract_urls.py <input.json> <student_id>", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    student_id = sys.argv[2]

    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    output_text = extract_urls_with_proxy(data)

    # 确保 Text 目录存在
    os.makedirs("Text", exist_ok=True)
    output_path = os.path.join("Text", f"{student_id}.txt")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(output_text)

    # 同时打印到控制台（以便在 Actions 日志中查看）
    print("提取完成！结果如下：")
    print(output_text)
    print(f"\n结果已保存至: {output_path}")

if __name__ == "__main__":
    main()
