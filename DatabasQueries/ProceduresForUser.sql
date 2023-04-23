use [KARTA]

--создание процедур для USER
CREATE PROCEDURE CreateUser
@UserName nvarchar(30),
@UserPassword nvarchar(30),
@IsDeleted bit
as
INSERT [USER]
VALUES (@UserName, @UserPassword, @IsDeleted)

go

CREATE PROCEDURE GetUserByNicknamePassword
@UserName nvarchar(30),
@UserPassword nvarchar(30)
as
SELECT * FROM [USER] as U
WHERE U.[Name] = @UserName and U.[Password] = @UserPassword

go

CREATE PROCEDURE DeleteUserById
@UserId int
as
UPDATE [USER]
SET [IsDeleted] = 1
WHERE [USER].[Id] = @UserId

go

CREATE PROCEDURE GetUserList
as
SELECT U.[Id], U.[Name], U.[Password] FROM [USER] as U
where U.[IsDeleted] = 0

go

CREATE PROCEDURE GetDeletedUserList
as
SELECT U.[Id], U.[Name], U.[Password] FROM [USER] as U
where U.[IsDeleted] = 1

go

CREATE PROCEDURE FullUserDelete
@UserId int
as
DELETE FROM [USER] where [USER].[IsDeleted] = 1 and [USER].[Id] = @UserId

go
