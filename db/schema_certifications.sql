-- schema_certifications.sql
CREATE TABLE IF NOT EXISTS candidates (
  id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  email VARCHAR(255),
  location VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS certifications (
  id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  candidate_id INT UNSIGNED NOT NULL,
  name VARCHAR(255) NOT NULL,
  issuer VARCHAR(255),
  date_awarded DATE,
  expiration_date DATE NULL,
  credential_id VARCHAR(255) NULL,
  details TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (candidate_id) REFERENCES candidates(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- sample data
INSERT INTO candidates (first_name, last_name, email, location) VALUES
('Aisha','Johnson','aisha@example.com','Nashville, TN'),
('Carlos','Martinez','carlos@example.com','Austin, TX'),
('Mei','Wong','mei@example.com','Seattle, WA');

INSERT INTO certifications (candidate_id, name, issuer, date_awarded, credential_id, details) VALUES
(1,'AWS Certified Cloud Practitioner','Amazon','2024-05-12','AWS-CP-1234','Foundational AWS knowledge'),
(1,'Scrum Master','Scrum.org','2023-09-01','SM-987','Agile practices'),
(2,'Google Data Analyst','Google','2024-02-20','GDA-555','Data analysis with BigQuery'),
(3,'CompTIA Security+','CompTIA','2022-11-15','SY0-601','Security fundamentals');
