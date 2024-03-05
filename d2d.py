import signal
import sys

import discum

from conf import TOKEN, TO_CHANNEL, FROM_CHANNELS, Verbose

bot = discum.Client(token=TOKEN, log=False)


def sigint_handler(signum, frame):
    print('Stop pressing the CTRL+C!')
    sys.exit(1)


signal.signal(signal.SIGINT, sigint_handler)


@bot.gateway.command
def helloworld(resp):
    if resp.event.ready_supplemental:  # ready_supplemental is sent after ready
        user = bot.gateway.session.user
        print("Logged in as {}#{}".format(user['username'], user['discriminator']))
    if resp.event.message:
        m = resp.parsed.auto()
        guildID = m['guild_id'] if 'guild_id' in m else None  # because DMs are technically channels too
        channelID = m['channel_id']
        username = m['author']['username']
        discriminator = m['author']['discriminator']
        content = m['content']
        attachments = m['attachments']
        embeds = m['embeds']

        try:
            serverName = bot.gateway.session.guild(guildID).name
            channelName = bot.gateway.session.guild(guildID).channels[channelID]['name']
        except:
            serverName = ""
            channelName = ""
        channelID = int(channelID)

        if channelID not in FROM_CHANNELS:
            return

        if Verbose:
            print("> {} | {} | {}#{} | {}".format(serverName, channelName, username, discriminator, content))

        # forward message to the target channel
        msg = f'🤖{username}\n'
        msg += content
        bot.sendMessage(f"{TO_CHANNEL}", msg)
        if attachments:
            # add attachments
            for attachment in m['attachments']:
                url = attachment['url']
                bot.sendFile(f"{TO_CHANNEL}", url, True)
                if Verbose:
                    print("> + attachment {}".format(url))
        if embeds:
            for embed in embeds:
                image = embed.get('image', {}).get('url', None)
                desc = embed.get('description', None)
                if image:
                    bot.sendFile(f"{TO_CHANNEL}", image, True)
                    if Verbose:
                        print("> + embed {}".format(image))
                elif desc:
                    bot.sendMessage(f"{TO_CHANNEL}", desc)
                    if Verbose:
                        print("> + embed {}".format(desc))
        print("\t> forwarded.")


if __name__ == '__main__':
    while True:
        try:
            bot.gateway.run(auto_reconnect=True)
        except:
            print('Found Exception')
            pass
        print('Restart')
