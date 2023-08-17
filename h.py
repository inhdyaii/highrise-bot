from __future__ import annotations
from asyncio import Queue, sleep
from collections import Counter
from itertools import count
from typing import TYPE_CHECKING, Any, Callable, Literal, Protocol, TypeVar, Union
from aiohttp import ClientWebSocketResponse
from cattrs.preconf.json import make_converter
from quattro import TaskGroup
from highrise._unions import configure_tagged_union
from highrise.models import (
    AnchorHitRequest,
    AnchorPosition,
    BuyItemRequest,
    BuyRoomBoostRequest,
    BuyVoiceTimeRequest,
    ChangeBackpackRequest,
    ChangeRoomPrivilegeRequest,
    ChannelEvent,
    ChannelRequest,
    ChatEvent,
    ChatRequest,
    CheckVoiceChatRequest,
    CurrencyItem,
    EmoteEvent,
    EmoteRequest,
    Error,
    FloorHitRequest,
    GetBackpackRequest,
    GetConversationsRequest,
    GetInventoryRequest,
    GetMessagesRequest,
    GetRoomPrivilegeRequest,
    GetRoomUsersRequest,
    GetUserOutfitRequest,
    GetWalletRequest,
    IndicatorRequest,
    InviteSpeakerRequest,
    Item,
    KeepaliveRequest,
    LeaveConversationRequest,
    MessageEvent,
    ModerateRoomRequest,
    MoveUserToRoomRequest,
    Position,
    Reaction,
    ReactionEvent,
    ReactionRequest,
    RemoveSpeakerRequest,
    RoomModeratedEvent,
    RoomPermissions,
    SendMessageRequest,
    SessionMetadata,
    SetOutfitRequest,
    TeleportRequest,
    TipReactionEvent,
    TipUserRequest,
    User,
    UserJoinedEvent,
    UserLeftEvent,
    UserMovedEvent,
    VoiceEvent,
)
import random
from highrise.webapi import WebAPI

if TYPE_CHECKING:
    from attrs import AttrsInstance
else:

    class AttrsInstance(Protocol):
        pass
__all__ = [
    "BaseBot",
    "Highrise",
    "User",
    "Position",
    "Reaction",
    "AnchorPosition",
    "RoomPermissions",
]
A = TypeVar("A", bound=AttrsInstance)
T = TypeVar("T")

welc =["♥️{} نورت يا", "وان هالغيبة {} 🥲 ", "وسعوا للمعلم {} 🥸", "احلى حدا بالروم {}🤤 ", "{}  وبس والباقي كله خس", "ريقة ريقة ريقة {}  يا حريقة", "سنانك ولا ضو القمر {} 😮", " شفتك هات بوسة 💋{}  "]

