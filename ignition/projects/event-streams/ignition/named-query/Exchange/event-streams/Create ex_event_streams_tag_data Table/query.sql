CREATE TABLE ex_event_streams_tag_data (
    id SERIAL PRIMARY KEY,
    tag_path VARCHAR(200),
    value BOOLEAN,
    quality VARCHAR(50),
    ts TIMESTAMP,
    event_stream_ts TIMESTAMP
);