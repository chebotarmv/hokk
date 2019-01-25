import pandas as pd
import csv



def make_data(teams, ft_shots, ft_reject, st_shots, st_reject, data):
    dft = pd.read_csv(teams, header=None)
    dft.columns = ['ft', 'st']
    dft['ft'] = dft['ft'].str[2:]
    dft['ft'] = dft['ft'].str[:-1]
    dft['st'] = dft['st'].str[2:]
    dft['st'] = dft['st'].str[:-2]
    dft = dft.replace('Металлург Магнитогорск', 'Металлург Мг')
    dft = dft.replace('Динамо Москва', 'Динамо Мск')
    dft = dft.replace('Динамо Минск', 'Динамо Мн')
    dft = dft.replace('Динамо Рига', 'Динамо Р')
    dft = dft.replace('Слован Братислава', 'Слован')
    dft = dft.replace('Сочи', 'ХК Сочи')
    dft = dft.replace('Витязь Подольск', 'Витязь')
    dft = dft.replace('Спартак Москва', 'Спартак')


    df1 = pd.read_csv(ft_shots, header=None)
    df1.columns = ['ftfps', 'ftsps', 'fttps']
    df1['ftfps'] = df1['ftfps'].str[2:]
    df1['ftfps'] = df1['ftfps'].str[:-1]
    df1['ftsps'] = df1['ftsps'].str[2:]
    df1['ftsps'] = df1['ftsps'].str[:-1]
    df1['fttps'] = df1['fttps'].str[2:]
    df1['fttps'] = df1['fttps'].str[:-2]
    df1['ftfps'] = pd.to_numeric(df1['ftfps'])
    df1['ftsps'] = pd.to_numeric(df1['ftsps'])
    df1['fttps'] = pd.to_numeric(df1['fttps'])

    df2 = pd.read_csv(ft_reject, header=None)
    df2.columns = ['ftfpr', 'ftspr', 'fttpr']
    df2['ftfpr'] = df2['ftfpr'].str[2:]
    df2['ftfpr'] = df2['ftfpr'].str[:-1]
    df2['ftspr'] = df2['ftspr'].str[2:]
    df2['ftspr'] = df2['ftspr'].str[:-1]
    df2['fttpr'] = df2['fttpr'].str[2:]
    df2['fttpr'] = df2['fttpr'].str[:-2]
    df2['ftfpr'] = pd.to_numeric(df2['ftfpr'])
    df2['ftspr'] = pd.to_numeric(df2['ftspr'])
    df2['fttpr'] = pd.to_numeric(df2['fttpr'])

    dft['ftfps'] = df1['ftfps']
    dft['ftfpr'] = df2['ftfpr']
    dft['ftsps'] = df1['ftsps']
    dft['ftspr'] = df2['ftspr']
    dft['fttps'] = df1['fttps']
    dft['fttpr'] = df2['fttpr']

    df3 = pd.read_csv(st_shots, header=None)
    df3.columns = ['stfps', 'stsps', 'sttps']
    df3['stfps'] = df3['stfps'].str[2:]
    df3['stfps'] = df3['stfps'].str[:-1]
    df3['stsps'] = df3['stsps'].str[2:]
    df3['stsps'] = df3['stsps'].str[:-1]
    df3['sttps'] = df3['sttps'].str[2:]
    df3['sttps'] = df3['sttps'].str[:-2]
    df3['stfps'] = pd.to_numeric(df3['stfps'])
    df3['stsps'] = pd.to_numeric(df3['stsps'])
    df3['sttps'] = pd.to_numeric(df3['sttps'])

    df4 = pd.read_csv(st_reject, header=None)
    df4.columns = ['stfpr', 'stspr', 'sttpr']
    df4['stfpr'] = df4['stfpr'].str[2:]
    df4['stfpr'] = df4['stfpr'].str[:-1]
    df4['stspr'] = df4['stspr'].str[2:]
    df4['stspr'] = df4['stspr'].str[:-1]
    df4['sttpr'] = df4['sttpr'].str[2:]
    df4['sttpr'] = df4['sttpr'].str[:-2]
    df4['stfpr'] = pd.to_numeric(df4['stfpr'])
    df4['stspr'] = pd.to_numeric(df4['stspr'])
    df4['sttpr'] = pd.to_numeric(df4['sttpr'])

    dft['stfps'] = df3['stfps']
    dft['stfpr'] = df4['stfpr']
    dft['stsps'] = df3['stsps']
    dft['stspr'] = df4['stspr']
    dft['sttps'] = df3['sttps']
    dft['sttpr'] = df4['sttpr']

    dfd = pd.read_csv(data, header=None)
    dfd.columns = ['data']
    dfd['data'] = dfd['data'].str[2:]
    dfd['data'] = dfd['data'].str[:-8]
    dft['data'] = dfd['data']
    dft.to_csv('/home/mikhail/PycharmProjects/hokk/result.csv', index=False)

make_data('/home/mikhail/PycharmProjects/hokk/first/teams.txt', \
          '/home/mikhail/PycharmProjects/hokk/first/first_team_shots.txt', \
          '/home/mikhail/PycharmProjects/hokk/first/first_team_rejects.txt', \
          '/home/mikhail/PycharmProjects/hokk/first/second_team_shots.txt', \
          '/home/mikhail/PycharmProjects/hokk/first/second_team_rejects.txt', \
          '/home/mikhail/PycharmProjects/hokk/first/data.txt')

