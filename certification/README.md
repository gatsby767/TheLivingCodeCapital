# Candidate Certifications (PHP + MySQL)

This component provides a server-rendered PHP page to list candidates and their certifications, with a simple search and filter UI. It is designed to work on shared hosting (cPanel/GoDaddy) and uses plain CSS for styling.

Files added
- certification.php — main page (public)
- styles.css — plain responsive styles
- certification.js — small client-side enhancements (debounced search + auto-submit)
- db/schema_certifications.sql — database schema + sample data
- db.php.example — database connection template (do NOT commit credentials)
- .htaccess — optional redirects and access rules

Quick setup
1. Import the SQL: Use phpMyAdmin or CLI to import `db/schema_certifications.sql` into your MySQL database.
2. Copy db.php.example to db.php and edit the DB constants with your credentials. For better security, move db.php outside your public_html and update the require path in certification.php.
3. Upload the files to your site root (public_html) or a subdirectory. Recommended structure:

  public_html/
  ├─ certification.php
  ├─ styles.css
  ├─ certification.js
  ├─ db.php (generated from db.php.example, NOT committed)

4. Open the page in your browser: https://your-domain.example/certification.php

Security notes
- db.php.example contains placeholders. Never commit real credentials to the repository.
- For production, keep db.php outside the webroot and restrict access in .htaccess or server config.
- PDO is used with prepared statements to reduce SQL injection risk. Ensure display errors are turned off in production.

Next steps (optional)
- Add pagination and sorting
- Create an admin CRUD interface for candidates and certifications
- Add caching for large datasets
