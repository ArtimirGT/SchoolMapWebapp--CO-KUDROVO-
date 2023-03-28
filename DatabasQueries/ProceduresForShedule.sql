use [KARTA]

CREATE PROCEDURE CreateShedule
@DayOfWeekId int,
@StartTime time,
@EndTime time,
@EventId int,
@Date datetime
as
INSERT [SHEDULE]
values
(@DayOfWeekId, @StartTime, @EndTime, @EventId, @Date)

go


CREATE PROCEDURE DeleteSheduleById
@Id int
as
DELETE FROM [SHEDULE] where [SHEDULE].[Id] = @Id

go

CREATE PROCEDURE GetShedulesByEventId
@Id int
as
SELECT S.Id, E.[Name] as EventName, S.[DayOfWeek], S.[StartTime], S.[EndTime], S.[Date] FROM [SHEDULE] as S
inner join [EVENT] as E on E.[Id] = S.[EventId]
where S.[EventId] = @Id

go

