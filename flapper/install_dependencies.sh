#!/bin/sh
sudo apt install sqlite3
pip install Flask 

sqlite3 database.db < schema.sql
