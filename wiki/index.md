# 天命图书馆 · 知识总索引

> 人类只剪藏收集，LLM全权理解编译沉淀，知识自动生长复利。
> 
> 最后更新：2026-04-27

---

## 🚀 CLI 快速入口

```bash
# 剪藏网页到 raw/
obsidian-cli clip <url>

# 导入文件到 raw/
obsidian-cli import <文件路径>

# 触发知识库同步编译
obsidian-cli compile

# 检索知识库
obsidian-cli search <关键词>
```

---

## ☁️ 多端同步配置

**同步方式**：Nutstore Sync 插件（Obsidian 社区插件）

**配置参数**：
- 登录方式：单点登录
- 同步模式：宽松模式（防限流、大库必开）
- 冲突策略：智能合并
- 自动同步：文件变更时自动同步

**Vault 路径**：`~/Nutstore/天命图书馆-天命系统v1.0`

> 注意：Vault 实际存储在外置盘 `/Volumes/OpenClawData/我的坚果云/天命图书馆-天命系统v1.0/`，`~/Nutstore/` 为访问入口。

---

## 📁 目录导航
### [[raw|原始素材层]]
- `raw/articles/` — 剪藏文章（CLI: `obsidian-cli clip`）
- `raw/notes/` — 手写笔记/思维导图
- `raw/images/` — 截图/图片素材
- `raw/pdfs/` — PDF文献资料
- `raw/logs/` — 系统运行日志

### [[wiki|知识编译层]]（雅典娜全权维护）
- `wiki/agents/` — Agent能力档案与使用指南
- `wiki/concepts/` — 核心概念与方法论
- `wiki/首领日记/` — 创始人日记与业务观察（[[藏山海开店日记_结构化]]）
- `wiki/products/` — 产品/项目知识沉淀
- `wiki/systems/` — 系统架构与运维知识
- `wiki/workflows/` — 标准操作流程SOP

### [[schema|规则约束层]]
- `schema/rules/` — 全局强制规则（[[schema/rules|系统核心铁律]]）
- `schema/templates/` — 标准模板
- `schema/prompts/` — Prompt规范库

### [[wiki/天命系统总览|系统总览]]
- [[wiki/天命系统总览|天命系统 v1.0 总览]] — 架构、状态、指令、Agent 组织
- [[wiki/systems/故障排查指南|快速故障排查指南]] — 问题速查与常见误区
- [[wiki/systems/v1.1升级计划|v1.1 升级计划]] — 务实版演进路线图
- [[wiki/agents/莫娜职责边界|莫娜职责边界]] — 全局调度 Agent 权责清单

### [[shared|共享分发层]]
- `shared/knowledge/` — 跨Agent共享知识包

---

## 🔗 核心知识图谱

```
[CLI剪藏/import] --> [raw/原始层] --编译--> [wiki/知识层] --链接--> [知识图谱]
     ↑                                                              ↓
[人类剪藏]                                                    [Agent调用/CLI检索]
```

---

## 📌 业务域快速入口

| 业务域 | 对应目录 | 负责Agent |
|--------|---------|----------|
| 线上运营 | `wiki/products/线上运营/` | 玛门/美杜莎/瓦兹 |
| 内容创作 | `wiki/products/内容创作/` | 辛德瑞拉/尼尔 |
| 用户运营 | `wiki/products/用户运营/` | 伊芙/哈索尔 |
| 线下运营 | `wiki/products/线下运营/` | 丽萨/海王星/希尔德 |
| AI开发 | `wiki/systems/AI开发/` | 克洛诺斯/赛特/阿芙洛狄忒/克洛托/达勒/赫菲斯托斯 |
| 知识管理 | `wiki/systems/知识管理/` | 雅典娜/赫卡忒/赫尔墨斯 |

---

> 🛡️ **权限声明**：仅[[雅典娜]]拥有写入权限，其余Agent只读调用。CLI仅开放检索和归集权限。
