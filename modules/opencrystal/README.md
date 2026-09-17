# OpenCrystal module

OpenCrystal 是 SoulFlow v0.2.0 的「水晶象徵反思」開源模組。

它不是水晶療效資料庫，而是把常見水晶名稱、顏色與文化性象徵整理成 **結構化的自我反思資料**，可供 CLI、App、Bot 或 AI Agent 使用。

## 能做什麼

- 依主題匹配水晶象徵：清晰、專注、界線、關係、轉換、創作、價值、行動等。
- 產生反思問題與一個可觀察的小行動。
- 建立 5–30 分鐘的低風險反思流程。
- 支援中文名、英文名與 id 查詢。
- 不需要 API Key，不依賴第三方套件。

## 不能做什麼

- 不宣稱治病、治療心理疾病、調整人體能量或磁場。
- 不用水晶推斷疾病、懷孕、財運、投資、死亡或他人的想法。
- 不保證招財、復合、轉運、避邪或任何確定結果。

## CLI

```bash
python -m soulflow.cli crystals --theme "工作很亂，想更專注" --limit 3
python -m soulflow.cli crystal-card --theme "最近很難拒絕別人的要求" --crystal 黑碧璽
python -m soulflow.cli ritual --theme "準備進入新的工作階段" --minutes 10
```

資料來源檔：`data/crystals.json`  
程式：`soulflow/crystals.py`  
AI Skill：`skills/crystal-reflection/SKILL.md`
