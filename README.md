# snowflake-dbt-scd2
An end-to-end ELT pipeline using Python, Amazon S3, Snowflake, and dbt. Raw files are uploaded to S3, loaded into Snowflake via an external stage, transformed in dbt silver models, versioned with dbt snapshots for SCD2 history, and published as gold-layer views for reporting.
