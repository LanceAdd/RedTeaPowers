# RedTeaPowers

```text
   (( 
  ))  
[ R>T ]
```

RedTeaPowers is a curated skill library for structured software work with lighter process by default.

RedTeaPowers 是一套面向结构化软件开发的技能库，默认采用更轻、更快、更贴近真实交付节奏的流程。

Character icon asset:
`assets/redteapowers-icon.txt`

---

## English

### Overview

RedTeaPowers started from the original `superpowers` ecosystem, then was selectively rebuilt into a cleaner, more execution-oriented package.

It keeps the parts of process that actually help:

- work shaping
- explicit validation choices
- durable documentation when it is truly useful
- repeatable execution workflows

and pushes back on the parts that often slow teams down:

- mandatory brainstorm -> spec -> plan chains
- excessive convergence before implementation
- one-problem-one-loop fragmentation
- silent TDD defaults
- document sprawl without taxonomy

### Character Icon

Primary ASCII mark:

```text
   (( 
  ))  
[ R>T ]
```

Compact mark:

```text
[R>T]
```

Meaning:

- `((` and `))` suggest tea steam, warmth, and active momentum
- `R>T` suggests `RedTea`, terminal-style routing, and forward movement
- brackets suggest a tool boundary, package shell, or command surface

### Core Defaults

RedTeaPowers follows these defaults:

1. Start with the lightest workflow that preserves clarity and safety.
2. Shape the work before writing process artifacts.
3. If 3 or more same-kind low-risk items are visible, batch them by default.
4. Use a thin first slice only to open uncertainty, then move into batch progress quickly.
5. Choose the cheapest validation strategy that protects the real risk.
6. Read and write all project documents as UTF-8 text.

### Included Skills

Workflow and routing:

- `using-redteapowers`
- `shaping-work`
- `brainstorming`
- `writing-plans`
- `executing-plans`

Validation and debugging:

- `choosing-test-strategy`
- `test-driven-development`
- `systematic-debugging`
- `verification-before-completion`

Documentation and collaboration:

- `managing-project-docs`
- `requesting-code-review`
- `receiving-code-review`
- `subagent-driven-development`

Supporting skills:

- `using-git-worktrees`
- `finishing-a-development-branch`

### What We Changed From The Original Superpowers

RedTeaPowers is not just a rename. It changes the operating defaults of the original library.

#### 1. Workflow Is Routed, Not Forced

Old instinct:

```text
brainstorm -> spec -> plan -> execute
```

RedTeaPowers default:

```text
route -> shape -> add only the next layer that materially helps
```

That means direct execution, batch checklist, lightweight plan, and spec-plus-plan are all valid routes depending on task shape.

#### 2. Demand Convergence Is Explicitly Guarded

RedTeaPowers adds anti-over-convergence rules:

- use a small convergence budget by default
- ask only the questions that would change the route
- avoid creating more than one active artifact before implementation starts
- batch same-kind low-risk issues when they are already visible
- avoid staying in endless tiny-slice mode after the topic is understood

#### 3. Spec And Plan Are No Longer Universal Defaults

In RedTeaPowers:

- `spec` is for approved behavior and boundaries
- `plan` is for executable sequencing
- `todolist` is the default home for active near-term work when a formal plan is unnecessary
- `guide`, `discuss`, `reference`, `change`, and `archive` are first-class document types

#### 4. TDD Is A Strategy, Not A Doctrine

The original ecosystem often leaned toward implicit TDD-first behavior.

RedTeaPowers requires choosing a validation strategy first:

- TDD
- regression test
- integration check
- manual verification
- exploration first

TDD is still supported, but only when it is actually the right fit.

#### 5. Documentation Taxonomy Was Expanded

Instead of centering nearly everything around `spec` and `plan`, RedTeaPowers formalizes a broader doc system:

- `guide`
- `discuss`
- `spec`
- `plan`
- `reference`
- `change`
- `archive`
- `todolist`
- `scripts`

#### 6. Naming, Namespace, And Paths Were Reworked

