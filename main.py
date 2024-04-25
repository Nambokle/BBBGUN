import json , requests , aiohttp , nextcord , config , re , os
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

async def logsend(embed):
  async with aiohttp.ClientSession() as session:
    webhook = nextcord.Webhook.from_url(config.webhook, session=session)
    await webhook.send(embed=embed)
    
async def logtopup(embed):
  async with aiohttp.ClientSession() as session:
    webhook = nextcord.Webhook.from_url(config.topup_log, session=session)
    await webhook.send(embed=embed)

class Modal1(nextcord.ui.Modal):
    def __init__(self):
        super().__init__(f"รู้จักจากใคร") 
        self.username = nextcord.ui.TextInput(label="ชื่อ (ถ้าไม่มีให้ - เฉยๆ)", required=True)
        self.add_item(self.username)

    async def callback(self, interaction: nextcord.Interaction):
        accdata = json.load(open('./db/acc.json', 'r'))
        accdata[str(interaction.user.id)]['point'] -= 0
        json.dump(accdata, open("./db/acc.json", "w"), indent=1)
        if self.username.value:
            role = nextcord.utils.get(interaction.guild.roles, id=1230910045236236358)
            if role in interaction.user.roles:
                embed = nextcord.Embed(description=f"ไม่สำเร็จกรุณาลองใหม่อีกครั้ง :NightWolves69: ", color=0xff6961)
                await interaction.send(embed=embed, ephemeral=True)
            else:
                embed = nextcord.Embed(description=f"เข้าร้านสำเร็จยินดีต้อนรับรุ่นใหญ่", color=0x77dd77)
                await logsend(nextcord.Embed(title=f"คนเข้าร้านมาใหม่",description=f"คนนี้ <@{interaction.user.id}> \n\n รู้จักจาก {self.username.value}"))
                await interaction.user.add_roles(role)
                await interaction.send(embed=embed, ephemeral=True)
        else:
            await interaction.response.send_message(embed=nextcord.Embed(description=f"กรุณากรอกชื่อ"), ephemeral=True)

class Modal2(nextcord.ui.Modal):
    def __init__(self):
        super().__init__(f"รู้จักจากใคร") 
        self.username = nextcord.ui.TextInput(label="ชื่อ (ถ้าไม่มีให้ - เฉยๆ)", required=True)
        self.add_item(self.username)

    async def callback(self, interaction: nextcord.Interaction):
        accdata = json.load(open('./db/acc.json', 'r'))
        accdata[str(interaction.user.id)]['point'] -= 0
        json.dump(accdata, open("./db/acc.json", "w"), indent=1)
        if self.username.value:
            role = nextcord.utils.get(interaction.guild.roles, id=1230910045236236358)
            if role in interaction.user.roles:
                embed = nextcord.Embed(description=f"ไม่สำเร็จกรุณาลองใหม่อีกครั้ง :NightWolves69: ", color=0xff6961)
                await interaction.send(embed=embed, ephemeral=True)
            else:
                embed = nextcord.Embed(description=f"เข้าร้านสำเร็จยินดีต้อนรับรุ่นใหญ่", color=0x77dd77)
                await logsend(nextcord.Embed(title=f"คนเข้าร้านมาใหม่",description=f"คนนี้ <@{interaction.user.id}> \n\n รู้จักจาก {self.username.value}"))
                await interaction.user.add_roles(role)
                await interaction.send(embed=embed, ephemeral=True)
        else:
            await interaction.response.send_message(embed=nextcord.Embed(description=f"กรุณากรอกชื่อ"), ephemeral=True)

class Modal3(nextcord.ui.Modal):
    def __init__(self):
        super().__init__(f"รู้จักจากใคร") 
        self.username = nextcord.ui.TextInput(label="ชื่อ (ถ้าไม่มีให้ - เฉยๆ)", required=True)
        self.add_item(self.username)

    async def callback(self, interaction: nextcord.Interaction):
        accdata = json.load(open('./db/acc.json', 'r'))
        accdata[str(interaction.user.id)]['point'] -= 0
        json.dump(accdata, open("./db/acc.json", "w"), indent=1)
        if self.username.value:
            role = nextcord.utils.get(interaction.guild.roles, id=1230910045236236358)
            if role in interaction.user.roles:
                embed = nextcord.Embed(description=f"ไม่สำเร็จกรุณาลองใหม่อีกครั้ง :NightWolves69: ", color=0xff6961)
                await interaction.send(embed=embed, ephemeral=True)
            else:
                embed = nextcord.Embed(description=f"เข้าร้านสำเร็จยินดีต้อนรับรุ่นใหญ่", color=0x77dd77)
                await logsend(nextcord.Embed(title=f"คนเข้าร้านมาใหม่",description=f"คนนี้ <@{interaction.user.id}> \n\n รู้จักจาก {self.username.value}"))
                await interaction.user.add_roles(role)
                await interaction.send(embed=embed, ephemeral=True)
        else:
            await interaction.response.send_message(embed=nextcord.Embed(description=f"กรุณากรอกชื่อ"), ephemeral=True)

