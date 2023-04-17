use [KARTA]

--�������� ���� ������
CREATE DATABASE [KARTA]

CREATE TABLE [USER]
(
[Id] int primary key identity,
[Name] nvarchar(30),
[Password] nvarchar(30),
[IsDeleted] bit
)

CREATE TABLE [EVENT]
(
[Id] int primary key identity,
[UserId] int,
[Name] nvarchar(30),
[Description] nvarchar(255),
[Location] nvarchar(30),
[IsSchool] bit
)

CREATE TABLE [SHEDULE]
(
[Id] int primary key identity,
[DayOfWeek] int,
[StartTime] time,
[EndTime] time,
[EventId] int,
[Date] datetime
)

CREATE TABLE [DAYOFWEEK]
(
[Id] int primary key identity,
[Name] nvarchar(30)
)

CREATE TABLE [TASK]
(
[Id] int primary key identity,
[SheduleId] int,
[DayOfWeekId] int,
[Description] nvarchar(255),
[IsDone] bit
)

--DROP ALL
DROP TABLE [USER]
DROP TABLE [EVENT]
DROP TABLE [SHEDULE]
DROP TABLE [DAYOFWEEK]
DROP TABLE [TASK]

--SELECT

SELECT * FROM [USER]
SELECT * FROM [EVENT]
SELECT * FROM [SHEDULE]
SELECT * FROM [DAYOFWEEK]
SELECT * FROM [TASK]

-- User procedures
exec CreateUser 
exec DeleteUserById
exec GetUserList
exec GetDeletedUserList
exec FullUserDelete

-- TASK procedures
exec CreateTask
exec DeleteTaskById 
exec UpdateTaskDescriptionById
exec DoneTaskById 
exec GetTasksBySheduleId

--EVENT procedures
exec CreateEvent 1, 'Free day', 'Just a free day, I can do nothing today', 'Home', 0
exec DeleteEventById 
exec UpdateEventNameById
exec UpdateEventLocationById
exec UpdateEventDescriptionById
exec GetAllEventsByUserId 1

--TESTS

INSERT [USER]
Values
('Gleb', 'qwerty123', 0),
('Kabanchig', 'qwerty228', 0)

INSERT [EVENT]
Values
(1, 'Usual day', 'hafhaldfklad', 'Doma', 0),
(1, 'School day', 'Lessons', 'School', 1),
(2, 'Hru hru', 'saray', 'pohrukat', 0)

INSERT [DAYOFWEEK]
Values
('�����������'),
('�������'),
('�����'),
('�������'),
('�������'),
('�������'),
('�����������')

INSERT [SHEDULE]
Values
(1, '14:30', '21:00', 1, '02/21/23'),
(2, '15:00', '17:00', 1, '03/21/23'),
(1, '12:45', '13:00', 2, '02/21/23')

INSERT [TASK]
Values
(1, 7, 'Play Dota 2', 0),
(1, 7, 'Poobedat', 0),
(2, 1, 'Lemozersky', 0),
(2, 1, 'Russky', 0),
(2, 1, 'HIMIYA BOZE SPASI', 0),
(3, 1, 'Hru', 0),
(3, 2, 'Hru hru', 0)