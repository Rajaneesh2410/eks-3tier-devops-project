CREATE TABLE IF NOT EXISTS employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    role VARCHAR(100) NOT NULL
);

INSERT INTO employees (name, role)
VALUES
('Raj', 'DevOps Engineer'),
('Alex', 'Software Engineer'),
('John', 'Cloud Engineer');
