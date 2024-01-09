#!/usr/bin/python3
""" initialization the package"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
