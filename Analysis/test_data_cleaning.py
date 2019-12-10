import unittest


class DataCleaningTest(unittest.TestCase):
    '''
    These test functions have been created to test the effectiveness of
    the data cleaning functions in the data_cleaning.py file.
    '''

    # test merge_data() function
    def test_merge_annual_data(self):
        '''
        Similar to the unit test for get_annual_data(). The test function for
        merge_annual_data() first remove the final dataset (crash_data) in the
        database and then recreate the table.
        '''

        # set the working directory to the data folder
        set_directory()

        # set up a connection to the database
        conn = dbi.connect('crash_database')

        # create a database cursor that can execute query statements
        cu = conn.cursor()
        
                # drop the crash_data table if it exists in the database
        cu.execute('DROP TABLE IF EXISTS '2020'')

        # call the function to generate the final dataset
        merge_annual_data(conn)

        # get the database table name list
        tables = get_tables(conn)

        # close the database connection
        conn.close()

        # check if a new df table has been created in the database
        self.assertTrue('df' in tables.name.tolist())

    # test get_data() function
    def test_get_data(self):

        # call the function to get the data
        df = get_data()

        # check if the returned dataframe is not empty
        self.assertFalse(df.empty)


if __name__ == '__main__':
    unittest.main()