name_ad = ["your_username", "anther_username"]
valuesss = "ghjk"
dans = [
  "emote-kiss",
  "emote-no",
  "emote-sad",
  "emote-yes",
  "emote-laughing",
  "emote-hello",
  "emote-wave",
  "emote-shy",
  "emote-tired",
  "emoji-angry",
  "idle-loop-sitfloor",
  "emoji-thumbsup",
  "emote-lust",
  "emoji-cursing",
  "emote-greedy",
  "emoji-flex",
  "emoji-gagging",
  "emoji-celebrate",
  "dance-macarena",
  "dance-tiktok8",
  "dance-blackpink",
  "emote-model",
  "dance-tiktok2",
  "dance-pennywise",
  "emote-bow",
  "dance-russian",
  "emote-curtsy",
  "emote-snowball",
  "emote-hot",
  "emote-snowangel",
  "emote-charging",
  "dance-shoppingcart",
  "emote-confused",
  "idle-enthusiastic",
  "emote-telekinesis",
  "emote-float",
  "emote-teleporting",
  "emote-swordfight",
  "emote-maniac",
  "emote-energyball",
  "emote-snake",
  "idle-singing",
  "emote-frog",
  "emote-superpose",
  "emote-cute",
  "dance-tiktok9",
  "dance-weird",
  "dance-tiktok10",
  "emote-pose7",
  "emote-pose8",
  "idle-dance-casual",
  "emote-pose1",
  "emote-pose3",
  "emote-pose5",
  "emote-cutey",
  "dance-wrong"
]
ter = ""
import asyncio
class BaseBot:
    """A base class for Highrise bots.
    Bots join a room and interact with everything in it.

    Subclass this class and implement the handlers you want to use.

    The `self.highrise` attribute can be used to make requests.
    """

    highrise: Highrise
    webapi: WebAPI

    valuesss = "ghjk"
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
    async def before_start(self, tg: TaskGroup) -> None:
        """Called before the bot starts."""
        pass

    async def on_start(self, session_metadata: SessionMetadata) -> None:
        """On a connection to the room being established.

        This may be called multiple times, since the connection may be dropped
        and reestablished.
        """
        try:
            await self.highrise.walk_to(Position(17.0, 0.0, 3.5))
        except:
            print("erorr")
        pass
    async def on_user_move(
        self, user: User, destination: Position | AnchorPosition
    ) -> None :

        try:
            if valuesss == user.username:
                self.x = destination.x
                self.y = destination.y
                self.z = destination.z
                await self.highrise.walk_to(Position(self.x, self.y, self.z - 1))
            if user.username == ter :
                list = await self.highrise.get_room_users()
                for user, position in list.content:
                    if user.username == ter:
                        if isinstance(position, AnchorPosition):
                            print(f"AnchorPosition(entity_id={position.entity_id}, anchor_ix={position.anchor_ix}")
                        else:
                            await self.highrise.teleport(user.id, Position(x=position.x, y=position.y, z=position.z))
        except Exception as e:
            print(f"حدث خطأ: {e}")
        pass
    async def on_chat(self, user: User, message: str) -> None:
        """On a received room-wide chat."""


        if message.startswith("اجلس") and user.username in name_ad:
            try:
                await self.highrise.walk_to(AnchorPosition(entity_id='643330af000000000000040d', anchor_ix=0))
            except Exception as e:
                print(f"حدث خطأ: {e}")
        if message.startswith("تحول") and user.username in name_ad:
            await self.highrise.set_outfit(outfit=[
				                  Item(
                                                      type='clothing',
                                                      amount=1,
                                                      id='body-flesh',
                                                      account_bound=False,
                                                      active_palette=27
                                                  ),
                                                  Item(
                                                      type='clothing',
                                                      amount=1,
                                                      id='eye-n_basic2018malesquaresleepy',
                                                      account_bound=False,
                                                      active_palette=7
                                                  ),
                                                  Item(
                                                      type='clothing',
                                                      amount=1,
                                                      id='eyebrow-n_basic2018newbrows07',
                                                      account_bound=False,
                                                      active_palette=0
                                                  ),
                                                  Item(
                                                      type='clothing',
                                                      amount=1,
                                                      id='nose-n_basic2018newnose05',
                                                      account_bound=False,
                                                      active_palette=0
                                                  ),

                                                  Item(
                                                      type='clothing',
                                                      amount=1,
                                                      id='hair_front-n_basic2018wavypulledback',
                                                      account_bound=False,
                                                      active_palette=0
                                                  ),
                                                  Item(
                                                      type='clothing',
                                                      amount=1,
                                                      id='hair_back-n_basic2018straightlonglowpigtails',
                                                      account_bound=False,
                                                      active_palette=0
                                                  ),
		                                              Item(
		                                                  type='clothing',
		                                                  amount=1,
		                                                  id='mouth-basic2018chippermouth',
		                                                  account_bound=False,
		                                                  active_palette=-1
		                                              ),
		                                              Item(
		                                                  type='clothing',
		                                                  amount=1,
		                                                  id='glasses-n_starteritems201roundframesbrown',
		                                                  account_bound=False,
		                                                  active_palette=-1
		                                              ),
		                                              Item(
		                                                  type='clothing',
		                                                  amount=1,
		                                                  id='bag-n_room32019sweaterwrapblack',
		                                                  account_bound=False,
		                                                  active_palette=-1
		                                              ),
		                                              Item(
		                                                  type='clothing',
		                                                  amount=1,
		                                                  id='shirt-n_starteritems2019pulloverblack',  #shirt-n_starteritems2019tankwhite
		                                                  account_bound=False,
		                                                  active_palette=-1
		                                              ),
		                                              Item(
		                                                  type='clothing',
		                                                  amount=1,
		                                                  id='shorts-f_pantyhoseshortsnavy',
		                                                  account_bound=False,
		                                                  active_palette=-1
		                                              ),
		                                              Item(
		                                                  type='clothing',
		                                                  amount=1,
		                                                  id='shoes-n_whitedans',
		                                                  account_bound=False,
		                                                  active_palette=-1
		                                              ),
		                                              ])





            if message.startswith("لوب") and user.username in name_ad:
                random_dans = "dance-wrong"
                list = await self.highrise.get_room_users()
                for user, position in list.content:
                    try:
                        await self.highrise.send_emote(random_dans, user.id)
                    except:
                        print("erorr")

            if message.startswith("هزو") and user.username in name_ad:
                random_dans = random.sample(dans, 1)[0]
                list = await self.highrise.get_room_users()
                for user, position in list.content:
                    try:
                        await self.highrise.send_emote(random_dans, user.id)
                    except:
                        print("erorr")
            if message.startswith(".") and user.username in name_ad:
                list = await self.highrise.get_room_users()
                for user, position in list.content:
                    if user.username == "mr_cat":
                        positions = f"{position.x}, {position.y}, {position.z}"
                try:
                    for user, position in list.content:
                        await self.highrise.teleport(user.id, Position(x=position.x, y=position.y, z=position.z - 1))
                except Exception as e:
                    print(f"حدث خطأ: {e}")
        try:

            if message.startswith("رقصني") :
                random_dans = random.sample(dans, 1)[0]
                print(random_dans)
                await self.highrise.send_emote(random_dans, user.id)
            elif message.startswith("رقص") :
                random_dans = "idle-dance-casual"
                print(random_dans)
                await self.highrise.send_emote(random_dans, user.id)
        except:
            print("erorr")
        try:
            global valuesss
            if message.startswith("الحق") and user.username in name_ad:
                values = message.split()
                valuesss = values[1].replace("@", "")
            elif message.startswith("توقف") and user.username in name_ad:
                await self.highrise.chat("حسنا")
                valuesss = "#####"
                self.stopped = True
                return
        except:
            print("erorr")

        if message.startswith("انتقال") and user.username in name_ad:
            try:
                global ter
                values = message.split()
                ter = values[1].replace("@", "")
                print(ter)
            except:
                print("erorr")
        if message.startswith("id") and user.username in name_ad:
            try:
                values = message.split()
                valuesss = values[1].replace("@", "")
                print(f"{valuesss}")
                list = await self.highrise.get_room_users()
                username_targ = valuesss  # اسم المستخدم المطلوب
                for user, position in list.content:
                    if user.username == username_targ:
                        print(f"{user.id}")
            except:
                print("erorr")

        if message.startswith("يلا") and user.username == "mr_cat":
            list = await self.highrise.get_room_users()
            for user, position in list.content:
                try:
                    await self.highrise.move_user_to_room(user.id, '6433191')
                except Exception as e:
                    print(f"حدث خطأ: {e}")


        if message.startswith("كب") and user.username in name_ad:
            try:
                m = message.split()
                v = m[1].replace("@", "")
                print(f" v  :  {v}")
                room_users = await self.highrise.get_room_users()
                print(f"{room_users}")

                username_targ = v
                for user, position in room_users.content:
                    if user.username == username_targ:
                        print(f"ddd: {user.username}")
                        id_user = user.id
                        await self.highrise.move_user_to_room(id_user, '62b81')
            except Exception as e:
                print(f"حدث خطأ: {e}")

        if message.startswith("تعال") and user.username in name_ad:
            username_targ = user.username  # اسم المستخدم المطلوب
            list = await self.highrise.get_room_users()
            for user, position in list.content:
                if user.username == username_targ:
                    positions = f"{position.x}, {position.y}, {position.z}"
                    await self.highrise.walk_to(Position(x=position.x, y=position.y, z=position.z - 1))
        if message.startswith("/") and user.username in name_ad:
            values = message[1:].split(",")
            x = float(values[0])
            y = float(values[1])
            z = float(values[2])
            await self.highrise.teleport(user.id, Position(x, y, z))

        if message.startswith("k"):
           kl = await self.highrise.get_room_users()
           print (kl)
           list = await self.highrise.get_room_users()
           m = message.split()
           v = m[1].replace("@", "")
           username_targ = v

           for user, position in list.content:
               if user.username == username_targ:
                   print(f"User: {user.username}")
                   print(f"Position: ({position.x}, {position.y}, {position.z})")
                   print(f"id: {user.id}")
        pass

    async def on_whisper(self, user: User, message: str) -> None:
        """On a received room whisper."""
        if user.username in name_ad :
            txt = message
            await self.highrise.chat(txt)
        else:
            print("Invalid message format")
        pass

    async def on_emote(self, user: User, emote_id: str, receiver: User | None) -> None:
        """On a received emote."""
        pass

    async def on_reaction(self, user: User, reaction: Reaction, receiver: User) -> None:
        """Called when someone reacts in the room."""
        if reaction == "clap" and user.username in name_ad:
            r_username = receiver.username
            print(f"receiver: {r_username}")
            list = await self.highrise.get_room_users()
            username_targ = user.username
            for user, position in list.content:
                if user.username == username_targ:
                    print(f"User: {user.username}")
                    print(f"id: {user.id}")
                    positions = f"{position.x}, {position.y}, {position.z}"
                    await self.highrise.teleport(receiver.id, Position(x=position.x, y=position.y, z=position.z - 1))
        pass

    async def on_user_join(
        self, user: User, position: Position | AnchorPosition
    ) -> None:
        """On a user joining the room."""
        try:
            random_dans = random.sample(dans, 1)[0]
            await self.highrise.send_emote(random_dans, user.id)

            welc_j = random.sample(welc, 1)[0]
            await self.highrise.chat(welc_j.format(user.username))
            await self.highrise.send_whisper(user.id, "hi")
        except Exception as e:
                print(f"حدث خطأ: {e}")
        pass

    async def on_user_leave(self, user: User) -> None:
        """On a user leaving the room."""
        pass

    async def on_tip(
        self, sender: User, receiver: User, tip: CurrencyItem | Item
    ) -> None:
        """On a tip received in the room."""
        pass

    async def on_channel(self, sender_id: str, message: str, tags: set[str]) -> None:
        """On a hidden channel message."""
        pass

    async def on_voice_change(
        self, users: list[tuple[User, Literal["voice", "muted"]]], seconds_left: int
    ) -> None:
        """On a change in voice status in the room."""
        pass

    async def on_message(
        self, user_id: str, conversation_id: str, is_new_conversation: bool
    ) -> None:

        pass
    async def on_moderate(
        self,
        moderator_id: str,
        target_user_id: str,
        moderation_type: Literal["kick", "mute", "unmute", "ban", "unban"],
        duration: int | None,
    ) -> None:
        """When room moderation event is triggered."""
        pass

