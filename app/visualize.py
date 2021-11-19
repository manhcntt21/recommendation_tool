import matplotlib.pyplot as plt
import pandas as pd


def read_data(col, path):
    """

    """
    data = pd.read_csv(path, header=None, sep=',', names=col, encoding='utf-8')
    return data

def addlabels(x,y):
    """

    """
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha='center')

def preprocessing(data, column, top, type=1, column2=None):
    """
        data - thong ke so luong cai gi do theo nhan vien
        column - ten cot tao ra
        top -  so luong cot muon dua bieu do (sap xep theo thu tu giam dan)
        column - cột mới tạo ở bảng nhân viên
        column - id để join với bảng khác, ví dụ employee-hobby có hobby id để lấy ra tên của hobby
    """
    parameters = {}
    if type == 1:
        data[column] = data.groupby('employee_id')['employee_id'].transform('count')
        data = data[['employee_id', column]].drop_duplicates()
        data = data.sort_values(column, ascending=False)
        x = data[column]
        y = data['employee_id']
        parameters["x"] = x[:top]
        parameters["y"] = y[:top]
    elif type == 2:
        data[column] = data.groupby(column2)[column2].transform('count')
        data = data[[column2, column]].drop_duplicates()
        data = data.sort_values(column, ascending=False)
        x = data[column2]
        y = data[column]
        parameters["x"] = x[:top]
        parameters["y"] = y[:top]
    return parameters


def visualize_invidual(data_reference, data, xlabel, ylabel, title, type=1, column='employee', ax=None):
    """
        data - dictionary chua du lieu, ma nhan vien va cot can thong ke
        data_reference - la bang nhan vien hoac cac bang khac lien quan
        xlabel - chua nhan
        ylabel
        title - chua title cua bang
        column - de join
    """

    if type == 1:
        x = data['x']
        y = pd.DataFrame(data['y'])
        data_reference['last_name'] = data_reference['name'].str.split(expand=True)[0]
        data_reference['first_name'] = data_reference['name'].str.split(expand=True)[2]
        result = pd.merge(y, data_reference, left_on=column, right_on='id', how='inner')
        bar = ax.barh(result['first_name'] + ' ' + result['last_name'], x, align='center', height=0.5)
        ax.invert_yaxis()
        ax.bar_label(bar, x)
        plt.rcdefaults()
    elif type == 2:
        x = pd.DataFrame(data['x'])
        y = data['y']
        result = pd.merge(x, data_reference, left_on=column, right_on='id', how='inner')
        bar = ax.bar(result['name'], y, align='center', color='g', width=0.5)
        ax.bar_label(bar, y)
    ax.set_xlabel(xlabel, fontsize=8)
    ax.set_ylabel(ylabel, fontsize=8)
    ax.set_title(title, fontsize=10)
    # plt.show()
    return ax
