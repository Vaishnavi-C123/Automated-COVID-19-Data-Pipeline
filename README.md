* Automated COVID-19 Data Pipeline:

Built an end-to-end ETL pipeline using Python, Pandas, and PostgreSQL to extract COVID-19 data from a public API, transform it, and load 232+ records into a database.

* Technologies Used:
- Python
- Pandas
- PostgreSQL
- psycopg2
- REST API

* Workflow:
API → Extract → Transform → PostgreSQL

* Results:
- Processed and loaded 232+ country records into PostgreSQL.
- Implemented an end-to-end ETL workflow.


 * Project Architecture

         COVID-19 API
               │
               ▼
      Extract (Python)
               │
               ▼
    Transform (Pandas)
               │
               ▼
   PostgreSQL Database
               │
               ▼
     Reports / Analysis
