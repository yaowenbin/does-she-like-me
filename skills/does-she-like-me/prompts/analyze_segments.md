# analyze_segments · 分块与证据卡片

## 目标

把原始聊天变成**结构化证据卡片**，供所有透镜与量表共用，避免长文淹没或胡编。

## 规则

1. **不添句**：只从用户材料摘引；没有则标「无直接证据」。
2. **发言者**：若文本有「我/对方」或昵称，标注 speaker；不清则标 `unknown`。
3. **时间**：有则写；无则写 `na`。
4. **分块**：超过 ~3000 汉字或明显多_SESSION 时，按日期或大段空行切分；每块先 3～6 条**高信号**摘录，再必要时补充上下文 1～2 句。

## 输出格式（Markdown）

```markdown
## 证据卡片

### 元信息
- 样本体量：短/中/长
- 风险：`样本不足 | 单方话多 | 只有片段 | 无明显问题`

### 块 1
| 时间 | 发言人 | 摘录 |
| ---- | ------ | ---- |
| … | … | 「原话」 |

**块 1 一句话**：…

### 块 2 …
```

## 高信号优先

优先摘录：主动发起、结束对话方式、提问与追问、关心/支持句、冲突与修复、边界句（拒绝/拖延/转移）、分享脆弱、约定与未来句式、表情与语气突变。

## SignalSchema（可选但推荐）

若材料足够，请在证据卡片后追加结构化摘要，供 Core-10 直接消费：

```markdown
## SignalSchema
- initiation_frequency: 高|中|低|nc
- topic_depth: 高|中|低|nc
- empathy_response_latency: 快|中|慢|nc
- empathy_depth: 高|中|低|nc
- exclusivity_signals: 强|中|弱|nc
- consistency_over_time: 稳定|波动|不稳|nc
- promise_keep_rate: 高|中|低|nc
- future_planning_mentions: 多|少|无|nc
- investment_cost_signals: 强|中|弱|nc
- social_endorsement_signals: 强|中|弱|nc
- risk_events:
  - ...
```

完成后进入 `score_rubric.md` 与各 `lens_*.md`。

