CREATE TABLE ex_event_streams_example_data (
    id SERIAL PRIMARY KEY,
    process_step integer,
    beans_inventory integer,
    mixer_weight integer,
    rice_inventory integer,
    event_stream_ts TIMESTAMP
);