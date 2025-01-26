CREATE DATABASE meter_reading;

\c meter_reading;

CREATE TABLE IF NOT EXISTS electricity_consumption (
    consumption NUMERIC NOT NULL,
    interval_start TIMESTAMP NOT NULL,
    interval_end TIMESTAMP NOT NULL,
    PRIMARY KEY (interval_start, interval_end)
);

CREATE TABLE IF NOT EXISTS gas_consumption (
    consumption NUMERIC NOT NULL,
    interval_start TIMESTAMP NOT NULL,
    interval_end TIMESTAMP NOT NULL,
    PRIMARY KEY (interval_start, interval_end)
);
