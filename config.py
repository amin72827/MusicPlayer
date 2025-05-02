"""
Music Player, Telegram Voice Chat Bot
Copyright (c) 2021-present Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    def __init__(self) -> None:
        self.API_ID: str = os.environ.get("19769686", None)
        self.API_HASH: str = os.environ.get("515b64f5d2d955cdd6aa85a808fd4cb4", None)
        self.SESSION: str = os.environ.get("AgEtqVYAIBz31WyrBBjdK2i8aIYndovh8dymI1u9doyOd5YH73WsXanvTiOw99g7zwVMobNUdfEmAEITi0MIiRReM8HeQj9Ua6t0yNtkenEAdik9L8mplzz7DojXJIdksBtKNuBMNggBrB06yyX_dfMUcB49nJcKnbo-b-7hFITypHiN8aBAxSSRnAsIydX3HSuCqVjztPh1YLDdkwVbaRGz5VmuT3Qhx7GabaThHAXCygszzr6fJKoPN6tS9Xkjdh_de4WOdQel_JFtd0Im7s3dhG6orAgxqNMgOaa-ITseZVk3ZetZWHAHgTklhrDsxqiX39aOzYEMVWRfS8SPOPaor2Yu1gAAAAGC_6I6AA", None)
        self.BOT_TOKEN: str = os.environ.get("7128782242:AAENypkyECvS57mm7nGhIQNvqkTWQS2VLeI", None)
        self.SUDOERS: list = [
            int(id) for id in os.environ.get("SUDOERS", "7652416346").split() if id.isnumeric()
        ]
        if not self.SESSION or not self.API_ID or not self.API_HASH:
            print("ERROR: SESSION, API_ID and API_HASH is required!")
            quit(0)
        self.SPOTIFY: bool = False
        self.QUALITY: str = os.environ.get("QUALITY", "high").lower()
        self.PREFIXES: list = os.environ.get("PREFIX", "!").split()
        self.LANGUAGE: str = os.environ.get("LANGUAGE", "en").lower()
        self.STREAM_MODE: str = (
            "audio"
            if (os.environ.get("STREAM_MODE", "audio").lower() == "audio")
            else "video"
        )
        self.ADMINS_ONLY: bool = os.environ.get("ADMINS_ONLY", False)
        self.SPOTIFY_CLIENT_ID: str = os.environ.get("SPOTIFY_CLIENT_ID", None)
        self.SPOTIFY_CLIENT_SECRET: str = os.environ.get("SPOTIFY_CLIENT_SECRET", None)


config = Config()
