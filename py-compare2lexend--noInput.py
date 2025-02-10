# # Copyright
    # Python differences reporter - hardcoded for Lexend
    # Copyright (C) 2025 Nicolò Arrigo
    # SPDX-License-Identifier: AGPL-3.0-only
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, version 3.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.
# You should have received a copy of the GNU Affero General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

# # FILE INFO # 
# ## Script summary:
    # 1) The user inputs the path to the file. 
    # 2) Lookup index is already set to `40` for Lexend.
    # 3) The script compares it to `MY_LIST`, outputs a report and saves changes to the original file. 
# ## WorkFlows using this code
    # WF01: .ttf => .ttx ;; py-compare2lexend;; .ttx ⇒ .ttf ;;
# ## Status check
    # ✅ Script working on Python 3.11.2 as of 2025-02-05. 
    # 🛠️EDIT__HERE🛠️ occurrences: 01

import os       # 'os' is what checks if the files exist
import sys      # 'sys' is what anables me to drag & drop a file over the script

# This is MY-LIST:
PY_SCRIPT_INDEX = '40'  # 🛠️EDIT__HERE🛠️ This script was made for <Lookup index="40">
MY_LIST = [
    ('<Substitution in="I" out="I.ss01"/>', 'delete'),
    ('<Substitution in="IJ" out="IJ.ss01"/>', 'delete'),
    ('<Substitution in="Iacute" out="Iacute.ss01"/>', 'delete'),
    ('<Substitution in="Ibreve" out="Ibreve.ss01"/>', 'delete'),
    ('<Substitution in="Icircumflex" out="Icircumflex.ss01"/>', 'delete'),
    ('<Substitution in="Idieresis" out="Idieresis.ss01"/>', 'delete'),
    ('<Substitution in="Idotaccent" out="Idotaccent.ss01"/>', 'delete'),
    ('<Substitution in="Igrave" out="Igrave.ss01"/>', 'delete'),
    ('<Substitution in="Imacron" out="Imacron.ss01"/>', 'delete'),
    ('<Substitution in="Iogonek" out="Iogonek.ss01"/>', 'delete'),
    ('<Substitution in="Itilde" out="Itilde.ss01"/>', 'delete'),
    ('<Substitution in="J" out="J.ss01"/>', 'delete'),
    ('<Substitution in="Jcircumflex" out="Jcircumflex.ss01"/>', 'delete'),
    ('<Substitution in="a" out="a.ss01"/>', 'keep'),
    ('<Substitution in="aacute" out="aacute.ss01"/>', 'keep'),
    ('<Substitution in="abreve" out="abreve.ss01"/>', 'keep'),
    ('<Substitution in="acircumflex" out="acircumflex.ss01"/>', 'keep'),
    ('<Substitution in="adieresis" out="adieresis.ss01"/>', 'keep'),
    ('<Substitution in="agrave" out="agrave.ss01"/>', 'keep'),
    ('<Substitution in="amacron" out="amacron.ss01"/>', 'keep'),
    ('<Substitution in="aogonek" out="aogonek.ss01"/>', 'keep'),
    ('<Substitution in="aring" out="aring.ss01"/>', 'keep'),
    ('<Substitution in="aringacute" out="aringacute.ss01"/>', 'keep'),
    ('<Substitution in="atilde" out="atilde.ss01"/>', 'keep'),
    ('<Substitution in="g" out="g.ss01"/>', 'keep'),
    ('<Substitution in="gbreve" out="gbreve.ss01"/>', 'keep'),
    ('<Substitution in="gcaron" out="gcaron.ss01"/>', 'keep'),
    ('<Substitution in="gcircumflex" out="gcircumflex.ss01"/>', 'keep'),
    ('<Substitution in="gdotaccent" out="gdotaccent.ss01"/>', 'keep'),
    ('<Substitution in="uni0123" out="uni0123.ss01"/>', 'keep'),
    ('<Substitution in="uni01C7" out="uni01C7.ss01"/>', 'delete'), # LJ
    ('<Substitution in="uni01CA" out="uni01CA.ss01"/>', 'delete'), # NJ
    ('<Substitution in="uni01CE" out="uni01CE.ss01"/>', 'keep'),   # a
    ('<Substitution in="uni01CF" out="uni01CF.ss01"/>', 'delete'), # i
    ('<Substitution in="uni0201" out="uni0201.ss01"/>', 'keep'),   # a
    ('<Substitution in="uni0203" out="uni0203.ss01"/>', 'keep'),   # a
    ('<Substitution in="uni0208" out="uni0208.ss01"/>', 'delete'), # i
    ('<Substitution in="uni020A" out="uni020A.ss01"/>', 'delete'), # i
    ('<Substitution in="uni1E21" out="uni1E21.ss01"/>', 'keep'),   # g
    ('<Substitution in="uni1E2E" out="uni1E2E.ss01"/>', 'delete'), # i
    ('<Substitution in="uni1EA1" out="uni1EA1.ss01"/>', 'keep'),   # a
    ('<Substitution in="uni1EA3" out="uni1EA3.ss01"/>', 'keep'),   # a
    ('<Substitution in="uni1EA5" out="uni1EA5.ss01"/>', 'keep'),   # a
    ('<Substitution in="uni1EA7" out="uni1EA7.ss01"/>', 'keep'),   # a
    ('<Substitution in="uni1EA9" out="uni1EA9.ss01"/>', 'keep'),   # a
    ('<Substitution in="uni1EAB" out="uni1EAB.ss01"/>', 'keep'),   # a
    ('<Substitution in="uni1EAD" out="uni1EAD.ss01"/>', 'keep'),   # a
    ('<Substitution in="uni1EAF" out="uni1EAF.ss01"/>', 'keep'),   # a
    ('<Substitution in="uni1EB1" out="uni1EB1.ss01"/>', 'keep'),   # a
    ('<Substitution in="uni1EB3" out="uni1EB3.ss01"/>', 'keep'),   # a
    ('<Substitution in="uni1EB5" out="uni1EB5.ss01"/>', 'keep'),   # a
    ('<Substitution in="uni1EB7" out="uni1EB7.ss01"/>', 'keep'),   # a
    ('<Substitution in="uni1EC8" out="uni1EC8.ss01"/>', 'delete'), # i
    ('<Substitution in="uni1ECA" out="uni1ECA.ss01"/>', 'delete')  # i
]

