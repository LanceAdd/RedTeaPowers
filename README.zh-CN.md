# RedTeaPowers

[English Version / 英文说明](README.md)

```text
    ____           __  ______              ____                            
   / __ \___  ____/ / /_  __/__  ____ _   / __ \____ _      _____  __________
  / /_/ / _ \/ __  /   / / / _ \/ __ `/  / /_/ / __ \ | /| / / _ \/ ___/ ___/
 / _, _/  __/ /_/ /   / / /  __/ /_/ /  / ____/ /_/ / |/ |/ /  __/ /  (__  ) 
/_/ |_|\___/\__,_/   /_/  \___/\__,_/  /_/    \____/|__/|__/\___/_/  /____/  
```

> 更轻的流程，更清晰的边界，更真实的交付节奏。

## 🍵 这是什么

RedTeaPowers 是一套面向结构化软件开发的 skill 库。

它保留真正有价值的工程纪律：

- 在动手前先给工作定型
- 明确选择验证方式
- 只在真正有价值时沉淀文档
- 执行、评审、收尾都有清晰边界

它主动拿掉最容易拖慢团队的部分：

- 每个任务都默认写 `spec` 和 `plan`
- 一个问题一个微循环
- 默认 TDD-first 的隐性压力
- 文档分类模糊，最后什么都往一起堆

## ✨ 它的设计方向

RedTeaPowers 现在的核心取向是：

- **默认更轻**：从最小够用流程开始
- **边界更 sharp**：`discuss`、`guide`、`spec`、`plan`、`reference`、`change`、`archive` 各司其职
- **证据优先**：没有新鲜验证，就不宣称完成
- **主线稳定后合批推进**：不把同类低风险后续工作继续切成碎片
- **按分发后的真实形态设计**：skill 运行时不能偷偷依赖仓库根文档

## 🧭 工作流总览

```text
先路由 -> 缺事实就先调研 -> 只有真需要时才做设计 -> 只有真需要时才写计划 -> 执行 -> 验证 -> 收尾
```

推荐入口：

1. `using-redteapowers` 负责顶层流程路由
2. `shaping-work` 决定是直接执行、会话任务跟踪、plan，还是 `spec + plan`
3. `researching-and-collecting` 用于缺事实、缺盘点、缺对比时
4. `choosing-test-strategy` 用于先锁定验证方式
5. `managing-project-docs` 用于决定该落什么文档工件

## 🧩 技能地图

| 领域 | 技能 |
|------|------|
| 路由与定型 | `using-redteapowers`, `shaping-work`, `researching-and-collecting`, `brainstorming` |
| 计划与执行 | `writing-plans`, `executing-plans`, `subagent-driven-development` |
| 验证与调试 | `choosing-test-strategy`, `test-driven-development`, `systematic-debugging`, `verification-before-completion` |
| 文档与迁移 | `managing-project-docs`, `migrating-project-docs` |
| 评审与分支流转 | `requesting-code-review`, `receiving-code-review`, `using-git-worktrees`, `finishing-a-development-branch` |

## 🔄 相对 Superpowers 的变化

RedTeaPowers 不是简单换名字，而是重置了一套默认工作方式。

| 旧倾向 | RedTeaPowers 默认 |
|--------|-------------------|
| `brainstorm -> spec -> plan -> execute` 被习惯性套用 | 先路由，再只增加真正有帮助的下一层 |
| 前期过度收敛 | 使用小收敛预算和明确停手规则 |
| `spec` 和 `plan` 成为默认文档终点 | 用更完整的 taxonomy 承接不同用途，加上 `TodoWrite` / `update_plan` 会话任务跟踪 |
| 默认 TDD-first | 先选验证方式，再决定是否用 TDD |
| 一眼看到的问题全拆成小循环 | 同类低风险后续工作优先合批推进 |
| 第一刀后长期停留在 first slice 模式 | 打开局面后尽快切入稳定交付 |

## 📚 文档分类原则

这套仓库现在把文档边界看得很重。

几个关键点：

- `discuss` 只用于暂不进入执行的需求讨论
- 决定做之后，批准的行为和边界进入 `spec`
- `guide` 只用于阶段性的开发纲领或分阶段开发方向
- `reference` 放稳定事实和持久的技术说明
- `change` 在执行和 review 收口后再写

详见：

- [Document Taxonomy Clarifications](docs/reference/003-document-taxonomy-clarifications.md)

## 🧱 新模块开发

新模块、新子系统、新能力，不应该一上来就写任务清单。

现在仓库里已经补了这套方法论入口：

- [新模块开发总流程](skills/shaping-work/references/003-new-module-development-flow.md)
- [新模块 Spec 模板](skills/brainstorming/references/001-new-module-spec-template.md)
- [模块设计记录模板](skills/brainstorming/references/002-module-design-record-template.md)
- [新模块 Plan 模板](skills/writing-plans/references/001-new-module-plan-template.md)

当前项目采用的串行原则是：

1. 需求未决定执行前放在 `discuss`
2. 决定执行后，把批准的行为与边界落到 `spec`
3. 如果技术设计细节过多，就单独写到 `reference`
4. 设计稳定后再写 `plan`

## 📦 当前 active package

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

详见：

- [Package Overview](PACKAGE.md)
- [Library Status Matrix](skills/using-redteapowers/references/library-status-matrix.md)

## 🗂️ 当前仓库结构

仓库现在已经明确区分“源码结构”和“运行时分发结构”。

```text
RedTeaPowers/
├─ skills/    # source skill 目录
├─ docs/      # 仓库级参考文档、校准文档
├─ assets/    # 共享展示资源
├─ README.md
├─ README.zh-CN.md
└─ PACKAGE.md
```

`skills/` 下每个子目录都是一个可安装 skill：

```text
skills/<skill-name>/
├─ SKILL.md
├─ agents/openai.yaml
├─ references/
└─ scripts/
```

## 🚀 安装方式

先克隆仓库：

```powershell
git clone git@github.com:LanceAdd/RedTeaPowers.git
```

然后把你需要的 skill 目录从 `skills/` 复制到 Codex 的 skills 目录：

```text
~/.codex/skills
```

`PACKAGE.md` 适合作为 package 说明，但运行时真正被发现的是每个独立的 skill 目录。

## 🔧 打包规则

这也是当前项目的一个明确规则：

- 源码仓库里的 skill 放在 `skills/`
- 分发时仍然是把 skill 目录扁平复制到运行时 skills 目录
- skill 的运行行为不能依赖仓库根下不会一起分发的文件

换句话说：

- 运行时引用要么放在 skill 自己内部
- 要么引用分发后仍然存在的 sibling skill

## 🔁 从旧版迁移

如果你正在从旧版 `superpowers` 迁移，建议先看：

- [Migrating From Superpowers](skills/using-redteapowers/references/migrating-from-superpowers.md)
- [Workflow Overview](skills/using-redteapowers/references/workflow-overview.md)
- [Library Status Matrix](skills/using-redteapowers/references/library-status-matrix.md)

## 📝 项目规则

所有项目文档都应以 UTF-8 文本读写。
