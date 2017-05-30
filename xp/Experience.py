#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File : xp/Experience.py
# Description : Experience object.
# Auteur : Nils Schaetti <nils.schaetti@unine.ch>
# Date : 30.05.2017
# Lieu : Nyon, Suisse
#
# This file is part of the Reservoir Computing NLP Project.
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

# Import package
import random
import sys
import traceback


# Experience object
class Experience(object):
    """
    Experience object.
    """

    # Constructor
    def __init__(self, lab, name, instance_id=-1):
        """
        Constructor
        :param lab: Experience's laboratory
        :param name: Experience's name
        :param instance_id: Instance's ID.
        """
        # Property
        self._lab = lab
        self._name = name
        self._collection = lab.get_collection()

        # Generate a random id
        if instance_id == -1:
            self._id = self._generate_id()
            self.save_globals()
        else:
            self._id = instance_id
        # end id
    # end __init__

    #########################################
    # Public functions
    #########################################

    # Save globals
    def save_globals(self):
        """
        Save globals
        :return:
        """

        # Cleaned data
        cleaned_globals = self._to_mongodb_data(globals())

        # Save
        if cleaned_globals is not None:
            self._collection.insert_one({"exp": self._name, "instance": self._id, "globals": cleaned_globals,
                                         "count": len(cleaned_globals)})
        # end if
    # end save_globals

    # Save variables
    def save_variables(self, variables):
        """
        Save variables
        :param variables:
        :return:
        """

        # Cleaned data
        cleaned_vars = self._to_mongodb_data(variables)

        # Insert
        self._collection.insert_one({"exp": self._name, "instance": self._id, "vars": cleaned_vars,
                                     "count": len(cleaned_vars)})
    # end save_variables

    # Save parameter value
    def save_parameter(self, param, value):
        """
        Save parameter value
        :param param:
        :param value:
        :return:
        """
        self._collection.insert_one({"exp": self._name, "instance": self._id, "param": param, "value": value})
    # end save_parameter

    # Save results
    def save_results(self, name, value, params=[]):
        """
        Save results
        :param name:
        :param value:
        :param params:
        :return:
        """
        self._collection.insert_one({"exp": self._name, "instance": self._id, "result": name, "value": value,
                                     "params": params})
    # end save_results

    # Save log
    def save_log(self, message):
        """
        Save log
        :param message:
        :return:
        """
        self._collection.insert_one({"exp": self._name, "instance": self._id, "message": unicode(message)})
    # end save_log

    # Save exec traces
    def save_traces(self):
        """
        Save exec traces
        :param e:
        :return:
        """
        self._collection.insert_one({"exp": self._name, "instance": self._id, "exc_info": unicode(sys.exc_info()[0]),
                                     "traceback": traceback.format_tb(sys.exc_info()[2])})
    # end save_exception

    #########################################
    # Private functions
    #########################################

    # Clean dictionary
    def _clean_dict(self, data):
        """
        Clean dictionary.
        :param data:
        :return:
        """
        result = dict()
        for index in data:
            cleaned = self._to_mongodb_data(data[index])
            if cleaned is not None:
                result[index] = cleaned
            # end if
        # end for
        return result
    # end _clean_dict

    # Clean list
    def _clean_list(self, data):
        """
        Clean list
        :param data:
        :return:
        """
        result = list()
        for value in data:
            cleaned = self._to_mongodb_data(value)
            if cleaned is not None:
                result.append(cleaned)
            # end if
        # end for
        return result
    # end _clean_list

    # To MongoDB data
    def _to_mongodb_data(self, data):
        """
        To MongoDB data
        :param data:
        :return:
        """
        if type(data) == str:
            return data
        elif type(data) == int:
            return data
        elif type(data) == float:
            return data
        elif type(data) == long:
            return data
        elif type(data) == complex:
            return data
        elif type(data) == unicode:
            return data
        elif type(data) == dict:
            return self._clean_dict(data)
        elif type(data) == list or type(data) == tuple:
            return self._clean_list(data)
        # end if
        return None
    # end _to_mongodb_data

    # ID exists
    def _id_exists(self, instance_id):
        """
        ID exists?
        :param instance_id:
        :return:
        """
        return self._collection.find_one({"exp": self._name, "instance": instance_id}) is not None
    # end _id_exists

    # Generate random ID
    def _generate_id(self):
        """
        Generate random ID.
        :return:
        """
        found = False
        random_id = 1
        while not found:
            random_id = random.randint(0, sys.maxint)
            if not self._id_exists(random_id):
                found = True
            # end if
        # end while
        return random_id
    # end _generate_id

# end Experience
