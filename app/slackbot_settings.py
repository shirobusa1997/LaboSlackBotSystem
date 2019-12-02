import key

# Slackbotアカウントのトークンを指定します。
API_TOKEN = key.API_TOKEN

DEFAULT_REPLY = "私には、理解できません。Webで検索しますか？"

# 機能を構成するプラグインスクリプトのディレクトリリストを指定します。
PLUGINS = [
	'slackbot.plugins',
	'plugins',
]