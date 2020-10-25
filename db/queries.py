#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###################################################
#........../\./\...___......|\.|..../...\.........#
#........./..|..\/\.|.|_|._.|.\|....|.c.|.........#
#......../....../--\|.|.|.|i|..|....\.../.........#
#        Mathtin (c)                              #
###################################################
#   Author: Daniel [Mathtin] Shiko                #
#   Copyright (c) 2020 <wdaniil@mail.ru>          #
#   This file is released under the MIT license.  #
###################################################

__author__ = 'Mathtin'

from .models import *
from .session import DBSession

def get_user_by_id(db: DBSession, id: int) -> User:
    return db.query(User).filter(User.did == id).first()

def get_msg_by_id(db: DBSession, id: int) -> MessageEvent:
    return db.query(MessageEvent).filter(MessageEvent.message_id == id).first()

