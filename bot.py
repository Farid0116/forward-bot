from telethon import TelegramClient
import asyncio

# 🔹 Telegram API ma'lumotlari
API_ID = 22623074
API_HASH = "36d5d9407dc71a568e3a41c61f85e8f6"

# 🔹 Kanal ID yoki username
CHANNEL_IDENTIFIER = "UzTg_Price"  # Agar username bo‘lsa
# CHANNEL_IDENTIFIER = -1002266661579  # Agar ID bo‘lsa

# 🔹 Forward qilmoqchi bo‘lgan xabar ID
MESSAGE_ID = 2  # **To‘g‘ri ID kiriting!**

# 🔹 Xabar yuboriladigan guruh va kanallar ID-lari
TARGET_GROUPS = [-1002085547736, -1002137321912, -1002208256136, -1002458058163, -1002405419976]

client = TelegramClient("bot_session", API_ID, API_HASH)

async def send_messages():
    async with client:
        try:
            print("🔍 Xabar tekshirilmoqda...")

            # ✅ Kanaldan entity (ID) olish
            channel = await client.get_entity(CHANNEL_IDENTIFIER)

            # ✅ Xabarni olish
            message = await client.get_messages(channel, ids=MESSAGE_ID)

            # ❗️ Xabar borligini tekshirish
            if message is None:
                print(f"⚠️ Xabar ID {MESSAGE_ID} topilmadi! Xabar ID ni yana tekshirib ko'ring.")
            else:
                # ✅ Xabarni forward qilish
                for group_id in TARGET_GROUPS:
                    target_chat = await client.get_entity(group_id)
                    await client.forward_messages(target_chat, message)
                    print(f"✅ Xabar {MESSAGE_ID} forward qilindi: {group_id}")

        except Exception as e:
            print(f"❌ Xatolik: {e}")

# 🔹 Har 3 daqiqada xabar yuborish uchun loop
async def periodic_forward(interval=180):  # 180 soniya = 3 daqiqa
    while True:
        await send_messages()
        print("⌛ Keyingi xabar 3 daqiqadan keyin yuboriladi...")
        await asyncio.sleep(interval)  # Kutish

# 🔹 Botni ishga tushirish
if __name__ == "__main__":
    asyncio.run(periodic_forward(180))  # **Har 3 daqiqada xabar yuborish**