- `using-superpowers` -> `using-redteapowers`
- `superpowers:skill-name` -> `redteapowers:skill-name`
- `.superpowers/` -> `.redteapowers/`
- `~/.config/superpowers/...` -> `~/.config/redteapowers/...`

#### 7. Historical Material Was Curated Instead Of Left Active

This package is intentionally selective. Not every original top-level skill was carried forward into the default active library.

#### 8. Some Skill Boundaries Were Renamed Or Reframed

- `using-superpowers` was replaced by `using-redteapowers`
- agent-dispatch workflow ideas were kept, but the active packaged skill is framed as `subagent-driven-development`
- review prompts were updated to fit the newer scope-first model instead of rigid spec-centric assumptions
- only the current packaged working set stays active by default

### Repository Layout

- `README.md` is the repository overview.
- `PACKAGE.md` describes the packaged skill set.
- each top-level directory is a skill
- `agents/openai.yaml` provides UI-facing metadata where present
- `references/` holds load-on-demand guidance
- `scripts/` holds reusable helper scripts where needed
- `assets/` holds reusable presentation assets such as the character icon

### How To Use

Use as a git repository:

```powershell
git clone git@github.com:LanceAdd/RedTeaPowers.git
```

Use as a Codex skill library by installing or copying the skill folders into:

```text
~/.codex/skills
```

On this machine, that path is typically:

```text
C:\Users\lanceadd\.codex\skills
```

`PACKAGE.md` is useful as repository and package documentation, but it is not required for Codex runtime discovery.

### Recommended Entry Points

1. Use `using-redteapowers` for top-level routing.
2. Use `shaping-work` to choose between direct execution, checklist, plan, or spec-plus-plan.
3. Use `choosing-test-strategy` before locking in validation.
4. Use `managing-project-docs` when deciding what kind of artifact should exist.

### Migration Notes

If you are migrating an older `superpowers` setup, start here:

- `using-redteapowers/references/migrating-from-superpowers.md`
- `using-redteapowers/references/workflow-overview.md`
- `using-redteapowers/references/library-status-matrix.md`

### Encoding Policy

All project documents should be read and written as UTF-8 text.

This is a project rule, not a suggestion.

---

## 中文

### 项目概述

`RedTeaPowers` 基于原版 `superpowers` 体系整理而来，但不是简单换名，而是一次有明确方向的重构和裁剪。

它保留了真正有价值的流程能力：

- 先给工作定型
- 明确验证策略
- 只在真正有用时保留文档
- 提供可重复执行的开发工作流

同时主动削弱常见的低效来源：

- 强制性的 `brainstorm -> spec -> plan` 链路
- 实现前过度收敛
- 一类小问题被拆成很多微循环
- TDD 被默认为唯一正确方式
- 文档没有分类，最后全部堆进 `spec` 和 `plan`

### 字符图标

主图标：

```text
   (( 
  ))  
[ R>T ]
```

紧凑图标：

```text
[R>T]
```

设计含义：

- `((` 和 `))` 表示茶的热气，也表示持续工作的动能
- `R>T` 同时代表 `RedTea`、终端提示风格和向前推进
- 方括号表示命令边界、工具外壳和可执行工作面

完整字符图标资产见：

`assets/redteapowers-icon.txt`

### 核心默认规则

RedTeaPowers 的默认规则是：

1. 先使用最轻但足够安全的流程。
2. 先定型工作，再决定是否需要文档和流程工件。
3. 当同时出现 `3` 个以上同类低风险问题时，默认合批处理。
4. 第一刀只用于打开专题局面，不用于无限切小片。
5. 先选择最贴近真实风险的验证方式，再进入实现。
6. 所有项目文档统一使用 UTF-8 读写。

### 内置技能

工作流与路由：

- `using-redteapowers`
- `shaping-work`
- `brainstorming`
- `writing-plans`
- `executing-plans`

验证与调试：

- `choosing-test-strategy`
- `test-driven-development`
- `systematic-debugging`
- `verification-before-completion`

文档与协作：

- `managing-project-docs`
- `requesting-code-review`
- `receiving-code-review`
- `subagent-driven-development`

辅助技能：

- `using-git-worktrees`
- `finishing-a-development-branch`

