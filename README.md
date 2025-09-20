# claraoke-database

This is a database of CSV files exported from the database that runs the Claraoke Database website separated by the YouTube `video ID` for each stream they represent.

To submit changes you can either generate PRs for large edits, or open an issue to make recommendations and smaller fixes.

To maintain consistency in naming conventions, use parentheses `(...)` for comments, comments on songs should always be placed in the artist field. For artist names when there are two artists separate with `and`, `&`, `feat.`, `ft.` or similiar. For multiple artists of 3 or more, just separate all artists by commas `, `.

For songs with both English and foreign titles like Japanese, use the dominant language for the song first, then have an English title if available in square brackets `[...]`.

Database limits are `255` characters for each the song title and artist, these limits will be checked when updates are commited to the running database.

Database information originally was sourced from the generous timestampers in the comments of each video then collected and attributed here: [Claraoke Google Doc](https://docs.google.com/spreadsheets/d/1MvMMqr2_qwVdnFR7m7gLAocx3cUauLC8MMyqJ2Mq8LE/edit?gid=967897437#gid=967897437)