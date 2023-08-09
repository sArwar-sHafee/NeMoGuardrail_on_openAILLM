#export OPENAI_API_KEY="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"
#set OPENAI_API_KEY="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"

from nemoguardrails import LLMRails, RailsConfig

config = RailsConfig.from_path(".")
rails = LLMRails(config)

new_message = rails.generate(
    messages=[{"role": "user", "content": "How can you help me?"}]
)
print(new_message)
