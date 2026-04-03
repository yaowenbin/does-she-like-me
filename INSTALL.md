# 安装说明

## Cursor（推荐：只装 Skill 子目录）

在 **git 仓库根目录**：

**PowerShell**

```powershell
New-Item -ItemType Directory -Force -Path .cursor/skills | Out-Null
Copy-Item -Recurse -Force "path/to/她爱你嘛-skills/skills/does-she-like-me" ".cursor/skills/does-she-like-me"
```

**bash**

```bash
mkdir -p .cursor/skills
cp -R path/to/她爱你嘛-skills/skills/does-she-like-me .cursor/skills/does-she-like-me
```

确保 `.cursor/skills/does-she-like-me/SKILL.md` 存在。

## Claude Code

```bash
mkdir -p .claude/skills
cp -R path/to/她爱你嘛-skills/skills/does-she-like-me .claude/skills/does-she-like-me
```

若 `CLAUDE_SKILL_DIR` 指向该目录，则 `SKILL.md` 内 `${CLAUDE_SKILL_DIR}/tools/*.py` 可直接调用。

## Web 后端（does-she-like-me-app）

若使用仓库内的 **does-she-like-me-app** 管理端，技能包由后端自动解析；也可在 `backend` 目录预装到本地数据目录：

```bash
cd path/to/does-she-like-me-app/backend
python -m app.skills_bundle install
```

详见该子项目 README 中的环境变量说明（`DOES_SHE_LIKE_ME_SKILL_ROOT`、`DOES_SHE_LIKE_ME_SKILLS_GIT_URL`、`DOES_SHE_LIKE_ME_SKILLS_AUTO_INSTALL`）。

## 依赖

工具脚本 **仅标准库**，Python 3.9+ 即可；无需 `pip install`。

## 触发

`/她爱你嘛`、`/does-she-like-me`、或自然语言请求解读聊天记录（须符合 Skill 内安全边界）。
