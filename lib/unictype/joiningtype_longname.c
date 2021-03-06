/* Arabic joining type of Unicode characters.
   Copyright (C) 2011-2020 Free Software Foundation, Inc.
   Written by Bruno Haible <bruno@clisp.org>, 2011.

   This program is free software: you can redistribute it and/or modify it
   under the terms of the GNU Lesser General Public License as published
   by the Free Software Foundation; either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
   Lesser General Public License for more details.

   You should have received a copy of the GNU Lesser General Public License
   along with this program.  If not, see <https://www.gnu.org/licenses/>.  */

#include <config.h>

/* Specification.  */
#include "unictype.h"

static const char u_joining_type_long_name[6][14] =
{
  "Non Joining",
  "Transparent",
  "Join Causing",
  "Left Joining",
  "Right Joining",
  "Dual Joining"
};

const char *
uc_joining_type_long_name (int joining_type)
{
  if (joining_type >= 0
      && joining_type < sizeof (u_joining_type_long_name) / sizeof (u_joining_type_long_name[0]))
    return u_joining_type_long_name[joining_type];
  return NULL;
}
