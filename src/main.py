import os

import discord
from dotenv import load_dotenv

from src.game.test import p1, p2, print_info

MY_GUILD = discord.Object(id='1344764484681465928')

class MyClient(discord.Client):

    johnny = 0

    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = discord.app_commands.CommandTree(self)

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author.bot:
            return
        await message.channel.send(print_info() + "\n" + "What card would you like to play? Do /test_game [index of card]")
        # print(f'Message from {message.author}: {message.content}')
        # file = discord.File("../resources/images/characters/liu_bei.png")
        # embed = discord.Embed(title="Liu Aei's baobei", type='image', description="Baobei大家好こんにちは")
        # embed.set_image(url="attachment://../resources/images/characters/liu_bei.png")
        # channel = message.channel
        # await channel.send(file = file, embed = embed)

    async def setup_hook(self) -> None:
        # This copies the global commands over to your guild.
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)

def main():
    load_dotenv()

    intents = discord.Intents.default()
    intents.message_content = True

    client = MyClient(intents=intents)

    @client.tree.command(name="test_game", description="Zoinks")
    async def test_game(interaction: discord.Interaction, index: int, is_self: bool) -> None:
        if MyClient.johnny % 2 == 0:
            if is_self:
                p1.play(index, p1)
            else:
                p1.play(index, p2)
        else:
            if is_self:
                p2.play(index, p2)
            else:
                p2.play(index, p1)
        MyClient.johnny += 1
        await interaction.response.send_message("Hi")

    client.run(os.getenv("DISCORD_TOKEN"))


if __name__ == "__main__":
    main()