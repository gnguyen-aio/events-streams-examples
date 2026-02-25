SET search_path TO public;

-- Create table: ex_event_streams_example_data
CREATE TABLE IF NOT EXISTS ex_event_streams_example_data (
    id SERIAL PRIMARY KEY,
    beans_inventory INT4,
    event_stream_ts TIMESTAMP,
    mixer_weight INT4,
    process_step INT4,
    rice_inventory INT4
);

-- Create table: ex_event_streams_tag_data
CREATE TABLE IF NOT EXISTS ex_event_streams_tag_data (
    id SERIAL PRIMARY KEY,
    event_stream_ts TIMESTAMP,
    quality VARCHAR(255),
    tag_path VARCHAR(255),
    ts TIMESTAMP,
    value BOOLEAN
);