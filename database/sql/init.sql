CREATE DATABASE IF NOT EXISTS advanced_calc;

USE advanced_calc;

CREATE TABLE IF NOT EXISTS calc_history
(
	line VARCHAR(512),
	answer FLOAT,
    is_ans_int TINYINT(1),
	date VARCHAR(50) PRIMARY KEY
);