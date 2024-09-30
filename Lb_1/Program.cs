using MySql.Data.MySqlClient;
using System;

class Program
{
    static void Main(string[] args)
    {
        string connectionString = "server=netflix-manya4560-9acc.j.aivencloud.com;port=21425;database=defaultdb;user=avnadmin;password=AVNS_H9XkQzsdnJUK3P_lk38;sslmode=Required";
        
        using (MySqlConnection connection = new MySqlConnection(connectionString))
        {
            try
            {
                connection.Open();
                Console.WriteLine("Connection successful!");

                bool exit = false;
                while (!exit)
                {
                    Console.WriteLine("\n--- Menu ---");
                    Console.WriteLine("1. Display all tables");
                    Console.WriteLine("2. Display data from a specific table");
                    Console.WriteLine("3. Insert values into tables");
                    Console.WriteLine("4. Perform a JOIN query");
                    Console.WriteLine("5. Perform a filtering query");
                    Console.WriteLine("6. Perform an aggregate query");
                    Console.WriteLine("7. Exit");

                    Console.Write("\nSelect an option (1-7): ");
                    string choice = Console.ReadLine();

                    switch (choice)
                    {
                        case "1":
                            SelectAllTables(connection);
                            break;
                        case "2":
                            SelectFromTable(connection);
                            break;
                        case "3":
                            InsertValuesToTables(connection);
                            break;
                        case "4":
                            SomeJoinFunction(connection);
                            break;
                        case "5":
                            SomeFilterFunction(connection);
                            break;
                        case "6":
                            SomeAggregateFunction(connection);
                            break;
                        case "7":
                            exit = true;
                            Console.WriteLine("Exiting program.");
                            break;
                        default:
                            Console.WriteLine("Invalid option. Please select a number between 1 and 7.");
                            break;
                    }
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error: {ex.Message}");
            }
        }
    }
    static void SelectAllTables(MySqlConnection connection)
    {
        string[] queries = {
            "SELECT * FROM Genres;",
            "SELECT * FROM Subscriptions;",
            "SELECT * FROM Videos;",
            "SELECT * FROM Users;",
            "SELECT * FROM Views;"
        };

        try
        {
            foreach (string query in queries)
            {
                MySqlCommand cmd = new MySqlCommand(query, connection);
                MySqlDataReader reader = cmd.ExecuteReader();

                Console.WriteLine($"\n--- {cmd.CommandText} ---");
                for (int i = 0; i < reader.FieldCount; i++)
                {
                    Console.Write(reader.GetName(i) + "\t");
                }
                Console.WriteLine();

                while (reader.Read())
                {
                    for (int i = 0; i < reader.FieldCount; i++)
                    {
                        Console.Write(reader[i] + "\t");
                    }
                    Console.WriteLine();
                }
                reader.Close();
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }
    static void SelectFromTable(MySqlConnection connection)
    {
        Console.WriteLine("Select a table to display data from (Genres, Subscriptions, Videos, Users, Views): ");
        string table = Console.ReadLine();
        string query = $"SELECT * FROM {table};";

        try
        {
            MySqlCommand cmd = new MySqlCommand(query, connection);
            MySqlDataReader reader = cmd.ExecuteReader();

            Console.WriteLine($"\n--- {table} ---");
            for (int i = 0; i < reader.FieldCount; i++)
            {
                Console.Write(reader.GetName(i) + "\t");
            }
            Console.WriteLine();

            while (reader.Read())
            {
                for (int i = 0; i < reader.FieldCount; i++)
                {
                    Console.Write(reader[i] + "\t");
                }
                Console.WriteLine();
            }
            reader.Close();
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }
    static void InsertValuesToTables(MySqlConnection connection)
    {
        try
        {
            // Insert into Subscriptions table
            Console.WriteLine("Inserting into Subscriptions table...");
            string subscriptionsQuery = @"
                INSERT INTO Subscriptions (Type, Price) VALUES 
                ('Standard', 9.99), 
                ('Ultimate', 19.99);";
            MySqlCommand subscriptionsCmd = new MySqlCommand(subscriptionsQuery, connection);
            int subscriptionsRowsAffected = subscriptionsCmd.ExecuteNonQuery();
            Console.WriteLine($"{subscriptionsRowsAffected} row(s) inserted into Subscriptions.");

            // Insert into Genres table
            Console.WriteLine("Inserting into Genres table...");
            string genresQuery = @"
                INSERT INTO Genres (Name) VALUES 
                ('Thriller'), 
                ('Romance');";
            MySqlCommand genresCmd = new MySqlCommand(genresQuery, connection);
            int genresRowsAffected = genresCmd.ExecuteNonQuery();
            Console.WriteLine($"{genresRowsAffected} row(s) inserted into Genres.");

            // Insert into Videos table
            Console.WriteLine("Inserting into Videos table...");
            string videosQuery = @"
                INSERT INTO Videos (Title, Description, GenreID, Duration) VALUES 
                ('New Thriller Movie', 'A suspenseful thriller.', 1, 110),
                ('Romantic Story', 'A touching romance film.', 2, 90);";
            MySqlCommand videosCmd = new MySqlCommand(videosQuery, connection);
            int videosRowsAffected = videosCmd.ExecuteNonQuery();
            Console.WriteLine($"{videosRowsAffected} row(s) inserted into Videos.");

            // Insert into Users table
            Console.WriteLine("Inserting into Users table...");
            string usersQuery = @"
                INSERT INTO Users (Name, Email, Password, SubscriptionID) VALUES 
                ('Emma Watson', 'emma@example.com', 'emmapass', 1), 
                ('Daniel Brown', 'daniel@example.com', 'danielpass', 2);";
            MySqlCommand usersCmd = new MySqlCommand(usersQuery, connection);
            int usersRowsAffected = usersCmd.ExecuteNonQuery();
            Console.WriteLine($"{usersRowsAffected} row(s) inserted into Users.");

            // Insert into Views table
            Console.WriteLine("Inserting into Views table...");
            string viewsQuery = @"
                INSERT INTO Views (UserID, VideoID, ViewDate) 
                VALUES (1, 1, '2024-10-01'),
                    (2, 2, '2024-10-03');";
            MySqlCommand viewsCmd = new MySqlCommand(viewsQuery, connection);
            int viewsRowsAffected = viewsCmd.ExecuteNonQuery();
            Console.WriteLine($"{viewsRowsAffected} row(s) inserted into Views.");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }

    static void SomeJoinFunction(MySqlConnection connection)
    {
        string query = @"
            SELECT Views.ViewID, Users.Name AS UserName, Videos.Title AS VideoTitle, Views.ViewDate
            FROM Views
            INNER JOIN Users ON Views.UserID = Users.UserID
            INNER JOIN Videos ON Views.VideoID = Videos.VideoID;";

        try
        {
            MySqlCommand cmd = new MySqlCommand(query, connection);
            MySqlDataReader reader = cmd.ExecuteReader();

            Console.WriteLine("\n--- Views with JOIN ---");
            for (int i = 0; i < reader.FieldCount; i++)
            {
                Console.Write(reader.GetName(i) + "\t");
            }
            Console.WriteLine();

            while (reader.Read())
            {
                for (int i = 0; i < reader.FieldCount; i++)
                {
                    Console.Write(reader[i] + "\t");
                }
                Console.WriteLine();
            }
            reader.Close();
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }
    static void SomeFilterFunction(MySqlConnection connection)
    {
        string query = "SELECT * FROM Videos WHERE Duration > 100;";

        try
        {
            MySqlCommand cmd = new MySqlCommand(query, connection);
            MySqlDataReader reader = cmd.ExecuteReader();

            Console.WriteLine("\n--- Videos with Duration > 100 ---");
            for (int i = 0; i < reader.FieldCount; i++)
            {
                Console.Write(reader.GetName(i) + "\t");
            }
            Console.WriteLine();

            while (reader.Read())
            {
                for (int i = 0; i < reader.FieldCount; i++)
                {
                    Console.Write(reader[i] + "\t");
                }
                Console.WriteLine();
            }
            reader.Close();
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }
    static void SomeAggregateFunction(MySqlConnection connection)
    {
        string query = @"
            SELECT 
                SUM(Price) AS TotalRevenue, 
                AVG(Price) AS AveragePrice 
            FROM Subscriptions;";

        try
        {
            MySqlCommand cmd = new MySqlCommand(query, connection);
            using (MySqlDataReader reader = cmd.ExecuteReader())
            {
                if (reader.Read())
                {
                    Console.WriteLine($"\nTotal revenue from subscriptions: {reader["TotalRevenue"]}");
                    Console.WriteLine($"Average price of subscriptions: {reader["AveragePrice"]}");
                }
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }
}
