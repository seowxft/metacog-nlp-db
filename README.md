# metacog-nlp-db

Only if executing local copy
-use python v3.14
-use virtual environment, activate venv -`pip install -r requirements.txt` to install all dependencies
-run `python app.py`

Extract data

Use `export_csv.py`, not the MySQL Workbench "export recordset" button.
Workbench does not escape quote marks inside a value, so a participant's
"quoted words" or the `clientFlags` JSON get split across several columns
when the CSV is opened. The script writes standard CSV that pandas, R and
Excel all read correctly.

1. Open a tunnel to the Scalingo database (needs the Scalingo CLI, `scalingo login`):
   `scalingo --app <app-name> db-tunnel DATABASE_URL`
   It prints the local port (10000 by default). Leave it running.
2. In a second terminal, in this folder with the virtual environment active:
   `DATABASE_URL="mysql://<username>:<password>@127.0.0.1:10000/<database>" python export_csv.py --out export`
   (username, password and database are the ones from the Scalingo DATABASE_URL
   environment variable; the same values Workbench uses.)
3. One CSV per table appears in `export/` (pre_post_conf.csv, mem_task_data.csv, ...).

Workbench is still fine for browsing the data. Connection details:

- add new connection
- Connection Method: Standard TCP/IP over SSH
  SSH Hostname: ssh.osc-fr1.scalingo.com
  SSH Username: git
  SSH Password: (empty)
  SSH Key File: /Users/.ssh/rd_rsa
  MySQL Hostname: <hostname>
  MySQL Server Port: <port>
  Username: <username>
  Password: <password>
