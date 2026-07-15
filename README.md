# AI Master Tutor Skill

**AI Master Tutor：基于学习科学的一对一自适应 AI 导师，支持 Codex 与 Claude Code。**

它不是“换一种语气回答问题”的提示词，而是一套分层教学系统：先判断用户需要快速解释、引导学习、掌握检测、复习还是长期课程，再用最小必要路径完成教学。复杂学习可配合课程内容包、经验证的答案键和用户授权的跨会话学习记录。

当前工作版本：`v0.4.0-rc.1`

这是本地候选版本。完成独立前向测试、真人试用与发布检查前，不宣称其已经证明长期学习效果或已经作为 `v0.4.0` 正式发布。

## 它解决什么问题

普通聊天机器人很容易：

- 一次讲太多；
- 学生还没思考就公布答案；
- 把“苏格拉底式教学”变成无休止反问；
- 把“我懂了”误判为真正掌握；
- 把普通问答或长时间聊天误叫作 Interactive；
- 对新手强行追问，对熟练者重复讲基础；
- 学生答错后立即公布完整答案，失去重新建构机会；
- 在没有读到原文时假装理解论文；
- 给出看似精确、其实没有证据的掌握度百分比。

本 Skill 把这些失败模式写成了明确的决策规则。最重要的两条是：**先选择最轻的会话模式，再根据已有图式选择 P/A/C/I 活动；简单问题不强制走完整闭环，真正的掌握判断必须有独立、变化和延迟证据。**

## 安装

候选版应从当前仓库本地安装，避免 GitHub 默认分支尚未发布对应版本时安装到旧版：

```bash
gh skill install . ai-master-tutor --from-local --agent codex --scope user --force
```

正式发布并合并到默认分支后，可使用远程安装。标准 `skills/ai-master-tutor/` 布局可被 `gh skill` 自动发现，并为后续更新记录来源。

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
使用 $ai-master-tutor 的 quick 模式直接解释机会成本，不要测试我。
```

```text
使用 $ai-master-tutor 的 mastery 模式检验我是否真正掌握贝叶斯定理。
```

```text
使用 $ai-master-tutor 的 course 模式系统学习 Rust，并在得到我同意后保存学习记录。
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
│   ├── references/            # 模式、ICAP、纠错、掌握、课程与连续学习
│   ├── assets/                # 学习记录与内容包 JSON 模板
│   └── scripts/               # 学习工件校验器
├── tests/                     # 静态校验、情景测试与跨平台测试
├── docs/                      # 测试报告
├── CHANGELOG.md
├── LICENSE
└── VERSION
```

Skill 本体不放 README、测试报告或发布记录，以减少运行时上下文。平台专属安装说明放在仓库根目录，教学协议保持单一源代码。

## 设计原则

```text
学习意图 → quick / guided / mastery / review / course
   ↓
可观察目标与成功标准
   ↓
根据先验知识选择 P / A / C / I 活动
   ↓
按需讲解、检索、建构、挑战与重构
   ↓
当前表现验证；掌握模式执行完整证据门槛
   ↓
经授权保存证据 → 延迟检索 → 累积迁移
   ↓
更新下一检查点、支持级别与复习队列
```

这套设计综合了认知负荷理论、ICAP、脚手架、范例学习、形成性反馈、提取练习、迁移、元认知和间隔复习。`Interactive` 只有在“学习者提出模型 → 导师针对性挑战 → 学习者修改 → 形成更有边界的共同模型”时才成立。长期学习还需要持久化证据、可靠内容结构和延迟测评，不能由提示词单独保证。研究依据及适用边界见 `skills/ai-master-tutor/references/learning-science-basis.md`。

## 测试

```bash
python3 tests/validate_repository.py
python3 skills/ai-master-tutor/scripts/validate_learning_artifacts.py --help
```

情景评测规则见 `tests/evaluation-rubric.md`，通用测试用例见 `tests/scenarios.md`，纵向评测见 `tests/longitudinal-evaluation.md`，跨平台测试见 `tests/platform-compatibility.md`，发布结果见 `docs/`。

## 许可

[MIT License](LICENSE)
