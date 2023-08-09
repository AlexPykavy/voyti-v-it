import sqlite3 as sq
DB = 'clinic.db'
with sq.connect(DB) as con:
    cur = con.cursor()

    cur.execute("""INSERT OR REPLACE INTO Patient
    VALUES (001, "Ivan", "Kuksa", "02.11.1995",
    "Brest, 9 Lutskaya St., apt.81", "+375335987878", "kuks69@mail.ru")""")

    cur.execute("""INSERT OR REPLACE INTO Patient
    VALUES (002, "Andrey", "Pik", "16.08.1989",
    "Brest, 17 Lenina St., apt.33", "+375292524689", "andypik@mail.ru")""")

    cur.execute("""INSERT OR REPLACE INTO Patient
    VALUES (003, "Artyom", "Voron", "27.03.1999",
    "Brest, 384 Moskovskaya St., apt.108", "+375297854562", "voron99@mail.ru")""")

    cur.execute("""INSERT OR REPLACE INTO Patient
    VALUES (004, "Alexey", "Molotov", "22.06.1941",
    "Brest, 14 GOBK St., apt.88", "+375336589916", "lublypakty@mail.ru")""")

    cur.execute("""INSERT OR REPLACE INTO Patient
    VALUES (005, "Victor", "Khrustalyov", "14.01.1967",
    "Brest, 77 Mashensckogo St., apt.1", "+375333338564", "vichui@yandex.ru")""")

    cur.execute("""INSERT OR REPLACE INTO Doctor
    VALUES (001, "Ivan", "Nekupidman", "15.03.1988",
    "Brest, 55 Halturina St., apt.17", "+375336055588", "docnekupidman@mail.ru")""")

    cur.execute("""INSERT OR REPLACE INTO Doctor
    VALUES (002, "Moysha", "Liberman", "11.02.1965",
    "Brest, 108 Zubachyova St., apt.3", "+375333678757", "docliberman@mail.ru")""")

    cur.execute("""INSERT OR REPLACE INTO Doctor
    VALUES (003, "Sara", "Liberman", "11.02.1972",
    "Brest, 108 Zubachyova St., apt.3", "+375297250404", "docsliberman@mail.ru")""")

    cur.execute("""INSERT OR REPLACE INTO Doctor
    VALUES (004, "Lavrinty", "Beriabaym", "14.08.1988",
    "Brest, 88 Orlovskaya St., apt.6", "+375292890489", "docberiabaym@mail.ru")""")

    cur.execute("""INSERT OR REPLACE INTO Doctor
    VALUES (005, "Aleksandra", "Krinzhova", "27.11.1991",
    "Kobrin, 24 Lenina St., apt.28", "+375297275981", "dockrinzhova@mail.ru")""")

    cur.execute("""INSERT OR REPLACE INTO Department
    VALUES (1, "Therapeutic", +375292000301, "therapydep@mail.ru")""")

    cur.execute("""INSERT OR REPLACE INTO Department
    VALUES (2, "Traumotology", +375292000302, "traumotldep@mail.ru")""")

    cur.execute("""INSERT OR REPLACE INTO Department
    VALUES (3, "Surgery", +375292000303, "surgdep@mail.ru")""")

    cur.execute("""INSERT OR REPLACE INTO Department
    VALUES (4, "Neurological", +375292000304, "neurologdep@mail.ru")""")

    cur.execute("""INSERT OR REPLACE INTO Department
    VALUES (5, "Cardiology", +375292000305, "cardiologdep@mail.ru")""")

    cur.execute("""INSERT OR REPLACE INTO Room
    VALUES (001, 5, 101)""")

    cur.execute("""INSERT OR REPLACE INTO Room
    VALUES (002, 1, 102)""")

    cur.execute("""INSERT OR REPLACE INTO Room
    VALUES (003, 3, 104)""")

    cur.execute("""INSERT OR REPLACE INTO Room
    VALUES (004, 4, 103)""")

    cur.execute("""INSERT OR REPLACE INTO Room
    VALUES (005, 2, 105)""")

    cur.execute("""INSERT OR REPLACE INTO Appointment
    VALUES (001, 005, 001, "01.08.2022", 005)""")

    cur.execute("""INSERT OR REPLACE INTO Appointment
    VALUES (002, 003, 002, "02.08.2022", 001)""")

    cur.execute("""INSERT OR REPLACE INTO Appointment
    VALUES (003, 001, 003, "02.08.2022", 004)""")

    cur.execute("""INSERT OR REPLACE INTO Appointment
    VALUES (004, 002, 004, "08.08.2022", 003)""")

    cur.execute("""INSERT OR REPLACE INTO Appointment
    VALUES (005, 004, 005, "08.08.2022", 002)""")

    cur.execute("""INSERT OR REPLACE INTO Prescription
    VALUES (001, 001, "01.08.2022", "16.08.2022", "diclofenac 3 times every 7 days", "yes")""")

    cur.execute("""INSERT OR REPLACE INTO Prescription
    VALUES (002, 002, "02.08.2022", "07.08.2022", "isoptin 1 tablet 3 times per day", "yes")""")

    cur.execute("""INSERT OR REPLACE INTO Prescription
    VALUES (003, 003, "02.08.2022", "10.08.2022", "glycine 2 tablets 3 times per day","yes")""")

    cur.execute("""INSERT OR REPLACE INTO Prescription
    VALUES (004, 004, "08.08.2022", "14.08.2022", "emisulide (solution) 1 time per day", "yes")""")

    cur.execute("""INSERT OR REPLACE INTO Prescription
    VALUES (005, 005, "08.08.2022", "04.08.2022", "ibuprofen 1 tablet 2 times per dayn", "yes")""")

    cur.execute("""INSERT OR REPLACE INTO Job
    VALUES (001, 001, 2, "traumatologist of the highest category", "01.02.2010", "10.11.2023")""")

    cur.execute("""INSERT OR REPLACE INTO Job
    VALUES (002, 002, 5, "chief physician, cardiologist of the highest category", "01.03.2002", "03.10.2025")""")

    cur.execute("""INSERT OR REPLACE INTO Job
    VALUES (003, 003, 4, "neurologist of the 1st category", "07.05.2005", "02.09.2025")""")

    cur.execute("""INSERT OR REPLACE INTO Job
    VALUES (004, 004, 3, "surgeon of the 1st category", "03.06.2012", "11.03.2026")""")

    cur.execute("""INSERT OR REPLACE INTO Job
    VALUES (005, 005, 1, "therapist of the 2st category", "22.02.2018", "15.04.2024")""")

    cur.execute("""INSERT OR REPLACE INTO Job
    VALUES (005, 005, 1, "therapist of the 2st category", "22.02.2018", "15.04.2024")""")

    cur.execute("""INSERT OR REPLACE INTO Service
    VALUES (001, 1, "general acceptance", "examination of the tonsils", "40 BYN")""")

    cur.execute("""INSERT OR REPLACE INTO Service
    VALUES (002, 2, "joint adjustment", "inspection and adjustment of the joint", "60 BYN")""")

    cur.execute("""INSERT OR REPLACE INTO Service
    VALUES (003, 3, "wart removal", "opening the skin with a scalpel and removing the neoplasm", "45 BYN")""")

    cur.execute("""INSERT OR REPLACE INTO Service
    VALUES (004, 4, "brain encephalography", "conducting research on encelograph", "80 BYN")""")

    cur.execute("""INSERT OR REPLACE INTO Service
    VALUES (005, 5, "cardiologist's appointment", "study surveys. assignment of recommendations.", "40 BYN")""")

    cur.execute("""INSERT OR REPLACE INTO RenderedService
    VALUES (001, 001, 002 , 1)""")

    cur.execute("""INSERT OR REPLACE INTO RenderedService
    VALUES (002, 002, 005 , 1)""")

    cur.execute("""INSERT OR REPLACE INTO RenderedService
    VALUES (003, 003, 004 , 1)""")

    cur.execute("""INSERT OR REPLACE INTO RenderedService
    VALUES (004, 004, 003 , 1)""")

    cur.execute("""INSERT OR REPLACE INTO RenderedService
    VALUES (005, 005, 001 , 1)""")

    cur.execute("""INSERT OR REPLACE INTO Invoice
    VALUES (001, 001)""")

    cur.execute("""INSERT OR REPLACE INTO Invoice
    VALUES (002, 002)""")

    cur.execute("""INSERT OR REPLACE INTO Invoice
    VALUES (003, 003)""")

    cur.execute("""INSERT OR REPLACE INTO Invoice
    VALUES (004, 004)""")

    cur.execute("""INSERT OR REPLACE INTO Invoice
    VALUES (005, 005)""")
