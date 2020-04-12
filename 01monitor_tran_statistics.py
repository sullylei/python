import os
import sys
if __name__ == "__main__":
    threshold_value=0.3
    last_hour_trs=[]
    last_week_hour_trs=[]
    last_hour_trs.append(517227)
    last_hour_trs.append(24038)
    last_hour_trs.append(318.85)
    last_week_hour_trs.append(470167)
    last_week_hour_trs.append(12128)
    last_week_hour_trs.append(321.79)
    print(last_hour_trs)
    print(last_week_hour_trs)
    if last_week_hour_trs[0]==0 or last_hour_trs[0]==0 or (last_hour_trs[0]>last_week_hour_trs[0] and ((last_hour_trs[0]-last_week_hour_trs[0])/last_week_hour_trs[0])>threshold_value):
        warning_msg="交易量增幅超"+str(threshold_value)
        print(warning_msg)
    if last_week_hour_trs[1]==0 or last_hour_trs[1]==0 or (last_hour_trs[1]>last_week_hour_trs[1] and ((last_hour_trs[1]-last_week_hour_trs[1])/last_week_hour_trs[1])>threshold_value):
        warning_msg="失败量增幅超"+str("%.2f%%" % (threshold_value * 100))
        print(warning_msg)
    if last_week_hour_trs[2]==0 or last_hour_trs[2]==0 or (last_hour_trs[2]>last_week_hour_trs[2] and ((last_hour_trs[2]-last_week_hour_trs[2])/last_week_hour_trs[2])>threshold_value):
        warning_msg="平均耗时增幅超"+str("%.2f%%" % (threshold_value * 100))
        print(warning_msg)