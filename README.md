# Script info
## Script summary:
1) The user inputs the path to the file. 
2) Lookup index is already set to `40` for Lexend.
3) The script compares it to `MY_LIST` (a hardcoded list containing the substitution pairs of the last version of Lexend) and ...
choose one:
- 4/a) ![📥 py-compare2lexend.py](py-compare2lexend.py) asks what kind of report the user wants. The user can also save changes to the original file. 
- 4/b) ![📥 py-compare2lexend--noInput.py](py-compare2lexend--noInput.py) outputs a report and saves changes to the original file. 

## WorkFlows using this code
    # WF01: .ttf => .ttx ;; py-compare2lexend;; .ttx ⇒ .ttf ;;

## Status check
    # ✅ Script working on Python 3.11.2 as of 2025-02-05. 
    # 🛠️EDIT__HERE🛠️ occurrences: 01

# Copyright
Python differences reporter - hardcoded for Lexend

Copyright (C) 2025 Nicolò Arrigo

SPDX-License-Identifier: AGPL-3.0-only

This program is free software: you can redistribute it and/or modify 
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
