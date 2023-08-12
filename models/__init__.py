#!/usr/bin/python3
from models.engine.file_storage import FileStorage
"""__init__ module defining the global storage management object"""

storage = FileStorage()
storage.reload()
