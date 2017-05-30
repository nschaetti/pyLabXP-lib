#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File : insert_data.py
# Description : Insert data for testing.
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

import sys
from db.Connection import Connection

rc_size = 500

if __name__ == "__main__":

    # Open a connection
    con = Connection()

    # New instance
    instance = con.instance(lab_name="RCNLP", exp_name="Exploring reservoir size", instance_id=768477309779781668)

    # Locals
    instance.save_variables(locals())

    # Save params
    instance.save_parameter("leaky_rate", 0.5)
    instance.save_parameter("spectral_radius", 0.9)

    try:
        # Save result
        instance.save_results("success_rate", 91.0, params={"size": 10})
        instance.save_results("success_rate", 93.0, params={"size": 30})
        test = 10.0 / 0
        instance.save_results("success_rate", 85.0, params={"size": 50})
    except Exception as e:
        instance.save_traces()
    # end try

# end if
