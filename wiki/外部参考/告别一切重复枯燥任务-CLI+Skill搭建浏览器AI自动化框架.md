# 告别一切重复枯燥任务：CLI + Skill 搭建浏览器 AI 自动化框架

> 原视频链接：https://www.bilibili.com/video/BV1ooDyBmE6v

## 核心思路

这套流程可以让 AI 自动操作浏览器，代替你完成一切机械重复性的工作，而且特别省 Token。很多工作流甚至全程不需要 AI 参与，**零 Token 就能把自动化任务跑起来**。

应用场景：
- 零 Token 抓取电商网站评论，导出成 CSV 文件
- 自动把 Markdown 文章发布到 X（Twitter）
- 对自己开发的 Web App 进行 AI 自动化测试

特点：不需要懂浏览器相关知识，**只用自然语言就能完成这些任务**。

## 技术栈

- AI 框架：Kimi Code / Codex
- 浏览器自动化：**Playwright CLI** + 配套 Skill
- Playwright CLI 是 2026 年初微软开源的全新浏览器自动化工具

根据官方基准测试，**Playwright CLI 相比传统 Playwright MCP 方案，能减少 4 倍 Token 消耗**。

## 核心原理

工具搭建好以后，可以把很多固定的工作流程沉淀成 Skills，让 AI 能够又快又省地完成任务。熟练后会发现：很多固定流程甚至不需要 AI 参与，只需要让 AI 编写好一个固定脚本，就可以零 Token 全自动完成工作。

## 准备工作

1. 确保安装了 Node.js
   - 如果没安装，去 Node.js 官网下载对应安装包
   
2. 命令行安装 Playwright CLI

3. 确保安装了 Chrome 浏览器，推荐使用 Chrome，也可以用 Edge

## Playwright CLI 基础使用

### 第一个测试命令

```bash
playwright install chrome
playwright codegen --headed https://www.google.com
```

参数说明：
- `--headed`：表示使用有头浏览器，可以看到页面
- 不加这个参数，Playwright 默认使用无头浏览器，在后台运行，虽然省内存但看不到页面，方便调试一般加上

运行后 Playwright CLI 自动操作 Chrome 打开谷歌官网。

**关键设计**：控制台只输出简洁的网页摘要，不返回整个网页的完整 DOM 结构。下面附带网页结构文件地址，AI 需要更详细信息时再读取，不需要就不读。这就是比 MCP 节省上下文的核心秘密 —— **MCP 把网页全部塞进上下文，Playwright CLI 可以按需读取**。

同样，截图也是以文件形式存放在本地磁盘，由 AI 决定是否读取，而不像 MCP 那样直接把图片塞入 AI 上下文。

### 重要参数：`--persistent`

`--persistent` 表示把 Cookie、登录状态、本地存储写到磁盘，下次使用继续用，不需要每次重新登录。

## 接入 AI Agent

Playwright CLI 是新生的命令行工具，AI Agent 不知道怎么用这些命令，**所以需要搭配 Skill 一起使用**：
- Playwright CLI = 技术底座
- Skill = 使用说明文档
- CLI + Skill 搭配，取代传统 MCP 方式

这是 2026 年最新技术趋势。

### Cloud Code 接入步骤

1. 新建项目文件夹，打开命令行
2. 安装 Skill：`npx install-playwright-cli-skill`
3. Skill 放在项目目录下
4. 启动 Cloud Code，询问 "你有哪些 Skills"，能读取到 Playwright CLI 技能 → 接入完成

### Codex 接入步骤

只需要在项目里把 Skill 文件夹从 `.cloud` 改成 `.codex` 适配 Codex：
1. 打开 Codex
2. 输入命令 `list skills`，能列出 Playwright CLI → 配置完成

## 完整工作流（六步走）

### 示例 1：抓取电商商品评论

目标：用 Playwright CLI 查看商品前 100 条评论，保存到 CSV。

**第一步：AI 摸索试错**
- AI 先学习 Playwright CLI 技能
- 打开商品页面，自己摸索解决问题
- 第一次尝试会走弯路，消耗 41% 上下文，但最终能完成任务，得到 CSV 文件