class Modal4(nextcord.ui.Modal):
    def __init__(self):
        super().__init__(f"รู้จักจากใคร") 
        self.username = nextcord.ui.TextInput(label="ชื่อ (ถ้าไม่มีให้ - เฉยๆ)", required=True)
        self.add_item(self.username)

    async def callback(self, interaction: nextcord.Interaction):
        accdata = json.load(open('./db/acc.json', 'r'))
        accdata[str(interaction.user.id)]['point'] -= 0
        json.dump(accdata, open("./db/acc.json", "w"), indent=1)
        if self.username.value:
            role = nextcord.utils.get(interaction.guild.roles, id=1230910045236236358)
            if role in interaction.user.roles:
                embed = nextcord.Embed(description=f"ไม่สำเร็จกรุณาลองใหม่อีกครั้ง :NightWolves69: ", color=0xff6961)
                await interaction.send(embed=embed, ephemeral=True)
            else:
                embed = nextcord.Embed(description=f"เข้าร้านสำเร็จยินดีต้อนรับรุ่นใหญ่", color=0x77dd77)
                await logsend(nextcord.Embed(title=f"คนเข้าร้านมาใหม่",description=f"คนนี้ <@{interaction.user.id}> \n\n รู้จักจาก {self.username.value}"))
                await interaction.user.add_roles(role)
                await interaction.send(embed=embed, ephemeral=True)
        else:
            await interaction.response.send_message(embed=nextcord.Embed(description=f"กรุณากรอกชื่อ"), ephemeral=True)

class Modal5(nextcord.ui.Modal):
    def __init__(self):
        super().__init__(f"รู้จักจากใคร") 
        self.username = nextcord.ui.TextInput(label="ชื่อ (ถ้าไม่มีให้ - เฉยๆ)", required=True)
        self.add_item(self.username)

    async def callback(self, interaction: nextcord.Interaction):
        accdata = json.load(open('./db/acc.json', 'r'))
        accdata[str(interaction.user.id)]['point'] -= 0
        json.dump(accdata, open("./db/acc.json", "w"), indent=1)
        if self.username.value:
            role = nextcord.utils.get(interaction.guild.roles, id=1230910045236236358)
            if role in interaction.user.roles:
                embed = nextcord.Embed(description=f"ไม่สำเร็จกรุณาลองใหม่อีกครั้ง :NightWolves69: ", color=0xff6961)
                await interaction.send(embed=embed, ephemeral=True)
            else:
                embed = nextcord.Embed(description=f"เข้าร้านสำเร็จยินดีต้อนรับรุ่นใหญ่", color=0x77dd77)
                await logsend(nextcord.Embed(title=f"คนเข้าร้านมาใหม่",description=f"คนนี้ <@{interaction.user.id}> \n\n รู้จักจาก {self.username.value}"))
                await interaction.user.add_roles(role)
                await interaction.send(embed=embed, ephemeral=True)
        else:
            await interaction.response.send_message(embed=nextcord.Embed(description=f"กรุณากรอกชื่อ"), ephemeral=True)


