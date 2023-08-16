from pyrogram import Client

api_id = 9899039  # API ID KIRITING
api_hash = '5bab03171ae5e0d92e3e0ce70137943c' # API HASH KIRITING
app = Client(
    "my_bot",
    api_id=api_id,
    api_hash=api_hash
)

app.start()
from_chat_id = int(input("AZO OLMOQCHI BOLGAN GURUH IDSINI KIRITING: "))# A'zo tanlamoqchi bolgan guruhingiz ID raqamini kiritng
my_chat_id = int(input("AZO QO'SHMOQCHI BOLGAN GURUH IDSINI KIRITING: "))
# DASTURCHI @MrGayratov Kanal : @KingsOfPy
while True:
    from_chat_id = from_chat_id # A'zo tanlamoqchi bolgan guruhingiz ID raqamini kiritng
    my_chat_id = my_chat_id # A'zolarni qo'shmoqchi bo'lgan guruhingiz ID raqamini kiritng
    members = [] # Foidalanuvchi idlarini ro'yxatga ko'chirish yani olish uchun
    # DASTURCHI @MrGayratov Kanal : @KingsOfPy
    for member in app.get_chat_members(from_chat_id):
        members.append(member.user.id)
    # DASTURCHI @MrGayratov Kanal : @KingsOfPy
    try:
        app.add_chat_members(chat_id=my_chat_id, user_ids=members)
    except:pass
# DASTURCHI @MrGayratov Kanal : @KingsOfPy
app.run()
