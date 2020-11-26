class Test:

    def my_init(self):
        data = 'A'

        def check_data():
            data += 'New data'
            print(data)
        check_data()
        print(data)
