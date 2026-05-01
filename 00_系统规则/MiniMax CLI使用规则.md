---
rule_id: MINIMAX_CLI_RULE_001
priority: 中
effective_time: 2026-04-30
executor: 系统权限控制器
---
# MiniMax CLI工具使用规则
## 权限分配
允许以下Agent调用：
1. 玛门（小红书文案创作）：调用Minimax模型生成、润色文案
2. 辛德瑞拉（视觉设计）：调用Minimax多模态模型生成Prompt、优化图片参数
3. 美杜莎（情报分析）：调用Minimax模型处理、分析爬取到的内容
4. 伏尔甘（技能开发）：调用Minimax模型开发、测试自定义技能
## 配额限制
✅ 每日调用上限：1000次，超过自动排队
✅ 单次生成长度上限：4096 tokens
✅ 仅允许调用内容创作、分析类模型，禁止调用高消耗的大模型微调、训练接口
## 配置要求
需要配置环境变量：
- MINIMAX_API_KEY：MiniMax平台API密钥
- MINIMAX_GROUP_ID：MiniMax平台Group ID
配置完成后所有Agent自动调用，无需手动指定