# Check if a file path was provided as a command line argument (This enables drag & drop over script)
if len(sys.argv) > 1:
    source_file_path = sys.argv[1]
else:
    # Get the source file path from user input
    while True:
        source_file_path = input("╙─── Enter the path to the source file: \n>> ")
        if os.path.isfile(source_file_path):
            break
        else:
            print("♠ The file does not exist. Be sure to enter a valid file path.")
source_file_dir = os.path.dirname(source_file_path)                         # Get directory name
source_file_name = os.path.splitext(os.path.basename(source_file_path))[0]  # Get file name

# Initialize search_option to None
search_option = None
var_search = "<Lookup index=\""

# Loop until a valid index is entered
while search_option is None:
    search_option = PY_SCRIPT_INDEX

    # Find the starting point of UPLOADED-LIST
    uploaded_list_start = None
    with open(source_file_path, "r") as source_file:
        all_lines = source_file.readlines()

        for i, line in enumerate(all_lines):
            if f'{var_search}{search_option}"' in line:
                for j, inner_line in enumerate(all_lines[i + 1:], start=i + 1):  # Inner loop to find a better starting point after Lookup Index 40
                    if '<Substitution in="' in inner_line:
                        uploaded_list_start = j
                        break
                break

    if uploaded_list_start is None:
        print("♠ Invalid index. Please try again.")
        search_option = None

# Lists to store results
KEPT_LINES = []
DELETED_LINES = []
MY_LIST_NOT_FOUND = []
UPLOADED_LIST_NEW_LINES = []

# Find the ending point of UPLOADED-LIST
for j, inner_line in enumerate(all_lines[uploaded_list_start:], start=uploaded_list_start):
    if "</SingleSubst>" in inner_line:
        uploaded_list_end = j
        break

# Extract UPLOADED-LIST lines
uploaded_list_lines = all_lines[uploaded_list_start:uploaded_list_end]

# Iterate over each string and choice in MY_LIST
for string, choice in MY_LIST: # This syntax means that I'm defining string, choice as my duple in MY_LIST for easy referencing
    string_found = False

    # Check if the string is present in any line of UPLOADED-LIST
    for line in uploaded_list_lines:
        if string in line:
            string_found = True

            # Check the choice and add the string to the corresponding list
            if choice == "delete":
                DELETED_LINES.append(line.strip())
            elif choice == "keep":
                KEPT_LINES.append(line.strip())

            break

    # If the string is not found in UPLOADED-LIST, add it to MY_LIST_NOT_FOUND
    if not string_found:
        MY_LIST_NOT_FOUND.append(string.strip())

# Check for lines in UPLOADED-LIST that were not assigned "keep" or "delete"
for line in uploaded_list_lines:
    if line.strip() not in KEPT_LINES and line.strip() not in DELETED_LINES:
        UPLOADED_LIST_NEW_LINES.append(line.strip())

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# Define ASCI ART & Printing queue
a_art = '■■■■■■■■■■■■■■■■■■■■'
ascii_kept = f'{a_art} KEPT-LINES {a_art}'
ascii_del = f'{a_art} DELETED-LINES {a_art}'
ascii_nfound = f'{a_art} MY-LIST-NOT-FOUND {a_art}'
ascii_new = f'{a_art} UPLOADED-LIST-NEW-LINES {a_art}'

queue_print = f"{ascii_kept}\n" + "\n".join(KEPT_LINES) + f"\n\n{ascii_del}\n" + "\n".join(DELETED_LINES) + f"\n\n{ascii_nfound}\n" + "\n".join(MY_LIST_NOT_FOUND) + f"\n\n{ascii_new}\n" + "\n".join(UPLOADED_LIST_NEW_LINES)  # we need '+ "\n"' in front of .join so that {ascii_kept} is correctly placed outside of the join() method, allowing it to be printed as intended.

# ▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣
# Construct the output file path
output_file_name = f"{source_file_name}-pyLookupsAnalyzer-I{PY_SCRIPT_INDEX}-01.txt"
output_file_path = os.path.join(source_file_dir, output_file_name)

# Increment the file number suffix if the file already exists
counter = 1
while os.path.exists(output_file_path):
    counter += 1
    output_file_name = f"{source_file_name}-pyLookupsAnalyzer-I{PY_SCRIPT_INDEX}-{counter:02d}.txt" # KM
    output_file_path = os.path.join(source_file_dir, output_file_name)

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# ✴️DIFF__VERSION-
#   This version of the script does not ask the user for any more inputs. It just exports the results.
# -DIFF__VERSION✴️

# Save the resulting lists to the output file
with open(output_file_path, "w", encoding="utf-8") as output_file:
    output_file.write(queue_print)
print(f"♥ Comparison results saved to: {output_file_path}")
        

# Delete lines from the source file
with open(source_file_path, "w") as source_file:
    for line in all_lines:
        if line.strip() not in DELETED_LINES:
            source_file.write(line)
print(f"♥ Source file overwritten: {source_file_path}")
        

print("♣ Last line of the script.")