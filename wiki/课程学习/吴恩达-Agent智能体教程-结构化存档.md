---
id: course-andrew-ng-agentic-ai-2026
title: 吴恩达 Agentic AI 智能体完整教程
author: DeepLearning.AI / Andrew Ng
publish_date: 2026-01-15
source_url: https://b23.tv/HQ33KTq
video_count: 43
module_count: 6
play_count: 1723000
archive_date: 2026-04-29
status: pending_learning
version: 1.0
tags:
  - agent
  - agentic-ai
  - reflection
  - tool-use
  - planning
  - multi-agent
  - mcp
  - knowledge-graph
  - andrew-ng
  - deeplearning-ai
  - course
related_systems:
  - 天命系统架构
  - OpenClaw MCP协议
  - Skills机制
  - 莫娜调度器
  - 雅典娜知识库
---

# 吴恩达 Agentic AI 智能体教程 - 结构化存档

> **机器可读格式**：本文件设计为 Agent 可快速解析提取的结构化文档
> **核心用途**：Agent 学习参考、架构设计参考、技能开发指南

---

## 📌 核心信息速查（Agent 优先读取）

```yaml
course_id: course-andrew-ng-agentic-ai-2026
learning_objectives:
  - 智能体四大设计模式：反射、工具使用、规划、多智能体
  - 外部工具集成：数据库、API、网络搜索、代码执行
  - 评估优化：性能指标、错误分析、生产部署
core_concepts:
  - reflection: 反射/自我审查
  - tool_use: 工具使用
  - planning: 任务规划
  - multi_agent: 多智能体协作
  - evals: 评估体系
  - mcp: Model Context Protocol
  - knowledge_graph: 知识图谱
alignment_with_destiny:
  mcp_protocol: implemented_in_openclaw
  multi_agent: implemented_6_teams
  tool_use: implemented_skills_system
  reflection: implemented_mona_verification
  knowledge_graph: pending_athena_upgrade
```

---

## 🧩 四大核心设计模式（Agent 必学）

### 1. 反射模式 (Reflection)
```yaml
pattern_id: reflection
core_idea: 生成 -> 审查 -> 修正 -> 输出
application_scenarios:
  - 高质量内容生成
  - 代码编写与审查
  - 数据图表生成
key_techniques:
  - 自我评估输出质量
  - 识别错误与不足
  - 多轮迭代优化
destiny_implementation: 莫娜最终验收机制
video_segments: [模块2]
```

### 2. 工具使用模式 (Tool Use)
```yaml
pattern_id: tool_use
core_idea: 调用外部功能扩展能力边界
tool_types:
  - database_query: 数据库查询
  - api_call: API 调用
  - web_search: 网络搜索
  - code_execution: 代码执行
key_protocols:
  - mcp: Model Context Protocol（OpenClaw已实现）
security_concerns:
  - sandbox_isolation: 沙箱隔离
  - permission_control: 权限控制
destiny_implementation: Skills 技能系统
video_segments: [模块3]
```

### 3. 规划模式 (Planning)
```yaml
pattern_id: planning
core_idea: 自主制定任务执行计划
workflow: plan -> execute -> check -> adjust
application_scenarios:
  - 复杂多步骤任务
  - 需要动态调整的任务
  - 目标导向的任务
key_techniques:
  - 任务分解
  - 计划生成
  - 执行监控
  - 动态调整
destiny_implementation: 莫娜任务调度（待增强）
video_segments: [模块5]
```

### 4. 多智能体模式 (Multi-Agent)
```yaml
pattern_id: multi_agent
core_idea: 分工协作、各司其职
communication_patterns:
  - message_passing: 消息传递
  - shared_memory: 共享内存
  - task_queue: 任务队列
architecture_types:
  - hierarchical: 层级结构（莫娜调度模式）
  - peer_to_peer: 对等协作
destiny_implementation: 6大业务小组架构
video_segments: [模块5]
```

---

## 📚 模块结构索引（按学习顺序）

