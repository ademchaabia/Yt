#!/usr/bin/env python3
# Copyright (C) @subinps
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
class Config:
    API_ID = int(os.environ.get("10586376", ''))
    API_HASH = os.environ.get("0b450b5173377b25f61a758d0b60019a", "")
    BOT_TOKEN = os.environ.get("5177999465:AAEOWM1xYaqswwM3LUvJ-xyWEJoXk7K9zfM", "")     
    LOG_CHANNEL = int(os.environ.get("@ou_3n", ''))
