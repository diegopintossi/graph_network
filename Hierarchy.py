import pandas as pd

# hierarchy_dict = {
#     'UP':     ['CA', 'CA', 'CA', 'CA', 'CA', 'CA', 'CA', 'CA'],
#     'Parent': ['CA', 'CA', '02', '02', '04', '04', '06', '01'],
#     'Child':  ['01', '02', '03', '04', '05', '06', '07', '08'],
# }

# hierarchy_dict = {
#     'UP':     ['CA', 'CA', 'CA', 'CA', 'CA', 'CA', 'CA', 'CA', 'CA', 'CA', 'CA', 'CA', 'CA', 'CA', 'CA'],
#     'Parent': ['CA', 'CA', '02', '02', '04', '04', '06', '01', '01', '09', '03', '03', '12', '12', '12'],
#     'Child':  ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15'],
# }

hierarchy_dict = {
    'UP':     ['CA', 'CA', 'CA', 'CA', 'CA', 'CA', 'CA', 'CA', 'CA', 'CA', 'CA', 'CA', 'CA', 'CA', 'CA', 'CA', 'CA', 'CA', 'CA', 'CA', 'CA', 'CA', 'CA', 'CA'],
    'Parent': ['CA', 'CA', '02', '02', '04', '04', '06', '01', '01', '09', '03', '03', '12', '12', '12', '12', '05', '01', '01', '06', '12', '12', '06', '06'],
    'Child':  ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24'],
}

hierarchy_df = pd.DataFrame(hierarchy_dict, dtype=str).sort_values(by='Parent')
hierarchy_df.to_csv('hierarchy_table.csv')
