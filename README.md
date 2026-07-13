# AI Master Tutor Skill

**AI Master Tutor：基于学习科学的一对一自适应 AI 导师，支持 Codex 与 Claude Code。**

它不是“换一种语气回答问题”的提示词，而是一套可复用的教学协议：诊断起点、控制认知负荷、引出主动尝试、动态搭建脚手架、即时反馈、逐步撤掉帮助，并用解释、应用与迁移检验掌握。

当前版本：`v0.2.0`

## 它解决什么问题

普通聊天机器人很容易：

- 一次讲太多；
- 学生还没思考就公布答案；
- 把“苏格拉底式教学”变成无休止反问；
- 把“我懂了”误判为真正掌握；
- 在没有读到原文时假装理解论文；
- 给出看似精确、其实没有证据的掌握度百分比。

本 Skill 把这些失败模式写成了明确的决策规则。最重要的一条是：**有推理基础时提问；缺少前置知识时直接讲；连续失败时增加帮助；成功后逐步撤掉帮助。**

## 安装

推荐使用 GitHub CLI。标准 `skills/ai-master-tutor/` 布局可被 `gh skill` 自动发现，并为后续更新记录来源。

### Codex

```bash
gh skill install 3eyes88/ai-master-tutor-skill ai-master-tutor \
  --agent codex --scope user
```

### Claude Code

```bash
gh skill install 3eyes88/ai-master-tutor-skill ai-master-tutor \
  --agent claude-code --scope user
```

也可以手动复制：

```bash
git clone https://github.com/3eyes88/ai-master-tutor-skill.git

cp -R ai-master-tutor-skill/skills/ai-master-tutor ~/.codex/skills/
cp -R ai-master-tutor-skill/skills/ai-master-tutor ~/.claude/skills/
```

Claude Code 的个人 Skill 路径是 `~/.claude/skills/<skill-name>/SKILL.md`，项目级路径是 `.claude/skills/<skill-name>/SKILL.md`。详见 [Claude Code Skills 官方文档](https://code.claude.com/docs/en/slash-commands)。

## 调用

### Codex

```text
使用 $ai-master-tutor 从零教我认知负荷理论。
```

```text
Use $ai-master-tutor to test whether I truly understand this paper.
```

### Claude Code

```text
/ai-master-tutor 从零教我认知负荷理论。
```

```text
/ai-master-tutor Test whether I truly understand this paper.
```

两种平台都支持根据自然语言学习意图自动调用，例如“辅导我理解这篇论文”或“测验我是否真正掌握这个概念”。Claude Code 也会把目录名暴露为 `/ai-master-tutor` 命令。

## 更新

通过 `gh skill install` 安装后，可检查并应用所有已安装 Skill 的更新：

```bash
gh skill update --dry-run
gh skill update --all
```

## 仓库结构

```text
ai-master-tutor-skill/
├── skills/ai-master-tutor/    # 跨平台的标准 Agent Skill
│   ├── SKILL.md
│   ├── agents/openai.yaml     # Codex UI 元数据；Claude Code 会忽略
│   └── references/
├── tests/                     # 静态校验、情景测试与跨平台测试
├── docs/                      # 测试报告
├── CHANGELOG.md
├── LICENSE
└── VERSION
```

Skill 本体不放 README、测试报告或发布记录，以减少运行时上下文。平台专属安装说明放在仓库根目录，教学协议保持单一源代码。

## 设计原则

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

这套设计综合了认知负荷管理、主动学习、脚手架、范例学习、形成性反馈、提取练习和间隔复习。研究依据及适用边界见 `skills/ai-master-tutor/references/learning-science-basis.md`。

## 测试

```bash
python3 tests/validate_repository.py
```

情景评测规则见 `tests/evaluation-rubric.md`，通用测试用例见 `tests/scenarios.md`，跨平台测试见 `tests/platform-compatibility.md`，发布结果见 `docs/`。

## 许可

[MIT License](LICENSE)
