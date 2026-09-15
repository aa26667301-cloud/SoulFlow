# SoulFlow

**Open-source Mind · Body · Spirit Reflection Engine**

SoulFlow 是一個以繁體中文為優先的開源「身心靈自我覺察引擎」。它將日常狀態拆成 **Mind（心理／思緒）**、**Body（身體）**、**Spirit（意義／價值／內在連結）** 三個維度，提供可解釋、可擴充、可被 AI Agent 或 App 重複使用的反思工作流。

> SoulFlow 是自我照護與反思工具，不是醫療、心理治療、診斷或危機處理服務。

## 特色

- 三軸狀態 Check-in：Mind / Body / Spirit
- 規則式建議引擎：結果可解釋，不需要 API Key
- 12 種低風險反思與放鬆練習
- 日誌 Prompt 產生器
- 安全邊界：避免診斷、療效保證、依賴式陪伴
- JSON 資料層，方便網站、Bot、App、AI Agent 串接
- `SKILL.md`：可做為 AI 身心靈陪伴 Skill 的基礎
- CLI：可直接在終端機執行
- MIT License

## 快速開始

需要 Python 3.10+，不需安裝第三方套件。

```bash
python -m soulflow.cli checkin --mind 2 --body 4 --spirit 3
```

產生反思問題：

```bash
python -m soulflow.cli journal --theme "工作焦慮"
```

列出練習：

```bash
python -m soulflow.cli practices
```

## 三軸模型

### Mind
關注思緒速度、注意力、情緒負荷與心理空間。

### Body
關注疲勞、呼吸、肌肉緊繃、睡眠感受與身體訊號。

### Spirit
此處不是宗教判定，而是「意義感、價值感、方向感、與自己連結的感受」。

三軸採 1–5 分自評：

- 1：非常低／非常吃力
- 2：偏低
- 3：普通
- 4：穩定
- 5：良好

系統只根據使用者自評提供低風險建議，不從分數推導疾病或人格標籤。

## 專案結構

```text
SoulFlow/
├── README.md
├── LICENSE
├── SAFETY.md
├── AGENTS.md
├── CONTRIBUTING.md
├── CHANGELOG.md
├── pyproject.toml
├── data/
│   ├── practices.json
│   └── journal_prompts.json
├── soulflow/
│   ├── __init__.py
│   ├── engine.py
│   ├── journal.py
│   ├── safety.py
│   └── cli.py
├── skills/
│   └── mind-body-soul/
│       └── SKILL.md
├── examples/
│   └── example_usage.py
└── tests/
    └── test_engine.py
```

## 設計原則

1. **反思，不診斷**：不把自評結果轉成心理疾病、醫療判斷或靈性權威結論。
2. **自主，不依賴**：建議使用者保有決定權，不塑造「只有 AI 懂你」的關係。
3. **低風險優先**：預設使用呼吸、伸展、散步、喝水、寫日誌、休息、整理環境等一般性做法。
4. **靈性內容採選擇性框架**：冥想、意圖設定、象徵性反思可使用，但不宣稱超自然結果為客觀事實。
5. **可解釋**：建議會附上觸發原因。

## 可延伸方向

- Web UI / Streamlit
- 個人化日誌
- 週／月狀態趨勢
- Apple Health / Google Fit 等資料接入（需另外處理隱私與授權）
- OpenTarot 串接：將塔羅視為「象徵性反思工具」而非確定性預言
- 多語系
- 本機模型／LLM Agent Adapter

## License

MIT License。你可以自由使用、修改與二次開發，但請保留授權聲明。
