# 天命系统 LLM-Wiki 知识库全局强制规则（含 CLI 规范）

## 核心理念
人类只剪藏收集，LLM全权理解编译沉淀，知识自动生长复利。

## 三层结构强制规范
1. **raw/原始层**：只读不写、永不删除、永不修改，原始资料永久留存。
2. **wiki/知识层**：AI全权维护、自动更新、自动链接、自动合并迭代。
3. **schema/规则层**：系统永久规则，所有编译工作严格遵循。

## 同步规范
1. 多端同步通过 **Nutstore Sync 插件** 完成，宽松模式 + 智能合并
2. `.obsidian/nutstore-sync/` 和 `nutstore-sync/` 不纳入 Git 跟踪
3. 冲突文件由智能合并处理，复杂冲突由雅典娜人工审核

## CLI 操作规范
1. 人类/Agent可通过 `obsidian-cli clip [url]` 或 `obsidian-cli import [文件]` 向 raw/ 层归集知识，永不删改原始文件
2. raw/ 永久只读、不删、不改，CLI 自动归集的内容同样遵循
3. wiki/ 由雅典娜全权维护，自动双向链接、自动生成知识图谱
4. 标签统一、结构统一、命名干净无特殊符号，CLI 剪藏内容需自动打基础标签
5. 冲突文件保留双版本，由雅典娜合并，CLI 同步冲突时自动标记
6. 仅雅典娜可写，其他 Agent 只读，CLI 仅开放检索和归集权限
7. 每次 `obsidian-cli compile` 必须更新 index.md 和知识图谱

## 命名规范
所有文件命名：简洁中文、无特殊符号、日期前缀统一。

## 链接规范
所有知识必须添加Obsidian双向[[内部链接]]，必须关联对应业务与Agent。

## 更新规范
每次知识库同步后，自动更新总索引、自动去重、自动归档复盘踩坑记录。

## 系统核心铁律（绝对不可修改）

1. **雅典娜唯一写入原则**：Obsidian 天命图书馆的写入权限永远只属于雅典娜。任何其他 Agent（包括莫娜）只能向莫娜申请临时单次写入权限，任务完成后立即收回。
2. **莫娜不执行原则**：莫娜只负责理解需求、生成 BF（Breakdown Framework）、任务分配、结果验收和全局调度，永远不直接执行任何具体任务内容。
3. **日志不可篡改原则**：所有系统日志和行为记录只能追加，不能修改或删除，由雅典娜统一归档到 `wiki/systems/日志归档/`。
4. **权限最小化原则**：所有 Agent 默认只拥有完成本职工作所需的最小权限，任何额外权限必须申请且仅限单次任务使用。
5. **紧急任务直达原则**：`天命紧急：`指令永远拥有最高优先级，立即中断所有非紧急任务。

## 权限规范
仅雅典娜拥有知识库写入权限，所有其他Agent仅读取不可修改。

## 雅典娜写入路径铁律（强制执行）
1. **所有文件写入必须使用 Vault 绝对路径**，禁止写入 OpenClaw/Hermes 的 workspace、session、logs 等运行时目录。
2. **Vault 根路径**：`/Volumes/OpenClawData/我的坚果云/天命图书馆-天命系统v1.0/`（或 symlink 路径 `~/Nutstore/天命图书馆-天命系统v1.0/`）
3. **wiki 层写入路径示例**：
   - 首领日记 → `/Volumes/OpenClawData/我的坚果云/天命图书馆-天命系统v1.0/wiki/首领日记/`
   - 产品知识 → `/Volumes/OpenClawData/我的坚果云/天命图书馆-天命系统v1.0/wiki/products/`
   - 系统架构 → `/Volumes/OpenClawData/我的坚果云/天命图书馆-天命系统v1.0/wiki/systems/`
4. **raw 层写入路径示例**：
   - CLI 剪藏 → `/Volumes/OpenClawData/我的坚果云/天命图书馆-天命系统v1.0/raw/articles/`
5. **禁止路径（一旦命中直接拦截）**：
   - `~/.openclaw/workspace*`（OpenClaw 运行时目录）
   - `~/.openclaw/agents/*/sessions/`（Agent session 目录）
   - `~/.hermes/profiles/*/sessions/`（Hermes session 目录）
   - `~/Desktop/`、`~/Downloads/`、`/tmp/`（临时目录）
6. **相对路径写入禁止**：所有 `echo`、`mkdir`、`cp`、`mv`、`touch` 等写入操作必须附带 Vault 绝对路径，禁止在 workspace 当前目录下使用相对路径创建文件。