### 相对原版 Superpowers 的主要魔改

#### 1. 从强制流程改成按需路由

原版更容易把任务推向：

```text
brainstorm -> spec -> plan -> execute
```

RedTeaPowers 改成：

```text
route -> shape -> 只增加真正有帮助的下一层
```

也就是说，直接开发、批量 checklist、轻量 plan、`spec + plan` 都是合法路径，不再只有一条固定通道。

#### 2. 增加“需求收敛护栏”

这是 RedTeaPowers 最核心的魔改之一：

- 默认使用小收敛预算
- 只提会改变路线的问题
- 开发前避免生成多个活跃工件
- 已经能看到的同类低风险问题优先合批
- 第一刀打开方向后，要尽快转入批量推进

#### 3. `spec` 和 `plan` 不再是默认终点

在 RedTeaPowers 里：

- `spec` 用于已批准的目标行为和边界
- `plan` 用于可执行的实现顺序
- `todolist` 用于近期活跃任务
- `guide`、`discuss`、`reference`、`change`、`archive` 都是正式文档类型

#### 4. TDD 从默认教条变成可选策略

原版生态更容易形成“默认 tests first”的惯性。

RedTeaPowers 要求先选验证方式，再决定是否需要 TDD：

- TDD
- 回归测试
- 集成检查
- 人工验证
- 先探索后收敛

#### 5. 文档体系从双轨扩展为多类型系统

RedTeaPowers 正式支持：

- `guide`
- `discuss`
- `spec`
- `plan`
- `reference`
- `change`
- `archive`
- `todolist`
- `scripts`

这样可以减少文档碎片化，也避免把很多不同用途的内容强塞进同一种文档。

#### 6. 名称、命名空间和路径整体重做

- `using-superpowers` -> `using-redteapowers`
- `superpowers:skill-name` -> `redteapowers:skill-name`
- `.superpowers/` -> `.redteapowers/`
- `~/.config/superpowers/...` -> `~/.config/redteapowers/...`

#### 7. 不是全盘照搬，而是主动裁剪

这个仓库不是“原版全量镜像”，而是当前活跃技能的干净工作集。

历史内容、实验材料和不适合默认启用的部分，没有继续保留在主包里当作活跃指导。

#### 8. 一些技能边界被重新定义

- `using-superpowers` 被正式替换为 `using-redteapowers`
- 原本偏 agent dispatch 的思路，被重构进 `subagent-driven-development`
- 一些 prompt 从 `spec` 中心视角改成了更贴近实际范围控制的写法
- 默认活跃技能集合被重新筛选，强调“少而有效”

### 仓库结构

- `README.md`：仓库首页说明
- `PACKAGE.md`：当前打包技能集说明
- 每个顶层目录都是一个 skill
- `agents/openai.yaml`：技能的界面元数据
- `references/`：按需加载的参考资料
- `scripts/`：可复用脚本
- `assets/`：可复用展示资源，例如字符图标

### 使用方式

作为 Git 仓库使用：

```powershell
git clone git@github.com:LanceAdd/RedTeaPowers.git
```

作为 Codex skills 使用时，把 skill 目录安装或复制到：

```text
~/.codex/skills
```

在这台机器上通常是：

```text
C:\Users\lanceadd\.codex\skills
```

`PACKAGE.md` 适合作为仓库级和包级说明，但不是 Codex 运行时发现 skill 的硬性要求。

### 推荐入口

1. 先用 `using-redteapowers` 做总路由。
2. 用 `shaping-work` 决定是直接开发、checklist、plan，还是 `spec + plan`。
3. 在锁定验证方式前先用 `choosing-test-strategy`。
4. 需要决定文档类型时使用 `managing-project-docs`。

### 迁移入口

如果你在迁移旧版 `superpowers` 工作流，建议先看：

- `using-redteapowers/references/migrating-from-superpowers.md`
- `using-redteapowers/references/workflow-overview.md`
- `using-redteapowers/references/library-status-matrix.md`

### 编码策略

所有项目文档都应以 UTF-8 文本读写。

这不是建议，而是项目规则。
