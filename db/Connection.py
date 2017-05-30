#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File : db/Connection.py
# Description : Connection object to mongoDB.
# Auteur : Nils Schaetti <nils.schaetti@unine.ch>
# Date : 30.05.2017
# Lieu : Nyon, Suisse
#
# This file is part of the PyLabXP Project.
# The PyLabXP Project is a set of free software:
# you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Foobar is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
#

# Import packages
from pymongo import MongoClient
from xp.Lab import Lab


# Connection object
class Connection(object):
    """
    Connection object.
    """

    # Constructor
    def __init__(self, host="localhost", port=27017, db_name="pylabxp"):
        """
        Constructor
        :param host:
        :param port:
        """
        # Global params
        self._host = host
        self._port = port
        self._db_name = db_name

        # Connect
        self._client = MongoClient(host, port)
        self._db = self._client[db_name]
    # end __init__

    #########################################
    # Getter / setter
    #########################################

    # Get hostname
    def get_hostname(self):
        """
        Get hostname
        :return: Hostname
        """
        return self._host
    # end get_hostname

    # Get port
    def get_port(self):
        """
        Get port
        :return: Port number
        """
        return self._port
    # end get_port

    # Get DB name
    def get_db_name(self):
        """
        Get DB name
        :return: DB name
        """
        return self._db_name
    # end get_db_name

    # Get DB
    def get_db(self):
        """
        Get DB object
        :return: DB object
        """
        return self._db
    # end get_db

    #########################################
    # Public functions
    #########################################

    # Create or open an instance
    def instance(self, lab_name, exp_name, instance_id=-1):
        """
        Create or get an instance.
        :param lab_name:
        :param exp_name:
        :param instance_id:
        :return:
        """
        lab = self.get_lab(lab_name)
        return lab.create_experience(name=exp_name, instance_id=instance_id)
    # end create

    # Create a laboratory
    def create_lab(self, name):
        """
        Create a laboratory.
        :param name: Laboratory's name
        :return: A laboratory object
        """
        # New lab.
        return Lab(self, name)
    # end create_experience

    # Get a laboratory
    def get_lab(self, name):
        """
        Get a laboratory
        :param name:
        :return:
        """
        return self.create_lab(name)
    # end get_lab

    # Insert a document
    def insert_one(self, post):
        """
        Insert a document.
        :param post:
        :return:
        """
        self._db.insert_one(post)
    # end insert_one

# end Connection