# This is a sample Python script.

# Press the green button in the gutter to run the script.
from enviroments import label
from app import visualize
from enviroments import constant
import matplotlib.pyplot as plt

if __name__ == '__main__':
    print('PyCharm')
    base = './data/vss_exm/'

    fig, ax = plt.subplots(2, 2)
    plt.xticks(rotation=45)
    # for i in range(int(len(label.EMPLOYEE) / 4)):
    #     # thong ke theo nhan vien
    #     for key in label.EMPLOYEE:
    #         ax[label.EMPLOYEE[key]['location'][0], label.EMPLOYEE[key]['location'][1]] = visualize.visualize_invidual(
    #             data_reference=visualize.read_data(constant.COL_EMPLOYEE, base + 'employee.csv'),
    #             data=visualize.preprocessing(
    #                 data=visualize.read_data(label.EMPLOYEE[key]['header'],
    #                                          base + label.EMPLOYEE[key]['file']),
    #                 column=label.EMPLOYEE[key]['column'],
    #                 top=10,
    #                 type=1),
    #             xlabel=label.EMPLOYEE[key]['xlabel'],
    #             ylabel=label.EMPLOYEE[key]['ylabel'],
    #             title=label.EMPLOYEE[key]['title'],
    #             type=1, column='employee_id',
    #             ax=ax[label.EMPLOYEE[key]['location'][0], label.EMPLOYEE[key]['location'][1]])
    #     plt.show()

    # thong ke theo cac doi tuong khac nhu skill, expectedskill, role ...
    for i in range(int(len(label.EMPLOYEE) / 4)):
        for k1, k2 in zip(label.EMPLOYEE, label.OTHERS_ENTITIES):
            ax[label.EMPLOYEE[k1]['location'][0], label.EMPLOYEE[k1]['location'][1]] = visualize.visualize_invidual(
                data_reference=visualize.read_data(label.OTHERS_ENTITIES[k2]['header'],
                                                   base + label.OTHERS_ENTITIES[k2]['file']),
                data=visualize.preprocessing(data=visualize.read_data(label.EMPLOYEE[k1]['header'],
                                                                      base + label.EMPLOYEE[k1][
                                                                          'file']),
                                             column=label.OTHERS_ENTITIES[k2]['column'],
                                             column2=label.OTHERS_ENTITIES[k2]['column2'], top=10,
                                             type=2),
                xlabel=label.OTHERS_ENTITIES[k2]['xlabel'],
                ylabel=label.OTHERS_ENTITIES[k2]['ylabel'],
                title=label.OTHERS_ENTITIES[k2]['title'], type=2,
                column=label.OTHERS_ENTITIES[k2]['column2'],
                ax=ax[label.EMPLOYEE[k1]['location'][0], label.EMPLOYEE[k1]['location'][1]])
        plt.show()