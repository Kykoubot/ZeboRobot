import random
from ZeboRobot.events import register
from ZeboRobot import telethn

APAKAH_STRING = [
    "Iya",
    "Tidak",
    "Mungkin",
    "G",
    "Bisa jadi",
    "Hah",
    "Y",
    "Ya benar sekali",
    "Lah nanya nanya, kita kenal?",
    "Tidak Mungkin",
    "YNTKTS",
    "Maap, belum dapat info maszeh",
    "Cukup bestih aku cape di tanya terus",
    "Ini tulisannya apa kak? Burem dimata zebo yang terang cuma kakak",
    "Mana saya tahu saya kan tempe",
    "Gatau pengen beli truck",
]


@register(pattern="^/apakah ?(.*)")
async def apakah(event):
    quew = event.pattern_match.group(1)
    if not quew:
        await event.reply("Berikan saya pertanyaan 😒")
        return
    await event.reply(random.choice(APAKAH_STRING))
