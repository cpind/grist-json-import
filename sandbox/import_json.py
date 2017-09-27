

def parse_file(file_path, parse_options=None, num_rows=None, table_name_hint=None):
    #Mocking data
    return {}, [{
        "table_name": "mytable",
        "column_metadata": [{
            "id": "foo",
            "type": "Text"
        },{
            "id": "bar",
            "Type": "Numeric"
        }],
        "table_data": [["apples", "pears"], [10, 11]]
    }]


def can_parse(file_name):
    return True if file_name.lower().endswith('.json') else False