class Modal6(nextcord.ui.Modal):
    def __init__(self):
        super().__init__(f"Win100") 
        self.username = nextcord.ui.TextInput(label="Yes / No ", required=True)
        self.add_item(self.username)

    async def callback(self, interaction: nextcord.Interaction):
        accdata = json.load(open('./db/acc.json', 'r'))
        accdata[str(interaction.user.id)]['point'] -= 0
        json.dump(accdata, open("./db/acc.json", "w"), indent=1)
        if self.username.value:
            role = nextcord.utils.get(interaction.guild.roles, id=1230910045236236358)
            if role in interaction.user.roles:
                embed = nextcord.Embed(description=f"โหลด -> [Download](https://cdn.discordapp.com/attachments/1230937747653656596/1231281410711752828/Winner100.bat?ex=6636632c&is=6623ee2c&hm=bc19fd07e5e3924b8db621d3a90fc55baeb375afd5835f29efeabef02f3b43bc&) \n หากไฟล์ Error หรือ มีปัญหา ให้แจ้งแอดมิน หรือคนที่มียศ <@&1230909514685874329> นะคะ :NightWolves30: ", color=0x77dd77)
                await logsend(nextcord.Embed(title=f"คนนี้รับโปรแกรม",description=f"คนนี้ <@{interaction.user.id}> \n\n ได้รับ ProFiveM"))
                await interaction.send(embed=embed, ephemeral=True)
            else:
                embed = nextcord.Embed(description=f"เกิดข้อผิดพลาดกรุณาลองใหม่ภายหลัง :NightWolves69: " , color=0xff6961)
        else:
            await interaction.response.send_message(embed=nextcord.Embed(description=f"กรุณาแจ้ง ADMIN :NightWolves69: "), ephemeral=True)

            
class Menu(nextcord.ui.Select):
    def __init__(self):
      options = [
        nextcord.SelectOption(label='YouTube',description='รู้จากYouTube',value='1'),
        nextcord.SelectOption(label='FaceBook',description='รู้จากFaceBook',value='2'),
        nextcord.SelectOption(label='เพื่อนแนะนำ',description='รู้จากกับเพื่อนรัก',value='3'),
        nextcord.SelectOption(label='จาก X',description='รู้จาก Twitter',value='4'),
        nextcord.SelectOption(label='TikTok',description='รู้จาก TikTok',value='5'),
      ]
      super().__init__(custom_id='menu',placeholder='เลือกสักอย่าง',options=options)
    async def callback(self, interaction: nextcord.Interaction):
        type = self.values[0]
        money = json.load(open('./db/acc.json'))[str(interaction.user.id)]['point']
        if type == '1':
            need = 0 - money
            if money < 0:
             await interaction.send(f'มีเงินไม่พอ ต้องการ 50 บาท (ขาดอีก {need} บาท)',ephemeral=True)
             return 
            else:
             await interaction.response.send_modal(Modal1())
        if type == '2':
            need = 0 - money
            if money < 0:
             await interaction.send(f'มีเงินไม่พอ ต้องการ 75 บาท (ขาดอีก {need} บาท)',ephemeral=True)
             return 
            else:
             await interaction.response.send_modal(Modal2())

        if type == '3':
            need = 0 - money
            if money < 0:
             await interaction.send(f'มีเงินไม่พอ ต้องการ 100 บาท (ขาดอีก {need} บาท)',ephemeral=True)
             return 
            else:
             await interaction.response.send_modal(Modal3())

        if type == '4':
            need = 0 - money
            if money < 0:
             await interaction.send(f'มีเงินไม่พอ ต้องการ 150 บาท (ขาดอีก {need} บาท)',ephemeral=True)
             return 
            else:
             await interaction.response.send_modal(Modal4())

        if type == '5':
            need = 0 - money
            if money < 0:
             await interaction.send(f'มีเงินไม่พอ ต้องการ 200 บาท (ขาดอีก {need} บาท)',ephemeral=True)
             return 
            else:
             await interaction.response.send_modal(Modal5())


