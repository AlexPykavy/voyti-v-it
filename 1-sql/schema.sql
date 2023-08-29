BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS "Department" (
	"id" integer NOT NULL,
	"Name" varchar(200) NOT NULL,
	"Telephone" varchar(200) NOT NULL,
	"Email" varchar(200) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "Doctor" (
	"id" integer NOT NULL,
	"FirstName" varchar(200) NOT NULL,
	"LastName" varchar(200) NOT NULL,
	"BirthDate" date NOT NULL,
	"Address" varchar(200) NOT NULL,
	"Telephone" varchar(200) NOT NULL,
	"Email" varchar(200) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "Patient" (
	"id" integer NOT NULL,
	"FirstName" varchar(200) NOT NULL,
	"LastName" varchar(200) NOT NULL,
	"BirthDate" date NOT NULL,
	"Address" varchar(200) NOT NULL,
	"Telephone" varchar(200) NOT NULL,
	"Email" varchar(200) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "Service" (
	"id" integer NOT NULL,
	"Name" varchar(200) NOT NULL,
	"Description" varchar(200) NOT NULL,
	"Price" real NOT NULL,
	"Department_id" bigint NOT NULL,
	FOREIGN KEY("Department_id") REFERENCES "Department"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "Room" (
	"id" integer NOT NULL,
	"Number" integer NOT NULL,
	"Department_id" bigint NOT NULL,
	FOREIGN KEY("Department_id") REFERENCES "Department"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "RenderedService" (
	"id" integer NOT NULL,
	"Quantity" integer NOT NULL,
	"Appointment_id" bigint NOT NULL,
	"Service_id" bigint NOT NULL,
	FOREIGN KEY("Appointment_id") REFERENCES "Appointment"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("Service_id") REFERENCES "Service"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "Prescription" (
	"id" integer NOT NULL,
	"StartDate" date NOT NULL,
	"EndDate" date NOT NULL,
	"Medication" varchar(200) NOT NULL,
	"Approved" varchar(50) NOT NULL,
	"Appointment_id" bigint NOT NULL,
	FOREIGN KEY("Appointment_id") REFERENCES "Appointment"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "Job" (
	"id" integer NOT NULL,
	"Title" varchar(200) NOT NULL,
	"StartDate" date NOT NULL,
	"EndDate" date NOT NULL,
	"Department_id" bigint NOT NULL,
	"Doctor_id" bigint NOT NULL,
	FOREIGN KEY("Doctor_id") REFERENCES "Doctor"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("Department_id") REFERENCES "Department"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "Invoice" (
	"id" integer NOT NULL,
	"RenderedService_id" bigint NOT NULL,
	FOREIGN KEY("RenderedService_id") REFERENCES "RenderedService"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "Appointment" (
	"id" integer NOT NULL,
	"Date" date NOT NULL,
	"Doctor_id" bigint NOT NULL,
	"Patient_id" bigint NOT NULL,
	"Room_id" bigint NOT NULL,
	FOREIGN KEY("Patient_id") REFERENCES "Patient"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("Doctor_id") REFERENCES "Doctor"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("Room_id") REFERENCES "Room"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);

COMMIT;