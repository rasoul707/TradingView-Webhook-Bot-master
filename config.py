# ----------------------------------------------- #
# Plugin Name           : TradingView-Webhook-Bot #
# Author Name           : fabston                 #
# File Name             : config.py               #
# ----------------------------------------------- #

# TradingView Example Alert Message:
# {
# "key":"9T2q394M92", "telegram":"-1001298977502", "discord":"789842349670960670/BFeBBrCt-w2Z9RJ2wlH6TWUjM5bJuC29aJaJ5OQv9sE6zCKY_AlOxxFwRURkgEl852s3", "msg":"Long #{{ticker}} at `{{close}}`"
# }

sec_key = (
    # Can be anything. Has to match with "key" in your TradingView alert message
    "rasoul7077777777"
)

# Telegram Settings
send_telegram_alerts = True
# Bot token. Get it from @Botfather
tg_token = "5386492523:AAFxvoCs0mFyMAx8yhklnVHHJiCM_ks4qM4"
channel = -1001368926240  # Channel ID (ex. -1001487568087)

# Discord Settings
send_discord_alerts = False
# Discord Webhook URL (https://support.discordapp.com/hc/de/articles/228383668-Webhooks-verwenden)
discord_webhook = ""

# Slack Settings
send_slack_alerts = False
# Slack Webhook URL (https://api.slack.com/messaging/webhooks)
slack_webhook = ""

# Twitter Settings
send_twitter_alerts = False
tw_ckey = ""
tw_csecret = ""
tw_atoken = ""
tw_asecret = ""

# Email Settings
send_email_alerts = False
email_sender = ""  # Your email address
email_receivers = ["", ""]  # Receivers, can be multiple
email_subject = "Trade Alert!"

email_port = 465  # SMTP SSL Port (ex. 465)
email_host = ""  # SMTP host (ex. smtp.gmail.com)
email_user = ""  # SMTP Login credentials
email_password = ""  # SMTP Login credentials
