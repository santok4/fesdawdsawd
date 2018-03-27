import discord
import time
import os
import sys
import requests
import json
import time
import datetime

def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any 
cleanup action (like
    saving data) must be done before calling 
this function. by https://www.daniweb.com/programming/software-development/code/260268/restart-your-python-program"""
    python = sys.executable
    os.execl(python, python, * sys.argv)

client = discord.Client()
TOKEN = os.environ.get('TOKEN', None)
Bot_Owner = '385407187796623360'

@client.event
async def on_ready():
    print(client.user.name + '으로 라현봇이 로그인 함.')
    await client.change_presence(game=discord.Game(name="기능 추가 문의 해 주세요! 라현#6731"))
@client.event
async def on_message(message):
    if message.content.startswith('라현아 테스트'): #if message.content.startswith('(명령어)'): = 명령어
        await client.send_message(message.channel, '테스트 성공!') #await client.send_message(message.channel, '(대답)') = (명령어)를 입력시 그 채널에 (대답)을 말합니다.

    if message.content.startswith("R.기능"):
        embed = discord.Embed(title="기능을 알려드리겠슙니다!", description="저는 R.재시작(봇을 재시작시킬수있음)\n라현아 테스트(이걸 가장먼저했을때 제가 테스트할려고썼던명령업니다)\nR.번역(번역을할수있습니다 하지만 아직불가능)\nR.코인시세(빗썸으로 코인 12개의 현재시가를보실수있음)\nR.현재시간(현재시간을보실수있어염)", color=0xFFFFFF)
        await client.send_message(message.channel, embed=embed)
    
    if message.content.startswith('R.재시작'):
        if message.author.id in Bot_Owner:
            embed = discord.Embed(title="재시작", description="재시작중.. 완료!", color=0xFFFFFF)
            await client.send_message(message.channel, embed=embed)
            time.sleep(2)
            restart_program()
            
    if message.content.startswith("R.번역"): 
        embed = discord.Embed(title="번역", description="아.직.불.가", color=0xFFFFFF)
        await client.send_message(message.channel, embed=embed)
   
    if message.content.startswith("R.코인시세"):
        r = requests.get("https://api.bithumb.com/public/ticker/all").content
        data = json.loads(r)
        data = data["data"]
        btc = data["BTC"]["closing_price"]
        eth = data["ETH"]["closing_price"]
        dash = data["DASH"]["closing_price"]
        ltc = data["LTC"]["closing_price"]
        etc = data["ETC"]["closing_price"]
        xrp = data["XRP"]["closing_price"]
        bch = data["BCH"]["closing_price"]
        xmr = data["XMR"]["closing_price"]
        zec = data["ZEC"]["closing_price"]
        qtum = data["QTUM"]["closing_price"]
        btg = data["BTG"]["closing_price"]
        eos = data["EOS"]["closing_price"]
        embed=discord.Embed(title="빗썸", description="빗썸 api에서 제공하는 현재 암호화폐 시세입니다.",color=0x62bf42)
        embed.add_field(name="비트코인 (BTC)", value=btc + "￦", inline=True)
        embed.add_field(name="이더리움 (ETH)", value=eth+ "￦", inline=True)
        embed.add_field(name="대시 (DASH)", value=dash+ "￦", inline=True)
        embed.add_field(name="라이트코인 (LTC)", value=ltc+ "￦", inline=True)
        embed.add_field(name="이더리움 클래식 (ETC)", value=etc+ "￦", inline=True)
        embed.add_field(name="리플 (XRP)", value=xrp+ "￦", inline=True)
        embed.add_field(name="비트캐시 (BCH)", value=bch+ "￦", inline=True)
        embed.add_field(name="모네로 (XMR)", value=xmr+ "￦", inline=True)
        embed.add_field(name="제트캐쉬 (ZEC)", value=zec+ "￦", inline=True)
        embed.add_field(name="퀀텀 (QTUM)", value=qtum+ "￦", inline=True)
        embed.add_field(name="비트코인 골드 (BTG)", value=btg+ "￦", inline=True)
        embed.add_field(name="이오스 (EOS)", value=eos+ "￦", inline=True)
        embed.set_footer(text="오류 수정은 라현#6731으로 문의 바랍니다 이코딩을 알려면 BGM#0970 님께 빌거나 아니면 불가능....")
        await client.send_message(message.channel, embed=embed)
       
    if message.content.startswith("R.라현봇 데려오기"): 
        await client.send_message(message.channel, "아 라현봇 데려오고 싶으세요? https://discordapp.com/api/oauth2/authorize?client_id=425562709967372288&permissions=0&redirect_uri=http%3A%2F%2Frahyan.bot&scope=bot 여기로 가시거나 라현#6731 로 해서 받는 디코 방 링크받으세요 ")  
        
    if message.content.startswith("R.현재시간"):
        now = time.localtime()
        now = "%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
        embed = discord.Embed(title="Time | 시간", description="현재시간은 (서버기준) " + now + " 입니다.", color=0xCC723D)
        await client.send_message(message.channel, embed=embed)
 


client.run(TOKEN)
