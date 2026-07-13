# AI Master Tutor Skill

**AI Master Tutor：基于学习科学的一对一自适应 AI 导师。**

它不是“换一种语气回答问题”的提示词，而是一套可复用的教学协议：诊断起点、控制认知负荷、引出主动尝试、动态搭建脚手架、即时反馈、逐步撤掉帮助，并用解释、应用与迁移来检验掌握。

当前版本：`v0.1.0`

## 它解决什么问题

普通聊天机器人很容易：

- 一次讲太多；
- 学生还没思考就公布答案；
- 把“苏格拉底式教学”变成无休止反问；
- 把“我懂了”误判为真正掌握；
- 在没有读到原文时假装理解论文；
- 给出看似精确、其实没有证据的掌握度百分比。

本 Skill 把这些失败模式写成了明确的决策规则。最重要的一条是：**有推理基础时提问；缺少前置知识时直接讲；连续失败时增加帮助；成功后逐步撤掉帮助。**

## 能做什么

- 辅导论文、书籍、文章与课程材料；
- 从零学习概念或理论；
- 学习数学、编程等问题解决流程；
- 纠正稳定误解，而非只替换答案；
- 进行闭卷提取、测验和考前复习；
- 检验解释、应用和迁移能力；
- 生成轻量的间隔复习计划和会话交接记录。

## 安装

把纯 Skill 文件夹复制到 Codex Skills 目录：

```bash
git clone <your-repository-url>
cp -R ai-master-tutor-skill/skill/ai-master-tutor ~/.codex/skills/
```

重新启动或刷新 Codex，使它发现新 Skill。

## 使用

显式调用：

```text
Use $ai-master-tutor to teach me this paper. Start by checking what I already understand.
```

```text
使用 $ai-master-tutor 从零教我认知负荷理论。不要一次讲太多，确认我会应用后再进入下一步。
```

```text
使用 $ai-master-tutor 测试我是否真正理解了这章内容，重点检查迁移，不要只考定义。
```

当用户明确表达“教我、辅导我、测验我、陪我学、纠正我的理解”等学习意图时，Skill 也允许隐式触发。

## 仓库结构

```text
ai-master-tutor-skill/
├── skill/ai-master-tutor/     # 可直接安装的纯 Skill
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   └── references/
├── tests/                     # 静态校验、情景测试与评分规则
├── docs/                      # 测试报告
├── LICENSE
└── VERSION
```

Skill 本体刻意不放 README、测试报告和发布记录，以减少运行时上下文并遵守 Codex Skill 的渐进披露原则。

## 设计原则

核心运行闭环：

```text
最小诊断
   ↓
主动尝试
   ↓
诊断错误来源
   ↓
提问 / 提示 / 范例 / 直接讲解
   ↓
平行题验证
   ↓
撤掉或增加帮助
   ↓
应用与迁移检验
   ↓
闭卷总结与后续复习
```

这套设计综合了认知负荷管理、主动学习、脚手架、范例学习、形成性反馈、提取练习和间隔复习。研究依据及适用边界见 Skill 内的 `references/learning-science-basis.md`。

## 测试

运行仓库静态校验：

```bash
python3 tests/validate_repository.py
```

情景评测规则见 `tests/evaluation-rubric.md`，测试用例见 `tests/scenarios.md`，v0.1.0 的结果见 `docs/test-report-v0.1.0.md`。

## 许可

[MIT License](LICENSE)
