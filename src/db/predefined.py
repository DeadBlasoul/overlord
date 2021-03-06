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

EVENT_TYPES = [
    { 'name': 'member_join', 'description': 'user joined DS' },
    { 'name': 'member_leave', 'description': 'user left DS by himself' },
    { 'name': 'new_message', 'description': 'user posted new message' },
    { 'name': 'message_edit', 'description': 'user edited message' },
    { 'name': 'message_delete', 'description': 'user deleted message' },
    { 'name': 'vc_join', 'description': 'user joined VC' },
    { 'name': 'vc_leave', 'description': 'user left VC' }
]

USER_STAT_TYPES = [
    { 'name': 'new_message_count', 'description': 'overall message sent count per user' },
    { 'name': 'delete_message_count', 'description': 'overall message delete count per user' },
    { 'name': 'edit_message_count', 'description': 'overall message edit count per user' },
    { 'name': 'vc_time', 'description': 'overall time spent in voice chat per user in seconds' },
    { 'name': 'membership', 'description': 'days user being member of discord server' },
    { 'name': 'min_weight', 'description': 'minimal weith (rank) applicable to user' },
    { 'name': 'max_weight', 'description': 'maximal weith (rank) applicable to user' },
    { 'name': 'exact_weight', 'description': 'exact weith (rank) applicable to user' }
]
