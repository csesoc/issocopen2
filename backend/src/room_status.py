# -*- coding: utf-8 -*-
import time
from datetime import datetime
class RoomStatus():
    def __init__(self):
        self._is_door_closed = None
        self._is_people_inside = None
        self._timestamp = datetime.now().strftime("%d-%m-%Y %H:%M")

    def set_is_door_closed(self, status: bool):
        '''
        set self._is_door_closed = status
        '''
        if not isinstance(status, bool):
            raise TypeError(f"type of status should be bool but I get {type(bool)}")
        self._is_door_closed = status
        self._timestamp = datetime.now().strftime("%d-%m-%Y %H:%M")

    def set_people_status(self, status: bool):
        '''
        set self._is_people_closed = status
        '''
        if not isinstance(status, bool):
            raise TypeError(f"type of status should be bool but I get {type(bool)}")
        
        self._is_people_inside = status
        self._timestamp = datetime.now().strftime("%d-%m-%Y %H:%M")

    def get_room_status(self) -> str:
        '''
        this method returns the  general status of the room
        '''

        if self._is_people_inside is None or self._is_door_closed is None:
            return "Unknown"
        elif self._is_door_closed and self._is_people_inside:
            return "The soc is open"
        elif self._is_door_closed and not self._is_people_inside:
            return "The soc is closed" 
        elif not self._is_door_closed:
            return "The soc is open"

    # properties
    @property
    def door_status(self):
        if self._is_door_closed is None:
            return "Unkown"
        return "Closed" if self._is_door_closed else "Open"

    @property
    def is_people_inside(self):
        if self._is_door_closed is None:
            return "Unknown"
        return "People inside" if self._is_people_inside else "Empty"

    @property
    def timestamp(self):
        return self._timestamp



