INSERT INTO
	"Patient" (
		"id",
		"FirstName",
		"LastName",
		"BirthDate",
		"Address",
		"Telephone",
		"Email"
	)
VALUES
	(
		1,
		'Ivan',
		'Kuksa',
		'02.11.1995',
		'Brest, 9 Lutskaya St., apt.81',
		'+375335987878',
		'kuks69@mail.ru'
	),
	(
		2,
		'Andrey',
		'Pik',
		'16.08.1989',
		'Brest, 17 Lenina St., apt.33',
		'+375292524689',
		'andypik@mail.ru'
	),
	(
		3,
		'Artyom',
		'Voron',
		'27.03.1999',
		'Brest, 384 Moskovskaya St., apt.108',
		'+375297854562',
		'voron99@mail.ru'
	),
	(
		4,
		'Alexey',
		'Molotov',
		'22.06.1941',
		'Brest, 14 GOBK St., apt.88',
		'+375336589916',
		'lublypakty@mail.ru'
	),
	(
		5,
		'Victor',
		'Khrustalyov',
		'14.01.1967',
		'Brest, 77 Mashensckogo St., apt.1',
		'+375333338564',
		'vichui@yandex.ru'
	);

INSERT INTO
	"Appointment" (
		"id",
		"Patient_id",
		"Doctor_id",
		"Date",
		"Room_id"
	)
VALUES
	(1, 5, 1, '01.08.2022', 5),
	(2, 3, 2, '02.08.2022', 1),
	(3, 1, 3, '02.08.2022', 4),
	(4, 2, 4, '08.08.2022', 3),
	(5, 4, 5, '08.08.2022', 2);

INSERT INTO
	"Prescription" (
		"id",
		"Appointment_id",
		"StartDate",
		"EndDate",
		"Medication",
		"Approved"
	)
VALUES
	(
		1,
		4,
		'08.08.2022',
		'16.08.2022',
		'diclofenac 3 times every 7 days',
		'yes'
	),
	(
		2,
		1,
		'02.08.2022',
		'07.08.2022',
		'nemisulide (solution) 1 time per day',
		'yes'
	),
	(
		3,
		3,
		'02.08.2022',
		'10.08.2022',
		'glycine 2 tablets 3 times per day',
		'yes'
	),
	(
		4,
		5,
		'08.08.2022',
		'14.08.2022',
		'ibuprofen 1 tablet 2 times per day',
		'yes'
	),
	(
		5,
		2,
		'01.08.2022',
		'04.08.2022',
		'isoptin 1 tablet 3 times per day',
		'yes'
	);

INSERT INTO
	"Doctor" (
		"id",
		"FirstName",
		"LastName",
		"BirthDate",
		"Address",
		"Telephone",
		"Email"
	)
VALUES
	(
		1,
		'Ivan',
		'Nekupidman',
		'15.03.1988',
		'Brest, 55 Halturina St., apt.17',
		'+375336055588',
		'docnekupidman@mail.ru'
	),
	(
		2,
		'Moysha',
		'Liberman',
		'11.02.1965',
		'Brest, 108 Zubachyova St., apt.3',
		'+375333678757',
		'docliberman@mail.ru'
	),
	(
		3,
		'Sara',
		'Liberman',
		'11.02.1972',
		'Brest, 108 Zubachyova St., apt.3',
		'+375297250404',
		'docsliberman@mail.ru'
	),
	(
		4,
		'Lavrinty',
		'Beriabaym',
		'14.08.1988',
		'Brest, 88 Orlovskaya St., apt.6',
		'+375292890489',
		'docberiabaym@mail.ru'
	),
	(
		5,
		'Aleksandra',
		'Krinzhova',
		'27.11.1991',
		'Kobrin, 24 Lenina St., apt.28',
		'+375297275981',
		'dockrinzhova@mail.ru'
	);

INSERT INTO
	"Room" ("id", "Department_id", "NUMBER")
VALUES
	(1, 5, 101),
	(2, 1, 102),
	(3, 3, 104),
	(4, 4, 103),
	(5, 2, 105);

INSERT INTO
	"RenderedService" ("id", "Appointment_id", "Service_id", "Quantity")
VALUES
	(1, 1, 2, 1),
	(2, 2, 5, 1),
	(3, 3, 4, 1),
	(4, 4, 3, 1),
	(5, 5, 1, 1);

INSERT INTO
	"Invoice" ("id", "RenderedService_id")
VALUES
	(1, 1),
	(2, 2),
	(3, 3),
	(4, 4),
	(5, 5);

INSERT INTO
	"Department" ("id", "Name", "Telephone", "Email")
VALUES
	(
		1,
		'Therapeutic',
		'375292000301',
		'therapydep@mail.ru'
	),
	(
		2,
		'Traumotology',
		'375292000302',
		'traumotldep@mail.ru'
	),
	(3, 'Surgery', '375292000303', 'surgdep@mail.ru'),
	(
		4,
		'Neurological',
		'375292000304',
		'neurologdep@mail.ru'
	),
	(
		5,
		'Cardiology',
		'375292000305',
		'cardiologdep@mail.ru'
	);

INSERT INTO
	"Service" (
		"id",
		"Department_id",
		"Name",
		"Description",
		"Price"
	)
VALUES
	(
		1,
		1,
		'general acceptance',
		'examination of the tonsils',
		'40 BYN'
	),
	(
		2,
		2,
		'joint adjustment',
		'inspection and adjustment of the joint',
		'60 BYN'
	),
	(
		3,
		3,
		'wart removal',
		'opening the skin with a scalpel and removing the neoplasm',
		'45 BYN'
	),
	(
		4,
		4,
		'brain encephalography',
		'conducting research on encelograph',
		'80 BYN'
	),
	(
		5,
		5,
		'cardiologist''s appointment',
		'study surveys. assignment of recommendations.',
		'40 BYN'
	);

INSERT INTO
	"Job" (
		"id",
		"Doctor_id",
		"Department_id",
		"Title",
		"StartDate",
		"EndDate"
	)
VALUES
	(
		1,
		1,
		2,
		'traumatologist of the highest category',
		'01.02.2010',
		'10.11.2023'
	),
	(
		2,
		2,
		5,
		'chief physician, cardiologist of the highest category',
		'01.03.2002',
		'03.10.2025'
	),
	(
		3,
		3,
		4,
		'neurologist of the 1st category',
		'07.05.2005',
		'02.09.2025'
	),
	(
		4,
		4,
		3,
		'surgeon of the 1st category',
		'03.06.2012',
		'11.03.2026'
	),
	(
		5,
		5,
		1,
		'therapist of the 2st category',
		'22.02.2018',
		'15.04.2024'
	);

COMMIT;