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

RedTeaPowers 是一套面向结构化软件开发的技能库，默认采用更轻、更快、更贴近真实交付节奏的流程。

## 项目概述

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

## 为什么不继续用 Superpowers，而要重新做这套 Skill

做 `RedTeaPowers`，不是因为 `superpowers` 没有价值，而是因为继续沿用它的默认行为，会持续把同一类交付问题带回项目里。

原体系在“提供结构”这件事上是强的，但也很容易被过度使用。实际开发中，团队可能会在真正开始编码前花太多时间做需求收敛、写流程文档、切过小的闭环，最后流程感很强，推进速度却不高。

`RedTeaPowers` 的目标不是抛弃这些能力，而是保留有价值的纪律，同时改掉默认工作方式。

## 它解决了哪些痛点

- 实现前过度收敛。很多中小任务在真正开始开发前，会陷入过多澄清、过多切片、过多前置结构设计。
- `spec` 和 `plan` 被习惯性强制产出。即使 checklist 或直接开发已经足够，也很容易先写文档再说。
- 文档体系太单薄。大量信息被挤进 `spec` 和 `plan`，导致文档难导航、易碎片化、用途混杂。
- TDD 被默认化。哪怕任务本质上更适合人工验证、探索式开发或集成检查，也会承受 tests-first 的惯性压力。
- 同类小问题被拆成多个微循环。明明可以一次批量处理的低风险问题，被拆成很多轮单独推进。
- 第一刀之后缺少转批量推进的机制。先切一刀打开局面本来是合理的，但如果没有后续规则，很容易长期停留在“小步但低效”的状态里。
- 文档编码不一致。没有明确规范时，项目文档很容易混入不同编码，影响长期维护和自动化处理。

一句话概括：`RedTeaPowers` 面向的是那些仍然需要结构，但更希望结构服务交付效率，而不是反过来拖慢交付的团队。

## 核心默认规则

RedTeaPowers 的默认规则是：

1. 先使用最轻但足够安全的流程。
2. 先定型工作，再决定是否需要文档和流程工件。
3. 当同时出现 `3` 个以上同类低风险问题时，默认合批处理。
4. 第一刀只用于打开专题局面，不用于无限切小片。
5. 先选择最贴近真实风险的验证方式，再进入实现。
6. 所有项目文档统一使用 UTF-8 读写。

## 内置技能

工作流与路由：

- `using-redteapowers`
- `shaping-work`
- `researching-and-collecting`
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
- `migrating-project-docs`
- `requesting-code-review`
- `receiving-code-review`
- `subagent-driven-development`

辅助技能：

- `using-git-worktrees`
- `finishing-a-development-branch`

## 相对原版 Superpowers 的主要魔改

RedTeaPowers 不是简单重命名，而是修改了原体系的默认工作方式。

### 1. 从强制流程改成按需路由

原版更容易把任务推向：

```text
brainstorm -> spec -> plan -> execute
```

RedTeaPowers 改成：

```text
route -> shape -> 只增加真正有帮助的下一层
```

也就是说，直接开发、批量 checklist、轻量 plan、`spec + plan` 都是合法路径，不再只有一条固定通道。

### 2. 增加“需求收敛护栏”

这是 RedTeaPowers 最核心的魔改之一：

- 默认使用小收敛预算
- 只提会改变路线的问题
- 开发前避免生成多个活跃工件
- 已经能看到的同类低风险问题优先合批
- 第一刀打开方向后，要尽快转入批量推进

### 3. `spec` 和 `plan` 不再是默认终点

在 RedTeaPowers 里：

- `spec` 用于已批准的目标行为和边界
- `plan` 用于可执行的实现顺序
- `todolist` 用于近期活跃任务
- `guide`、`discuss`、`reference`、`change`、`archive` 都是正式文档类型

### 4. TDD 从默认教条变成可选策略

原版生态更容易形成“默认 tests first”的惯性。

RedTeaPowers 要求先选验证方式，再决定是否需要 TDD：

- TDD
- 回归测试
- 集成检查
- 人工验证
- 先探索后收敛

### 5. 文档体系从双轨扩展为多类型系统

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

### 6. 名称、命名空间和路径整体重做

- `using-superpowers` -> `using-redteapowers`
- `superpowers:skill-name` -> `redteapowers:skill-name`
- `.superpowers/` -> `.redteapowers/`
- `~/.config/superpowers/...` -> `~/.config/redteapowers/...`

### 7. 不是全盘照搬，而是主动裁剪

这个仓库不是“原版全量镜像”，而是当前活跃技能的干净工作集。

历史内容、实验材料和不适合默认启用的部分，没有继续保留在主包里当作活跃指导。

### 8. 一些技能边界被重新定义

- `using-superpowers` 被正式替换为 `using-redteapowers`
- 原本偏 agent dispatch 的思路，被重构进 `subagent-driven-development`
- 一些 prompt 从 `spec` 中心视角改成了更贴近实际范围控制的写法
- 默认活跃技能集合被重新筛选，强调“少而有效”

## 仓库结构

- `README.md` 是英文版仓库首页
- `README.zh-CN.md` 是中文版仓库首页
- `PACKAGE.md` 是当前打包技能集说明
- 每个顶层目录都是一个 skill
- `agents/openai.yaml` 是技能的界面元数据
- `references/` 是按需加载的参考资料
- `scripts/` 是可复用脚本
- `assets/` 是可复用展示资源，例如字符图标

## 使用方式

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

## 推荐入口

1. 先用 `using-redteapowers` 做总路由。
2. 用 `shaping-work` 决定是直接开发、checklist、plan，还是 `spec + plan`。
3. 在锁定验证方式前先用 `choosing-test-strategy`。
4. 需要决定文档类型时使用 `managing-project-docs`。

## 迁移入口

如果你在迁移旧版 `superpowers` 工作流，建议先看：

- `using-redteapowers/references/migrating-from-superpowers.md`
- `using-redteapowers/references/workflow-overview.md`
- `using-redteapowers/references/library-status-matrix.md`

## 编码策略

所有项目文档都应以 UTF-8 文本读写。

这不是建议，而是项目规则。
