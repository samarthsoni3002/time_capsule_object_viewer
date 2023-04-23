import openai

secretKey = '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'

openai.api_key = secretKey
openai.Model.list()

