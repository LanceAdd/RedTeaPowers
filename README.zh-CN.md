# RedTeaPowers

[English Version / 英文说明](README.md)

```text
        )   )  (
       (   (   ) )
        )   ) ( (
      ╭───────────╮
      │ RedTea >  │__
      │ Powers    │  )
      ╰───────────╯__/
```

RedTeaPowers 是一套面向结构化软件开发的技能库。它保留有价值的工程纪律，同时主动去掉最容易拖慢交付的流程负担。

它来自对原版 `superpowers` 体系的重构与裁剪，目标不是“更重的流程”，而是“更稳、更快、更贴近真实交付节奏的流程”。

## 为什么做 RedTeaPowers

很多流程型开发体系的问题并不在“有没有结构”，而在“结构太容易被过度使用”：

- 实现前过度收敛
- `spec` 和 `plan` 被习惯性强制产出
- 一类小问题被拆成很多微循环
- TDD 被默认为唯一正确方式
- 文档缺少清晰分类，最后都挤进同几个桶里

RedTeaPowers 保留这些真正有用的能力：

- 先给工作定型
- 明确验证策略
- 在真正有价值时保留文档
- 提供可重复执行的开发与收尾工作流

同时把默认行为改成更服务交付的版本。

## 它在优化什么

RedTeaPowers 主要优化这几件事：

- 默认采用更轻的流程
- 主线稳定后尽快切到 batch 推进
- 先有证据，再做结论
- 文档按用途分类，而不是堆在一起
- 所有项目文档统一使用 UTF-8

## 核心默认规则

1. 先使用最轻但足够安全的流程。
2. 先给工作定型，再决定是否需要流程工件。
3. 当出现 3 个以上同类低风险问题时，默认合批处理。
4. 第一刀只用于打开局面，不用于无限切小片。
5. 验证方式按真实风险选，不按习惯选。
6. 所有项目文档统一使用 UTF-8 读写。

## 工作流一眼看懂

```text
先路由 -> 缺事实就先调研 -> 只有真需要时才做设计 -> 只有真需要时才写计划 -> 执行 -> 验证 -> 收尾
```

推荐入口：

1. `using-redteapowers` 负责总路由
2. `shaping-work` 决定是直接执行、会话任务跟踪、plan，还是 `spec + plan`
3. `researching-and-collecting` 用于缺事实、缺盘点、缺对比材料时
4. `choosing-test-strategy` 用于先锁定验证方式
5. `managing-project-docs` 用于决定应该存在什么文档工件

## 技能地图

| 领域 | 技能 |
|------|------|
| 路由与定型 | `using-redteapowers`, `shaping-work`, `researching-and-collecting`, `brainstorming` |
| 计划与执行 | `writing-plans`, `executing-plans`, `subagent-driven-development` |
| 验证与调试 | `choosing-test-strategy`, `test-driven-development`, `systematic-debugging`, `verification-before-completion` |
| 文档与迁移 | `managing-project-docs`, `migrating-project-docs` |
| 评审与分支流转 | `requesting-code-review`, `receiving-code-review`, `using-git-worktrees`, `finishing-a-development-branch` |

## 相对原版 Superpowers 的主要变化

RedTeaPowers 不是简单换名，而是改了原体系的默认工作方式。

| 原版更容易出现的倾向 | RedTeaPowers 的默认做法 |
|----------------------|--------------------------|
| `brainstorm -> spec -> plan -> execute` 被习惯性套用 | 先路由，再只增加真正有帮助的下一层 |
| 前期过度收敛 | 使用小收敛预算和明确的停止规则 |
| `spec` 和 `plan` 成为默认文档终点 | 用更完整的文档体系承接不同用途 |
| 默认 TDD-first | 先选验证方式，再决定是否需要 TDD |
| 一眼看到的问题一个个拆小循环处理 | 同类低风险问题优先合批 |
| 第一刀之后长期停留在微推进 | 打开局面后尽快转入稳定 batch 交付 |

## 当前打包包含的技能

当前 active package 包含：

- `using-redteapowers`
- `shaping-work`
- `researching-and-collecting`
- `choosing-test-strategy`
- `managing-project-docs`
- `migrating-project-docs`
- `brainstorming`
- `writing-plans`
- `executing-plans`
- `subagent-driven-development`
- `systematic-debugging`
- `verification-before-completion`
- `using-git-worktrees`
- `requesting-code-review`
- `receiving-code-review`
- `finishing-a-development-branch`
- `test-driven-development`

具体打包说明见 [PACKAGE.md](PACKAGE.md)，技能保留/重写/归档状态见 [using-redteapowers/references/library-status-matrix.md](using-redteapowers/references/library-status-matrix.md)。

## 快速开始

先克隆仓库：

```powershell
git clone git@github.com:LanceAdd/RedTeaPowers.git
```

然后把 skill 目录安装或复制到 Codex skills 目录：

```text
~/.codex/skills
```

在这台机器上通常是：

```text
C:\Users\lanceadd\.codex\skills
```

`PACKAGE.md` 适合作为包级说明，但不是运行时发现 skill 的硬性要求。

## 仓库结构

- `README.md` 是英文版首页
- `README.zh-CN.md` 是中文版首页
- `PACKAGE.md` 描述当前打包的 active skill 集
- 每个顶层目录都是一个 skill
- `agents/openai.yaml` 是界面元数据
- `references/` 是按需加载的参考资料
- `scripts/` 是可复用脚本
- `assets/` 是可复用展示资源

## 迁移入口

如果你正在从旧版 `superpowers` 迁移，建议先看：

- [using-redteapowers/references/migrating-from-superpowers.md](using-redteapowers/references/migrating-from-superpowers.md)
- [using-redteapowers/references/workflow-overview.md](using-redteapowers/references/workflow-overview.md)
- [using-redteapowers/references/library-status-matrix.md](using-redteapowers/references/library-status-matrix.md)

## 项目规则

所有项目文档都应以 UTF-8 文本读写。
