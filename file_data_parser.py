class ParseData:
    date_delimiter = '==='
    record_info_delimiter = ','
    template_value_for_date = [{'income': []}, {'expense': []}]

    def __init__(self, filename):
        self.filename = filename
        self.parsed_data = {}
        self.parse()

    def extract_date(self, string, delimiter):
        return string.split(delimiter)[1].strip()

    def extract_record_info(self, record, delimiter):
        record_components = record.split(delimiter)
        record_components = [component.strip() for component in record_components]
        return (record_components[0], record_components[1], record_components[2])

    def is_date(self, string):
        return string.startswith(self.date_delimiter) and string.endswith(self.date_delimiter)

    def add_date_to_records_dict(self, string):
        current_date = self.extract_date(string, self.date_delimiter)
        self.parsed_data[current_date] = self.template_value_for_date
        return current_date

    def add_record_to_records_dict(self, string, current_date):
        amount, category, category_type = self.extract_record_info(string, self.record_info_delimiter)
        amount_category = {'amount': float(amount), 'category': category}
        if category_type == 'New Expense':
            self.parsed_data[current_date][1]['expense'].append(amount_category)
        elif category_type == 'New Income':
            self.parsed_data[current_date][0]['income'].append(amount_category)

    def parse_data_to_dict(self, data):
        lines_data = data.split('\n')
        if len(lines_data) <= 1:
            return

        current_date = ""
        for line in lines_data:
            if len(line) == 0:
                continue
            elif self.is_date(line):
                current_date = self.add_date_to_records_dict(line)
            else:
                self.add_record_to_records_dict(line, current_date)

    def parse(self):
        with open(self.filename, 'a+') as f:
            f.seek(0)
            data = f.read()
            print(data)
        self.parse_data_to_dict(data)

if __name__ == '__main__':
    main()