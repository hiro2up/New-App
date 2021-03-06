USE [database]
GO
/****** Object:  Table [dbo].[Customers]    Script Date: 30 May 2021 01:59:29 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Customers](
	[CustomerId] [int] IDENTITY(1,1) NOT NULL,
	[Email] [varchar](50) NOT NULL,
	[Pass] [varchar](200) NULL,
	[FirstName] [varchar](50) NOT NULL,
	[LastName] [varchar](50) NOT NULL,
	[AddrLine1] [varchar](150) NOT NULL,
	[AddrLine2] [varchar](150) NULL,
	[City] [varchar](50) NOT NULL,
	[Eircode] [varchar](10) NOT NULL,
 CONSTRAINT [pk_Customers] PRIMARY KEY CLUSTERED 
(
	[CustomerId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY],
 CONSTRAINT [up_Customers] UNIQUE NONCLUSTERED 
(
	[Email] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Orders]    Script Date: 30 May 2021 01:59:30 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Orders](
	[OrderId] [int] IDENTITY(1,1) NOT NULL,
	[CustomerId] [int] NOT NULL,
	[Photo] [varchar](max) NOT NULL,
	[Size] [varchar](20) NOT NULL,
	[Requests] [varchar](300) NULL,
	[Amount] [decimal](19, 2) NULL,
	[Frame] [varchar](20) NOT NULL,
	[Giftbox] [varchar](20) NOT NULL,
	[AddrLine1] [varchar](150) NOT NULL,
	[AddrLine2] [varchar](150) NULL,
	[City] [varchar](50) NOT NULL,
	[Eircode] [varchar](10) NOT NULL,
	[Cancelled] [bit] NULL,
	[TimeStamps] [datetime] NULL,
 CONSTRAINT [pk_Orders] PRIMARY KEY CLUSTERED 
(
	[OrderId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
ALTER TABLE [dbo].[Orders]  WITH CHECK ADD  CONSTRAINT [fk_Orders_Customers] FOREIGN KEY([CustomerId])
REFERENCES [dbo].[Customers] ([CustomerId])
GO
ALTER TABLE [dbo].[Orders] CHECK CONSTRAINT [fk_Orders_Customers]
GO
/****** Object:  StoredProcedure [dbo].[sp_DeleteCustomer]    Script Date: 30 May 2021 01:59:30 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[sp_DeleteCustomer] @CustomerId int
AS
DELETE FROM Orders WHERE CustomerId =  @CustomerId
DELETE FROM Customers WHERE CustomerId =  @CustomerId
GO
/****** Object:  StoredProcedure [dbo].[sp_NewCustomerH]    Script Date: 30 May 2021 01:59:30 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[sp_NewCustomerH] @Email varchar(50),
							@Pass varchar(200),
							@FirstName varchar(50),
							@LastName varchar(50),
							@AddrLine1 varchar(150),
							@AddrLine2 varchar(150),
							@City varchar(50),
							@Eircode varchar(10)
AS
INSERT INTO Customers (Email, Pass, FirstName, LastName, AddrLine1, AddrLine2, City, Eircode)
VALUES (@Email, @Pass, @FirstName, @LastName, @AddrLine1, @AddrLine2, @City, @Eircode)
GO
/****** Object:  StoredProcedure [dbo].[sp_NewOrder]    Script Date: 30 May 2021 01:59:30 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[sp_NewOrder] @CustomerId int,
							@Photo varchar(max),
							@Size varchar(20),
							@Frame varchar(20),
							@Giftbox varchar(20),
							@Requests varchar(300) = NULL,
							@Amount decimal(19,2),
							@AddrLine1 varchar(150),
							@AddrLine2 varchar(150) = NULL,
							@City varchar(50),
							@Eircode varchar(10),
							@Timestamps datetime
AS
INSERT INTO Orders (CustomerId, Photo, Size, Frame, Giftbox, Requests, Amount, AddrLine1, AddrLine2, City, Eircode, Timestamps)
VALUES (@CustomerId,@Photo,@Size,@Frame,@Giftbox,@Requests,@Amount,@AddrLine1,@AddrLine2,@City,@Eircode,@Timestamps)
GO
/****** Object:  StoredProcedure [dbo].[sp_UpdateCustomer]    Script Date: 30 May 2021 01:59:30 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[sp_UpdateCustomer] @FirstName varchar(50),
							@LastName varchar(50),
							@AddrLine1 varchar(150),
							@AddrLine2 varchar(150) = NULL,
							@City varchar(50),
							@Eircode varchar(10),
							@Email varchar(50)
AS
UPDATE Customers
SET FirstName = @FirstName, LastName = @LastName, AddrLine1 = @AddrLine1, AddrLine2 = @AddrLine2, City = @City, Eircode = @Eircode
WHERE Email = @Email
GO
