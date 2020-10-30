#!/usr/bin/env python3
from dataclasses import dataclass


@dataclass
class Authentication:
    token: str = None
    user_id = None
    key = None
