<<<<<<< HEAD
# 批量翻译过程

该项目展示了一个批量处理实现，可以同时将文档翻译成多种语言。它旨在高效处理markdown文件的翻译，同时保持格式。
=======
<div align="center">
  <img src="https://github.com/The-Pocket/.github/raw/main/assets/title.png" alt="Pocket Flow – 100-line minimalist LLM framework" width="600"/>
</div>

[English](https://github.com/The-Pocket/PocketFlow/blob/main/README.md) | 中文 | [Español](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_SPANISH.md) | [日本語](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_JAPANESE.md) | [Deutsch](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_GERMAN.md) | [Русский](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_RUSSIAN.md) | [Português](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_PORTUGUESE.md) | [Français](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_FRENCH.md) | [한국어](https://github.com/The-Pocket/PocketFlow/blob/main/cookbook/pocketflow-batch/translations/README_KOREAN.md)
>>>>>>> 5e3b529b8f8440220020c1bde2b1fb017e12d342

## 功能

<<<<<<< HEAD
- 并行将markdown内容翻译成多种语言
- 将翻译后的文件保存到指定的输出目录

## 开始使用

1. 安装所需的软件包：
```bash
pip install -r requirements.txt
```

2. 设置你的API密钥：
```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

3. 运行翻译过程：
```bash
python main.py
```
=======
Pocket Flow 是一个[100行代码](https://github.com/The-Pocket/PocketFlow/blob/main/pocketflow/__init__.py)的极简主义LLM框架

- **轻量级**：仅100行代码。零臃肿，零依赖，零供应商锁定。
  
- **表达力强**：包含你喜爱的一切—([多-](https://the-pocket.github.io/PocketFlow/design_pattern/multi_agent.html))[智能体](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html)，[工作流](https://the-pocket.github.io/PocketFlow/design_pattern/workflow.html)，[RAG](https://the-pocket.github.io/PocketFlow/design_pattern/rag.html)等等。

- **[智能体编码](https://zacharyhuang.substack.com/p/agentic-coding-the-most-fun-way-to)**：让AI智能体（例如Cursor AI）构建智能体—生产力提升10倍！

Pocket Flow入门：
- 安装方式，```pip install pocketflow```或者直接复制[源代码](https://github.com/The-Pocket/PocketFlow/blob/main/pocketflow/__init__.py)（仅100行）。
- 了解更多，查看[文档](https://the-pocket.github.io/PocketFlow/)。了解动机，阅读[故事](https://zacharyhuang.substack.com/p/i-built-an-llm-framework-in-just)。
- 有问题？查看这个[AI助手](https://chatgpt.com/g/g-677464af36588191b9eba4901946557b-pocket-flow-assistant)，或[创建issue！](https://github.com/The-Pocket/PocketFlow/issues/new)
- 🎉 加入我们的[Discord](https://discord.gg/hUHHE9Sa6T)，与其他使用Pocket Flow构建应用的开发者交流！
- 🎉 Pocket Flow最初是Python版本，但我们现在有[Typescript](https://github.com/The-Pocket/PocketFlow-Typescript)，[Java](https://github.com/The-Pocket/PocketFlow-Java)，[C++](https://github.com/The-Pocket/PocketFlow-CPP)和[Go](https://github.com/The-Pocket/PocketFlow-Go)版本！
>>>>>>> 5e3b529b8f8440220020c1bde2b1fb017e12d342

## 工作原理

<<<<<<< HEAD
实现使用了一个 `TranslateTextNode` 来处理翻译请求的批量：
=======
当前的LLM框架过于臃肿... 你只需要100行代码就能构建LLM框架！
>>>>>>> 5e3b529b8f8440220020c1bde2b1fb017e12d342

```mermaid
flowchart LR
    batch[TranslateTextNode]
```

`TranslateTextNode`：
1. 准备多语言翻译的批次
2. 使用模型并行执行翻译
3. 将翻译后的内容保存到单个文件中
4. 保持原始markdown结构

<<<<<<< HEAD
这种方法展示了PocketFlow如何高效地并行处理多个相关任务。
=======
  |                | **抽象**          | **应用特定包装器**                                      | **供应商特定包装器**                                    | **代码行数**       | **大小**    |
|----------------|:-----------------------------: |:-----------------------------------------------------------:|:------------------------------------------------------------:|:---------------:|:----------------------------:|
| LangChain  | Agent, Chain               | 很多 <br><sup><sub>(例如，QA, 摘要)</sub></sup>              | 很多 <br><sup><sub>(例如，OpenAI, Pinecone等)</sub></sup>                   | 405K          | +166MB                     |
| CrewAI     | Agent, Chain            | 很多 <br><sup><sub>(例如，FileReadTool, SerperDevTool)</sub></sup>         | 很多 <br><sup><sub>(例如，OpenAI, Anthropic, Pinecone等)</sub></sup>        | 18K           | +173MB                     |
| SmolAgent   | Agent                      | 一些 <br><sup><sub>(例如，CodeAgent, VisitWebTool)</sub></sup>         | 一些 <br><sup><sub>(例如，DuckDuckGo, Hugging Face等)</sub></sup>           | 8K            | +198MB                     |
| LangGraph   | Agent, Graph           | 一些 <br><sup><sub>(例如，语义搜索)</sub></sup>                     | 一些 <br><sup><sub>(例如，PostgresStore, SqliteSaver等) </sub></sup>        | 37K           | +51MB                      |
| AutoGen    | Agent                | 一些 <br><sup><sub>(例如，Tool Agent, Chat Agent)</sub></sup>              | 很多 <sup><sub>[可选]<br> (例如，OpenAI, Pinecone等)</sub></sup>        | 7K <br><sup><sub>(仅核心)</sub></sup>    | +26MB <br><sup><sub>(仅核心)</sub></sup>          |
| **PocketFlow** | **Graph**                    | **无**                                                 | **无**                                                  | **100**       | **+56KB**                  |
>>>>>>> 5e3b529b8f8440220020c1bde2b1fb017e12d342

## 示例输出

当你运行翻译过程时，你将看到类似于以下的输出：

<<<<<<< HEAD
```
翻译的中文文本
翻译的西班牙文本
翻译的日文文本
翻译的德文文本
翻译的俄文文本
翻译的葡萄牙文本
翻译的法文文本
翻译的韩文文本
将翻译保存到 translations/README_CHINESE.md
将翻译保存到 translations/README_SPANISH.md
将翻译保存到 translations/README_JAPANESE.md
将翻译保存到 translations/README_GERMAN.md
将翻译保存到 translations/README_RUSSIAN.md
将翻译保存到 translations/README_PORTUGUESE.md
将翻译保存到 translations/README_FRENCH.md
将翻译保存到 translations/README_KOREAN.md

=== 翻译完成 ===
翻译已保存到：translations
============================
```

## 文件
=======
这[100行代码](https://github.com/The-Pocket/PocketFlow/blob/main/pocketflow/__init__.py)捕捉了LLM框架的核心抽象：图（Graph）！
<br>
<div align="center">
  <img src="https://github.com/The-Pocket/.github/raw/main/assets/abstraction.png" width="900"/>
</div>
<br>

从这里开始，很容易实现流行的设计模式，如([多-](https://the-pocket.github.io/PocketFlow/design_pattern/multi_agent.html))[智能体](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html)，[工作流](https://the-pocket.github.io/PocketFlow/design_pattern/workflow.html)，[RAG](https://the-pocket.github.io/PocketFlow/design_pattern/rag.html)等。
<br>
<div align="center">
  <img src="https://github.com/The-Pocket/.github/raw/main/assets/design.png" width="900"/>
</div>
<br>
✨ 以下是基础教程：

<div align="center">
  
|  名称  | 难度    |  描述  |  
| :-------------:  | :-------------: | :--------------------- |  
| [聊天](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-chat) | ☆☆☆ <br> *入门*   | 带有对话历史的基础聊天机器人 |
| [结构化输出](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-structured-output) | ☆☆☆ <br> *入门* | 通过提示从简历中提取结构化数据 |
| [工作流](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-workflow) | ☆☆☆ <br> *入门*   | 一个写作工作流，包括大纲编写、内容创作和样式应用 |
| [智能体](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-agent) | ☆☆☆ <br> *入门*   | 一个可以搜索网络并回答问题的研究智能体 |
| [RAG](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-rag) | ☆☆☆ <br> *入门*   | 一个简单的检索增强生成过程 |
| [批处理](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-batch) | ☆☆☆ <br> *入门* | 一个将markdown内容翻译成多种语言的批处理器 |
| [流式处理](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-llm-streaming) | ☆☆☆ <br> *入门*   | 具有用户中断功能的实时LLM流式演示 |
| [聊天护栏](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-chat-guardrail) | ☆☆☆ <br> *入门*  | 一个仅处理旅行相关查询的旅行顾问聊天机器人 |
| [Map-Reduce](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-map-reduce) | ★☆☆ <br> *初级* | 使用map-reduce模式进行批量评估的简历资格处理器 |
| [多智能体](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-multi-agent) | ★☆☆ <br> *初级* | 两个智能体之间异步通信的禁忌词游戏 |
| [监督者](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-supervisor) | ★☆☆ <br> *初级* | 研究智能体变得不可靠...让我们构建一个监督流程|
| [并行](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-parallel-batch) | ★☆☆ <br> *初级*   | 展示3倍加速的并行执行演示 |
| [并行流](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-parallel-batch-flow) | ★☆☆ <br> *初级*   | 展示使用多个过滤器实现8倍加速的并行图像处理演示 |
| [多数投票](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-majority-vote) | ★☆☆ <br> *初级* | 通过聚合多次解决方案尝试来提高推理准确性 |
| [思考](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-thinking) | ★☆☆ <br> *初级*   | 通过思维链解决复杂推理问题 |
| [记忆](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-chat-memory) | ★☆☆ <br> *初级* | 具有短期和长期记忆的聊天机器人 |
| [Text2SQL](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-text2sql) | ★☆☆ <br> *初级* | 使用自动调试循环将自然语言转换为SQL查询 |
| [MCP](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-mcp) | ★☆☆ <br> *初级* |  使用模型上下文协议进行数值运算的智能体 |
| [A2A](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-a2a) | ★☆☆ <br> *初级* | 使用智能体到智能体协议包装的智能体，用于智能体间通信 |
| [Web HITL](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-web-hitl) | ★☆☆ <br> *初级* | 具有SSE更新的人工审核循环的最小Web服务 |
>>>>>>> 5e3b529b8f8440220020c1bde2b1fb017e12d342

- [`main.py`](./main.py): 批量翻译节点的实现
- [`utils.py`](./utils.py): 调用Anthropic模型的简单包装器
- [`requirements.txt`](./requirements.txt): 项目依赖项

<<<<<<< HEAD
翻译内容保存在 `translations` 目录中，每个文件根据目标语言命名。
=======
👀 想看其他入门教程？[创建一个issue！](https://github.com/The-Pocket/PocketFlow/issues/new)

## 如何使用Pocket Flow？

🚀 通过**智能体编码**—最快的LLM应用开发范式—*人类设计*，*智能体编码*！

<br>
<div align="center">
  <a href="https://zacharyhuang.substack.com/p/agentic-coding-the-most-fun-way-to" target="_blank">
    <img src="https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F423a39af-49e8-483b-bc5a-88cc764350c6_1050x588.png" width="700" alt="IMAGE ALT TEXT" style="cursor: pointer;">
  </a>
</div>
<br>

✨ 以下是更复杂LLM应用的示例：

<div align="center">
  
|  应用名称     |  难度    | 主题  | 人类设计 | 智能体代码 |
| :-------------:  | :-------------: | :---------------------: |  :---: |  :---: |
| [用Cursor构建Cursor](https://github.com/The-Pocket/Tutorial-Cursor) <br> <sup><sub>我们很快将达到奇点...</sup></sub> | ★★★ <br> *高级*   | [智能体](https://the-pocket.github.io/PocketFlow/design_pattern/agent.html) | [设计文档](https://github.com/The-Pocket/Tutorial-Cursor/blob/main/docs/design.md) | [Flow代码](https://github.com/The-Pocket/Tutorial-Cursor/blob/main/flow.py)
| [代码库知识构建器](https://github.com/The-Pocket/Tutorial-Codebase-Knowledge) <br> <sup><sub>生命太短暂，不应该困惑地盯着他人的代码</sup></sub> |  ★★☆ <br> *中级* | [工作流](https://the-pocket.github.io/PocketFlow/design_pattern/workflow.html) | [设计文档](https://github.com/The-Pocket/Tutorial-Codebase-Knowledge/blob/main/docs/design.md) | [Flow代码](https://github.com/The-Pocket/Tutorial-Codebase-Knowledge/blob/main/flow.py)
| [询问AI Paul Graham](https://github.com/The-Pocket/Tutorial-YC-Partner) <br> <sup><sub>询问AI Paul Graham，以防你没被录取</sup></sub> | ★★☆ <br> *中级*  | [RAG](https://the-pocket.github.io/PocketFlow/design_pattern/rag.html) <br> [Map Reduce](https://the-pocket.github.io/PocketFlow/design_pattern/mapreduce.html) <br> [TTS](https://the-pocket.github.io/PocketFlow/utility_function/text_to_speech.html) | [设计文档](https://github.com/The-Pocket/Tutorial-AI-Paul-Graham/blob/main/docs/design.md) | [Flow代码](https://github.com/The-Pocket/Tutorial-AI-Paul-Graham/blob/main/flow.py)
| [Youtube摘要器](https://github.com/The-Pocket/Tutorial-Youtube-Made-Simple)  <br> <sup><sub> 像你5岁一样向你解释YouTube视频 </sup></sub> | ★☆☆ <br> *初级*   | [Map Reduce](https://the-pocket.github.io/PocketFlow/design_pattern/mapreduce.html) |  [设计文档](https://github.com/The-Pocket/Tutorial-Youtube-Made-Simple/blob/main/docs/design.md) | [Flow代码](https://github.com/The-Pocket/Tutorial-Youtube-Made-Simple/blob/main/flow.py)
| [冷启动生成器](https://github.com/The-Pocket/Tutorial-Cold-Email-Personalization)  <br> <sup><sub> 将冷门线索转变为热门的即时破冰工具 </sup></sub> | ★☆☆ <br> *初级*   | [Map Reduce](https://the-pocket.github.io/PocketFlow/design_pattern/mapreduce.html) <br> [Web搜索](https://the-pocket.github.io/PocketFlow/utility_function/websearch.html) |  [设计文档](https://github.com/The-Pocket/Tutorial-Cold-Email-Personalization/blob/master/docs/design.md) | [Flow代码](https://github.com/The-Pocket/Tutorial-Cold-Email-Personalization/blob/master/flow.py)

</div>

- 想学习**智能体编码**？

  - 查看[我的YouTube](https://www.youtube.com/@ZacharyLLM?sub_confirmation=1)获取关于如何制作上述应用的视频教程！

  - 想构建自己的LLM应用？阅读这篇[文章](https://zacharyhuang.substack.com/p/agentic-coding-the-most-fun-way-to)！从[这个模板](https://github.com/The-Pocket/PocketFlow-Template-Python)开始！
>>>>>>> 5e3b529b8f8440220020c1bde2b1fb017e12d342
