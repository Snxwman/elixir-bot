import argparse

import hikari
import lightbulb

from elixir.config import Config

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dev', action='store_true')
    args = parser.parse_args()

    filepath = 'config.toml' if not args.dev else 'config_dev.toml'
    config = Config(filepath)

    bot = lightbulb.BotApp(
        token=config.discord_token,
        prefix=None,
        intents=hikari.Intents.all
    )   

    bot.run()