# SoulFlow

**Open-source Mind · Body · Spirit Reflection Engine**

SoulFlow 是繁體中文優先的開源身心靈自我覺察引擎。它把日常反思拆成可重複使用的資料、規則與 AI Skills，讓 CLI、Bot、App 與 Agent 都能使用。

> SoulFlow 是自我照護與反思工具，不是醫療、心理治療、診斷、危機處理或預測服務。

## v0.3.0 模組

### OpenCrystal
24 種常見水晶的文化／象徵式反思資料，不宣稱療效或能量效果。

### OpenMoon
8 階段月相反思模板，把月相當成週期式日誌框架，不做運勢預測。

### OpenDream
夢境記錄、主題標籤與個人聯想工作流，不提供固定夢典，也不把夢當成預言或診斷。

### OpenMeditation
8 種一般性覺察與冥想練習，3–30 分鐘可調整，任何不適都可以立即停止。

## 核心功能

- Mind / Body / Spirit 三軸 Check-in
- 12 種低風險日常練習
- 日誌 Prompt 產生器
- OpenCrystal 水晶象徵反思
- OpenMoon 月相週期反思
- OpenDream 夢境日誌
- OpenMeditation 冥想工作流
- AI `SKILL.md`
- JSON 資料層
- Python CLI
- MIT License
- 核心功能不需要 API Key

## 快速開始

需要 Python 3.10+。

```bash
python -m soulflow.cli checkin --mind 2 --body 4 --spirit 3
python -m soulflow.cli journal --theme "工作焦慮"
python -m soulflow.cli crystals --theme "最近工作很亂，想更專注"
python -m soulflow.cli moon --phase 滿月 --theme "最近的工作成果"
python -m soulflow.cli dream --text "我夢到在學校趕不上考試"
python -m soulflow.cli meditations --theme "最近太忙，想安靜一下" --minutes 10
```

## CLI

```text
checkin        Mind / Body / Spirit 自評
journal        日誌問題
practices      一般性練習
crystals       水晶象徵素材推薦
crystal-card   水晶反思卡
ritual         水晶象徵反思流程
moon           單一月相反思
moon-cycle     八階段月相反思循環
dream          夢境標籤與日誌問題
meditations    冥想練習推薦
meditate       建立冥想 Session
```

## 設計原則

1. **反思，不診斷**：不把結果轉成疾病、人格或醫療判斷。
2. **象徵，不預測**：水晶、月相與夢境可作為反思素材，但不宣稱能預知結果。
3. **自主，不依賴**：AI 與模組提供選項，不替使用者決定人生。
4. **低風險優先**：呼吸、伸展、日誌、散步、休息、界線與可觀察的小行動。
5. **Local-first**：核心規則與資料可在本機執行，不需 API Key。
6. **可解釋**：推薦與標籤以明確規則產生。

## 專案結構

```text
SoulFlow/
├── data/
│   ├── practices.json
│   ├── journal_prompts.json
│   ├── crystals.json
│   ├── moon_phases.json
│   ├── dream_themes.json
│   └── meditations.json
├── soulflow/
│   ├── engine.py
│   ├── journal.py
│   ├── crystals.py
│   ├── moon.py
│   ├── dreams.py
│   ├── meditation.py
│   ├── safety.py
│   └── cli.py
├── modules/
│   ├── opencrystal/
│   ├── openmoon/
│   ├── opendream/
│   └── openmeditation/
├── skills/
│   ├── mind-body-soul/
│   ├── crystal-reflection/
│   ├── moon-reflection/
│   ├── dream-reflection/
│   └── meditation-guide/
└── tests/
```

## 測試

```bash
python -m unittest discover -s tests -v
```

## License

MIT License。可自由使用、修改與二次開發，請保留授權聲明。
