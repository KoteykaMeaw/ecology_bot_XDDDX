import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


ecology = ['Покупать только то, что действительно необходимо, отдавая предпочтение долговечным вещам. Вы избавитесь от бесконечного захламления, окружите себя качественными предметами и будете производить меньше мусора.'
'Ответственно избавляться от опасных отходов, к которым, например, относятся электроника, ртутные лампы и термометры, бытовая химия, лаки, краски, просроченные лекарства, отработанные масла, автомобильные покрышки и др. Если они попадут на свалку, то будут загрязнять воздух, почву и подземные воды, а если на переработку, то станут источником ценных материалов. Пункты приема опять же можно найти на карте recyclemap.ru или следить за акциями вроде #ЭлектроОсень. А чтобы снизить потребление тех же батареек, можно их заменить аккумуляторами (батарейки стандартных размеров бывают перезаряжаемыми, и их можно приобрести в любом магазине электроники).',
'Займитесь облагораживанием своего города. Субботники, общественные акции по посадке деревьев, волонтерские программы по сбору мусора в парках – в этих мероприятиях можно поучаствовать без вреда для бюджета и с пользой для собственного здоровья.  Попробуйте пойти туда вместе с близкими  - так вы не только поможете улучшить экологическую обстановку, но и хорошо проведете время с семьей, ведь совместный труд, как известно, сближает.',
'Отдавайте ненужные вещи.  Дома зачастую можно обнаружить массу вещей, которые вы не используете, но почему-то храните. Через некоторое время «хлам» полетит на свалку. Но ведь вы можете отдать те вещи, которые еще не утратили свои полезные свойства,  туда, где они могут пригодиться.  Есть множество благотворительных организаций, которые готовы принять старую одежду, технику, детские игрушки и передать их в приюты, детские дома или ночлеги для бездомных. Еще один вариант – разместить в интернете объявление с указанием того, что вы можете отдать даром. К примеру, на сайте «Отдам в дар» обмениваться вещами могут жители Москвы, Санкт-Петербурга и Украины, а на сайте «ДаруДар» обмениваться вещами можно из любой точки земного шара.',
'Не нарушайте закон. Это касается незаконной вырубки лесов, сбора редких и занесенных в  Красную книгу растений, браконьерства, умышленных или случайных поджогов, загрязнения речных вод химическими отходами и прочей противоправной деятельности. Иногда люди могут нарушить закон просто по незнанию – срубить елку к Новому году, сорвать подснежник, бросить непогашенный окурок в лесу, из-за которого разгорится пожар. За нарушение российского законодательства могут быть применены строгие санкции, вплоть до возникновения уголовной ответственности.  Но главное – может быть  нанесен непоправимый вред  природе, что, в конечном счете, негативно скажется  на самих жителях Земли.',
'Выбирайте правильные материалы. Экологи советуют избегать пластиковые пакетов и одноразовых товаров – полиэтилен  и пластик могут разлагаться на свалках долгие годы, а при их сжигании выделяется едкий черный дым. Так, пакеты в супермаркетах можно легко заменить холщовыми сумками, а одноразовую пластиковую посуду для пикника – картонными тарелками и многоразовыми приборами.',
'Избегать одноразовой посуды. Даже кажущиеся столь безобидными «бумажные» стаканчики для кофе сделаны не только из бумаги, но и из слоя пластика, из-за чего их практически не перерабатывают. Кстати, многоразовые кружки бывают складными, а экомагазины давно уже придумали целые наборы для еды в офисе и в дороге.',
'Во время праздников отказаться от воздушных шаров, пластиковых и фольгированных украшений, цветочных букетов и некачественных сувениров. Шарики и блестящие украшения нельзя сдать в переработку, и разлагаться они будут веками, а выращивание и транспортировка срезанных цветов с других континентов наносят большой ущерб природе. Некачественные или ненужные подарки, в свою очередь, рискуют оказаться среди мусора. Что делать? Для мероприятий можно подобрать украшения из бумаги, фруктов и овощей, а подарки делать с учетом пожеланий адресата, опять же избегая излишней одноразовой упаковки.',
'Интересоваться экологией и делиться информацией с другими. Если вам кажется, что в своем городе вы одиноки в своих «зеленых» стремлениях, проверьте, нет ли в вашем регионе инициативной группы проектов «Мусора.Больше.Нет», «РазДельный Сбор», «ЭКА», не проводятся ли уже «Чистые игры»? Даже если пока нет, к ним можно присоединиться или почерпнуть знания с их онлайн-ресурсов.'
]
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command('ecology')
async def what(ctx):
    um = random.choice(ecology)
    await ctx.send(um)

bot.run('token')
