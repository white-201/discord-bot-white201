import discord

TOKEN = access_token
client = discord.Client()
@client.event

async def on_message(message):
    if message.author.bot:
        return None
    if message.content.startswith("바보"):
        await message.channel.send("응 바보 니가 더 바보")
        print('응 바보 니가 더 바보')
    if message.content.startswith("카르페"):
        await message.channel.send("팀빨")
        print('팀빨')
    if message.content.startswith("!비고"):
        await message.channel.send("전43 현마딱")
        print('전43 현마딱')
    if message.content.startswith("!베놈"):
        await message.channel.send("잘할때는 4500, 못할때는 450")
        print('잘할때는 4500, 못할때는 450')
    if message.content.startswith("멍청이"):
        await message.channel.send("응 너가 더 멍청이")
        print('응 너가 더 멍청이')
    if message.content.startswith("?"):
        await message.channel.send("먼 물음표야 갈고리 펴 임마 (! 이렇게)")
        print('먼 물음표야 갈고리 펴 임마 (! 이렇게)')
    #if message.content.startswith("!"):
        #await message.channel.send("먼 느낌표야 예의 바르게 굽혀 임마 (? 이렇게)")
        #print('먼 물음표야 갈고리 펴 임마 (! 이렇게)')
    if message.content.startswith("ㅇㅇ"):
        await message.channel.send("먼 싸가지 없게 ㅇㅇ이야 귀엽게 웅♥ 하십쇼")
        print('먼 싸가지 없게 ㅇㅇ이야 귀엽게 웅♥ 하십쇼')
    if message.content.startswith("ㅈㅅ"):
        await message.channel.send("미안하지 말고, 잘하십쇼")
        print('미안하지 말고, 잘하십쇼')
    if message.content.startswith("ㅠ"):
        await message.channel.send("울지마라 토닥토닥 해주기 전에")
        print('울지마라 토닥토닥 해주기 전에')
    if message.content.startswith("ㅎ"):
        await message.channel.send("웃지마라 그 웃음 나만 볼꺼니까")
        print('웃지마라 그 웃음 나만 볼꺼니까')
    if message.content.startswith("귀엽다"):
        await message.channel.send("내가 더 귀엽지? 헹~♥")
        print('내가 더 귀엽지? 헹~♥')
    if message.content.startswith("귀여워"):
        await message.channel.send("내가 더 귀엽지? 헹~♥")
        print('내가 더 귀엽지? 헹~♥')
    if message.content.startswith("귀욤"):
        await message.channel.send("내가 더 귀엽지? 헹~♥")
        print('내가 더 귀엽지? 헹~♥')
    if message.content.startswith("ㅋ"):
        await message.channel.send("크크크킄")
        print('크크크킄')
    if message.content.startswith("ㅆㅂ"):
        await message.channel.send("욕하지 마라!")
        print('욕하지 마라!')
    if message.content.startswith("지랄"):
        await message.channel.send("욕하지 마라!")
        print('욕하지 마라!')
    if message.content.startswith("ㅅㅂ"):
        await message.channel.send("욕하지 마라!")
        print('욕하지 마라!')
    if message.content.startswith("ㅗ"):
        await message.channel.send("욕하지 마라!")
        print('욕하지 마라!')
    if message.content.startswith("밥줘"):
        await message.channel.send("밥줘")
        print('밥줘')
    if message.content.startswith("가능"):
        await message.channel.send("ㅆ가능")
        print('ㅆ가능')
    if message.content.startswith("웅♥"):
        await message.channel.send("에욱 우욱 에웁")
        print('에욱 우욱 에웁')
    if message.content.startswith("웅:heart:"):
        await message.channel.send("에욱 우욱 에웁")
        print('에욱 우욱 에웁')
    if message.content.startswith("ㅁㅊ"):
        await message.channel.send("나는 너를 못보면 미칠 것 같은데")
        print('나는 너를 조금이라도 안보면 미칠 것 같은데')
    if message.content.startswith("패드립"):
        await message.channel.send("니 애미 떡 돌리다 떡쳤냐 시발련아 (출처:김지수)")
        print('니 애미 떡 돌리다 떡쳤냐 시발련아')
    if message.content == "응애":
            channel = message.channel
            msg = "응애아가<@{}>밥죠".format(message.author.id)
            await channel.send(msg)
    if message.content == "야":
            channel = message.channel
            msg = "<@{}>아 왜 처부르냐".format(message.author.id)
            await channel.send(msg)
    if message.content.startswith("!채널메시지"):
        channel = message.content[7:25]
        msg = message.content[26:]
        await client.get_channel(int(channel)).send(msg)
    
    if message.content.startswith("!노래"):
        await message.channel.send("https://www.youtube.com/watch?v=YpCkdyhiVhw \nhttps://www.youtube.com/watch?v=9cxbIqnC8jI \n ")
        print('https://www.youtube.com/watch?v=YpCkdyhiVhw')


    if message.content.startswith("!빵톨이"):
        await message.channel.send("그냥 잼민이")
        print('그냥 잼민이')
    if message.content.startswith("!장은성"):
        await message.channel.send("그냥 잼민이")
        print('그냥 잼민이')
    if message.content.startswith("!이민현"):
        await message.channel.send("마빡왕")
    if message.content.startswith("!윤정익"):
        await message.channel.send("내가 제일 귀엽지")
        print('내가 제일 귀엽지')
    if message.content.startswith("!레바"):
        await message.channel.send("악질 민초단")
        print('악질 민초단')
    if message.content.startswith("!한동현"):
        await message.channel.send("떠들떠들")
        print('떠들떠들')
    if message.content.startswith("!김상권"):
        await message.channel.send("내가 좀 귀엽지? 나도 알아")
        print('내가 좀 귀엽지? 나도 알아')
    if message.content.startswith("!하재현"):
        await message.channel.send("다이어트 한다면서 안하신분")
        print('다이어트 한다면서 안하신분')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----------------')
    game = discord.Game("white201")
    await client.change_presence(status=discord.Status.online, activity=game)

client.run(TOKEN)
