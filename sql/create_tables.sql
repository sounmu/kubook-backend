CREATE TABLE `user` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`auth_id` VARCHAR(50) NOT NULL,
	`user_name` VARCHAR(45) NOT NULL DEFAULT None,
	`is_active` BOOLEAN NOT NULL DEFAULT TRUE,
	`email` VARCHAR(100) NOT NULL,
	`created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	`updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	`is_valid` BOOLEAN NOT NULL DEFAULT TRUE,
	PRIMARY KEY (`id`),
	UNIQUE KEY `auth_id` (`auth_id`),
	UNIQUE KEY `email` (`email`)
);

CREATE TABLE `requested_book` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`user_id` INT NOT NULL,
	`book_title` VARCHAR(255) NOT NULL,
	`publication_year` YEAR NULL,
	`reject_reason` TEXT NULL,
	`request_link` VARCHAR(100) NOT NULL,
	`reason` TEXT NOT NULL,
	`processing_status` TINYINT NOT NULL DEFAULT 0,
	`request_date` DATE NOT NULL,
	`created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	`updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	`is_valid` BOOLEAN NOT NULL DEFAULT FALSE,
	PRIMARY KEY (`id`),
	FOREIGN KEY (`user_id`) REFERENCES `user`(`id`)
);

CREATE TABLE `admin` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`user_id` INT NOT NULL,
	`admin_status` BOOLEAN NOT NULL,
	`expiration_date` DATE NULL,
	`created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	`updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	`is_valid` BOOLEAN NOT NULL DEFAULT FALSE,
	PRIMARY KEY (`id`),
	FOREIGN KEY (`user_id`) REFERENCES `user`(`id`)
);

CREATE TABLE `notice` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`admin_id` INT NOT NULL,
	`user_id` INT NULL,
	`title` VARCHAR(255) NOT NULL,
	`notice_content` TEXT NOT NULL,
	`created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	`updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	`is_valid` BOOLEAN NOT NULL DEFAULT TRUE,
	PRIMARY KEY (`id`),
	FOREIGN KEY (`admin_id`) REFERENCES `admin`(`id`)
);

CREATE TABLE `book_category` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`code` VARCHAR(5) NOT NULL,
	`name` VARCHAR(50) NOT NULL,
	`created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	`updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	`is_valid` BOOLEAN NOT NULL DEFAULT TRUE,
	PRIMARY KEY (`id`)
);

CREATE TABLE `book_info` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`title` VARCHAR(255) NOT NULL,
	`subtitle` VARCHAR(255) NULL,
	`author` VARCHAR(100) NOT NULL,
	`publisher` VARCHAR(45) NOT NULL,
	`publication_year` YEAR NOT NULL,
	`image_url` VARCHAR(255) NULL,
	`category_id` INT NOT NULL,
	`version` VARCHAR(45) NULL,
	`major` BOOLEAN NULL DEFAULT FALSE,
	`language` BOOLEAN NOT NULL DEFAULT TRUE,
	`created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	`updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	`is_valid` BOOLEAN NOT NULL DEFAULT TRUE,
	PRIMARY KEY (`id`),
	FOREIGN KEY (`category_id`) REFERENCES `book_category`(`id`)
);

CREATE TABLE `book_review` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`user_id` INT NOT NULL,
	`book_info_id` INT NOT NULL,
	`review_content` TEXT NOT NULL,
	`created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	`updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	`is_valid` BOOLEAN NOT NULL DEFAULT TRUE,
	PRIMARY KEY (`id`),
	FOREIGN KEY (`user_id`) REFERENCES `user`(`id`),
	FOREIGN KEY (`book_info_id`) REFERENCES `book_info`(`id`)
);

CREATE TABLE `book` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`book_info_id` INT NOT NULL,
	`book_status` TINYINT NOT NULL DEFAULT 0,
	`note` VARCHAR(255) NULL DEFAULT NULL,
	`donor_name` VARCHAR(255) NULL DEFAULT NULL,
	`created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	`updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	`is_valid` BOOLEAN NOT NULL DEFAULT TRUE,
	PRIMARY KEY (`id`),
	FOREIGN KEY (`book_info_id`) REFERENCES `book_info`(`id`)
);