### 模块1: 智能体工作流简介
```yaml
module_id: module1-intro
segment_count: 8
total_duration: ~46分钟
key_topics:
  - agent_definition: 智能体定义
  - autonomy_levels: 自主性层级
  - agent_advantages: Agentic AI vs 传统LLM
  - task_decomposition: 任务分解
  - evals_basics: 评估基础
  - design_patterns_overview: 设计模式概览
status: pending
```

### 模块2: 反射设计模式
```yaml
module_id: module2-reflection
segment_count: 5
total_duration: ~26分钟
key_topics:
  - reflection_basics: 反射基本概念
  - direct_vs_reflection: 直接生成 vs 反射生成
  - workflow_example: 图表生成工作流
  - impact_measurement: 反射效果评估
  - external_feedback: 外部反馈集成
status: pending
```

### 模块3: 工具使用
```yaml
module_id: module3-tool-use
segment_count: 5
total_duration: ~29分钟
key_topics:
  - tool_concept: 工具概念
  - tool_creation: 自定义工具开发
  - tool_syntax: 工具调用语法
  - code_execution: 代码执行安全
  - mcp_protocol: Model Context Protocol
status: pending
```

### 模块4: 实用技巧
```yaml
module_id: module4-practical
segment_count: 7
total_duration: ~51分钟
key_topics:
  - evals_comprehensive: 全面评估方法论
  - error_analysis: 误差根因分析
  - component_level_evals: 组件级评估
  - problem_solving_framework: 问题解决框架
  - cost_optimization: 延迟成本优化
  - production_best_practices: 开发最佳实践
status: pending
```

### 模块5: 高度自主智能体模式
```yaml
module_id: module5-advanced
segment_count: 6
total_duration: ~33分钟
key_topics:
  - planning_workflow: 规划工作流
  - llm_plan_execution: LLM计划执行
  - planning_with_code: 规划+代码执行
  - multi_agent_workflow: 多智能体工作流
  - multi_agent_communication: 多智能体通信模式
status: pending
```

### 模块6: Agent知识图谱
```yaml
module_id: module6-knowledge-graph
segment_count: 12
total_duration: ~179分钟
key_topics:
  - kg_basics: 知识图谱基础
  - multi_agent_architecture: 多智能体系统架构
  - google_adk: Google Agent Development Kit
  - user_intent: 用户意图理解
  - structured_data_schema: 结构化数据架构
  - unstructured_data_pattern: 非结构化数据模式
  - kg_construction: 知识图谱构建实践
status: pending
```

---

## 🔗 天命系统映射表

| 课程概念 | 系统组件 | 实现状态 | 对应文件/位置 |
|---------|---------|---------|--------------|
| MCP 协议 | OpenClaw 核心 | ✅ 已实现 | `openclaw config get tools` |
| 多智能体架构 | 6大业务小组 | ✅ 已实现 | `AGENTS.md` |
| 工具使用模式 | Skills 系统 | ✅ 已实现 | `~/.hermes/profiles/mona/skills/` |
| 反射模式 | 莫娜验收机制 | ✅ 基础实现 | 莫娜 prompt 逻辑 |
| 规划模式 | 莫娜任务调度 | ⚠️ 部分实现 | 待增强 |
| 评估体系 (Evals) | Agent 评估 | ⬜ 待建立 | 待开发 |
| 知识图谱 | 雅典娜知识库 | ⬜ 待升级 | 当前为文件系统 |

---

## 🎯 四阶段学习路径（Agent 能力提升）

### 阶段1: 基础认知提升
```yaml
phase_id: phase1-foundations
duration: 1-2 days
modules: [模块1, 模块2]
expected_outcomes:
  - 深入理解 Agent 核心概念
  - 掌握反射设计模式
  - 优化莫娜验收机制
action_items:
  - 学习模块1全部内容
  - 学习模块2全部内容
  - 设计反射增强的验收流程
  - 更新莫娜 prompt
status: pending
```

