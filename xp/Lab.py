#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File : xp/Experience.py
# Description : Experience object.
# Auteur : Nils Schaetti <nils.schaetti@unine.ch>
# Date : 30.05.2017
# Lieu : Nyon, Suisse
#
# This file is part of the RPyLabXP Project.
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
from xp.Experience import Experience


# Lab object
class Lab(object):
    """
    Lab object.
    """

    # Constructor
    def __init__(self, connection, name):
        """
        Constructor.
        :param connection: Connection object.
        :param name: Laboratory's name.
        """
        # Property
        self._connection = connection
        self._name = name
        self._db = connection.get_db()
        self._collection = self._db["lab_" + name]
    # end __init__

    #########################################
    # Getter / setter
    #########################################

    # Get collection
    def get_collection(self):
        """
        Get collection
        :return: MongoDB collection object.
        """
        return self._collection
    # end get_collection

    #########################################
    # Public functions
    #########################################

    # Create an experience
    def create_experience(self, name, instance_id=-1):
        """
        Create an experience.
        :param name: Experience's name.
        :param instance_id: Instance's ID.
        :return: Experience object.
        """
        return Experience(self, name, instance_id)
    # end create_instance

# end Experience