CREATE TABLE `reservation` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`book_id` INT NOT NULL,
	`user_id` INT NOT NULL,
	`reservation_date` DATE NOT NULL,
	`reservation_status` TINYINT NOT NULL DEFAULT 0,
	`created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	`updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	`is_valid` BOOLEAN NOT NULL DEFAULT TRUE,
	PRIMARY KEY (`id`),
	FOREIGN KEY (`book_id`) REFERENCES `book`(`id`),
	FOREIGN KEY (`user_id`) REFERENCES `user`(`id`)
);

CREATE TABLE `loan` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`book_id` INT NOT NULL,
	`user_id` INT NOT NULL,
	`loan_date` DATE NOT NULL,
	`due_date` DATE NOT NULL,
	`extend_status` BOOLEAN NOT NULL DEFAULT FALSE,
	`return_status` BOOLEAN NOT NULL DEFAULT FALSE,
	`return_date` DATE NULL,
	`overdue_days` INT NOT NULL DEFAULT 0,
	`created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	`updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	`is_valid` BOOLEAN NOT NULL DEFAULT TRUE,
	PRIMARY KEY (`id`),
	FOREIGN KEY (`book_id`) REFERENCES `book`(`id`),
	FOREIGN KEY (`user_id`) REFERENCES `user`(`id`)
);

CREATE TABLE `library_setting` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`name` VARCHAR(50) NOT NULL,
	`value` VARCHAR(50) NOT NULL,
	`data_type` VARCHAR(50) NOT NULL,
	`description` TEXT NULL,
	`created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	`updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	`is_valid` BOOLEAN NOT NULL DEFAULT TRUE,
	PRIMARY KEY (`id`)
);

INSERT INTO
	`library_setting` (
		`name`,
		`value`,
		`data_type`,
		`description`,
		`is_valid`
	)
VALUES
	-- Development Setting 관련
	(
		'backend_development_start_date',
		'2024-04-07',
		'DATETIME',
		'도서관 서비스 백엔드 개발 시작일',
		1
	),
	(
		'backend devlopers',
		'권민재, 한수빈',
		'TEXT',
		'개발자 목록',
		1
	),
	(
		'backend_development_end_date',
		'',
		'DATETIME',
		'도서관 서비스 백엔드 개발 종료일',
		1
	),
	-- Service Setting 관련
	(
		'service_start_date',
		'2023-06-01',
		'DATETIME',
		'도서관 서비스 시작일',
		1
	),
	(
		'service_termination_date',
		'',
		'DATETIME',
		'도서관 서비스 종료일',
		0
	),
	-- Loan Setting 관련
	(
		'max_books_per_loan',
		'5',
		'INT',
		'최대 대출 가능 권수',
		1
	),
	(
		'loan_duration_days',
		'14',
		'INT',
		'대출 기간 (일)',
		1
	),
	(
		'loan_extension_days',
		'7',
		'INT',
		'대출 연장 기간 (일)',
		1
	),
	-- Request Setting 관련
	(
		'max_books_per_request',
		'3',
		'INT',
		'최대 예약 가능 권수',
		1
	),
	(
		'max_request_value',
		'30000',
		'INT',
		'최대 예약 가능 금액',
		1
	),
	-- Reservation Setting 관련
	(
		'reservation_limit_per_user',
		'2',
		'INT',
		'사용자 당 최대 예약 가능 권수',
		1
	),
	(
		'reservation_limit_per_book',
		'3',
		'INT',
		'도서 당 최대 예약 가능 사용자 수',
		1
	);

CREATE VIEW `book_stat` AS
SELECT
	bi.id AS book_info_id,
	COUNT(DISTINCT br.id) AS review_count,
	COUNT(DISTINCT l.id) AS loan_count
FROM
	book_info bi
	LEFT JOIN book_review br ON bi.id = br.book_info_id
	AND br.is_valid = TRUE
	LEFT JOIN book b ON bi.id = b.book_info_id
	LEFT JOIN loan l ON b.id = l.book_id
	AND l.is_valid = TRUE
GROUP BY
	bi.id;