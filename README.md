# 她爱你嘛.skills

把聊天记录当成**互动样本**，用多透镜（演化隐喻、基因/模因修辞、心理学通俗框架、文学性的「欲望翻译」、**自愿标签**下的星座/MBTI 文化对照）做**结构化解读**——**不是算命，不是心理咨询**，更不是个体基因判决。

工程结构致敬 [therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill)：`SKILL.md` + `prompts/` + `tools/`。

## 安装

见 [INSTALL.md](./INSTALL.md)。

**Cursor（项目级）**：将 `skills/does-she-like-me` 复制或软链到仓库的 `.cursor/skills/does-she-like-me`（目录内须有 `SKILL.md`）。

**Claude Code**：可克隆整个仓库到 `.claude/skills/ta-aini`，并把内含的 `skills/does-she-like-me` 作为工作目录，或直接把 `does-she-like-me` 文件夹放到 skills 根目录并保证 Agent 能读到 `SKILL.md`。

## 使用

对 Agent 说：`/她爱你嘛` 或粘贴聊天记录并说明「帮我从多角度看看好感信号」。

Agent 应按 `SKILL.md` 主流程：拒答检查 → intake → 证据卡片 → 行为量表 → 各透镜 → synthesis。

## 可选本地工具（stdlib）

```bash
python skills/does-she-like-me/tools/redact.py -i chat.txt -o chat.redacted.txt
python skills/does-she-like-me/tools/split_chat.py -i chat.txt -n 80 -d ./chunks
```

## 伦理摘要

仅分析你有权使用的材料；禁止骚扰与操控话术；占星模块 **L5** 且需自愿标签；完整边界见各文件内「安全边界」。

## 文档

- 设计说明：`docs/方案书.md`

## License

MIT — 见 [LICENSE](./LICENSE)。
