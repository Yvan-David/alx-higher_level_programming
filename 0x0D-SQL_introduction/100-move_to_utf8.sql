-- convert Dbname and table with its attributes to utf8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT TO utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table MODIFY name TEXT utf8mb4 COLLATE utf8mb4_unicode_ci;
