use [KARTA]

CREATE PROCEDURE CreateTask
@SheduleId int,
@DayOfWeekId int,
@TaskDescription nvarchar(255),
@IsDone bit
as
INSERT [TASK]
Values (@SheduleId, @DayOfWeekId, @TaskDescription, @IsDone)

go

CREATE PROCEDURE DeleteTaskById
@Id int
as
DELETE FROM [TASK] WHERE [TASK].[Id] = @Id

go

CREATE PROCEDURE UpdateTaskDescriptionById
@Id int,
@Description nvarchar(255)
as
UPDATE [TASK]
SET [Description] = @Description where [Id] = @Id

go

CREATE PROCEDURE DoneTaskById
@Id int
as
UPDATE [TASK]
SET [IsDone] = 1 where [Id] = @Id

go

CREATE PROCEDURE GetTasksBySheduleId
@SheduleId int
as
SELECT U.[Name], E.[Name] as EventName, E.[Id], T.[SheduleId], T.[DayOfWeekId], T.[Description], T.[IsDone] FROM [TASK] as T
inner join [SHEDULE] as S on S.[Id] = T.[SheduleId]
inner join [EVENT] as E on E.[Id] = S.[EventId]
inner join [USER] as U on U.[Id] = E.[UserId]
where T.[SheduleId] = @SheduleId

go




DROP PROCEDURE GetTasksBySheduleId
DROP PROCEDURE CreateTask
DROP PROCEDURE DeleteTaskById
DROP PROCEDURE UpdateTaskDescriptionById
DROP PROCEDURE DoneTaskById