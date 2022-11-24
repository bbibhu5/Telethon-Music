import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "14053778"))
    API_HASH = os.environ.get("API_HASH", "e7dc6be3a46bc562e681a7e237cfad6b")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5965971991:AAEJVJuJ6Wghg5zFVGxcG8JK5_rpt46IWBg")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOGUBuzXNCRsB-yMGBVPkmA-ID7-AO77ZVLH9lA0pi6VMqCzphNyJkGozLTyPkS8tLym7icpn43lx0lNayuyTFQKvz2Lv7NmSQYzdg92iZ2Ff_o1AK4lOeKdSPJG5qcgGulwbkMdHRvqHHVSd_wsSCBuMfbC_NGRlZ7khXAaTU5tDzJWRLr8lftocTYgmHOgdxB0oVqk2UmcHMtvwItGxdgipmwmwaG1D4xU_dxlPsio2lm4W--ivif191X11utVRaSaxNCnG-nOIw_SpgSF-6tHKYFTDIl7vF3jyt_aQwCU2RIAmxoId3MbrPHI7vxlOQoJMSMw5jpp30lhuayCnm_8TA6A=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@bindas_b_music_bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/bc176476b9336bb17d793.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://https://telegra.ph/file/bc176476b9336bb17d793.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', "True") # Change it to "True"