### 阶段2: 工具能力增强
```yaml
phase_id: phase2-tool-capabilities
duration: 2-3 days
modules: [模块3, 模块4]
expected_outcomes:
  - 精通 MCP 协议
  - 建立 Skills 开发规范
  - 建立 Agent 评估体系
action_items:
  - 学习模块3全部内容
  - 学习模块4全部内容
  - 编写 Skills 开发指南
  - 建立 Evals 评估框架
status: pending
```

### 阶段3: 高级模式应用
```yaml
phase_id: phase3-advanced-patterns
duration: 2-3 days
modules: [模块5]
expected_outcomes:
  - 掌握规划模式
  - 优化多智能体协作
action_items:
  - 学习模块5全部内容
  - 增强莫娜任务规划能力
  - 优化 Agent 间通信协议
status: pending
```

### 阶段4: 知识图谱建设
```yaml
phase_id: phase4-knowledge-graph
duration: 3-5 days
modules: [模块6]
expected_outcomes:
  - 掌握知识图谱构建
  - 雅典娜知识库升级
action_items:
  - 学习模块6全部内容
  - 设计知识图谱 schema
  - 迁移现有知识库
  - 实现知识查询 API
status: pending
```

---

## 📋 关键概念定义表

| 术语 | 英文 | 定义 | 重要程度 |
|-----|------|------|---------|
| 智能体 AI | Agentic AI | 具有自主决策能力的 AI 系统，能够理解目标、规划步骤、调用工具、自我修正 | ⭐⭐⭐⭐⭐ |
| 反射 | Reflection | AI 对自身输出进行审查、评估和修正的过程 | ⭐⭐⭐⭐⭐ |
| 工具使用 | Tool Use | AI 调用外部功能（API、数据库、代码执行等）扩展能力边界 | ⭐⭐⭐⭐⭐ |
| 规划 | Planning | AI 自主制定任务执行计划并动态调整的能力 | ⭐⭐⭐⭐ |
| 多智能体 | Multi-Agent | 多个具有不同专长的 AI Agent 分工协作完成任务 | ⭐⭐⭐⭐ |
| 评估体系 | Evals | 衡量 Agent 性能的系统化方法，包括指标设计、错误分析、持续优化 | ⭐⭐⭐⭐⭐ |
| MCP协议 | Model Context Protocol | 标准化的工具调用协议，实现跨平台工具复用 | ⭐⭐⭐⭐ |
| 知识图谱 | Knowledge Graph | 结构化的知识表示，支持推理和关联查询 | ⭐⭐⭐ |

---

## 🔍 搜索关键词索引

```
Agent 架构设计:
  agent-design-pattern, agent-architecture, multi-agent-system
  hierarchical-agent, agent-communication

核心能力:
  reflection, self-correction, self-improvement, tool-use
  planning, task-decomposition, autonomous-decision

技术协议:
  mcp, model-context-protocol, tool-calling, function-calling
  api-integration, code-execution-sandbox

评估优化:
  evals, evaluation-framework, error-analysis, root-cause
  cost-optimization, latency-optimization, production-deployment

知识系统:
  knowledge-graph, structured-data, unstructured-data
  knowledge-representation, semantic-search

课程相关:
  andrew-ng, deeplearning-ai, agentic-ai-course
  google-adk, agent-development-kit
```

---

## 📝 学习进度追踪

```yaml
current_phase: not_started
completed_modules: []
completed_segments: []
notes_written: false
practice_done: false
production_applied: false
last_updated: 2026-04-29
```

---

## 📎 附加资源链接

```yaml
official_resources:
  - deeplearning_ai_course: https://www.deeplearning.ai/
  - course_materials: 视频评论区自取
related_bilibili_courses:
  - agent_skills: "https://b23.tv/..."
  - claude_code: "https://b23.tv/..."
reference_docs_in_destiny:
  - AGENTS.md: 天命系统完整架构
  - SOUL.md: 莫娜核心设定
  - MEMORY.md: 系统架构总览
```

---

**文档类型**：结构化学习存档（Agent 优化读取）
**维护 Agent**：雅典娜
**更新规则**：学习进度更新时修改 YAML 状态字段，不改变整体结构
**版本**：v1.0

