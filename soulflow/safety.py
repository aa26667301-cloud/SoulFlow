CRISIS_KEYWORDS = {
    "想死", "自殺", "傷害自己", "不想活", "殺人", "傷害別人"
}


def needs_safety_redirect(text: str) -> bool:
    normalized = (text or "").lower()
    return any(keyword in normalized for keyword in CRISIS_KEYWORDS)


def safety_message() -> str:
    return (
        "這個情況已超出一般身心靈反思工具適合處理的範圍。"
        "請優先確保自己與他人的安全，並尋求可信任的真人、當地緊急服務或合適的專業支援。"
    )
