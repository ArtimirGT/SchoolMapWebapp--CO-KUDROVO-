use [KARTA]


CREATE PROCEDURE CreateEvent
@UserId int,
@EventName nvarchar(30),
@EventDescription nvarchar(255),
@Location nvarchar(30),
@IsSchool bit
as
INSERT [EVENT]
VALUES (@UserId, @EventName, @EventDescription, @Location, @IsSchool)

go

CREATE PROCEDURE DeleteEventById
@EventId int
as
DELETE FROM [EVENT] where [EVENT].[Id] = @EventId

go

CREATE PROCEDURE UpdateEventNameById
@Id int,
@EventName nvarchar(30)
as
UPDATE [EVENT]
SET [Name] = @EventName
WHERE [Id] = @Id

go

CREATE PROCEDURE UpdateEventLocationById
@Id int,
@Location nvarchar(30)
as
UPDATE [EVENT]
SET [Location] = @Location
WHERE [Id] = @Id

go

CREATE PROCEDURE UpdateEventDescriptionById
@Id int,
@EventDescription nvarchar(255)
as
UPDATE [EVENT]
SET [Description] = @EventDescription
WHERE [Id] = @Id

go

CREATE PROCEDURE GetAllEventsByUserId
@Id int
as
select  U.[Id], U.[Name], E.[Id], E.[Name], E.[Description], E.[Location], E.[IsSchool] from [EVENT] as E
inner join [User] as U on U.[Id]=E.[UserId]
WHERE E.[UserId]=@Id

go

exec GetAllEventsByUserId 1
drop procedure GetAllEventsByUserId

drop procedure CreateEvent