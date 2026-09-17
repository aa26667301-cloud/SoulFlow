# SoulFlow

**Open-source Mind · Body · Spirit Reflection Engine**

SoulFlow 是繁體中文優先的開源「身心靈自我覺察引擎」。它把日常狀態拆成 **Mind（心理／思緒）**、**Body（身體）**、**Spirit（意義／價值／內在連結）** 三個維度，提供可解釋、可擴充、可讓 AI Agent、Bot、App 與 CLI 重複使用的反思工作流。

> SoulFlow 是自我照護與反思工具，不是醫療、心理治療、診斷或危機處理服務。

## v0.2.0 新增：OpenCrystal

OpenCrystal 將常見水晶整理成**象徵式反思素材**，目前內建 24 種水晶，支援：

- 主題 → 水晶象徵推薦
- 反思卡 `crystal-card`
- 5–30 分鐘象徵式反思流程 `ritual`
- 繁中／英文名稱與 id 查詢
- AI `SKILL.md`
- 完整安全聲明：不宣稱水晶具有醫療、心理治療、能量治療或預測效果

## 核心功能

- Mind / Body / Spirit 三軸 Check-in
- 規則式建議引擎，不需 API Key
- 12 種低風險反思與放鬆練習
- 日誌 Prompt 產生器
- OpenCrystal 24 種象徵資料與反思引擎
- AI Skills
- JSON 資料層
- CLI
- MIT License

## 快速開始

需要 Python 3.10+，核心功能不需第三方套件。

```bash
python -m soulflow.cli checkin --mind 2 --body 4 --spirit 3
python -m soulflow.cli journal --theme "工作焦慮"
python -m soulflow.cli practices
```

### 水晶象徵反思

```bash
python -m soulflow.cli crystals --theme "最近工作很亂，想更專注" --limit 3
```

指定水晶產生反思卡：

```bash
python -m soulflow.cli crystal-card --theme "最近很難拒絕別人的要求" --crystal 黑碧璽
```

建立 10 分鐘反思流程：

```bash
python -m soulflow.cli ritual --theme "準備進入新的工作階段" --minutes 10
```

## 三軸模型

### Mind
關注思緒速度、注意力、情緒負荷與心理空間。

### Body
關注疲勞、呼吸、肌肉緊繃、睡眠感受與身體訊號。

### Spirit
此處不是宗教判定，而是意義感、價值感、方向感，以及和自己連結的感受。

三軸採 1–5 分自評，系統只根據使用者自評提供低風險建議，不從分數推導疾病或人格標籤。

## 水晶模組的設計原則

SoulFlow 不把傳統或流行的水晶象徵描述成科學事實。資料中的「清晰、界線、轉換、創作」等欄位，是用來設計日誌問題與行動提示的**象徵標籤**。

例如「白水晶 → clarity」代表：

> 使用者可把白水晶當作「釐清與意圖」的提醒物件，接著回答一個問題並完成一個實際行動。

它不代表白水晶能治病、改變人體能量、保證招財或預測未來。

## 專案結構

```text
SoulFlow/
├── README.md
├── LICENSE
├── SAFETY.md
├── AGENTS.md
├── CONTRIBUTING.md
├── CHANGELOG.md
├── data/
│   ├── practices.json
│   ├── journal_prompts.json
│   └── crystals.json
├── soulflow/
│   ├── __init__.py
│   ├── engine.py
│   ├── journal.py
│   ├── crystals.py
│   ├── safety.py
│   └── cli.py
├── modules/
│   └── opencrystal/
│       └── README.md
├── skills/
│   ├── mind-body-soul/
│   │   └── SKILL.md
│   └── crystal-reflection/
│       └── SKILL.md
└── tests/
    ├── test_engine.py
    └── test_crystals.py
```

## 設計原則

1. **反思，不診斷**：不把自評或象徵內容轉成疾病、人格或醫療判斷。
2. **自主，不依賴**：AI 與象徵物只提供選項，不替使用者決定人生。
3. **低風險優先**：預設呼吸、伸展、散步、補水、日誌、整理環境等一般性做法。
4. **靈性內容採選擇性框架**：可使用冥想、意圖、水晶與塔羅等象徵素材，但不把超自然主張表述成客觀事實。
5. **可解釋**：推薦結果附帶 matched themes、反思問題與可觀察行動。

## 測試

```bash
python -m unittest discover -s tests -v
```

## 可延伸方向

- OpenTarot Adapter
- 月相日誌（象徵式、非天文預測）
- 夢境紀錄與主題標籤
- Web UI / Streamlit
- 週／月狀態趨勢
- 多語系
- 本機模型／LLM Agent Adapter

## License

MIT License。可自由使用、修改與二次開發，請保留授權聲明。