**第二步：提炼沉淀成 Skill**
- 提示词："创建一个新 Skill，把刚才打开网站查看评论并且保存评论的全过程，还有遇到的坑都写出来，保存到 Skill 里面"
- AI 创建 Skill，把可复用内容固化进知识，放到项目目录
- 现在有两个 Skill：Playwright CLI 基础 + 保存评论流程

**第三步：Skill 指导下重跑，验证效率提升**
- 清理上下文，用相同任务测试
- 有 Skill 指导后，AI 吸取经验，没有多余动作，没有报错，只用了 **5% 上下文** 就完成任务
- **效率提升近 10 倍**

**第四步（可选）：固化为脚本，零 Token 运行**
- 如果是完全固定流程，不需要 AI 智能控制，可以让 AI 直接编写固定脚本
- 提示词："把刚才所有 Playwright CLI 命令汇总成一个脚本，执行脚本就能获取商品前 100 条评论保存到 CSV，注意每步要有合理延时等待确保成功，写完测试一轮"
- Codex 编写完成并测试通过
- 以后直接执行脚本，**完全不需要 AI 参与，Token 消耗降为零**

## 完整方法论总结

| 阶段 | 操作 |
|------|------|
| 1 | 安装依赖：Node.js + Playwright CLI + Chrome |
| 2 | 选择 AI Agent 框架，安装 Playwright CLI Skill |
| 3 | AI 自己摸索执行完复杂任务 |
| 4 | AI 把执行结果提炼总结成 Skill，避免重复踩坑 |
| 5 | 相同任务在 Skill 指导下重跑，Token 消耗降低 10 倍 |
| 6（可选） | 完全固定流程让 AI 编写脚本，直接执行，零 Token |

## 实战案例 1：自动发 Markdown 文章到 X

X 发文步骤非常繁琐：
- Markdown 不能直接粘贴，格式会错乱，图片也显示不出来
- 转 HTML 可以粘贴，但图片粘不过来，变成占位符，需要手动删除占位符，一张张复制粘贴图片

使用上述自动化流程：

1. Codex 编写预处理脚本：
   - 下载文章里所有图片到本地文件夹，顺序编号
   - 转换为只使用本地图片的 Markdown
   - Pandoc 转换为 HTML，每张图片独立段落

2. AI 自动化发文：
   - Playwright CLI 打开网站，创建新文章
   - 粘贴 HTML
   - 按顺序找到每个占位符，删除，粘贴对应的本地图片
   - 全程自动完成

3. 沉淀 Skill：把整个流程整理成 Skill 放到项目
   - 以后给一个文章路径，就能自动发布

完整代码已经开源到 GitHub，可以参考。

## 实战案例 2：AI 自动化测试 Web App

对自己开发的 Web App 进行自动化测试：
1. 要求 AI 阅读代码，学习项目功能，从注册开始写出中文测试流程文档
2. Playwright CLI 打开网页，按测试用例完成测试
3. AI 自动创建账号、上传简历、完成主流程测试，给出结论：通过
4. 可以配置定时任务，修改代码后自动测试，发现 Bug 自动报告，节省人工测试成本

## 对我们的参考价值

这套思路完全可以用到**天命系统**里：

1. **我们现在就是这么干的**：OpenClaw + Hermes-Agent，Skill 就是说明书，CLI 实际执行 → 节省大量上下文
2. **可以直接复用**：
   - 小红书自动发布可以用这套流程，零 Token 自动执行
   - 竞品数据采集自动化，固定脚本直接跑
   - 天命图书馆内容整理自动化，预处理后归档
   - 系统测试自动化，修改配置后自动回归测试
3. **核心启发**：能固化成脚本就不要让 AI 每次重做，能沉淀 Skill 就不要让 AI 每次摸索 → Token 节省 10 倍，响应速度提升 10 倍

---

*转录完成存入天命图书馆，原视频约 12 分半，约 12500 字文字转录。*
