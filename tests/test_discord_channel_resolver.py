from main import DiscordChannelResolver


class DiscordEvent:
    unified_msg_origin = "discord-main:FriendMessage:1465742362952335532"
    session_id = "1465742362952335532"
    message_obj = None

    @staticmethod
    def get_platform_name():
        return "discord"


def test_discord_instance_id_and_session_channel_are_supported():
    resolver = DiscordChannelResolver()
    event = DiscordEvent()

    assert resolver.is_discord_event(event)
    assert resolver.extract_channel_id(event) == 1465742362952335532
