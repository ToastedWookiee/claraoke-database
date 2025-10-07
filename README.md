# claraoke-database

This is a database of CSV files exported from the database that runs the Claraoke Database website separated by the YouTube `video ID` for each stream they represent.

To submit changes you can either generate PRs for large edits, or open an issue to make recommendations and smaller fixes.

To maintain consistency in naming conventions, use parentheses `(...)` for comments, place comments in the song name or artist field for which it is applicable. For artist names when there are two artists separate with `and`, `&`, `feat.`, or `ft.`. For multiple artists of 3 or more, just separate all artists by commas `, `.

For songs with both English and foreign titles like Japanese, use the dominant language for the song first, then have an English title if available in square brackets `[...]`.

Database limits are `255` characters for each the song title and artist, these limits will be checked when updates are commited to the running database.

Database information originally was sourced from the generous timestampers in the comments of each video then collected and attributed here: [Claraoke Google Doc](https://docs.google.com/spreadsheets/d/1MvMMqr2_qwVdnFR7m7gLAocx3cUauLC8MMyqJ2Mq8LE/edit?gid=967897437#gid=967897437)

## Using editor.py

Step 1: Fork and clone your copy of the repo, this way you can make edits and changes that can be used in a pull request that can be compared to and merged with the main repo branch.

Step 2: With Python version `>3.9` install the requirements

```
cd claraoke-database
pip install -r "requirements.txt"
```

This should install the main dependencies: [pandas](https://github.com/pandas-dev/pandas) and [streamlit](https://github.com/streamlit/streamlit) as well as any of their own dependencies.

Step 3: Run the editor

```
streamlit run editor.py
```

This should open your browser to the CSV Editor page, if not your terminal should show the address for you to enter to access it. This editor allows you do some basic searching and sorting of the CSV database files and make edits. Make sure to hit the "Save Changes" button before re-sorting or enacting another search to save any edits, a refresh of the loaded data will lose any changes.
