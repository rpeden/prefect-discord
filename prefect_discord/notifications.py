from prefect.blocks.notifications import AppriseNotificationBlock


class DiscordWebhook(AppriseNotificationBlock):
    """
    Enables sending notifications via a Discord webhook.

    Attributes:
        url: The Discord webhook URL to send messages to.

    Examples:
        Load a saved Discord webhook and send a message:
        ```python
        from prefect_discord.notifications import DiscordWebhook

        discord_webhook_block = DiscordWebhook.load("BLOCK_NAME")
        discord_webhook_block.notify("Hello from Prefect!")
        ```
    """
    _block_type_name = "Discord Webhook"
    _block_type_slug = "discord-webhook"
    _logo_url = "https://res.cloudinary.com/dltn95ut1/image/upload/h_256/v1667583798/prefect/discord-logo-512_tyknd4.png" # noqa