class Menu1(nextcord.ui.Select):
    def __init__(self):
      options = [
        nextcord.SelectOption(label='Win100',description='โปรแกรมช่วยเล่น',value='6'),
      ]
      super().__init__(custom_id='menu',placeholder='เลือกสักอย่าง',options=options)
    async def callback(self, interaction: nextcord.Interaction):
        type = self.values[0]
        money = json.load(open('./db/acc.json'))[str(interaction.user.id)]['point']
        if type == '6':
            need = 0 - money
            if money < 0:
             await interaction.send(f'มีเงินไม่พอ ต้องการ 50 บาท (ขาดอีก {need} บาท)',ephemeral=True)
             return 
            else:
             await interaction.response.send_modal(Modal6())
        if type == '7':
            need = 0 - money
            if money < 0:
             await interaction.send(f'มีเงินไม่พอ ต้องการ 75 บาท (ขาดอีก {need} บาท)',ephemeral=True)
             return 
            else:
             await interaction.response.send_modal(Modal2())

        if type == '8':
            need = 0 - money
            if money < 0:
             await interaction.send(f'มีเงินไม่พอ ต้องการ 100 บาท (ขาดอีก {need} บาท)',ephemeral=True)
             return 
            else:
             await interaction.response.send_modal(Modal3())

        if type == '9':
            need = 0 - money
            if money < 0:
             await interaction.send(f'มีเงินไม่พอ ต้องการ 150 บาท (ขาดอีก {need} บาท)',ephemeral=True)
             return 
            else:
             await interaction.response.send_modal(Modal4())

        if type == '10':
            need = 0 - money
            if money < 0:
             await interaction.send(f'มีเงินไม่พอ ต้องการ 200 บาท (ขาดอีก {need} บาท)',ephemeral=True)
             return 
            else:
             await interaction.response.send_modal(Modal5())


class Button(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @nextcord.ui.button(label='กดเพื่อรับยศ', style=nextcord.ButtonStyle.green, emoji='✅',custom_id="buy")
    async def buy(self, button: nextcord.Button, interaction: nextcord.Interaction):
        if check(interaction.user.id) == False or True:
            await interaction.send(embed=nextcord.Embed(description=f"กรุณาเลือกว่าคุณรู้จักเราจากไหน",color=0xFFFF00).set_image(url='https://as1.ftcdn.net/v2/jpg/06/57/40/90/1000_F_657409059_DJfZw3x0862BneFTwrs3JKevADotLuzy.jpg'),view=Select(),ephemeral=True)



class Button1(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @nextcord.ui.button(label='กดเพื่อรับโปรแกรม', style=nextcord.ButtonStyle.green, emoji='🛒',custom_id="buy")
    async def buy(self, button: nextcord.Button, interaction: nextcord.Interaction):
        if check(interaction.user.id) == False or True:
            await interaction.send(embed=nextcord.Embed(description=f"ต้องการโปรแกรมอะไร",color=0xFFFF00).set_image(url='https://as2.ftcdn.net/v2/jpg/04/74/01/67/1000_F_474016746_VizB3ikvvjFUF5yfw7VMD4EEext4cIU4.jpg'),view=Select1(),ephemeral=True)



class Select(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(Menu())

class Select1(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(Menu1())
           
      
@bot.event
async def on_ready():
    bot.add_view(Button())
    print(f"BOT NAME : {bot.user}")


@bot.slash_command(guild_ids=[config.guild_id],description=f"setup")
async def setup(interaction: nextcord.Interaction):
        await interaction.channel.send(embed=nextcord.Embed(description=f"# กดเพื่อรับยศ",color=0xFFFF00).set_image(url='https://media.discordapp.net/attachments/1230913418580721715/1230923424076140604/pixlr-image-generator-03e4f964-24c1-4c72-b958-960c68d72175.png?ex=663515c5&is=6622a0c5&hm=b5a0e5717787ca80544ff703e5a74de4a1c66216940513414e1e4463909786df&=&format=webp&quality=lossless&width=550&height=314'),view=Button())
        await interaction.send('สำเร็จ!',ephemeral=True)

@bot.slash_command(guild_ids=[config.guild_id],description=f"setupshop")
async def setupshop(interaction: nextcord.Interaction):
        await interaction.channel.send(embed=nextcord.Embed(description=f"# กดเพื่อรับโปรแกรม",color=0xFFFF00).set_image(url='https://media.discordapp.net/attachments/1230913418580721715/1230925118340071484/pixlr-image-generator-55f3464d-cb23-4c8c-9493-5f0044d5a932.png?ex=66351759&is=6622a259&hm=90bdd1e702a05fe046a86e333dc2bfb4348f451aa58d3321bafcb4d388afdf62&=&format=webp&quality=lossless&width=869&height=497'),view=Button1())
        await interaction.send('สำเร็จ!',ephemeral=True)
    
def check(id):
    accdata = json.load(open('./db/acc.json', 'r'))
    if str(id) in accdata:
        print(f'{id} in db')
        return True
        
    else:
        print(f'{id} not in db')
        accdata[id] = {
            "point" : 0,
            "pointall" : 0
        }
        json.dump(accdata, open("./db/acc.json", "w"), indent = 4)

bot.run(config.token)
