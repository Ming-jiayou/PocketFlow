from openai import OpenAI
import os
from duckduckgo_search import DDGS
import requests
import aiohttp
import asyncio
import json

# def call_llm(prompt):    
#     client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "your-api-key"))
#     r = client.chat.completions.create(
#         model="gpt-4o",
#         messages=[{"role": "user", "content": prompt}]
#     )
#     return r.choices[0].message.content

def call_llm(prompt):
    client = OpenAI(api_key="sk-cwranjpgrwjqfxkzcwcpulsvtifhcgkmrkuqrsnzbglgiikj", 
                    base_url="https://api.siliconflow.cn/v1")
    
    response = client.chat.completions.create(
        model="Qwen/Qwen2.5-72B-Instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    
    return response.choices[0].message.content

def search_web(query):
    results = DDGS().text(query, max_results=5)
    # Convert results to a string
    results_str = "\n\n".join([f"Title: {r['title']}\nURL: {r['href']}\nSnippet: {r['body']}" for r in results])
    return results_str

def search_web_brave(query):
    # 设置请求的URL
    url = f"https://api.search.brave.com/res/v1/web/search?q={query}"
    api_key = "BSA9cyvPikDePs5-0ClSBSKqP5KMnJp"
    # 设置请求头
    headers = {
        "accept": "application/json",
        "Accept-Encoding": "gzip",
        "x-subscription-token": api_key
    }
    # 发送GET请求
    response = requests.get(url, headers=headers)
    # 检查请求是否成功
    if response.status_code == 200:
        # 请求成功，解析返回的JSON数据
        data = response.json()
        results = data['web']['results']
        results_str = "\n\n".join([f"Title: {r['title']}\nURL: {r['url']}\nDescription: {r['description']}" for r in results])     
    else:
        # 请求失败，打印错误信息
        print(f"Request failed with status code: {response.status_code}")
    return results_str

if __name__ == "__main__":
    query = "2024年诺贝尔物理学奖得主是谁？"
    results_str = search_web_brave(query)
    if results_str:
        print(results_str)