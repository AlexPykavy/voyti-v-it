BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS "Patient" (
	"Id" INTEGER NOT NULL,
	"FirstName" TEXT NOT NULL,
	"LastName" TEXT NOT NULL,
	"BirthDate" TEXT NOT NULL,
	"Address" TEXT,
	"Telephone" TEXT,
	"Email" TEXT,
	PRIMARY KEY("Id")
);

CREATE TABLE IF NOT EXISTS "Appointment" (
	"Id" INTEGER NOT NULL,
	"PatientId" INTEGER NOT NULL,
	"DoctorId" INTEGER NOT NULL,
	"Date" TEXT NOT NULL,
	"RoomId" INTEGER NOT NULL,
	PRIMARY KEY("Id" AUTOINCREMENT),
	FOREIGN KEY("DoctorId") REFERENCES "Doctor"("id"),
	FOREIGN KEY("RoomId") REFERENCES "Room"("id"),
	FOREIGN KEY("PatientId") REFERENCES "Patient"("id")
);

CREATE TABLE IF NOT EXISTS "Prescription" (
	"Id" INTEGER NOT NULL,
	"AppointmentId" INTEGER NOT NULL,
	"StartDate" TEXT NOT NULL,
	"EndDate" TEXT NOT NULL,
	"Medication" TEXT,
	"Approved" TEXT NOT NULL,
	FOREIGN KEY("AppointmentId") REFERENCES "Appointment"("id")
);

CREATE TABLE IF NOT EXISTS "Doctor" (
	"Id" INTEGER NOT NULL,
	"FirstName" TEXT NOT NULL,
	"LastName" TEXT NOT NULL,
	"BirthDate" TEXT NOT NULL,
	"Address" TEXT,
	"Telephone" TEXT,
	"Email" TEXT,
	PRIMARY KEY("Id")
);

CREATE TABLE IF NOT EXISTS "Room" (
	"Id" INTEGER NOT NULL,
	"DepartmentId" INTEGER NOT NULL,
	"NUMBER" INTEGER NOT NULL,
	PRIMARY KEY("Id" AUTOINCREMENT),
	FOREIGN KEY("DepartmentId") REFERENCES "Department"("id")
);

CREATE TABLE IF NOT EXISTS "RenderedService" (
	"Id" INTEGER NOT NULL,
	"AppointmentId" INTEGER NOT NULL,
	"ServiceId" INTEGER NOT NULL,
	"Quantity" INTEGER NOT NULL,
	PRIMARY KEY("Id" AUTOINCREMENT),
	FOREIGN KEY("AppointmentId") REFERENCES "Appointment"("id")
);

CREATE TABLE IF NOT EXISTS "Invoice" (
	"Id" INTEGER NOT NULL,
	"RenderedServiceId" INTEGER NOT NULL,
	FOREIGN KEY("RenderedServiceId") REFERENCES "RenderedService"("id")
);

CREATE TABLE IF NOT EXISTS "Department" (
	"Id" INTEGER NOT NULL,
	"Name" TEXT NOT NULL,
	"Telephone" TEXT NOT NULL,
	"Email" TEXT,
	PRIMARY KEY("Id" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "Service" (
	"Id" INTEGER NOT NULL,
	"DepartmentId" INTEGER NOT NULL,
	"Name" TEXT NOT NULL,
	"Description" TEXT,
	"Price" INTEGER NOT NULL,
	FOREIGN KEY("DepartmentId") REFERENCES "Department"("id")
);

CREATE TABLE IF NOT EXISTS "Job" (
	"Id" INTEGER NOT NULL,
	"DoctorId" INTEGER NOT NULL,
	"DepartmentId" INTEGER NOT NULL,
	"Title" INTEGER NOT NULL,
	"StartDate" INTEGER NOT NULL,
	"EndDate" INTEGER NOT NULL,
	FOREIGN KEY("DoctorId") REFERENCES "Doctor"("id"),
	FOREIGN KEY("DepartmentId") REFERENCES "Department"("id")
);

COMMIT;